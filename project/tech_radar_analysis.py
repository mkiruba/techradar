import os
import warnings
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from crewai.agents import CrewAgentExecutor

# Suppress warnings
warnings.filterwarnings('ignore')

class TechnologyRadarAnalyzer:
    def __init__(self, tech_radar_path: str):
        self.tech_radar_path = Path(tech_radar_path)
        self.tech_radar_content = self.tech_radar_path.read_text()
        self._setup_environment()
        self._create_agents()
        self._create_tasks()

    def _setup_environment(self):
        load_dotenv()
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7
        )

    def _create_agents(self):
        self.backend_expert = Agent(
            role="Backend Technology Expert",
            goal="Evaluate backend technologies, libraries, and frameworks from the Technology Radar.",
            backstory="You are an experienced backend architect with 15+ years of experience evaluating and implementing server-side technologies.",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            executor=CrewAgentExecutor()
        )

        self.frontend_expert = Agent(
            role="Frontend Technology Expert",
            goal="Evaluate frontend technologies, libraries, and frameworks from the Technology Radar.",
            backstory="You are a senior frontend architect who has led multiple enterprise UI projects.",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            executor=CrewAgentExecutor()
        )

        self.testing_expert = Agent(
            role="Testing Technology Expert",
            goal="Evaluate testing technologies, libraries, and frameworks from the Technology Radar.",
            backstory="You are a quality assurance architect with expertise in test automation strategies.",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            executor=CrewAgentExecutor()
        )

        self.coordinator = Agent(
            role="Technology Radar Coordinator",
            goal="Synthesize insights from domain experts and produce a final technology radar report.",
            backstory="You are a technology strategist responsible for maintaining and updating technology radars.",
            allow_delegation=True,
            verbose=True,
            llm=self.llm,
            executor=CrewAgentExecutor()
        )

    def _create_tasks(self):
        self.backend_task = Task(
            description=self._load_template("backend_evaluation.txt").format(
                tech_radar_content=self.tech_radar_content
            ),
            agent=self.backend_expert,
            expected_output="A comprehensive analysis of backend technologies with focus on adoption trends, licensing models, and recommendations for quadrant changes."
        )

        self.frontend_task = Task(
            description=self._load_template("frontend_evaluation.txt").format(
                tech_radar_content=self.tech_radar_content
            ),
            agent=self.frontend_expert,
            expected_output="A comprehensive analysis of frontend technologies with focus on adoption trends, licensing models, and recommendations for quadrant changes."
        )

        self.testing_task = Task(
            description=self._load_template("testing_evaluation.txt").format(
                tech_radar_content=self.tech_radar_content
            ),
            agent=self.testing_expert,
            expected_output="A comprehensive analysis of testing technologies with focus on adoption trends, licensing models, and recommendations for quadrant changes."
        )

        self.coordinator_task = Task(
            description=self._load_template("coordinator_summary.txt").format(
                backend_evaluation=self.backend_task.output,
                frontend_evaluation=self.frontend_task.output,
                testing_evaluation=self.testing_task.output
            ),
            agent=self.coordinator,
            expected_output="A comprehensive technology radar summary with cross-domain insights and strategic recommendations.",
            context=[self.backend_task, self.frontend_task, self.testing_task]
        )

    def _load_template(self, template_name: str) -> str:
        template_path = Path(__file__).parent / "templates" / template_name
        return template_path.read_text()

    def analyze(self) -> str:
        crew = Crew(
            agents=[self.backend_expert, self.frontend_expert, self.testing_expert, self.coordinator],
            tasks=[self.backend_task, self.frontend_task, self.testing_task, self.coordinator_task],
            verbose=True,
            process=Process.sequential
        )
        
        result = crew.kickoff()
        return result

    def save_results(self, output_path: str):
        result = self.analyze()
        with open(output_path, 'w') as f:
            f.write(result)

if __name__ == "__main__":
    analyzer = TechnologyRadarAnalyzer("technology-radar.md")
    analyzer.save_results("updated-technology-radar.md") 
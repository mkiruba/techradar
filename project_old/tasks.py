from crewai import Task
from pathlib import Path

class TechnologyTasks:
    def __init__(self, tech_radar_path: str):
        self.tech_radar_path = Path(tech_radar_path)
        self.tech_radar_content = self.tech_radar_path.read_text()

    def create_backend_evaluation_task(self, agent):
        return Task(
            description=(
                f"Evaluate backend technologies from this Technology Radar content:\n\n{self.tech_radar_content}\n\n"
                "Focus on .NET and Python ecosystems. For each technology:"
                "\n1. Evaluate current adoption levels in the industry"
                "\n2. Specify whether it's open-source or licensed"
                "\n3. Provide insights on why certain technologies are in their respective quadrants (Adopt, Trial, Assess, Hold)"
                "\n4. Highlight any technologies that should be moved to different quadrants based on current industry trends"
                "\n5. Provide specific examples and evidence for your recommendations"
            ),
            expected_output="A comprehensive analysis of backend technologies with focus on adoption trends, licensing models, and recommendations for quadrant changes.",
            agent=agent
        )

    def create_frontend_evaluation_task(self, agent):
        return Task(
            description=(
                f"Evaluate frontend technologies from this Technology Radar content:\n\n{self.tech_radar_content}\n\n"
                "Focus on Angular and modern web frameworks. For each technology:"
                "\n1. Evaluate current adoption levels in the industry"
                "\n2. Specify whether it's open-source or licensed"
                "\n3. Provide insights on why certain technologies are in their respective quadrants (Adopt, Trial, Assess, Hold)"
                "\n4. Highlight any technologies that should be moved to different quadrants based on current industry trends"
                "\n5. Provide specific examples and evidence for your recommendations"
            ),
            expected_output="A comprehensive analysis of frontend technologies with focus on adoption trends, licensing models, and recommendations for quadrant changes.",
            agent=agent
        )

    def create_testing_evaluation_task(self, agent):
        return Task(
            description=(
                f"Evaluate testing technologies from this Technology Radar content:\n\n{self.tech_radar_content}\n\n"
                "Focus on test automation tools and frameworks. For each technology:"
                "\n1. Evaluate current adoption levels in the industry"
                "\n2. Specify whether it's open-source or licensed"
                "\n3. Provide insights on why certain technologies are in their respective quadrants (Adopt, Trial, Assess, Hold)"
                "\n4. Highlight any technologies that should be moved to different quadrants based on current industry trends"
                "\n5. Provide specific examples and evidence for your recommendations"
            ),
            expected_output="A comprehensive analysis of testing technologies with focus on adoption trends, licensing models, and recommendations for quadrant changes.",
            agent=agent
        )

    def create_coordinator_task(self, agent, backend_task, frontend_task, testing_task):
        return Task(
            description=(
                "Synthesize the insights from all domain experts and produce a final technology radar report. "
                "Your report should:"
                "\n1. Identify patterns and trends across all domains"
                "\n2. Highlight any contradictions or inconsistencies in the recommendations"
                "\n3. Provide a clear summary of technology recommendations"
                "\n4. Suggest any cross-domain insights or opportunities"
                "\n5. Include specific examples and evidence for your conclusions"
                "\n\nPrevious expert analyses:"
                f"\nBackend Analysis: {backend_task.output}"
                f"\nFrontend Analysis: {frontend_task.output}"
                f"\nTesting Analysis: {testing_task.output}"
            ),
            expected_output="A comprehensive technology radar summary with cross-domain insights and strategic recommendations.",
            agent=agent,
            context=[backend_task, frontend_task, testing_task]
        ) 
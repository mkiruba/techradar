from crewai import Agent
from langchain_openai import ChatOpenAI

class TechnologyAgents:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            max_tokens=2000,
            request_timeout=120
        )

    def create_backend_expert(self):
        return Agent(
            role="Backend Technology Expert",
            goal="Evaluate backend technologies, libraries, and frameworks from the Technology Radar.",
            backstory="You are an experienced backend architect with 15+ years of experience evaluating and implementing server-side technologies. "
                    "You specialize in .NET and Python ecosystems and have deep knowledge of industry adoption trends, performance characteristics, "
                    "and licensing models. You're known for providing practical insights about enterprise-level adoption decisions.",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            max_iter=3
        )

    def create_frontend_expert(self):
        return Agent(
            role="Frontend Technology Expert",
            goal="Evaluate frontend technologies, libraries, and frameworks from the Technology Radar.",
            backstory="You are a senior frontend architect who has led multiple enterprise UI projects. "
                    "You specialize in Angular and modern web frameworks with expert knowledge on industry adoption, "
                    "community support, and licensing implications. You excel at differentiating between hype and practical value.",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            max_iter=3
        )

    def create_testing_expert(self):
        return Agent(
            role="Testing Technology Expert",
            goal="Evaluate testing technologies, libraries, and frameworks from the Technology Radar.",
            backstory="You are a quality assurance architect with expertise in test automation strategies across the entire tech stack. "
                    "You have implemented testing frameworks for both frontend and backend systems and can evaluate tools based on "
                    "industry adoption, effectiveness, learning curve, and licensing models. You advocate for practical testing approaches.",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            max_iter=3
        )

    def create_coordinator(self):
        return Agent(
            role="Technology Radar Coordinator",
            goal="Synthesize insights from domain experts and produce a final technology radar report.",
            backstory="You are a technology strategist responsible for maintaining and updating technology radars for the organization. "
                    "You excel at synthesizing information from domain experts and can identify patterns, contradictions, and insights across domains. "
                    "Your job is to ensure technology recommendations are consistent and aligned with business and technical objectives.",
            allow_delegation=True,
            verbose=True,
            llm=self.llm,
            max_iter=3
        ) 
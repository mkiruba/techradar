# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv
from typing import Optional, Dict, Any
from crewai import Agent, Task, Crew, Process
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

def load_env():
    """Load environment variables from .env file"""
    _ = load_dotenv(find_dotenv())

def get_openai_api_key() -> str:
    """Get OpenAI API key from environment variables"""
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    return openai_api_key

def get_serper_api_key() -> str:
    """Get Serper API key from environment variables"""
    load_env()
    serper_api_key = os.getenv("SERPER_API_KEY")
    if not serper_api_key:
        raise ValueError("SERPER_API_KEY not found in environment variables")
    return serper_api_key

def create_agent(
    role: str,
    goal: str,
    backstory: str,
    tools: Optional[list] = None,
    verbose: bool = True
) -> Agent:
    """
    Create a CrewAI agent with specified role, goal, and backstory
    
    Args:
        role: The role of the agent
        goal: The goal of the agent
        backstory: The backstory of the agent
        tools: List of tools the agent can use
        verbose: Whether to enable verbose output
        
    Returns:
        Agent: A configured CrewAI agent
    """
    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        tools=tools or [],
        verbose=verbose
    )

def create_task(
    description: str,
    agent: Agent,
    expected_output: str,
    context: Optional[Dict[str, Any]] = None
) -> Task:
    """
    Create a CrewAI task with specified description and agent
    
    Args:
        description: Description of the task
        agent: The agent assigned to the task
        expected_output: Expected output format
        context: Additional context for the task
        
    Returns:
        Task: A configured CrewAI task
    """
    return Task(
        description=description,
        agent=agent,
        expected_output=expected_output,
        context=context or {}
    )

def create_crew(
    agents: list[Agent],
    tasks: list[Task],
    process: Process = Process.sequential,
    verbose: bool = True
) -> Crew:
    """
    Create a CrewAI crew with specified agents and tasks
    
    Args:
        agents: List of agents in the crew
        tasks: List of tasks to be performed
        process: Process type (sequential or parallel)
        verbose: Whether to enable verbose output
        
    Returns:
        Crew: A configured CrewAI crew
    """
    return Crew(
        agents=agents,
        tasks=tasks,
        process=process,
        verbose=verbose
    )

@tool("Search the internet")
def search_internet(query: str) -> str:
    """
    Search the internet using DuckDuckGo
    
    Args:
        query: Search query
        
    Returns:
        str: Search results
    """
    search = DuckDuckGoSearchRun()
    return search.run(query)

def pretty_print_result(result: str) -> str:
    """
    Format result text with proper line breaks
    
    Args:
        result: Text to format
        
    Returns:
        str: Formatted text
    """
    parsed_result = []
    for line in result.split('\n'):
        if len(line) > 80:
            words = line.split(' ')
            new_line = ''
            for word in words:
                if len(new_line) + len(word) + 1 > 80:
                    parsed_result.append(new_line)
                    new_line = word
                else:
                    if new_line == '':
                        new_line = word
                    else:
                        new_line += ' ' + word
            parsed_result.append(new_line)
        else:
            parsed_result.append(line)
    return "\n".join(parsed_result)

import os
import warnings
import time
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import TechnologyAgents
from tasks import TechnologyTasks

# Suppress warnings
warnings.filterwarnings('ignore')

def main():
    print("Starting Technology Radar Analysis...")
    total_start_time = time.time()
    
    # Load environment variables
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    # Initialize components
    tech_radar_path = "technology-radar.md"
    print(f"Loading technology radar from: {tech_radar_path}")
    
    agents = TechnologyAgents()
    tasks = TechnologyTasks(tech_radar_path)

    # Create agents
    print("\nCreating agents...")
    agent_start_time = time.time()
    backend_expert = agents.create_backend_expert()
    print(f"Created Backend Expert in {time.time() - agent_start_time:.2f} seconds")
    
    agent_start_time = time.time()
    frontend_expert = agents.create_frontend_expert()
    print(f"Created Frontend Expert in {time.time() - agent_start_time:.2f} seconds")
    
    agent_start_time = time.time()
    testing_expert = agents.create_testing_expert()
    print(f"Created Testing Expert in {time.time() - agent_start_time:.2f} seconds")
    
    agent_start_time = time.time()
    coordinator = agents.create_coordinator()
    print(f"Created Coordinator in {time.time() - agent_start_time:.2f} seconds")

    # Create tasks
    print("\nCreating tasks...")
    task_start_time = time.time()
    backend_task = tasks.create_backend_evaluation_task(backend_expert)
    print(f"Created Backend Evaluation Task in {time.time() - task_start_time:.2f} seconds")
    
    task_start_time = time.time()
    frontend_task = tasks.create_frontend_evaluation_task(frontend_expert)
    print(f"Created Frontend Evaluation Task in {time.time() - task_start_time:.2f} seconds")
    
    task_start_time = time.time()
    testing_task = tasks.create_testing_evaluation_task(testing_expert)
    print(f"Created Testing Evaluation Task in {time.time() - task_start_time:.2f} seconds")
    
    task_start_time = time.time()
    coordinator_task = tasks.create_coordinator_task(
        coordinator, backend_task, frontend_task, testing_task
    )
    print(f"Created Coordinator Task in {time.time() - task_start_time:.2f} seconds")

    # Create and run the crew
    print("\nCreating crew...")
    crew_start_time = time.time()
    crew = Crew(
        agents=[backend_expert, frontend_expert, testing_expert, coordinator],
        tasks=[backend_task, frontend_task, testing_task, coordinator_task],
        verbose=True,
        process=Process.sequential
    )
    print(f"Crew created in {time.time() - crew_start_time:.2f} seconds")

    # Run the analysis
    print("\nStarting analysis...")
    analysis_start_time = time.time()
    try:
        result = crew.kickoff()
        print(f"\nAnalysis completed in {time.time() - analysis_start_time:.2f} seconds")
        print(f"Total execution time: {time.time() - total_start_time:.2f} seconds")
        
        # Save the results
        output_path = "updated-technology-radar.md"
        with open(output_path, "w") as f:
            f.write(result)
        print(f"\nResults saved to: {output_path}")
        
    except Exception as e:
        print(f"\nError during analysis: {str(e)}")
        print(f"Execution time before error: {time.time() - total_start_time:.2f} seconds")
        raise

if __name__ == "__main__":
    main() 
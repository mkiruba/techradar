# Technology Radar Analysis Notebook

This notebook demonstrates a multi-agent system for analyzing and evaluating technologies across different domains using the CrewAI framework.

## Overview

The notebook implements a technology radar analysis system with specialized agents for different technology domains:

1. **Backend Technologies Expert** - Evaluates server-side technologies, focusing on .NET and Python ecosystems
2. **Frontend Technologies Expert** - Analyzes UI frameworks and libraries, with emphasis on Angular
3. **Testing Technologies Expert** - Assesses testing frameworks and tools across the stack
4. **Technology Radar Coordinator** - Synthesizes insights from domain experts and produces final recommendations

## Features

- Multi-agent system for comprehensive technology evaluation
- Analysis of adoption rates and industry trends
- Evaluation of licensing models (open-source vs. licensed)
- Technology quadrant recommendations (Adopt, Trial, Assess, Hold)
- Cross-domain insights and strategic recommendations

## Requirements

The notebook requires the following dependencies:
```python
crewai==0.28.8
crewai_tools==0.1.6
langchain_community==0.0.29
```

## Usage

1. Ensure you have the required dependencies installed
2. Set up your OpenAI API key in the environment
3. Run the notebook cells sequentially to:
   - Create specialized agents
   - Define evaluation tasks
   - Run the technology radar analysis
   - Generate final recommendations

## Output

The analysis produces several output files:
- `src/tech_radar/files/backend_analysis.md` - Backend technology evaluation
- `src/tech_radar/files/frontend_analysis.md` - Frontend technology evaluation
- `src/tech_radar/files/testing_analysis.md` - Testing technology evaluation
- `src/tech_radar/files/coordinator_summary.md` - Final synthesis and recommendations

## Notes

- The notebook uses OpenAI's `gpt-3.5-turbo` model by default
- Task execution is sequential to ensure proper dependency handling
- The analysis includes memory capabilities for agent interactions
- Visualization suggestions are provided for potential radar chart generation 
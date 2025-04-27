# TechRadar Crew

Welcome to the TechRadar Crew project, powered by [crewAI](https://crewai.com). This project implements a multi-agent system for analyzing and evaluating technologies across different domains.

## Project Structure

```
tech_radar/
├── src/
│   ├── crew.py          # Crew and agent definitions
│   ├── main.py          # Entry point and execution logic
│   ├── files/           # Output files directory
│   ├── config/          # Configuration files
│   │   ├── agents.yaml  # Agent configurations
│   │   └── tasks.yaml   # Task configurations
│   └── tools/           # Custom tools
├── .venv/               # Virtual environment
└── pyproject.toml       # Project configuration
```

## Installation

1. Ensure you have Python >=3.10 <3.13 installed
2. Install dependencies:
```bash
pip install crewai[tools]
```

3. Add your `OPENAI_API_KEY` to the `.env` file

## Configuration

- Modify `src/config/agents.yaml` to define your agents
- Modify `src/config/tasks.yaml` to define your tasks
- Modify `src/crew.py` to customize agent behavior and tools
- Modify `src/main.py` to adjust execution parameters

## Running the Project

From the project root:
```bash
crewai run
```

This will execute the technology radar analysis and generate reports in the `src/files/` directory.

## Output Files

- `backend_analysis.md` - Backend technology evaluation
- `frontend_analysis.md` - Frontend technology evaluation
- `testing_analysis.md` - Testing technology evaluation
- `coordinator_summary.md` - Final synthesis and recommendations

## Support

- [Documentation](https://docs.crewai.com)
- [GitHub Repository](https://github.com/joaomdmoura/crewai)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)

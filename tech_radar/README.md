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
2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Unix/MacOS:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install crewai[tools]
pip install -e .
```

4. Add your `OPENAI_API_KEY` to the `.env` file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```

## Configuration

- Modify `src/config/agents.yaml` to define your agents
- Modify `src/config/tasks.yaml` to define your tasks
- Modify `src/crew.py` to customize agent behavior and tools
- Modify `src/main.py` to adjust execution parameters

## Running the Project

1. Make sure you're in the project root directory
2. Ensure your virtual environment is activated
3. Run the crew:
```bash
crewai run
```

This will execute the technology radar analysis and generate reports in the `src/files/` directory.

## Output Files

The analysis produces several output files in the `src/files/` directory:
- `backend_analysis.md` - Backend technology evaluation
- `frontend_analysis.md` - Frontend technology evaluation
- `testing_analysis.md` - Testing technology evaluation
- `coordinator_summary.md` - Final synthesis and recommendations

## Troubleshooting

If you encounter import errors:
1. Ensure you're in the project root directory
2. Verify your virtual environment is activated
3. Check that you've installed the package in development mode (`pip install -e .`)
4. Make sure your `PYTHONPATH` includes the project root

## Support

- [Documentation](https://docs.crewai.com)
- [GitHub Repository](https://github.com/joaomdmoura/crewai)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)

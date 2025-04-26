# Technology Radar Analysis

This project provides a multi-agent system for analyzing technology radar data using CrewAI.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Place your technology radar markdown file in the project root directory
2. Run the analysis:
```bash
python -m project.tech_radar_analysis
```

The analysis will generate an updated technology radar report in `updated-technology-radar.md`.

## Project Structure

```
project/
├── __init__.py
├── tech_radar_analysis.py
└── templates/
    ├── backend_evaluation.txt
    ├── frontend_evaluation.txt
    ├── testing_evaluation.txt
    └── coordinator_summary.txt
```

## Customization

You can modify the templates in the `templates` directory to customize the analysis criteria and output format.
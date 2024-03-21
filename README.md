
# AI Documentation System

## Overview
The AI Documentation System is designed to automatically fetch commit messages and issues from a specified GitHub repository, clean and process the text, and then analyze it using OpenAI's GPT model to generate concise, insightful explanations. This system acts as a project manager's assistant, providing natural language insights into the developments and discussions within a GitHub repository.

## Features
- Fetch data from GitHub repositories (commits and issues).
- Clean and preprocess textual data for NLP analysis.
- Analyze text using OpenAI's GPT model to generate natural language explanations.
- Provide concise insights as if from a project manager's assistant.

## Installation

### Prerequisites
- Python 3.x
- A GitHub Personal Access Token
- An OpenAI API Key

### Setup
1. **Clone the repository**:
    ```
    git clone <repository-url>
    cd AI Documentation System
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On Unix or MacOS
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add your GitHub and OpenAI credentials:
    ```
    GITHUB_ACCESS_TOKEN=your_github_token_here
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## Usage

To run the AI Documentation System, execute the `main.py` script:

```bash
python main.py
```

This script orchestrates the data collection, processing, and analysis workflow, outputting concise explanations for recent commit messages or issues from the configured GitHub repository.

## Configuration

You can customize the GitHub repository from which data is fetched by modifying the `git_collector.py` file with the desired `repo_owner` and `repo_name` values.

## Contributing

Contributions to the AI Documentation System are welcome! Please refer to the contributing guidelines for more information on how to contribute.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

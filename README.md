# LangChain Agent with Wikipedia and YouTube Search Tools

This project demonstrates how to build an AI agent using LangChain that utilizes Wikipedia and YouTube search tools to answer user queries. The agent uses OpenAI's GPT-based language model and is capable of searching Wikipedia for information and retrieving YouTube video links.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Example Output](#example-output)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Installation

1. Clone the repository or copy the files to your local machine.
2. Install the required Python packages using `pip`:

    ```bash
    pip install langchain langchain-openai wikipedia youtube_search python-dotenv langchain_community
    ```

3. Install any additional dependencies if required.

## Setup

1. **Environment Variables**:
   - Create a `.env` file in the root directory of the project. This file will hold your API keys and other configuration settings.
   - Add the following variables to your `.env` file:

   ```bash
   OPENAI_API_KEY=<Your OpenAI API Key>
   OPENAI_MODEL=gpt-3.5-turbo

Replace <Your OpenAI API Key> and <Your YouTube Data API Key> with your actual API keys.

2. **API Keys**:

You need to have API keys for:
OpenAI (for using GPT models).

3. **Load Environment Variables**:

Ensure that environment variables are loaded correctly from the .env file using the python-dotenv library.

## Usage

Run the agent using the Python script provided. The agent is configured to perform the following actions:

1. **Search Wikipedia for a given topic.**
2. **Retrieve a YouTube link for a related video.**

## Running the Agent
Run the Python script in your terminal or command prompt:

```
python main.py
```

## Contributing

Feel free to open issues or submit pull requests if you want to improve or add new features to this example.

## License

This project is licensed under the MIT License.
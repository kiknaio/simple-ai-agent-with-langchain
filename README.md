# LangChain Simple Agent

A simple weather agent built with LangChain that retrieves weather information using coordinates.

## Community & Resources

If this project helped you, I'm sharing more simple AI agent building guides (for free) here: https://newsletter.ai30.io 

## Features

- Uses OpenAI's GPT-4o-mini model
- Weather tool for fetching current temperature and wind speed
- Parses natural language requests to extract location information

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install langchain langchain-openai python-dotenv requests
   ```
3. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

Run the agent:

```
python src/agent.py
```

Example queries:
- "What's the weather like in Paris, France?"
- "Tell me the current weather at coordinates 40.7128, -74.0060"

## How it Works

The agent uses LangChain's framework to:
1. Process natural language queries
2. Extract latitude and longitude information
3. Call the Open-Meteo API to get current weather data
4. Format and return the results

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for API access 
# AI Travel Planning Agent - Tool-Based Agent

An intelligent Tool-Based AI agent built using the ReAct pattern that helps users plan travel by accessing destination weather, flights, and attractions.

## 🌟 Features
- Get weather information for various destinations
- Check flight times and estimated prices
- Discover popular attractions in cities

## 🧠 How It Works
This agent implements the ReAct (Reasoning + Acting) pattern to simulate human-like problem solving:

1. **Thought**: The agent thinks about what information is needed
2. **Action**: It calls specific functions to gather that information  
3. **Result**: It processes the results of those function calls
4. **Answer**: It synthesizes a helpful response based on all gathered information

## 🛠️ Technical Implementation
- **ReAct Prompting**: Structured system prompt for step-by-step reasoning
- **Function Calling Architecture**: Modular design with specialized tools
- **JSON Parsing**: Utilities to extract structured function calls
- **Conversation Management**: Multi-turn dialogue handling

## 🧩 Project Structure
- `main.py`: Core agent loop and conversation management
- `actions.py`: Tool functions the agent can use
- `prompts.py`: System prompt implementing the ReAct pattern
- `json_helpers.py`: Utilities for extracting function calls from text

## 🚀 Getting Started
```bash
# Clone repository
git clone https://github.com/GauravVarma-web/travel-planner-agent.git

# Set up virtual environment
python -m venv travelenv
source travelenv/bin/activate  # On Windows: travelenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key to .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Run the agent
python main.py

📋 #Example Queries
#Here are some commands to test different aspects of your Travel Planner Agent:
#Basic Single-Function Commands

#"What's the weather like in Paris?"
#"What's the weather in Tokyo?"
#"Tell me about attractions in London"
#"What attractions are in New York?"
#"What's the flight information from New York to London?"

#Multi-Function Commands

#"I'm planning a trip to Paris. What's the weather and what attractions should I visit?"
#"Tell me about the weather in Tokyo and how long it takes to fly there from London"
#"I want to travel from New York to Paris. What's the flight like and what can I do there?"
#"Compare the weather in London and Paris, and tell me about attractions in both cities"

#Edge Cases

#"What's the weather in Barcelona?" (City not in our database)
#"How long does it take to fly from Chicago to Berlin?" (Route not in our database)
#"What's the best hotel in Paris?" (Function not implemented)
#"What's the population of Tokyo?" (Outside the agent's capabilities)

#These commands will test:

#Basic functionality (single function calls)
#Complex reasoning (multiple function calls)
#Error handling (missing data or unavailable functions)
#Boundaries of the agent's capabilities

#Try different variations to see how the agent responds. This will help you understand how the ReAct pattern works in practice and how you could extend the agent with additional functions.
#🔍 Marketing Applications
#This project demonstrates the architecture used to create specialized marketing agents such as:

#Content Planning Agents: Suggest content topics based on SEO data and competitor analysis
#Campaign Optimization Agents: Analyze campaign performance and suggest improvements
#Customer Journey Agents: Personalize recommendations based on user preferences
#Social Media Managers: Schedule and optimize posts based on audience engagement data
#Competitive Intelligence Agents: Monitor competitor activities and suggest strategic responses

#These marketing-focused AI agents follow the same core architecture but with specialized functions tailored to marketing tasks. For example, instead of get_weather(), a content planning agent might have functions like analyze_keywords() or check_content_gaps().
#📚 Resources

#ReAct: Synergizing Reasoning and Acting in Language Models
#Function Calling in OpenAI API
#LangChain Documentation on ReAct Agents
#Prompt Engineering Guide
#Building AI Agents with OpenAI Functions

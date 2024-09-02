from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import YouTubeSearchTool
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate




import os
from os.path import join, dirname
from dotenv import load_dotenv

# Loading the environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Tools
# Initialize the Wikipedia tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# Initialize YouTube search tool
youtube_tool = YouTubeSearchTool()

tools = [wikipedia_tool, youtube_tool]

# Prompt for the agent
# Define the prefix and suffix for the prompt
tool_names = [wikipedia_tool.name, youtube_tool.name]
input_variables = ["input", "chat_history", "agent_scratchpad", "tool_names", "tools"]

prefix = """You are a helpful assistant. You have access to the following tools:

{tool_names}

{tools}

Please use these tools one time only to answer the user's query. 
First, determine which tool is needed and provide a clear, formatted response as shown below.

Output format:
1. Wikipedia Summary: <summary text here>
2. YouTube Link: <link here>

Only provide the answer once after using the tools."""

suffix = """
{chat_history}
Question: {input}
Thought: Let's first determine what information is needed and use the appropriate tool.
{agent_scratchpad}
Answer:"""

prompt = PromptTemplate(input_variables=input_variables, template=prefix + "\n\n" + suffix)

# Memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Chain
llm_chain = ChatOpenAI(temperature=0, model=os.environ.get('OPENAI_MODEL'), api_key=os.environ.get('OPENAI_API_KEY'))  # type: ignore

# Agent
agent = create_react_agent(llm=llm_chain, tools=tools, prompt=prompt)

# AgentExecutor with error handling for parsing errors
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, memory=memory, handle_parsing_errors=True)

# Invoke the agent with input
result = agent_executor.invoke({"input": "Tell me something about Shah Rukh Khan."})
print(result)

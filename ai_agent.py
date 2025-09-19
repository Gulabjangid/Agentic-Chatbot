from dotenv import load_dotenv; load_dotenv()

# Step1: Setup API Keys for Groq, Tavily, and Gemini
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# Prefer GOOGLE_API_KEY for Gemini; fall back to GEMINI_API_KEY
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GOOGLE_API_KEY and GEMINI_API_KEY:
    os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY  # picked up by langchain-google-genai

# Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

# Choose a free-tier friendly Gemini model
GEMINI_MODEL = "gemini-1.5-flash"  # also works with "gemini-2.5-flash"

groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
gemini_llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    convert_system_message_to_human=True,  # avoids Gemini system-role issues
)

# Tavily tool (new package)
search_tool = TavilySearch(max_results=2)

# Step3: Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage

system_prompt = "Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "Gemini":
        llm = ChatGoogleGenerativeAI(model=llm_id)
    else:
        raise ValueError("provider must be 'Groq' or 'Gemini'")

    tools = [TavilySearch(max_results=2)] if allow_search else []

    # Use prompt= (string interpreted as a system message)
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt,
    )

    # LangGraph agent expects a list of messages
    state = {"messages": [("human", query)]}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [m.content for m in messages if isinstance(m, AIMessage)]
    return ai_messages[-1]

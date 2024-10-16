import os, sys
import pytest
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv("resources")


@pytest.fixture("session")
def llm():
    chain_genai = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    return chain_genai

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def get_llm(model: str = "gpt-4o-mini", temperature: float = 0.3) -> ChatOpenAI:
    """
    Returns a ChatOpenAI instance.

    Parameters:
    - model (str): LLM model name, default "gpt-4"
    - temperature (float): Creativity level, default 0.3

    Returns:
    - ChatOpenAI instance
    """
    return ChatOpenAI(model=model, temperature=temperature)

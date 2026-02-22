"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "gemma3:12b",
    "qwen3:4b",
    "qwen3-coder"
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "qwen3-coder"

# OpenRouter API endpoint
OPENROUTER_API_URL = "http://localhost:8000/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"

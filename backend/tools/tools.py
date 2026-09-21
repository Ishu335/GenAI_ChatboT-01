
from langchain_community.tools import DuckDuckGoSearchRun


# Initialize tools once
search_tool = DuckDuckGoSearchRun()

def search(prompt: str):
    try:
        return search_tool.invoke(prompt)

    except Exception as e:
        print(f"DuckDuckGo error: {e}")
        return "DuckDuckGo search is currently unavailable."



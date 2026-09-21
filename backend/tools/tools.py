
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


# Initialize tools once
search_tool = DuckDuckGoSearchRun()

wikipedia_tool = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        top_k_results=2,
        doc_content_chars_max=4000
    )
)


def search(prompt: str):
    try:
        return search_tool.invoke(prompt)

    except Exception as e:
        print(f"DuckDuckGo error: {e}")
        return "DuckDuckGo search is currently unavailable."



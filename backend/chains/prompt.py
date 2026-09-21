from langchain_core.prompts import ChatPromptTemplate


general_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI assistant. "
        "Give clear, accurate and concise answers."
    ),
    (
        "human",
        "{question}"
    )
])
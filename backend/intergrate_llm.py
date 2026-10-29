# generate our retrieval-augmented 


def generate_output(query, retriever, llm, top_k=3):
    results = retriever.retrieve(query, top_k)

    context = "\n".join([doc["document"] for doc in results]) if results else ""

    if not context:
        print("we found no relevant context for the given query")

    # context + query
    prompt = f""" use given context to generate the answer for the query
                Context: {context}
                Query: {query} """
    print("\n ***** Prompt : {prompt} ****\n")
    response = llm.invoke(prompt) # expecting a string as prompt()
    return response
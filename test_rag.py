from dotenv import load_dotenv
from backend import get_retriever

load_dotenv()

retriever = get_retriever()

query = "What are the main topics discussed in this document?"

results = retriever.invoke(query)

print(f"\nRetrieved {len(results)} chunks\n")

for i, doc in enumerate(results, 1):
    print(f"\n========== CHUNK {i} ==========")
    print(doc.page_content[:1000])
    print("Page:", doc.metadata.get("page"))
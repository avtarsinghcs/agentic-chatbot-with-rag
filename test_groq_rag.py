from backend import chatbot
from langchain_core.messages import HumanMessage

config = {
    "configurable": {
        "thread_id": "rag_test_001"
    }
}

response = chatbot.invoke(
    {
        "messages": [
            HumanMessage(
                content="What projects are mentioned in my uploaded CV?"
            )
        ]
    },
    config=config
)

print("\n========== CHATBOT RESPONSE ==========\n")

for message in response["messages"]:
    print(f"\n{message.type.upper()}:")
    print(message.content)
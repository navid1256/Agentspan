import logging
from datetime import datetime
from dotenv import load_dotenv
from agentspan.agents import Agent, AgentRuntime, ConversationMemory, run, tool

load_dotenv()
logging.basicConfig(level=logging.WARNING)
logging.getLogger("agentspan").setLevel(logging.WARNING)
logging.getLogger("agentspan").setLevel(logging.WARNING)

assistant = Agent(
    name="assistant",
    model="openai/gpt-6.1-sol",
    instructions="You are a helpful assistant that can answer questions and provide information and remember details.",
    tools=[]
)



if __name__ == "__main__":
    print("Starting agent runtime...")

    with AgentRuntime() as runtime:
        while True:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting...")
                break

            if not user_input.strip():
                print("Please enter a message.")
                continue

            response = runtime.run(agent=assistant, prompt=user_input)
            print(f"Assistant: {response}")
import asyncio
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions

load_dotenv()

async def main():
    """Test basic query without agents"""
    try:
        print("Testing basic query without agents...")
        async for message in query(
            prompt="Hello, how are you?",
            options=ClaudeAgentOptions(
                allowed_tools=[]
            )
        ):
            if hasattr(message, "result"):
                print(f"Result: {message.result}")
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")

if __name__ == "__main__":
    asyncio.run(main())

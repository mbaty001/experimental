import asyncio
import json
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

load_dotenv()

import os

print(os.environ.get("ANTHROPIC_API_KEY"))

async def main():
    
    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
        
        async for message in query(
            prompt=(
                "You coordinate research by delegating to specialized subagents and synthesising their findings. "
                "Do not use WebSearch directly; delegate any web lookup to the web_search_agent subagent.\n\n"
                f"{user_input}"
            ),
            options=ClaudeAgentOptions(
                allowed_tools=["Agent"],
                agents={
                    "web_search_agent": AgentDefinition(
                        # description tells Claude when to use this subagent
                        description="Searches the web for current information and returns structured findings with metadata.",
                        # prompt defines the subagent's behavior and expertise
                        prompt="""Search for information on the given topic. Return findings as a JSON object with this structure:
{
  "findings": [
    {
      "claim": "The main assertion or finding",
      "source_url": "https://...",
      "document_name": "Title or name of web page",
      "page_number": null,
      "confidence": 0.85
    }
  ]
}
Confidence should be 0-1 based on source reliability and claim clarity.

Do not actually search the web - return stub data:
{"findings": [
    {
      "claim": "test claim",
      "source_url": "https://test-claim-source.com",
      "document_name": "Test Claim Source",
      "page_number": null,
      "confidence": 0.85
    }
  ]
}
""",
                        # tools restricts what the subagent can do (read-only here)
                        model="haiku",
                    )
                }
            )
        ):

            # Check for subagent invocation. Match both names: older SDK
            # versions emitted "Task", current versions emit "Agent".
            if hasattr(message, "content") and message.content:
                for block in message.content:
                    if getattr(block, "type", None) == "tool_use" and block.name in (
                        "Task",
                        "Agent",
                    ):
                        print(f"Subagent invoked: {block.input.get('subagent_type')}")

            # Check if this message is from within a subagent's context
            if hasattr(message, "parent_tool_use_id") and message.parent_tool_use_id:
                print("  (running inside subagent)")

            if hasattr(message, "result"):
                print(message.result)
asyncio.run(main())
import asyncio
import json
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

load_dotenv()

FINDING_SCHEMA = {
    "type": "object",
    "properties": {
        "findings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim": {"type": "string", "description": "The main finding or assertion"},
                    "source_url": {"type": "string", "description": "URL source (use 'local' for documents)"},
                    "document_name": {"type": "string", "description": "Name of source document or web page"},
                    "page_number": {"type": "integer", "description": "Page number if applicable, null otherwise"},
                    "confidence": {"type": "number", "description": "Confidence score 0-1"}
                },
                "required": ["claim", "source_url", "document_name", "confidence"]
            }
        }
    }
}

def format_findings(results):
    """Parse and format findings for display"""
    try:
        if isinstance(results, str):
            # Try to extract JSON from the result string
            data = json.loads(results)
        else:
            data = results
        
        if isinstance(data, dict) and "findings" in data:
            findings = data["findings"]
            print("\n" + "="*80)
            for i, finding in enumerate(findings, 1):
                print(f"\n📌 Finding {i}:")
                print(f"   Claim: {finding.get('claim', 'N/A')}")
                print(f"   Source: {finding.get('document_name', 'N/A')}")
                print(f"   URL: {finding.get('source_url', 'N/A')}")
                if finding.get('page_number'):
                    print(f"   Page: {finding.get('page_number')}")
                print(f"   Confidence: {finding.get('confidence', 'N/A')}")
            print("\n" + "="*80)
        else:
            print(f"\nAgent: {results}")
    except json.JSONDecodeError:
        print(f"\nAgent: {results}")

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
                    ),
                    "doc_analysis": AgentDefinition(
                        description="Analyses documents to extract key findings and claims, along with source metadata.",
                        prompt="""Analyse the provided documents. Return findings as a JSON object with this structure:
{
  "findings": [
    {
      "claim": "The main assertion or finding from the document",
      "source_url": "local",
      "document_name": "exact filename",
      "page_number": 5,
      "confidence": 0.9
    }
  ]
}
Confidence should be 0-1 based on evidence clarity and specificity.""",
                        # Bash access lets this subagent run test commands
                        tools=["read_file", "search_file"],
                        model="haiku"   
                    ),
                },                                                  
            )
        ):
            if hasattr(message, "result"):
                format_findings(message.result)

asyncio.run(main())
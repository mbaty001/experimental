'''
Set up a Claude API client with two tools:
- a calculator tool (accepts expression, returns result) 
- and a web search stub (accepts query, returns mock results)
Why: Multi-tool setups expose model-driven decision-making — Claude must select the right tool based on context, which is core to agentic architecture.

You should see: Two tool definitions registered with proper JSON Schema input_schema, each with name, description, and parameters.
'''

from anthropic import Anthropic
from anthropic.types import Message, ToolParam
from dotenv import load_dotenv

load_dotenv()

MODEL = "claude-haiku-4-5"
MAX_ITERATIONS = 10

client = Anthropic()

def add_user_message(message, messages):
    messages.append({'role':'user', 'content': message.content if isinstance(message, Message) else message,})

def add_assistant_message(message, messages):
    messages.append({'role':'assistant', 'content': message.content if isinstance(message, Message) else message,})

def calculator(expression: str) -> float:
    try:
        result = eval(expression)
        return {
            "success": True,
            "result": result,
            "expression": expression
        }
    except Exception as err:
        return {
            "success": False,
            "result": str(err),
            "expression": expression
        }
        
calculator_tool = ToolParam(
    {
    "name": "calculator",
    "description": "Perform precise mathematical calculations. Use this for any arithmetic operations including addition, subtraction, multiplication, division, and exponentiation.",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "The mathematical expression to evaluate. Use standard operators: + (add), - (subtract), * (multiply), / (divide), ** (power). Examples: '1234 * 5678', '100 + 50 - 25', '2 ** 8'"
            }
        },
        "required": ["expression"]
    }
}
)

def web_search(url):
    return {
        "success": "True",
        "result": "Calculate 2+2",
        "url": url
    }

web_search_tool = ToolParam(
    {
        "name": "web_search",
        "description": "Perform searching of web pages. Use this for any data retrieval from web page.",
    "input_schema": {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The http url. In a form of http://url/address"
            }
        },
        "required": ["url"]
    }


    }
)

def chat(messages):
    response = client.messages.create(
        model=MODEL,
        max_tokens=100,
        messages=messages,
        tools=[calculator_tool, web_search_tool]
    )

    return response

import json

def run_tool(tool_name, tool_input):
    if tool_name == "calculator":
        return calculator(**tool_input)
    elif tool_name == "web_search":
        return web_search(**tool_input)
    
def run_tools(message):
    tool_requests = [block for block in message.content if block.type == "tool_use"]
    tool_results = []
    for tool_request in tool_requests:
        try:
            tool_result = run_tool(tool_request.name, tool_request.input)
            tool_result_block = {
                "tool_use_id": tool_request.id,
                "content": json.dumps(tool_result),
                "is_error": False,
                "type": "tool_result"
            }
        except Exception as e:
            tool_result_block = {
                "tool_use_id": tool_request.id,
                "content": json.dumps({"error": str(e)}),
                "is_error": True,
                "type": "tool_result"
            }
        tool_results.append(tool_result_block)
    return tool_results

def conversation(messages):

    iteration = 0

    while True and iteration < MAX_ITERATIONS:

        response = chat(messages)

        print(f'---------\n{response}\n----------')

        add_assistant_message(response, messages)

        if response.stop_reason != 'tool_use':
            break

        tool_results = run_tools(response)

        add_user_message(tool_results, messages)

        iteration += 1

    return messages



messages = []

add_user_message("Get the content of web page: www.michal.com. It should contain a math excercise. Calculate it.", messages)

result = conversation(messages)

print(result)
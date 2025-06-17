import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


args = sys.argv
if len(args) < 2:
  print("Usage: python main.py \"Write your prompt here...\"")
  exit(1)
flag = args[2] if len(args) > 2 else ""

# print(flag)
user_prompt = args[1]
messages = [
  types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

response = client.models.generate_content(
  model="gemini-2.0-flash-001", 
  contents=messages,
  config=types.GenerateContentConfig(system_instruction=system_prompt),
)
prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

print(response.text)

if flag == '--verbose':
  print()
  print(f"User prompt: {user_prompt}")
  print(f"Prompt tokens: {prompt_tokens}")
  print(f"Response tokens: {response_tokens}")

import openai
import sys

filePath = "key.txt"

with open(filePath, 'r') as file:
  openai.api_key = file.read()

prompt = "Generate one sharp, funny, in-game trash talk line for CS2. Make it witty and mean. Make it unique aswell."

response = openai.ChatCompletion.create(
  model="gpt-4o-mini",
  messages=[{"role":"user", "content": prompt}],
  max_tokens=30
)

line=response['choices'][0]['message']['content'].strip()
print(line)
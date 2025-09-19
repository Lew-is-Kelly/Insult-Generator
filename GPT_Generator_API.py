import openai
import sys

filePath = "key.txt"

with open(filePath, 'r') as file:
  openai.api_key = file.read()

prompt = "Generate a line similar to \"YOU WILL LOSE\", \"YOU ARE SO BAD\", \"YOU MAY HAVE WON THAT ROUND BUT WE WILL WIN THE GAME\", \"YOU CANNOT WIN\""

response = openai.ChatCompletion.create(
  model="gpt-4o-mini",
  messages=[{"role":"user", "content": prompt}],
  max_tokens=30
)

line=response['choices'][0]['message']['content'].strip()
print(line)
#import stuff
from gpiozero import LED
from gpiozero import Button
import urllib.request
import os
import requests
#speach to text

#rest apt
//TODO: make the varibvle prompt the real one
url = "http://localhost:11434/api/generate"

while True:
    prompt = input("Enter prompt: ")
    data = "{\"model\": \"llama2\", \"prompt\":\"" + prompt + "\"}"
    headers = { 'Content-Type': 'application/json' }

    req = urllib.request.Request(url, data.encode('utf-8'), headers)

    with urllib.request.urlopen(req) as response:
        result = response.read()
        resp = result.decode('utf-8')
#text to speach
        //TODO: make say_text the real one


# Define the URL for the text-to-speech API
url = f'http://localhost:5002/api/tts'

# Prompt the user for input
say_text = input('What should I say? ')

# Send the input text to the API and save the response as a WAV file
response = requests.get(url, params={'text': say_text})
with open('response.wav', 'wb') as f:
    f.write(response.content)
print(f'saved wav for {url}')
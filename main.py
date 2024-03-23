#import stuff
from gpiozero import LED
from gpiozero import Button
import urllib.request
import os
import requests
#define stuff
button = Button(2)
while true:
    while button.is_pressed
        #speach to text
        //TODO: make the varibvle prompt the real one
        //TODO: record
        os.system("vosk-transcriber -i tempquest.mp4 -o tempquest.txt")
        #rest apt
        //TODO: make the varibvle prompt the real one
        url = "http://localhost:11434/api/generate"
        prompt = input("Enter prompt: ")
        data = "{\"model\": \"portagpt\", \"prompt\":\"" + prompt + "\"}"
        headers = { 'Content-Type': 'application/json' }
        req = urllib.request.Request(url, data.encode('utf-8'), headers)
        with urllib.request.urlopen(req) as response:
            result = response.read()
            resp = result.decode('utf-8')
        #text to speach
        //TODO: make say_text the real one
        # Define the URL for the text-to-speech API
        ttsurl = f'http://localhost:5002/api/tts'
        # Prompt the user for input
        say_text = input('What should I say? ')
        # Send the input text to the API and save the response as a WAV file
        response = requests.get(ttsurl, params={'text': say_text})
        with open('response.wav', 'wb') as f:
            f.write(response.content)
        print(f'saved wav for {ttsurl}')
        //TODO: play the audio
from gpiozero import LED
from gpiozero import Button
import urllib.request
import os
import requests

button = Button(2)

while True:
    while button.is_pressed:
        # record
        os.system("arecord --format=cd tempquest.wav")
    # speech to text

    # rest api
    url = "http://localhost:11434/api/generate"
    prompt = input("Enter prompt: ")
    data = "{\"model\": \"portagpt\", \"prompt\":\"" + prompt + "\"}"
    headers = { 'Content-Type': 'application/json' }
    req = urllib.request.Request(url, data.encode('utf-8'), headers)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        resp = result.decode('utf-8')

    # text to speech
    from TTS.api import TTS

    # Initialize the TTS object
    tts = TTS("tts_models/en/vctk/vits")

    # Synthesize speech
    tts.tts_to_file(resp, "output.wav")

    # play the audio
    os.system("aplay output.wav &")
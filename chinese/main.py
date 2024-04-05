from gpiozero import LED
from gpiozero import Button
import urllib.request
import os
import requests
from TTS.api import TTS

button = Button(2)
led = LED(21)

while True:
    while button.is_pressed:
        #shine led
        led.on()
        # record
        os.system("arecord --format=cd tempquest.wav")
    led.off()
    # speech to text
    os.system("vosk-transcriber --model-name vosk-model-cn-0.22 -i tempquest.wav -o tempquest.txt")
    os.system("rm tempquest.wav")
    with open("tempquest.txt", "r") as f:
        prompt = f.read()
    # rest api
    url = "http://localhost:11434/api/generate"
    data = "{\"model\": \"portagpt\", \"prompt\":\"" + prompt + "\"}"
    headers = { 'Content-Type': 'application/json' }
    req = urllib.request.Request(url, data.encode('utf-8'), headers)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        resp = result.decode('utf-8')

    # text to speech

    # Initialize the TTS object
    tts = TTS("tts_models/en/vctk/vits")

    # Synthesize speech 
    tts.tts_to_file(resp, "output.wav")

    # play the audio
    os.system("aplay output.wav &")
from gpiozero import LED
from gpiozero import Button
import urllib.request
import os
import requests
import time
from TTS.api import TTS
button = Button(2)
led = LED(21)
while True:
    os.system("dialog --title \"PortaGPT\" --msgbox 'Waiting' 300 440")
    while button.is_pressed:
        #shine led
        led.on()
        # record
        os.system("arecord --format=cd tempquest.wav")
        buttonispressed = True
    if buttonispressed = True
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
        while not button.is_pressed:
            # display on screen
            os.system("dialog --title \"PortaGPT Response\" --msgbox '" + resp + "' 300 440")
        os.system("dialog --title \"PortaGPT\" --msgbox 'Clearing, please wait.' 300 440")
        buttonispressed = False
        time.sleep(3)
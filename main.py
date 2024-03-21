#import stuff
from gpiozero import LED
from gpiozero import Button
import urllib.request
import os

#rest apt
//TODO: make result.decode('utf-8') a varible resp
//TODO: make the varibvle prompt the real one
url = "http://localhost:11434/api/generate"

while True:
    prompt = input("Enter prompt: ")
    data = "{\"model\": \"llama2\", \"prompt\":\"" + prompt + "\"}"
    headers = { 'Content-Type': 'application/json' }

    req = urllib.request.Request(url, data.encode('utf-8'), headers)

    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf-8'))
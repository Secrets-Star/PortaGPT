sudo bash -c curl -fsSL https://ollama.com/install.sh | sh
sudo apt install arecord
pip install TTS
cd ollama
ollama pull gemma:7b
pip install vosk
ollama create portagpt -f ./Modelfile
cd ..
mkdir vosk
cd vosk
wget https://alphacephei.com/vosk/models/vosk-model-en-us-0.42-gigaspeech.zip
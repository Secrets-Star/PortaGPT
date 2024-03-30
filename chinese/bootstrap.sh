curl -fsSL https://ollama.com/install.sh | sudo sh
pip install TTS
cd ollama
ollama pull gemma:7b
pip install vosk
ollama create portagpt -f ./Modelfile
cd ..
mkdir vosk
cd vosk
wget https://alphacephei.com/vosk/models/vosk-model-cn-0.22.zip
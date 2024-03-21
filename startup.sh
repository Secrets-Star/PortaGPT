sudo apt update
sudo apt full-upgrade
sudo reboot
sudo apt install git python3-venv libopenblas-dev libblas-dev m4 cmake cython python3-dev python3-yaml python3-setuptools libatomic-ops-dev llvm espeak libsndfile1 libzstd1 liblcms2–2 libjbig0 libopenjp2–7 libwebpdemux2 libtiff5 libwebpmux3 libwebp6 libatlas3-base
git clone — single-branch — branch master https://github.com/mozilla/TTS.git
cd TTS
git checkout 2e2221f
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
which python
python --version
which pip
pip --version
pip install -U pip
pip install numpy==1.16.1 matplotlib==3.2.1 bokeh==1.4.0 Flask pyyaml attrdict segments scipy tensorboard tensorboardX Pillow Unidecode>=0.4.20 tqdm soundfile phonemizer
cd .. # gets you out of TTS directory
git clone --recursive https://github.com/pytorch/pytorch -- branch=v1.0.0
cd pytorch
export NO_CUDA=1
export NO_DISTRIBUTED=1
export NO_MKLDNN=1
export NO_NNPACK=1
export NO_QNNPACK=1
pip install pyyaml
sudo apt install libopenblas-dev libblas-dev m4 cmake cython python3-dev python3-yaml python3-setuptools
sudo apt install libatomic-ops-dev
sed -i ‘/set(CMAKE_EXPORT_COMPILE_COMMANDS ON)/a set(CMAKE_CXX_FLAGS “${CMAKE_CXX_FLAGS} -latomic”)’ CMakeLists.txt
python setup.py build
python setup.py install
cd ..
sudo apt install llvm
llvm-config — version
llvm-config — libdir
which llvm-config
LLVM_CONFIG=/usr/bin/llvm-config pip install llvmlite
sudo apt install libatlas3-base
pip install numba==0.49.0
pip install librosa==0.6.2
sudo apt install espeak libsndfile1
sudo apt install libzstd1 liblcms2–2 libjbig0 libopenjp2–7 libwebpdemux2 libtiff5 libwebpmux3 libwebp6
cd TTS
python setup.py develop — no-deps
mkdir wheels
cd wheels/
wget https://github.com/reuben/TTS/releases/download/ljspeech-fwd-attn-pwgan/TTS-0.0.1+92aea2a-py3-none-any.whl
unzip TTS-0.0.1+92aea2a-py3-none-any.whl
cd .. # so you’re back in TTS directory
mkdir -p server/model/tts
cp wheels/TTS/server/model/tts/checkpoint.pth.tar ../server/model/tts/
cp wheels/TTS/server/model/tts/config.json ../server/model/tts/

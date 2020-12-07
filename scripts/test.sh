#! /bin/bash

echo $PATH
sudo apt update -y
pip3 install -r requirements.txt
python3 -m pytest service1 --cov service1
python3 -m pytest service2 --cov service2
python3 -m pytest service3 --cov service3
python3 -m pytest service4 --cov service4
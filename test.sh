!/bin/bash
sudo apt update && sudo apt install python3 python3-pip python3.8-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report=html 

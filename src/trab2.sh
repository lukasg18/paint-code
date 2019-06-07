sudo apt-get update
sudo apt install python3-pip
sudo pip3 install virtualenv
virtualenv venv --python=python3
source venv/bin/activate
pip install lark-parser
python main.py


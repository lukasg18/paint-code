sudo apt-get update
sudo apt-get -yqq install python3-pip python3-tk
sudo pip3 install virtualenv
virtualenv venv --python=python3
source venv/bin/activate
pip install lark-parser
pip install argparse
python main.py


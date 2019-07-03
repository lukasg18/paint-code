sudo apt-get update
sudo apt-get -yqq install python3-pip python3-tk
sudo pip3 install virtualenv
virtualenv venv --python=python3
source venv/bin/activate
pip install lark-parser argparse
cd src/
python main.py --file testes/example-frac2.pc


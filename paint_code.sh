echo "instalando ferramentas necessarias..."
sudo apt-get -yqq install python3-pip python3-tk
echo "instalando virtualenv..."
sudo pip3 install virtualenv
virtualenv venv --python=python3
source venv/bin/activate
echo "instalando depedencias do PaintCode..."
pip install lark-parser argparse
cd src/
python main.py --file testes/example-frac2.pc


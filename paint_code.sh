#!/bin/bash
echo "\n_________instalando ferramentas necessarias..._________\n"
sudo apt-get -yqq install python3-pip python3-tk
echo "\n_________instalando pipenv..."
if sudo pip install pipenv
then
    echo "\n_________instalando depedencias do PaintCode..._________\n"
    pipenv install
    pipenv shell
else
    echo "\n_________Erro ao instalar pipenv_________\n"
    exit 1
fi


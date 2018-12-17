#!/bin/bash
sudo pacman -Sy yaourt &&
yaourt -S --noconfirm sublime-text-dev bpython python-numpy tk python-pandas jupyter-notebook python-pip python-scipy python-pytables python-sqlalchemy python-matplotlib python-openpyxl python-xlrd python-xlwt python-xlsxwriter python-beautifulsoup4
sudo pip3 install tqdm sklearn lightgbm
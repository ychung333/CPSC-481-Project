// Because my pc have 2 versions of python so i need indicate to specific version that pygame can install
py -3.11 -m venv venv_pygame

// If only one python version in your pc and then plase intall pygame by this
python -m venv venv

// My case run this to activate venv
venv_pygame\Scripts\activate

// Normally run this to activate venv
venv\Scripts\activate

// Install in order to run game, aslo download this
pip install pygame
pip install numpy

// run game plz use this
python tictactoe.py

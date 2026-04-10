// Because my pc have 2 versions of python so i need indicate to specific version that pygame can install
py -3.11 -m venv venv_pygame

// If only one python and that is for pygame install
python -m venv venv

// My case run this
venv_pygame\Scripts\activate

// Normally run this
venv\Scripts\activate

// Install in order to run game
pip install pygame
pip install numpy

// run game
python tictactoe.py
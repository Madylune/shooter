import pygame
from components.player import Player

class Game:
  def __init__(self):
    # Generate a new player
    self.player = Player()
    self.pressed = {}

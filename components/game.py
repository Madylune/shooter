import pygame
from components.player import Player
from components.monster import Monster

class Game:
  def __init__(self):
    # Generate a new player
    self.player = Player()
    # Create an empty group of monsters
    self.all_monsters = pygame.sprite.Group()
    # Get pressed keys
    self.pressed = {}

    # Generate monsters when initialization
    self.spawn_monster()

  def spawn_monster(self):
    monster = Monster()
    self.all_monsters.add(monster)

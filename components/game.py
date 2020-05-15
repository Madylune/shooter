import pygame
from components.player import Player
from components.monster import Monster

class Game:
  def __init__(self):
    # Generate a new player
    self.all_players = pygame.sprite.Group()
    self.player = Player(self)
    self.all_players.add(self.player)
    # Create an empty group of monsters
    self.all_monsters = pygame.sprite.Group()
    # Get pressed keys
    self.pressed = {}

    # Generate monsters when initialization
    self.spawn_monster()
    self.spawn_monster()

  def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

  def spawn_monster(self):
    monster = Monster(self)
    self.all_monsters.add(monster)

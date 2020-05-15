import pygame
from components.projectile import Projectile

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__() # Inits the super class from parent (Sprite)
    self.health = 100
    self.max_health = 100
    self.attack = 10
    self.velocity = 5 # Moving speed
    self.all_projectiles = pygame.sprite.Group()

    self.image = pygame.image.load('assets/player.png')
    self.rect = self.image.get_rect() # Know image's side
    self.rect.x = 450
    self.rect.y = 500

  def launch_projectile(self):
    self.all_projectiles.add(Projectile(self))

  def move_right(self):
    self.rect.x += self.velocity

  def move_left(self):
    self.rect.x -= self.velocity

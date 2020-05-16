import pygame
from components.player import Player
from components.monster import Monster

class Game:
  def __init__(self):
    # Starting screen
    self.is_playing = False
    # Generate a new player
    self.all_players = pygame.sprite.Group()
    self.player = Player(self)
    self.all_players.add(self.player)
    # Create an empty group of monsters
    self.all_monsters = pygame.sprite.Group()
    # Get pressed keys
    self.pressed = {}

  def start(self):
    self.is_playing = True
    # Generate monsters when initialization
    self.spawn_monster()
    self.spawn_monster()

  def game_over(self):
    # Reset game
    self.all_monsters = pygame.sprite.Group()
    self.player.health = self.player.max_health
    self.is_playing = False

  def update(self, screen):
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)

    # Projectiles' moving
    for projectile in self.player.all_projectiles:
      projectile.move()

    # Monsters' moving
    for monster in self.all_monsters:
      monster.forward()
      monster.update_health_bar(screen)
    
    # Draw sprites on the screen
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)

    # Player's moving
    if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
      self.player.move_right()
    elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
      self.player.move_left()

  def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

  def spawn_monster(self):
    monster = Monster(self)
    self.all_monsters.add(monster)

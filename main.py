import pygame
import math
from components.game import Game
pygame.init()

pygame.display.set_caption("Shooter")

screen = pygame.display.set_mode((1080, 720))
background_image = pygame.image.load('assets/bg.jpg')

# Starting screen
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 1.8)

# Load the game
game = Game()

game_is_running = True

while game_is_running:
  screen.blit(background_image, (0, -200))

  if game.is_playing:
    game.update(screen)
  else:
    screen.blit(banner, banner_rect)
    screen.blit(play_button, play_button_rect)

  # Update screen
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_is_running = False
      pygame.quit()

    elif event.type == pygame.KEYDOWN:
      game.pressed[event.key] = True
      if event.key == pygame.K_SPACE:
        game.player.launch_projectile()

    elif event.type == pygame.KEYUP:
      game.pressed[event.key] = False
      
    elif event.type == pygame.MOUSEBUTTONDOWN:
      # Check collision between mouse and button
      if play_button_rect.collidepoint(event.pos):
        game.start()
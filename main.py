import pygame
from components.game import Game
pygame.init()

pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1080, 720))
background_image = pygame.image.load('assets/bg.jpg')

# Load the game
game = Game()

app_is_running = True

while app_is_running:
  screen.blit(background_image, (0, -200))
  screen.blit(game.player.image, game.player.rect)

  game.player.update_health_bar(screen)

  # Projectiles' moving
  for projectile in game.player.all_projectiles:
    projectile.move()

  # Monsters' moving
  for monster in game.all_monsters:
    monster.forward()
    monster.update_health_bar(screen)
  
  # Draw sprites on the screen
  game.player.all_projectiles.draw(screen)
  game.all_monsters.draw(screen)

  # Player's moving
  if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
    game.player.move_right()
  elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
    game.player.move_left()

  # Update screen
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      app_is_running = False
      pygame.quit()

    elif event.type == pygame.KEYDOWN:
      game.pressed[event.key] = True
      if event.key == pygame.K_SPACE:
        game.player.launch_projectile()

    elif event.type == pygame.KEYUP:
      game.pressed[event.key] = False
      
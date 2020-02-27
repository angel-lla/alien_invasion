import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf

def run_game():
    """Initialize game and create a screen object."""

    pygame.init()

    # Instance of Settings
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statisctics.
    stats = GameStats(ai_settings)

    # Make a ship
    ship = Ship(ai_settings=ai_settings, screen=screen)

    # Make an alien
    #alien = Alien(ai_settings, screen)
    aliens = Group()

    # Make a group to store bullets in.
    bullets = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens)

    # Start the main loop for the game.
    while True:
        # Call check_events method to watch for keyboard and mouse events.
        gf.check_events(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens, bullets=bullets)

run_game()
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

fontOne = pygame.font.SysFont("comicsansms", 75)
fontTwo = pygame.font.SysFont("comicsansms", 60)


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play Space Invaders")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    bg_color = (230, 230, 230)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


def text_objects(text, color, size):
    if size == "fontOne":
        textSurface = fontOne.render(text, True, color)
    elif size == "fontTwo":
        textSurface = fontTwo.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(self, msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (300),(200 + y_displace)
    self.ai_settings.blit(textSurf, textRect)


def game_intro(self):
    intro = True
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                intro = False
        self.ai_settings.fill(black)
        message_to_screen("SPACE", white, -100, "fontOne")
        message_to_screen("INVADERS", green, -150, "fontTwo")
        pygame.display.update()


game_intro()
run_game()

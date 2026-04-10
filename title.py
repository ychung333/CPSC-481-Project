import pygame

# colors matching main code
white = (255, 255, 255)
gray = (200, 200, 200)
green = (0, 255, 0)
black = (0, 0, 0)

# same screen size as main code
width = 300
height = 300


def draw_title_screen(screen):
    screen.fill(black)

    title_font = pygame.font.SysFont(None, 42)
    info_font = pygame.font.SysFont(None, 24)
    button_font = pygame.font.SysFont(None, 30)

    # title text
    title_text = title_font.render("TIC TAC TOE", True, white)
    title_rect = title_text.get_rect(center=(width // 2, 70))
    screen.blit(title_text, title_rect)

    # info text
    info_text = info_font.render("Play against AI", True, gray)
    info_rect = info_text.get_rect(center=(width // 2, 110))
    screen.blit(info_text, info_rect)

    # start button
    start_button = pygame.Rect(90, 170, 120, 50)
    pygame.draw.rect(screen, green, start_button, border_radius=8)

    start_text = button_font.render("START", True, black)
    start_rect = start_text.get_rect(center=start_button.center)
    screen.blit(start_text, start_rect)

    return start_button
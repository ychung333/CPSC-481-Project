import pygame

# colors matching main code
white = (255, 255, 255)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# same screen size as main code
width = 300
height = 300


def draw_result_screen(screen, result_message):
    screen.fill(black)

    title_font = pygame.font.SysFont(None, 40)
    button_font = pygame.font.SysFont(None, 26)
    small_font = pygame.font.SysFont(None, 22)

    # choose result color
    if result_message == "You Win!":
        result_color = green
    elif result_message == "You Lose!":
        result_color = red
    else:
        result_color = gray

    # result text
    result_text = title_font.render(result_message, True, result_color)
    result_rect = result_text.get_rect(center=(width // 2, 80))
    screen.blit(result_text, result_rect)

    # question text
    question_text = small_font.render("Do you want to continue?", True, white)
    question_rect = question_text.get_rect(center=(width // 2, 125))
    screen.blit(question_text, question_rect)

    # yes button
    yes_button = pygame.Rect(45, 180, 90, 45)
    pygame.draw.rect(screen, green, yes_button, border_radius=8)

    yes_text = button_font.render("YES", True, black)
    yes_rect = yes_text.get_rect(center=yes_button.center)
    screen.blit(yes_text, yes_rect)

    # no button
    no_button = pygame.Rect(165, 180, 90, 45)
    pygame.draw.rect(screen, red, no_button, border_radius=8)

    no_text = button_font.render("NO", True, black)
    no_rect = no_text.get_rect(center=no_button.center)
    screen.blit(no_text, no_rect)

    return yes_button, no_button
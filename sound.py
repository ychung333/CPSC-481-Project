import pygame

current_bgm = None

def init_audio():
    pygame.mixer.init()

def play_bgm(path, volume=0.5):
    global current_bgm
    if current_bgm != path:
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        current_bgm = path

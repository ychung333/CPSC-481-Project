import pygame

# keep track of what BGM is currently playing
# this prevents restarting the same music again and again
current_bgm = None

def init_audio():
    # initialize the pygame mixer (audio system)
    pygame.mixer.init()

def play_bgm(path, volume=0.5):
    global current_bgm

    # only change music if it's moving screen from title. game and result screen are run same music
    if current_bgm != path:
        pygame.mixer.music.load(path)        # load the music file
        pygame.mixer.music.set_volume(volume)  # set volume (0.0 to 1.0)
        pygame.mixer.music.play(-1)          # play in loop (-1 = infinite loop)
        current_bgm = path                  # remember current playing BGM

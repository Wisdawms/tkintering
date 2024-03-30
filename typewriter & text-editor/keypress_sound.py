import pygame, random, os

# Initialize Pygame Mixer
pygame.mixer.init()

sound_files = []
dirs = os.listdir("media/keyboardsounds")
for dir in dirs:
    sounds = os.listdir(f"media/keyboardsounds/{dir}")
    for sound in sounds:
        sound_files.append(f"{dir}/{sound}")

sounds = [
    pygame.mixer.Sound(f"media/keyboardsounds/{sound_file}")
    for sound_file in sound_files
]


def keypress_sound():
    random.choice(sounds).play()

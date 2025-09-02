import pygame

pygame.init()
pygame.mixer.init()

pos_beep = pygame.mixer.Sound("pos_beep.wav")
pos_beep.play()

pygame.time.wait(1000)
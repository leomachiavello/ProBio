import pygame

pygame.init()

delay = 1000  # 1000 ms = 1 segundo
next_action = pygame.time.get_ticks() + delay

clock = pygame.time.Clock()
running = True

while running:
    # Procesar eventos (necesario aunque no hagas nada)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    now = pygame.time.get_ticks()
    if now >= next_action:
        print("Un segundo pasó")
        next_action = now + delay

    clock.tick(60)  # limita a 60 iteraciones por segundo

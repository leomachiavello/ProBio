import pygame
import random

pygame.init()
pygame.mixer.init()

pos_beep = pygame.mixer.Sound("pos_beep.wav")

info = pygame.display.Info()
width, height = info.current_w, info.current_h

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

def cross():
    screen.fill((0, 0, 0))
    pygame.display.flip()

    color = (255, 255, 255) #color blanco
    thck = 2
    line_len = 20

    pygame.draw.line(screen, color, (width // 2, (height//2)-line_len), (width // 2, (height//2)+line_len), thck)   # línea vertical
    pygame.draw.line(screen, color, ((width//2)-line_len, height // 2), ((width//2)+line_len, height // 2), thck)  # línea horizontal

def point(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 7.5)
    pygame.display.flip()
    

cross()
pygame.display.flip()

clock = pygame.time.Clock()

n = 5                  # cantidad de puntos
delay_ms = 1000        # 1000 ms = 1 segundo (on/off)
blinks_left = 0        # contador de pasos
next_toggle = 0        # próximo cambio
point_visible = False
px, py = 0, 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
            elif event.key == pygame.K_RETURN:
                
                blinks_left = n * 2
                point_visible = False
                next_toggle = pygame.time.get_ticks()  # empieza ya

            elif event.key == pygame.K_SPACE:
                if point_visible:
                    pos_beep.play()

    now = pygame.time.get_ticks()
    if blinks_left > 0 and now >= next_toggle:
        point_visible = not point_visible
        blinks_left -= 1
        next_toggle = now + delay_ms

        if point_visible:
            # si toca mostrar, elegir nueva posición aleatoria
            px = random.randint(0, width - 1)
            py = random.randint(0, height - 1)

    # --- Dibujar frame ---
    cross()
    if point_visible:
        point(px, py)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
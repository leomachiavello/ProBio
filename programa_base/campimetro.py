import pygame
import random
import math

pygame.init()
pygame.mixer.init()

pos_beep = pygame.mixer.Sound("pos_beep.wav")

info = pygame.display.Info()
width, height = info.current_w, info.current_h
matrix_x, matrix_y = 8, 9
cell = 80

gw = matrix_y * cell
gh = matrix_x * cell
sx = (width - gw) // 2
sy = (height - gh) // 2

start_x_point = sx + cell//2
start_y_point = sy + cell//2

x_cords = []
y_cords = []

x_point = start_x_point
y_point = start_y_point

for i in range(matrix_x):
    x_cords.append(x_point)
    x_point += cell
    
for i in range(matrix_y-1):
    y_cords.append(y_point)
    y_point += cell

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

class pointFinal():
    def __init__(self, x, y, alpha):
        self.x = x
        self.y = y
        self.alpha = alpha
        self.check = False
    def correct(self):
        self.check = True

def calculate_db(intensity):
    # 1e-6 como referencia 
    I_0 = 1e-6
    db = 10 * math.log10(intensity / I_0)
    return db

def cross():
    color = (255, 255, 255) #color blanco
    thck = 2
    line_len = 10

    pygame.draw.line(screen, color, (width // 2, (height//2)-line_len), (width // 2, (height//2)+line_len), thck)   # línea vertical
    pygame.draw.line(screen, color, ((width//2)-line_len, height // 2), ((width//2)+line_len, height // 2), thck)  # línea horizontal
    
def matrix(rows=matrix_x, cols=matrix_y, cell_size=cell):
    # Calcular las coordenadas para centrar la matriz
    grid_width = cols * cell_size
    grid_height = rows * cell_size
    start_x = (width - grid_width) // 2
    start_y = (height - grid_height) // 2

    color = (255, 255, 255)  # Color de las celdas (blanco)
    line_thickness = 2  # Grosor de las líneas de la cuadrícula

    # Dibujar la cuadrícula
    for row in range(rows + 1):  # +1 para la última línea (abajo)
        pygame.draw.line(screen, color, (start_x, start_y + row * cell_size), 
                         (start_x + grid_width, start_y + row * cell_size), line_thickness)

    for col in range(cols + 1):  # +1 para la última línea (a la derecha)
        pygame.draw.line(screen, color, (start_x + col * cell_size, start_y), 
                         (start_x + col * cell_size, start_y + grid_height), line_thickness)

    pygame.display.flip()

def point(point_obj):
    color = (255, 255, 255, point_obj.alpha)  # RGB + Alfa (transparencia)
    point_surface = pygame.Surface((15, 15), pygame.SRCALPHA)  # Superficie con canal alfa
    pygame.draw.circle(point_surface, color, (7, 7), 7)  # Dibujar el círculo en la superficie
    screen.blit(point_surface, (point_obj.x - 7, point_obj.y - 7))  # Colocar el punto en las coordenadas
    pygame.display.flip()

clock = pygame.time.Clock()

n = 5                  # cantidad de puntos
delay_ms = 1000        # 1000 ms = 1 segundo (on/off)
blinks_left = 0        # contador de pasos
next_toggle = 0        # próximo cambio
started = False        # flag de inicio para el programa
point_visible = False
space_counter = 0      # contador de veces que se presiona el espacio
fp_counter = 0         # contador de falsos positivos
px, py = 0, 0
matrix_flag = True
change = False
point_spawn = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
            elif event.key == pygame.K_RETURN:
                point_list = list()
                blinks_left = n * 2
                started = True
                point_visible = False
                next_toggle = pygame.time.get_ticks()  # empieza ya

            elif event.key == pygame.K_SPACE:
                if started:
                    space_counter+=1
                    if point_visible:
                        point_list[-1].correct()
                        pos_beep.play()
                    if not point_visible:
                        fp_counter+=1

            elif event.key == pygame.K_m:
                matrix_flag = not matrix_flag
            
    now = pygame.time.get_ticks()
    if blinks_left > 0 and now >= next_toggle:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        point_visible = not point_visible
        blinks_left -= 1
        next_toggle = now + delay_ms
        

        if point_visible:
            # si toca mostrar, elegir nueva posición aleatoria
            px = random.choice(x_cords)
            py = random.choice(y_cords)
            alpha = 100 # intensidad del punto
            point_list.append(pointFinal(px, py, alpha)) # se crea un objeto point con la posición del punto
            point_spawn = True
            
    # --- Dibujar frame ---
    if matrix_flag:
        if not change:
            screen.fill((0, 0, 0))
        matrix()
        change = True
    else:
        if change:
            screen.fill((0, 0, 0))
            change = False
        cross()
    if point_visible and point_spawn:
        point(point_list[-1])
        point_spawn = False
    pygame.display.flip()
    
    # Una vez termina de mostrar los puntos, lo imprime
    if blinks_left == 0 and started:
        started = False
        print("Lista de puntos:")
        for pt in point_list:
            print(f"({pt.x}, {pt.y}, Alpha = {pt.alpha}) - {pt.check}")
        print(f"Presiones totales: {space_counter}")
        print(f"Falsos positivos: {fp_counter}")
        space_counter = 0
        fp_counter = 0
        
    clock.tick(60)

pygame.quit()
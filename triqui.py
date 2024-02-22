import pygame

# Inicialización de pygame
pygame.init()   

# Espacio de la pantalla del juego
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("TRIQUI")

# Creación de variables con su imagen
fondo = pygame.image.load('static/tictactoe_background.png')
circulo = pygame.image.load('static/circle.png')
equis = pygame.image.load('static/x.png')

# Tamaño de los elementos Equis y Círculo y la imagen de fondo
fondo = pygame.transform.scale(fondo, (450, 450))
circulo = pygame.transform.scale(circulo, (125, 125))
equis = pygame.transform.scale(equis, (125, 125))

# Coordenadas del tablero
coor = [[(40, 50), (165, 50), (290, 50)],
        [(40, 175), (165, 175), (290, 175)],
        [(40, 300), (165, 300), (290, 300)]]

# Espacios del tablero
tablero = [['', '', ''],
           ['', '', ''],
           ['', '', '']]

# Se inicia con el turno X
turno = 'X'
game_over = False
clock = pygame.time.Clock()

# Fuente para el texto
font = pygame.font.Font(None, 36)

# Función para mostrar texto en pantalla
def mostrar_mensaje(texto):
    mensaje = font.render(texto, True, (255, 255, 255))
    rect = mensaje.get_rect(center=screen.get_rect().center)
    screen.blit(mensaje, rect)

# Mostrar en el tablero X o O
def graficar_board():
    screen.blit(fondo, (0, 0))
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 'X':
                dibujar_x(fila, col)
            elif tablero[fila][col] == 'O':
                dibujar_0(fila, col)

def dibujar_x(fila, col):
    screen.blit(equis, coor[fila][col])

def dibujar_0(fila, col):
    screen.blit(circulo, coor[fila][col])

# Función para definir ganador
def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
        return True
    return False

while not game_over:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (40 <= mouseX < 415) and (50 <= mouseY < 425):
                fila = (mouseY - 50) // 125
                col = (mouseX - 40) // 125
                if tablero[fila][col] == '':
                    tablero[fila][col] = turno
                    fin_juego = verificar_ganador()
                    if fin_juego:
                        mensaje = f"El jugador {turno} ha ganado!!"
                        mostrar_mensaje(mensaje)
                        pygame.display.update()
                        pygame.time.wait(3000)  # Espera 3 segundos antes de salir
                        game_over = True
                    turno = 'O' if turno == 'X' else 'X'

    graficar_board()
    pygame.display.update()

# Finalización de pygame
pygame.quit()
    
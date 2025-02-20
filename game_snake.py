import pygame
import time
import random

pygame.init()

# colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Dimensiones de la ventana
ancho_pantalla = 800
alto_pantalla = 600

pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Juego de la Serpiente')

tamaño_bloque = 20
velocidad_serpiente = 11

reloj = pygame.time.Clock()


# Puntuación
mejor_puntuacion = 0

def mostrar_puntuacion(puntuacion):
    fuente_puntacion = pygame.font.SysFont(None, 35)
    texto = fuente_puntacion.render("Puntuación: " + str(puntuacion), True, blanco)
    pantalla.blit(texto, [10, 10])  

def mostrar_mejor_puntuacion(mejor_puntuacion):
    fuente_mejor = pygame.font.SysFont(None, 35)
    texto = fuente_mejor.render("Mejor Puntuación: " + str(mejor_puntuacion), True, blanco)
    pantalla.blit(texto, [10, 50])  

def dibujar_serpiente(tamaño_bloque, lista_serpiente):
    for x in lista_serpiente:
        pygame.draw.rect(pantalla, verde, [x[0], x[1], tamaño_bloque, tamaño_bloque])

def mensaje(msg, color, x, y):
    fuente = pygame.font.SysFont('times new roman', 30)
    texto = fuente.render(msg, True, color)
    pantalla.blit(texto, [x, y])  

def pantalla_inicio():
    pantalla.fill(negro)
    mensaje("¡Bienvenido al Juego de la Serpiente!", verde, ancho_pantalla / 5, alto_pantalla / 3)
    mensaje("Presiona S para iniciar o Q para salir.", azul, ancho_pantalla / 5, alto_pantalla / 3 + 40)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_s:
                    return

def pantalla_perdida():
    pantalla.fill(negro)
    mensaje("¡Oh no! Perdiste", rojo, ancho_pantalla / 3, alto_pantalla / 3)
    mensaje("Presiona C para jugar de nuevo o Q para salir.", rojo, ancho_pantalla / 9, alto_pantalla / 3 + 40)
    pygame.display.update()
    time.sleep(2)

def juego():
    global mejor_puntuacion
    pantalla_inicio()
    game_over = False
    game_cerrado = False

    x1 = ancho_pantalla / 2
    y1 = alto_pantalla / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_serpiente = []
    longitud_serpiente = 1

    comida_x = round(random.randrange(0, ancho_pantalla - tamaño_bloque) / 20.0) * 20.0
    comida_y = round(random.randrange(0, alto_pantalla - tamaño_bloque) / 20.0) * 20.0

    while not game_over:

        while game_cerrado:
            pantalla_perdida()
            mostrar_puntuacion(longitud_serpiente - 1)
            mostrar_mejor_puntuacion(mejor_puntuacion)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_cerrado = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_bloque
                    y1_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_bloque
                    y1_cambio = 0
                elif event.key == pygame.K_UP:
                    y1_cambio = -tamaño_bloque
                    x1_cambio = 0
                elif event.key == pygame.K_DOWN:
                    y1_cambio = tamaño_bloque
                    x1_cambio = 0

        if x1 >= ancho_pantalla or x1 < 0 or y1 >= alto_pantalla or y1 < 0:
            game_cerrado = True
            if longitud_serpiente - 1 > mejor_puntuacion:
                mejor_puntuacion = longitud_serpiente - 1

        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(negro)
        pygame.draw.rect(pantalla, rojo, [comida_x, comida_y, tamaño_bloque, tamaño_bloque])
        cabeza_serpiente = []
        cabeza_serpiente.append(x1)
        cabeza_serpiente.append(y1)
        lista_serpiente.append(cabeza_serpiente)
        if len(lista_serpiente) > longitud_serpiente:
            del lista_serpiente[0]

        for x in lista_serpiente[:-1]:
            if x == cabeza_serpiente:
                game_cerrado = True
                if longitud_serpiente - 1 > mejor_puntuacion:
                    mejor_puntuacion = longitud_serpiente - 1

        dibujar_serpiente(tamaño_bloque, lista_serpiente)
        mostrar_puntuacion(longitud_serpiente - 1)
        mostrar_mejor_puntuacion(mejor_puntuacion)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho_pantalla - tamaño_bloque) / 20.0) * 20.0
            comida_y = round(random.randrange(0, alto_pantalla - tamaño_bloque) / 20.0) * 20.0
            longitud_serpiente += 1

        reloj.tick(velocidad_serpiente)

    pygame.quit()
    quit()

juego()

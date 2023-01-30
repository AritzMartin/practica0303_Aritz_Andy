import pygame

pygame.init()

ventana = pygame. display.set_mode((640, 480))
pygame.display.set_caption('Ejemplo 1')

ball = pygame.image.load("Bola.png")
ancho = 30
alto = 30
imag_redimensionada = pygame.transform.scale(ball, (ancho, alto))
ballrect = imag_redimensionada.get_rect()
speed = [4,4]
ballrect.move_ip(0,0)

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
    ventana.fill((255, 255, 255))
    ventana.blit(imag_redimensionada, ballrect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
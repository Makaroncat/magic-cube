import pygame, sys

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MF',30)
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("МОЯ ИГРА")


clock = pygame.time.Clock()
FPS = 60
Name = 'Makaron'
BLACK = (0, 0,0)
WHITE = (255,255,255)




rect = pygame.Rect((70,70), (32,32))
image = pygame.Surface((32,32))
image.fill(WHITE)

speed = 1
movement = (0,0)

while True:

    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movement = (0,-speed)
            elif event.key == pygame.K_s:
                movement = (0, speed)
            elif event.key == pygame.K_d:
                movement = (speed,0)
            elif event.key == pygame.K_a:
                movement = (-speed,0)
            elif event.key == pygame.K_UP:
                speed+=1
            elif event.key == pygame.K_DOWN:
                speed-=1


    rect.move_ip(movement)
    if rect.topleft[1] < 0:
        rect = rect.move(0, 720)
    elif rect.topleft[1] > 720:
        rect = rect.move(0, -720)
    screen.fill(BLACK)
    speed+=100

    text_surface = my_font.render(f'Скорость: {speed}',False,WHITE)
    screen.blit(text_surface,(20,20))
    screen.blit(image,rect)
    pygame.display.update()



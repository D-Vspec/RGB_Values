import pygame
import json

pygame.init()
surface = pygame.display.set_mode((500, 625),pygame.RESIZABLE)

running =  True
while running:
    color_list = []

    f = open('colors.json')
    data = json.load(f)

    for i in data['colors']:
        print(i['color'])
        color_list.append(i['color'])

    f.close()

    x,y = surface.get_size()

    for i in range(0,5):
        pygame.draw.rect(surface, color_list[i], pygame.Rect(0, i*(y/5),(x) , y/5))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

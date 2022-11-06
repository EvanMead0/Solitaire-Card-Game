import os
import pygame

def update():
    pygame.display.flip()
    screen.blit(backdrop, (0, 0))

    screen.blit(standard, (280, 160))
    screen.blit(python, (360, 160))
    screen.blit(draw_1, (120, 150))
    screen.blit(draw_3, (120, 210))

    if selected_card_type == "sprites/card_back.png":
        screen.blit(selected, (278, 158))
    elif selected_card_type == "sprites/python_back.png":
        screen.blit(selected, (358, 158))

    if standard_box.collidepoint(pygame.mouse.get_pos()):
        screen.blit(highlight, (280, 160))
    if python_box.collidepoint(pygame.mouse.get_pos()):
        screen.blit(highlight, (360, 160))

runing = True

selected_card_type = ""

backdrop = pygame.image.load("sprites/backdrop.png")
standard = pygame.image.load("sprites/card_display.png")
python = pygame.image.load("sprites/python_display.png")
highlight = pygame.image.load("sprites/highlight_display.png")
selected = pygame.image.load("sprites/select.png")
draw_1 = pygame.image.load("sprites/draw1.png")
draw_3 = pygame.image.load("sprites/draw3.png")

standard_box = pygame.Rect(280, 150, 70, 90)
python_box = pygame.Rect(340, 150, 70, 90)

WINDOW_WIDTH = 560
WINDOW_HEIGHT = 360

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Solitaire')  

while runing:
    update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if standard_box.collidepoint(pygame.mouse.get_pos()):
                selected_card_type = "sprites/card_back.png"
            if python_box.collidepoint(pygame.mouse.get_pos()):
                selected_card_type = "sprites/python_back.png"
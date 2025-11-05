import Types
import pygame

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700

GRID_SIZE = 100
GRID_LINE_WIDTH = 2

CONNECTING_LINE_WIDTH = 5

TYPE_ICONS = {
    Types.NodeTypes.GOAL :          pygame.image.load("Assets/0.png"),
    Types.NodeTypes.ENEMIES :       pygame.image.load("Assets/1.png"),
    Types.NodeTypes.CLEAN_UP:       pygame.image.load("Assets/2.png"),
    Types.NodeTypes.SPEED_SAIL:     pygame.image.load("Assets/3.png"),
    Types.NodeTypes.BARRIER :       pygame.image.load("Assets/4.png"),
    Types.NodeTypes.FISHERS :       pygame.image.load("Assets/5.png"),
    Types.NodeTypes.SHOP :          pygame.image.load("Assets/6.png")
}
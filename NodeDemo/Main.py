#clears the console cuz vscode doesn't do that automatically 
import os

os.system("cls")

import pygame
import Constants
import random
from Node import Node
from typing import List
from Path import Path


window = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT), pygame.DOUBLEBUF | pygame.HWACCEL)

# Set up timer
clock = pygame.time.Clock()

run = True

bottom = pygame.image.load("Assets/bottom.png")

def redraw():
    window.fill((101,157,242))
    
    intWorldPos = pygame.Vector2(int(worldPosition.x), int(worldPosition.y))
    
    nodesToRemove:List[Node] = []
    
    path:Path
    
    rootPath.Draw(window, worldPosition)
        
        
    # for x in range(int(Constants.WINDOW_WIDTH/Constants.GRID_SIZE)):
    #     pygame.draw.line(window, (255, 255, 255), (x*Constants.GRID_SIZE, 0), (x*Constants.GRID_SIZE, Constants.WINDOW_HEIGHT), Constants.GRID_LINE_WIDTH)
    # for y in range(int(Constants.WINDOW_HEIGHT/Constants.GRID_SIZE)):
    #     pygame.draw.line(window, (255, 255, 255), (0, y*Constants.GRID_SIZE), (Constants.WINDOW_WIDTH, y*Constants.GRID_SIZE), Constants.GRID_LINE_WIDTH)
   
    window.blit(bottom, (0,Constants.WINDOW_HEIGHT-66))
   
    pygame.display.flip()



worldPosition:pygame.Vector2 = pygame.Vector2(0,0)

rootPath = Path(Node(5, 4), 0, 0)
rootPath.AddPaths()



moveTimer = 0
hasMoved = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    redraw()
    
    deltaTime = clock.tick()* 0.001 
    
    move = pygame.key.get_pressed()[pygame.K_UP]
    
    moveTimer += deltaTime
    if move and not hasMoved:
        moveTimer = 0
        hasMoved = True
        worldPosition.y+=1
        rootPath.Update(worldPosition)
        rootEndPos = worldPosition.y + rootPath.lastNode.position.y
        if rootEndPos == 5:
            r = random.randint(0,1)
            if r == 0:
                rootPath.lastNode.GoLeft()
                worldPosition.x -=1
            else:
                rootPath.lastNode.GoRight()
                worldPosition.x +=1
        elif rootEndPos >= 6:
            rootPath.AddPaths()
            del rootPath.lastNode.right
            del rootPath.lastNode.left
            oldPath = rootPath
            rootPath = rootPath.lastNode.chosen
            oldPath.nodes = []
            del oldPath
    elif hasMoved and not move:
        hasMoved = False

pygame.quit()
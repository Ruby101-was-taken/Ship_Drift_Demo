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

def redraw():
    window.fill((0,0,0))
    
    intWorldPos = pygame.Vector2(int(worldPosition.x), int(worldPosition.y))
    
    nodesToRemove:List[Node] = []
    
    path:Path
    
    for path in paths:
        path.Draw(window, worldPosition)
        
        
    for x in range(int(Constants.WINDOW_WIDTH/Constants.GRID_SIZE)):
        pygame.draw.line(window, (255, 255, 255), (x*Constants.GRID_SIZE, 0), (x*Constants.GRID_SIZE, Constants.WINDOW_HEIGHT), Constants.GRID_LINE_WIDTH)
    for y in range(int(Constants.WINDOW_HEIGHT/Constants.GRID_SIZE)):
        pygame.draw.line(window, (255, 255, 255), (0, y*Constants.GRID_SIZE), (Constants.WINDOW_WIDTH, y*Constants.GRID_SIZE), Constants.GRID_LINE_WIDTH)
   
   
    pygame.display.flip()
    

# def AddNode(node:Node, connectedNode:Node)->Node:
#     if len(nodes) > 0:
#         node.nextNodes.append(connectedNode)
#     nodes.append(node)
#     print(f"The current amount of nodes: {len(nodes)}")
#     return node
    
# def GeneratePath(length:int, x:int, lastNode:Node=None):
#     nodeAtPos = GetNodeAtPos(lastNode.position.x+x, lastNode.position.y-1) 
#     if nodeAtPos == None:
#         node:Node = AddNode(Node(lastNode.position.x+x, lastNode.position.y-1), lastNode)
#         length-=1
#         if length > 0:
#             GeneratePath(length, 0, nodes[-1])
#         else:
#             node.needsToSplit = True # tells the last node it needs to split
#     else:
#         lastNode.nextNodes.append(nodeAtPos)
        
# def GeneratePathsFromNode(node:Node, pathLength:int):
#     paths = random.randint(2, 2)
#     print(paths)
#     if paths == 2:
#         pathPos = [-1, 1]
#     else:
#         pathPos = [-1, 0, 1]
#     for i in range(paths):
#         GeneratePath(pathLength, pathPos[i], node)
        
# def GetNodeAtPos(x:int, y:int)->Node:
#     newPosition = pygame.Vector2(x, y)
#     for node in nodes:
#         if node.position == newPosition:
#             return node
#     return None

def AddPath(path:Path):
    paths.append(path)
def GeneratePath():
    pathSplits = random.randint(2, 2)
    pathLength = random.randint(3, 7)
    if pathSplits == 2:
        pathPos = [-1, 1]
    else:
        pathPos = [-1, 0, 1]
    for i in range(pathSplits):
        Path(paths[0].nodes[-1], pathLength, pathPos[i])

worldPosition:pygame.Vector2 = pygame.Vector2(0,0)

nodes:List[Node] = []
p = Path(Node(5, 4), 3, 1)

paths:List[Path] = [p]

GeneratePath()


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
        worldPosition.y += 1
        
        
        for node in nodes:
            node.Update(worldPosition)
    elif hasMoved and not move:
        hasMoved = False

pygame.quit()
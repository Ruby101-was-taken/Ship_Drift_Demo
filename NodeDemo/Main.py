#clears the console cuz vscode doesn't do that automatically 
import os

os.system("cls")

import pygame
import Constants
import random
from Node import Node
from typing import List


window = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT), pygame.DOUBLEBUF | pygame.HWACCEL)

# Set up timer
clock = pygame.time.Clock()

run = True

def redraw():
    window.fill((0,0,0))
    
    intWorldPos = pygame.Vector2(int(worldPosition.x), int(worldPosition.y))
    
    nodesToRemove:List[Node] = []
    
    node:Node
    for node in nodes:
        pos:pygame.Vector2 = node.Draw(window, intWorldPos)
        
        if pos.y > Constants.WINDOW_HEIGHT:
            nodesToRemove.append(node)
        
    for x in range(int(Constants.WINDOW_WIDTH/Constants.GRID_SIZE)):
        pygame.draw.line(window, (255, 255, 255), (x*Constants.GRID_SIZE, 0), (x*Constants.GRID_SIZE, Constants.WINDOW_HEIGHT), Constants.GRID_LINE_WIDTH)
    for y in range(int(Constants.WINDOW_HEIGHT/Constants.GRID_SIZE)):
        pygame.draw.line(window, (255, 255, 255), (0, y*Constants.GRID_SIZE), (Constants.WINDOW_WIDTH, y*Constants.GRID_SIZE), Constants.GRID_LINE_WIDTH)
        
    for node in nodes:
        node.DrawConnections(window, intWorldPos)
        
    for node in nodesToRemove:
        nodes.remove(node)
        
    pygame.display.flip()
    

def AddNode(node:Node, connectedNode:Node)->Node:
    if len(nodes) > 0:
        node.nextNodes.append(connectedNode)
    nodes.append(node)
    print(f"The current amount of nodes: {len(nodes)}")
    return node
    
def GeneratePath(length:int, x:int, lastNode:Node=None):
    nodeAtPos = GetNodeAtPos(lastNode.position.x+x, lastNode.position.y-1) 
    if nodeAtPos == None:
        node:Node = AddNode(Node(lastNode.position.x+x, lastNode.position.y-1), lastNode)
        length-=1
        if length > 0:
            GeneratePath(length, 0, nodes[-1])
        else:
            node.needsToSplit = True # tells the last node it needs to split
    else:
        lastNode.nextNodes.append(nodeAtPos)
        
def GeneratePathsFromNode(node:Node, pathLength:int):
    paths = random.randint(2, 2)
    print(paths)
    if paths == 2:
        pathPos = [-1, 1]
    else:
        pathPos = [-1, 0, 1]
    for i in range(paths):
        GeneratePath(pathLength, pathPos[i], node)
        
def GetNodeAtPos(x:int, y:int)->Node:
    newPosition = pygame.Vector2(x, y)
    for node in nodes:
        if node.position == newPosition:
            return node
    return None

worldPosition:pygame.Vector2 = pygame.Vector2(0,0)

nodes:List[Node] = []

GeneratePathsFromNode(AddNode(Node(5, 4), None), 3)

moveTimer = 0
hasMoved = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    redraw()
    
    deltaTime = clock.tick()* 0.001 
    
    moveTimer += deltaTime
    hasMoved = False
    if moveTimer >= 1:
        moveTimer = 0
        hasMoved = True
        worldPosition.y += 1
        
        for node in nodes:
            node.Update(worldPosition)
            if node.readyToSplit:
                pathLength = random.randint(2, 5)
                GeneratePathsFromNode(node, pathLength)
                node.readyToSplit = False
                node.needsToSplit = False
pygame.quit()
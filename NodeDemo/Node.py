import pygame
import Constants
from typing import List

class Node:
    def __init__(self, x:int, y:int):
        self.position = pygame.Vector2(x, y) #position on the grid
        
        self.surface = pygame.Surface((Constants.GRID_SIZE, Constants.GRID_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, (255, 0, 0), (Constants.GRID_SIZE/2, Constants.GRID_SIZE/2), Constants.GRID_SIZE/2)
        
        self.nextNodes:List[Node] = []
        
        self.needsToSplit=False
        self.readyToSplit=False
        
    def Update(self, worldPosition:pygame.Vector2):
        if self.needsToSplit:
            pos = self.position + worldPosition
            if pos.y >= 0:
                self.readyToSplit = True
                
    
    def DrawConnections(self, window:pygame.Surface, worldPosition:pygame.Vector2):
        selfRenderPosition =( self.position*Constants.GRID_SIZE + worldPosition*Constants.GRID_SIZE) + pygame.Vector2(Constants.GRID_SIZE/2, Constants.GRID_SIZE/2) # gets the center position where it should be rendered for self node
        for node in self.nextNodes:
            nextRenderPosition = (node.position*Constants.GRID_SIZE + worldPosition*Constants.GRID_SIZE) + pygame.Vector2(Constants.GRID_SIZE/2, Constants.GRID_SIZE/2) # gets the center position where it should be rendered for next node
            pygame.draw.line(window, (100, 255, 100), selfRenderPosition, nextRenderPosition, Constants.CONNECTING_LINE_WIDTH)
    
    def Draw(self, window:pygame.Surface, worldPosition:pygame.Vector2) -> pygame.Vector2: #position is returned so we know if this has gone off screen
        renderPosition = self.position + worldPosition # gets the grid position where it should be rendered
        window.blit(self.surface, (renderPosition.x*Constants.GRID_SIZE, renderPosition.y*Constants.GRID_SIZE))
        return renderPosition*Constants.GRID_SIZE
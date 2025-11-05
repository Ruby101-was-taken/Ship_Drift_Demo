import Node
import Types
import pygame

class Path:
    def __init__(self, parentNode:Node.Node, length:int, x = 0):
        self.nodes:list[Node.Node] = [parentNode]
        self.parentNode:Node.Node = parentNode
        self.CreatePath(length, x)
    def Draw(self, window:pygame.Surface, worldPosition:pygame.Vector2):
        node:Node.Node
        for node in self.nodes:
            node.Draw(window, worldPosition)
        for node in self.nodes:
            node.DrawConnections(window, worldPosition)
    def AddConnection(self, node:Node.Node):
        self.nodes[-1].nextNodes.append(node)
        self.nodes.append(node)
    def CreatePath(self, length, xOffset):
        if length > 7:
            length = 7
        x = self.parentNode.position.x + xOffset
        y = self.parentNode.position.y-1
        for i in range(length):
            self.AddConnection(Node.Node(x, y))
            y-=1
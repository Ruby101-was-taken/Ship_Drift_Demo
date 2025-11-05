import Node
import pygame
import Types
import random

class Path:
    def __init__(self, parentNode:Node.Node, length:int, x = 0):
        self.nodes:list[Node.Node] = [parentNode]
        self.parentNode:Node.Node = parentNode
        self.CreatePath(length, x)
        self.length = length
    def Update(self, worldPosition:pygame.Vector2):
        node:Node.Node
        for node in self.nodes:
            node.Update(worldPosition)
        
        if not self.lastNode.right is None and self.lastNode.right != "done":
            self.lastNode.right.Update(worldPosition)
            
        if not self.lastNode.left is None and self.lastNode.left != "done":
            self.lastNode.left.Update(worldPosition)
        
    def Draw(self, window:pygame.Surface, worldPosition:pygame.Vector2):
        node:Node.Node
        for node in self.nodes:
            node.DrawConnections(window, worldPosition)
        for node in self.nodes:
            node.Draw(window, worldPosition)
            
        if not self.lastNode.right is None and self.lastNode.right != "done":
            self.lastNode.right.Draw(window, worldPosition)
            
        if not self.lastNode.left is None and self.lastNode.left != "done":
            self.lastNode.left.Draw(window, worldPosition)
    def AddConnection(self, node:Node.Node):
        
        
        canAdd = self.CheckNodeType(node)
        while not canAdd:
            node.ShuffleType()
            canAdd = self.CheckNodeType(node)
        
        self.nodes[-1].nextNodes.append(node)
        self.nodes.append(node)
        
    def CheckNodeType(self, node:Node.Node)->bool:
        for n in self.nodes:
            if n.type == node.type:
                return False
        return True
        
    def CreatePath(self, length, xOffset):
        if length == 0:
            self.lastNode = Node.ChoiceNode(self.parentNode.position.x, self.parentNode.position.y)
            self.parentNode = self.lastNode
            self.nodes = [self.lastNode]
            return
        if length > 7:
            length = 7
        length-=1
        x = self.parentNode.position.x + xOffset
        y = self.parentNode.position.y-1
        for i in range(length):
            self.AddConnection(Node.Node(x, y))
            y-=1
            
        self.lastNode = Node.ChoiceNode(x, y)
        self.AddConnection(self.lastNode)
        
        randNode = random.choice(self.nodes)
        randNode.type = Types.NodeTypes.SHOP
        randNode.SetType()
        
    def AddPaths(self):
        if self.lastNode.right is None:
            self.lastNode.right = Path(self.lastNode, 4, -1)
        else:
            self.lastNode.right.AddPaths()
            
        if self.lastNode.left is None:
            self.lastNode.left = Path(self.lastNode, 4, 1)
        else:
            self.lastNode.left.AddPaths()
        
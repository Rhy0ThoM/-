# coding=gbk
'''
Created on 2017年10月9日

@author: RHy0ThoM
'''

from AttackGraphStructure.AttackElementNode import AttackGraphNode

class AttackGraph:
    
    def __init__(self, x = [], y = [] ):
        self.Node = x
        self.Edge = y
        
        
    def addNode(self,node):
        self.Node.append(node)
        
        
    def addEdge(self,nodeA,nodeB):
        self.Edge.append([nodeA,nodeB])
        
        
    def removeNode(self,node):
        self.Node.remove(node)
        
        
    def privileges(self):
        find_p = []
        for i in self.Node:
            if i.Type == 'Privilege':
                find_p.append(i)
        return find_p
    
    
    def vulnerabilityExploits(self):
        find_v = []
        for i in self.Node:
            if i.Type == 'VulnerabilityExploit':
                find_v.append(i)
        return find_v
    
    
    def informationSourceUsages(self):
        find_i = []
        for i in self.Node:
            if i.Type == 'InformationSource':
                find_i.append(i)
        return find_i
    
    
    def addNodeWithItsSubTree(self,nodeP = AttackGraphNode()):                   #添加节点与它的子树
        self.Node.append(nodeP)
        self.Edge.extend(nodeP.outEdges)
        for i in nodeP.outEdges:
            self.addNodeWithItsSubTree(i.TargetNode)
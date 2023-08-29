from collections import deque

class Node:
    def __init__(self, valor):
        self.valor = valor 
        self.left = None 
        self.right = None 
    
    def __repr__(self):
        return '%s <- %s -> %s' % (self.left and self.left.valor, self.valor, self.right and self.right.valor) 

class Tree:
    def __init__(self):
        self.raiz = None
    
    def inserirEmNiveis(self, valor):
        if self.raiz is None:
           self.raiz = Node(valor)
        else:
            self.inserirEmNivelRecursivo(valor, self.raiz)
    
    def inserirEmNivelRecursivo(self, valor, node):
        if valor < node.valor:
            if node.left is None:
                node.left = Node(valor)
            else:
                self.inserirEmNivelRecursivo(valor, node.left)
        else:
            if node.right is None:
                node.right = Node(valor)
            else:
                self.inserirEmNivelRecursivo(valor, node.right) 
    
    def PreOrdem(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.preOrdemRecursiva(self.raiz)  
    
    def preOrdemRecursiva(self, node):
        print(node.valor, end = " ")
        if node.left is not None:
            self.preOrdemRecursiva(node.left)
        if node.right is not None:
            self.preOrdemRecursiva(node.right)
    
    def PosOrdem(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.posOrdemRecursiva(self.raiz)
    
    def posOrdemRecursiva(self, node):
        if node.left is not None:
            self.preOrdemRecursiva(node.left)
        if node.right is not None:
            self.preOrdemRecursiva(node.right)
        print(node.valor, end = " ")
    
    def InOrdem(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.inOrdemRecursiva(self.raiz)
    
    def inOrdemRecursiva(self, node):
        if node is not None:
            self.inOrdemRecursiva(node.left)
            print(node.valor, end = " ")
            self.inOrdemRecursiva(node.right)

    def OrdemEmNiveis(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.ordemEmNiveisRecursivo(self.raiz)
    
    def ordemEmNiveisRecursivo(self, node):
        a = deque()
        a.append(node)
        
        while len(a):
            node = a.pop()
            if node:
                print(node.valor, end = " ")
            if node.left:
                a.append(node.left)
            if node.right:
                a.append(node.right)
           
    
# TESTES
arvore = Tree()
arvore.inserirEmNiveis(5)
arvore.inserirEmNiveis(3)
arvore.inserirEmNiveis(7)
arvore.inserirEmNiveis(2)
arvore.inserirEmNiveis(4)
arvore.inserirEmNiveis(6)
arvore.inserirEmNiveis(8)

print("Percorrendo em Pré-ordem: ")
arvore.PreOrdem()

print("\nPercorrendo em Pós-ordem: ")
arvore.PosOrdem()

print("\nPercorrendo em In-ordem: ")
arvore.InOrdem()

print("\nPercorrendo em Ordem de Níveis: ")
arvore.OrdemEmNiveis()
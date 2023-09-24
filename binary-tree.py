class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def contar_nos_arvore(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nos_arvore(raiz.left) + contar_nos_arvore(raiz.right)

def contar_nos_internos(raiz):
    if raiz is None:
        return 0
    if raiz.left is None or raiz.right is None:
        return 0
    
    return 1 + contar_nos_internos(raiz.left) + contar_nos_internos(raiz.right)

def contar_folhas(raiz):
    if raiz is None:
        return 0
    if raiz.left is None and raiz.right is None:
        return 1
    
    return contar_folhas(raiz.left) + contar_folhas(raiz.right)

def soma_valores_arvore(raiz):
    if raiz is None:
        return 0
    
    return raiz.data + soma_valores_arvore(raiz.left) + soma_valores_arvore(raiz.right)

def inserir_no(raiz,valor):
    if raiz is None:
        return TreeNode(valor)
    
    if valor < raiz.left:
        raiz.left = inserir_no(raiz.left,valor)
    elif valor > raiz.right:
        raiz.right = inserir_no(raiz.right,valor)

    return raiz

def encontrar_minimo(raiz):
    while raiz.left is not None:
        raiz = raiz.left
    return raiz


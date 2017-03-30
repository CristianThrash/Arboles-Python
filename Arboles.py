class Nodo():
    def _init_ (self, valor, izq = None, der = None):
        self.valor = valor
        self.izquierda = izq
        self.derecha = der

def inOrden(arbol):
    if arbol == None:
        return []
    else:
        return inorden(arbolizquierda) + [arbol.valor] + inOrden(arbol.derecha)

def postOrden(arbol):
    if arbol == None:
        return []
    else:
        return postOrden(arbol.izquierda) + postOrden(arbol.derecha) + [arbol.valor]

def preOrden(arbol):
    if arbol == None:
        return []
    else:
        return [arbol.valor] + preOrden(arbol.izquierda) + preOrden(arbol.derecha)

def buscar(arbol, valor):
    if arbol == None:
        return false
    elif arbol.valor == valor:
        return true
    else:
        return buscar(arbol.izquierda) or buscar(arbol.derecha)

def buscarOrdenado(arbol, valor):
    if arbol == None:
        return false
    elif arbol.valor == valor:
        return true
    elif int(valor) < int(arbol.valor):
        return buscar(arbol.izquierda)
    elif int(valor) > int(arbol.valor):
        return buscar(arbol.derecha)

def evaluar(arbol):
    if arbol.valor == '+':
        return evaluar(arbol.izquierda) + evaluar(arbol.derecha)
    elif arbol.valor == '-':
        return evaluar (arbol.izquierda) - evaluar(arbol.derecha)
    elif arbol.valor == '*':
        return evaluar (arbol.izquierda) * evaluar(arbol.derecha)
    elif arbol.valor == '/':
        return evaluar (arbol.izquierda) / evaluar(arbol.derecha)
    else:
        return int (arbol.valor)

def insertar(arbol, valor):
    if arbol == None:
        return Nodo(valor)
    elif int(valor) < int(arbol.valor):
        return Nodo(arbol.valor, insertar(arbol.izquierda, valor), arbol.derecha)
    elif int(valor) > int(arbol.valor):
        return Nodo(arbol.valor, arbol.izquierda, insertar(arbol.derecha, valor))    


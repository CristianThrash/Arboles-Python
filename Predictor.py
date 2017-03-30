class Nodo ():
    def __init__ (self, valor, hijos = []):
        self.valor = valor
        self.hijos = hijos

def buscar (arbol, valor):
    if arbol==None:
        return []
    elif arbol.valor == valor:
        return imprimir(arbol)
    else:
        return buscarHijos(arbol.hijos, valor)

def buscarHijos(hijos, valor):
    if hijos == []:
        return []
    else:
        return buscar(hijos[0], valor) + buscarHijos(hijos[1:], valor)

def imprimir(arbol):
    if arbol == None:
        return []
    else:
        return [arbol.valor] + imprimirHijos(arbol.hijos)

def imprimirHijos(hijos):
    if hijos == []:
        return []
    else:
        return imprimir(hijos[0]) + imprimirHijos(hijos[1:])

print buscar(Nodo("", [Nodo("a", [Nodo("al", [Nodo("ali"), Nodo("ale"), Nodo("ala")]), Nodo("ar", [Nodo("are",[Nodo("area", [Nodo("areas")])]), Nodo("ara", [Nodo("aras")]), Nodo("aro", [Nodo("arom", [Nodo("aroma", [Nodo("aromas"), Nodo("aromad",[Nodo("aromado")])]), Nodo("aromo"), Nodo("arome")]), Nodo("aros")])]
), Nodo("ah", [Nodo("ahi")])]),Nodo("b", [Nodo("ba",[Nodo("bas"), Nodo("bal", [Nodo("bala", [Nodo("balas")])])]), Nodo("be"), Nodo("bi")]),Nodo("c",[Nodo("ca",[Nodo("cas",[Nodo("casa")])]),Nodo("ce",[Nodo("ces",[Nodo("ceso")])])]),Nodo("d",[Nodo("da",[Nodo("daz",[Nodo("daza")])]),Nodo("de",[Nodo("dem",[Nodo("deme")
,Nodo("demo")])])]),Nodo("e",[Nodo("ella no te quiere :,v")]),Nodo("f",[Nodo("fe",[Nodo("fea"),Nodo("feo")])]), Nodo("g",[Nodo("ga",[Nodo("gan",[Nodo("gana")])]),Nodo("ge",[Nodo("gel")]),Nodo("gi",[Nodo("gil")])]),Nodo("h",[Nodo("ha",[Nodo("hab",[Nodo("haber")])]),Nodo("he",[Nodo("hel",[Nodo("heli",[Nodo("helio")])])])
,Nodo("hi",[Nodo("himno",[Nodo("hincha",[Nodo("hinchas")])])])]),Nodo("i",[Nodo("in",[Nodo("ind",[Nodo("indio"),Nodo("indu")])]),Nodo("ig",[Nodo("igual",[Nodo("iguala")])]),Nodo("ir",[Nodo("ira",[Nodo("iracundo")])])]),Nodo("j",[Nodo("ja",[Nodo("jau",[Nodo("jaula")])]),Nodo("je",[Nodo("jes",[Nodo("jesus")])])
,Nodo("jo",[Nodo("joco",[Nodo("jocoso")])])]),Nodo("k",[Nodo("ke",[Nodo("Kepis")]),Nodo("ki",[Nodo("kilo")]),Nodo("ka",[Nodo("kar",[Nodo("karen")])])]),Nodo("l",[Nodo("la",[Nodo("las",[Nodo("laso")])]),Nodo("le",[Nodo("les",[Nodo("lesion"),Nodo("leso")])]),Nodo("li",[Nodo("lin",[Nodo("linaje"),Nodo("lino"),Nodo("linterna")])])
,Nodo("lo",[Nodo("los",[Nodo("losa")]),Nodo("lor",[Nodo("loro")]),Nodo("lon",[Nodo("lona")])])]), Nodo("m",[Nodo("ma",[Nodo("man",[Nodo("manantial")])]),Nodo("me",[Nodo("mes",[Nodo("mesa")])]),Nodo("mi",[Nodo("mil",[Nodo("milo")])])]),Nodo("n",[Nodo("na",[Nodo("nar",[Nodo("naranja")])]),Nodo("ne",[Nodo("nec",[Nodo("necio")])])
,Nodo("no",[Nodo("nod",[Nodo("nodo")])])]),Nodo("o",[Nodo("ol",[Nodo("ola")]),Nodo("or",[Nodo("oro")]),Nodo("on",[Nodo("ond",[Nodo("onda")])])]),Nodo("p",[Nodo("pa",[Nodo("pan",[Nodo("pana")])]),Nodo("pe",[Nodo("pel",[Nodo("pelo")])]),Nodo("pi",[Nodo("pin",[Nodo("pino")])]),Nodo("po",[Nodo("pol",[Nodo("pollo")])])])
,Nodo("q",[Nodo("que",[Nodo("ques",[Nodo("queso")])]),Nodo("qui",[Nodo("quin",[Nodo("quinto")])])])]),raw_input("Busqueda: "))

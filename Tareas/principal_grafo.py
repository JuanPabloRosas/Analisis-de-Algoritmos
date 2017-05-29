import Grafo as g

grafo = g.Grafo()
lista = grafo.lista_ady_prueba()
print("Grafo:")
print(lista)
print("Insertar Nodo, nodo = 2")
print(grafo.insertar_nodo(lista,2))
print(lista)
print("Eliminar Nodo, nodo = 2")
print(grafo.eliminar_nodo(lista,12))
print(lista)
print("Insertar Arco, arco = (2,5) = 19")
print(grafo.insertar_arco(lista,2,5,19))
print(lista)

"""
#grafo.lista_ady_archivo('/home/pabloide/Documentos/Algoritmos/Grafo/instancia_grafo.txt')
lista = grafo.lista_ady_nodos(10)
print("Grafo",lista)
#grafo.graficar_peso(lista)
arbol = grafo.kruskal(lista)
pred, secuencia, peso = grafo.dfs_kruskal(arbol,lista)


print("Peso: ",peso, " secuencia: ",secuencia)

#grafo.graficar()
"""

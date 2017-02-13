import numpy as np
import matplotlib.pyplot as plt
import os, sys 
import networkx as nx
import random
import pylab

class Utility:
    def lista_adyacencia_prueba():
        """lista_ady = [[1, 6, 8],
                      [0, 4, 6, 9],
                      [4, 6],
                      [4, 5, 8],
                      [1, 2, 3, 5, 9],
                      [3, 4],
                      [0, 1, 2],
                      [8, 9],
                      [0, 3, 7],
                      [1, 4, 7]]
        """
        lista_ady = [ [[1,12], [6,2],  [8,12]],
                      [[0,2],  [4,23], [6,23], [9,4]],
                      [[4,34], [6,43]],
                      [[4,5],  [5,13], [8,6]],
                      [[1,6],  [2,11], [3,11], [5,15], [9,20]],
                      [[3,77], [4,32]],
                      [[0,4],  [1,4],  [2,11]],
                      [[8,2],  [9,3]],
                      [[0,12], [3,13], [7,12]],
                      [[1,11], [4,10], [7,15]]]
        return lista_ady

    def matriz_adyacencia_prueba():
                    #  0  1  2  3  4  5  6  7  8  9
        matriz_ady = [[0, 1, 0, 0, 0, 0, 6, 0, 8, 0],
                      [1, 0, 0, 0, 4, 0, 6, 0, 0, 9],
                      [0, 0, 0, 0, 4, 0, 6, 0, 0, 0],
                      [0, 0, 0, 0, 4, 5, 0, 0, 8, 0],
                      [0, 5, 1, 4, 0, 7, 0, 0, 0, 9],
                      [0, 0, 0, 3, 9, 0, 0, 0, 0, 0],
                      [6, 7, 7, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 7, 9],
                      [8, 0, 0, 4, 0, 0, 0, 8, 0, 0],
                      [0, 19,0, 0, 3, 0, 0, 5, 0, 0],]
        return matriz_ady

    def lista_adyacencia_nodos(num_nodos):
        lista_ady=[[] for _ in range(num_nodos)] 
        for i in range(0, num_nodos):
            nodos_ady = random.randint(0, num_nodos)
            lista_ady[i] = random.sample(range(0, num_nodos), nodos_ady)
            for j in range(0,len(lista_ady[i])):
                lista_ady[i][j] = random.sample(range(0, num_nodos),2)
        #print(lista_ady)
        return lista_ady

    def lista_adyacencia_archivo(path):
        #Recive un archivo de texto con el sig. formato, cada numero es una arista
        #   1 6 8
        #   0 41 6 9
        #   4 6
        #   4 5 8
        #   1 22 3 5 9
        #   3 4
        #   0 1 2
        #   8 9 12

        lista_ady = []
        with open(path) as file:
            for line in file:
                lista_ady.append([int(numero) for numero in line.split()])
        print(lista_ady)
        return lista_ady
    
    def conexo(list_ady):
        flag = False
        nodos = len(list_ady)
        conexo = [[0]* 2 for _ in range(nodos)]
        conexo[0][0] = 1
        suma = 1
        for i in range(0, nodos):
            if(conexo[i][0] == 1):
                    if(conexo[i][1] == 0):
                        conexo[i][1] = 1
                        for j in range(0 , len(list_ady[i])):
                            num = list_ady[i][j][0]
                            if(conexo[num][0] == 0):
                                suma = suma + 1
                            conexo[num][0] = 1
                        #print(i, " - ", conexo)
            if(suma == nodos):
                flag = True
                break
            
        return flag

    """
    def eliminar_vertice(grafo,vertice):
        try:
            del grafo[vertice]
            print("Vertice Eliminado")
        except ValueError:
            print("No se elimino el elemento")

    def agregar_vertice(grafo, vertice):
        try:
            grafo.append(vertice)
            print("Vertice agregado")
        except ValueError:
            print("Elemento invalido")

    
    def eliminar_arista(grafo, vertice, arista):
        try:
            del grafo[vertice][]
        except ValueError:
            print("No se elimino el elemento")

    def agregar_arista(grafo, arista):
        try:
            grafo.append(aristas)
        except ValueError:
            print("Elemento invalido")
    """            
    def dijkstra(matriz_ady, list_ady, x, y):
        nodos = len(list_ady)
        distancia = 0
        camino = []
        dj = [[0,0,-1]]# for _ in range(nodos)]
        dj[x][0] = 0 #distancia
        dj[x][1] = x #precedente
        dj[x][2] = 1 #fijo
        camino.append(x)
        menor = 100000
        
        for i in range(0 , len(list_ady[x])):
            num = list_ady[x][i]
            dist = matriz_adyacencia[x][num]
            distancia = distancia + dist
            prec = x
            dj[i][0] =  dist
            dj[i][1] = prec
            
            print(dj)
            if(dj[i][0] < menor):
                menor = dj[x][0]
                x = nunm
         
        camino.apend(menor)    
                 
        return camino

    def graficar(lista_ady):
        G=nx.Graph()
        G.add_nodes_from(range(0,len(lista_ady)))
        for i in range(0, len(lista_ady)):
            for j in range(0, len(lista_ady[i])):
                G.add_edge(i,lista_ady[i][j][0], weight = lista_ady[i][j][1] )
                #G.node[str(i)]['size']=1
                #G[i][j]['weight']=1

        print ("Nodos:" ,G.nodes())
        print ("Relaciones: ",G.edges())
        #nx.draw(G,node_size = 500, node_color="cyan", with_labels = True)
        #nx.draw_spectral(G,node_size = 500, node_color="cyan", with_labels = True)
        nx.draw_circular(G,node_size = 500, node_color="cyan", with_labels = True)
        #nx.draw_random(G,node_size = 500, node_color="cyan", with_labels = True)
                      
        plt.show()


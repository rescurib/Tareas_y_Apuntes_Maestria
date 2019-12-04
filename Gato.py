#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:05:50 2019

@author: Rodolfo Escobar
"""
import copy

class Estado():
    Tablero = [[0,0,0],
               [0,0,0],
               [0,0,0]]
    Eval = 0
    
    def tablleno(self):
        for i in range(3):
            for j in range(3):
                if self.Tablero[i][j]==0:
                    return False
        return True
    
    def turnoX(self):
        c = 0
        for i in range(3):
            for j in range(3):
                if self.Tablero[i][j]==1:
                    c += 1
                if self.Tablero[i][j]==2:
                    c -= 1
        return c==0

def printtablero(Estado):
    for i in range(3):
        for j in range(3):
            if Estado.Tablero[i][j]==0:
                print("     ",end = '')
            if Estado.Tablero[i][j]==1:
                print("  X  ",end='')
            if Estado.Tablero[i][j]==2:
                print("  O  ",end='')
            if j<2:
                print("|",end='')
            else:
                print('')
        if i<2:
            print("-----------------")
                  
def Estados_Siguientes(Estado):
    marca = 1 if Estado.turnoX() else 2
    ramas = []
    for i in range(3):
        for j in range(3):
            if Estado.Tablero[i][j] == 0:
                ramas.append(copy.deepcopy(Estado))
                ramas[-1].Tablero[i][j] = marca
    return ramas

def marcar(Edo, ren,col):
    Edo.Tablero[ren][col]=2

def evaluacion(E):
	posibles_victorias = []

	# 3 en fila
	for row in E.Tablero:
		posibles_victorias.append(set(row))

	# 3 en columna
	for i in range(3):
		posibles_victorias.append(set([E.Tablero[k][i] for k in range(3)]))

	# 3 en diagonal
	posibles_victorias.append(set([E.Tablero[i][i] for i in range(3)]))
	posibles_victorias.append(set([E.Tablero[i][2 - i] for i in range(3)]))

	# Verificar triadas
	for trio in posibles_victorias:
		if trio == set([1]):
			return 10
		elif trio == set([2]):
			return -10
	return 0

#----- Función minimax -----
def minmax(Estado):
    Estado.Eval = evaluacion(Estado)
    #--- Caso Base
    if Estado.Eval != 0 or Estado.tablleno():
        return Estado
    #---
    #---Ramas de recursión
    Ramas = Estados_Siguientes(Estado) #Lista de edos. siguientes        
    Ramas_Evaluadas = [minmax(r) for r in Ramas] #Lista de evaluaciones
    #---
    #--- Elegir mínimo/máximo
    if Estado.turnoX(): #Maximizador
         Ed_minimax  =  max(Ramas_Evaluadas,key=lambda x: x.Eval)
         ind = Ramas_Evaluadas.index(Ed_minimax) 
    else:		#Minimizador
         Ed_minimax = min(Ramas_Evaluadas,key=lambda x: x.Eval)
         ind = Ramas_Evaluadas.index(Ed_minimax)
    #---
    #--- Retona mejor movimiento
    Ramas[ind].Eval = Ed_minimax.Eval
    return Ramas[ind]    
#-------------------------------
#----- Programa Principal ------    
Edo = Estado()
Edo.Tablero = [[0,0,0],
               [0,0,0],
               [0,0,0]]

while(1):
    printtablero(Edo)
    print("Turno del CPU...")
    Edo = minmax(Edo)
    printtablero(Edo)
    print('')
    if evaluacion(Edo)!=0 or Edo.tablleno():
        break
    pos = input("Su turno (inserte renglón,columna): ")
    ren,col = pos.split(',')
    marcar(Edo,int(ren),int(col))
    printtablero(Edo)
    print('')
    if evaluacion(Edo)!=0 or Edo.tablleno():
        break

    

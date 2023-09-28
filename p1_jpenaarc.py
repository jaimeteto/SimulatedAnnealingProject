# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:16:49 2023

@author: jaime
"""



import random
import numpy as np
import math 
from random import choice
import statistics 
import copy
#generate random n in provided array
testArray = np.array([[1,4,3,4],[2,3,1,4],[3,1,2,3],[1,2,4,2]])
providedArray = [4,6,8,10,12,14,16,18,20]
#n = random.choice(providedArray)
n=4

#generate random N*N matrix (initial solution)
#matrix = np.random.randint(1,n+1,size=(n*n))

def createMatrix(n):
    # creates matrix with no duplicates so that a solution will alaways will be found
    
    matrix2 = []
    counter =1
    
    for i in range(n):
        for j in range(n):
            matrix2.append(counter)
        counter += 1
    random.shuffle(matrix2)
    
    #rowsMatrix = np.reshape(sequence,(n,n))
        
    
    return matrix2

#rowsMatrix = np.reshape(matrix,(n,n))

def printMatrix(matrix,n):
    nextRow =n-1
    row=[]
    for i in range(len(matrix)):
        
        row.append(matrix[i])
        if(i==nextRow):
            print(row)
            row.clear()
            nextRow+=n
    
        
def objectiveFucntionCost(matrix1,n):
    row=[]
    
    #get the cost of all rows(cost for eac row is equals the number of integers missing on each row)
    count =0
    for i in range(n):
        row = matrix1[i]
        #print(row)
        for j in range(1,(n+1)):
            
            if((np.count_nonzero(row == j))>=1):
                continue;
            else:
                count += 1
    return count


# matrix is a 1d array version of n*n array
def neighborGenerator(matrix,n):
    #this fucntion will generate a neighbor by swapping the values of two indices
    #radomly 
    matrixSize = (n*n)-1
    #get random two random places
    randomCell1 = random.randint(1,matrixSize)
    randomCell2 = random.randint(1,matrixSize)
    # make a copy of the given matrix and swap positions
    print("randomcell1: "+str (randomCell1)+"  randomCell2: "+ str (randomCell2))
    neighbor = copy.deepcopy(matrix)
    #save value in randomCell1
    firstValue = matrix[randomCell1]
    neighbor[randomCell1]=matrix[randomCell2]
    neighbor[randomCell2]=firstValue
    
    return neighbor
        
        
print("matrix")
print("\n")
testinMatrixFun = createMatrix(n)
#print(testinMatrixFun)
#print("testintg objective fucntion")
 #get the cost of all columns(number of integers missing on each column)
    #transpose the given ndarray

#rowsMatrix = np.reshape(testinMatrixFun,(n,n)) #converting to npdarray
#columnArray= rowsMatrix.T      # transposing rows to columns
#print(objectiveFucntionCost(rowsMatrix,n)+objectiveFucntionCost(columnArray,n))
#print(testinMatrixFun)
printMatrix(testinMatrixFun,n)
testingNei = neighborGenerator(testinMatrixFun,n)
print("\n")
printMatrix(testingNei,n)





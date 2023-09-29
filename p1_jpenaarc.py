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
#testArray = np.array([[1,4,3,4],[2,3,1,4],[3,1,2,3],[1,2,4,2]])
#providedArray = [4,6,8,10,12,14,16,18,20]
#n = random.choice(providedArray)
#n=4

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


#used for debuggin. takes a regular array
def printMatrix(matrix,n):
    nextRow =n-1
    row=[]
    for i in range(len(matrix)):
        
        row.append(matrix[i])
        if(i==nextRow):
            print(row)
            row.clear()
            nextRow+=n
    
#matrix1 should be a npdarray not a 1d array        
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
    matrixSize = (n*n)-1 # maximum index number in matrix
    #get random two random places
    randomCell1 = random.randint(1,matrixSize)
    randomCell2 = random.randint(1,matrixSize)
    # make a copy of the given matrix and swap positions
    #print("randomcell1: "+str (randomCell1)+"  randomCell2: "+ str (randomCell2))
    neighbor = copy.deepcopy(matrix)
    #save value in randomCell1
    firstValue = matrix[randomCell1]
    
    #do the swapping
    neighbor[randomCell1]=matrix[randomCell2]
    neighbor[randomCell2]=firstValue
    
    return neighbor


#this receives a 1d array represention of our initial state(matrix)
def getInitialTemp(matrix1,matrix2,matrix3,n):
    # conver from 1d array to ndarray()
    rowsMatrix1 = np.reshape(matrix1,(n,n)) #converting to npdarray
    columnArray1= rowsMatrix1.T      # transposing rows to columns
    #neigbor2
    rowsMatrix2 = np.reshape(matrix2,(n,n)) #converting to npdarray
    columnArray2= rowsMatrix2.T  
    #neibor3
    rowsMatrix3 = np.reshape(matrix3,(n,n)) #converting to npdarray
    columnArray3= rowsMatrix3.T   
    
    #get the total cost for each neigbor using objective fucntion
    cost1 = objectiveFucntionCost(rowsMatrix1,n)+objectiveFucntionCost(columnArray1,n)
    cost2=objectiveFucntionCost(rowsMatrix2,n)+objectiveFucntionCost(columnArray2,n)
    cost3=objectiveFucntionCost(rowsMatrix3,n)+objectiveFucntionCost(columnArray3,n)
    
    #get difference for each possible combination
    difBetween12=abs(cost1-cost2)
    #print("df 12: "+ str(difBetween12))
    difBetween13=abs(cost1-cost3)
    #print("df 13: "+ str(difBetween13))
    difBetween23=abs(cost2-cost3)
    #print("df 23: "+ str(difBetween23))
    
    values=[difBetween12,difBetween13,difBetween23]
    #returns the index with the max cots value
    return max(values)
    

#picks the matrix witht the smallest cost
#it returns a tupple (cost,index of the matrix with lowest cost)
def pickSmallestCost(matrix1,matrix2,matrix3,n):
    # conver from 1d array to ndarray()
    rowsMatrix1 = np.reshape(matrix1,(n,n)) #converting to npdarray
    columnArray1= rowsMatrix1.T      # transposing rows to columns
    #neigbor2
    rowsMatrix2 = np.reshape(matrix2,(n,n)) #converting to npdarray
    columnArray2= rowsMatrix2.T  
    #neibor3
    rowsMatrix3 = np.reshape(matrix3,(n,n)) #converting to npdarray
    columnArray3= rowsMatrix3.T   
    
    #get the total cost for each neigbor using objective fucntion
    cost1 = objectiveFucntionCost(rowsMatrix1,n)+objectiveFucntionCost(columnArray1,n)
    cost2=objectiveFucntionCost(rowsMatrix2,n)+objectiveFucntionCost(columnArray2,n)
    cost3=objectiveFucntionCost(rowsMatrix3,n)+objectiveFucntionCost(columnArray3,n)
    values=[cost1,cost2,cost3]
    
    return (min(values),values.index(min(values)))




def main():

    allowedInputs = [4,6,8,10,12,14,16,18,20]
   
    while(True):
        print("Please enter any of the following integers [4,6,8,10,12,14,16,18,20]")
    
        n = int (input("Enter value of n:"))
        if n in allowedInputs:
            break
        else:
            
            print("\n wrong input\n")
            
    
   
    
    
    #define the initial temperature
    # intitial temperature will be the max diference between neigbors as
    #as proposed in (Computing the Initial Temperature of Simulated Annealing)
    initialState = createMatrix(n)
    currentState = copy.deepcopy(initialState)
    initialStateDArray = np.reshape(initialState,(n,n))
    
    currentStateDArray =np.reshape(currentState,(n,n))
    #printMatrix(testinMatrixFun,n)
    #choose 3 neigbors
    neighbor1 = neighborGenerator(currentState,n)
    neighbor2 = neighborGenerator(currentState,n)
    neighbor3 = neighborGenerator(currentState,n)
    
    initialNeigbors = [neighbor1,neighbor2,neighbor3]
    
    
    print("\n")
    
    #pick the best option
    initialTemp = getInitialTemp(neighbor1,neighbor2,neighbor3,n)
    
    print("this is the initial temp value: "+ str(initialTemp))
    
    
    #initialize loop
    numberOfIterations =0
    currentTemp = initialTemp
    currentCost = objectiveFucntionCost(initialStateDArray,n)+objectiveFucntionCost(initialStateDArray.T,n)
    #currentNeighbors =[neighbor1,neighbor2,neighbor3]
    while(True):
    #check wether current state is goal state
        if(currentCost ==0):
            print("TERMINATED BY: Goal State")
            break
        
        if(currentTemp ==0):
            print("TERMINATED BY: Temperature =0")
            break
        #check neigbors
        else:
            if(currentTemp == initialTemp):
                #use initial neighbors
                #compare deltaE with intial state and pick the neigbor witht the smallest cost
                bestInitialCandidate = pickSmallestCost(neighbor1,neighbor2,neighbor3,n)
                bestInitialCandidateCost = bestInitialCandidate[0]
                deltaE = bestInitialCandidateCost-currentCost
                
                if(deltaE<0):
                    currentState = initialNeigbors[bestInitialCandidate[1]] #choose from initial neigbors list
                    currentStateDArray = np.reshape(currentState,(n,n))
                    #reduce temperature
                    currentTemp = currentTemp * 0.99
                    
                    currentCost = objectiveFucntionCost(initialStateDArray,n)+objectiveFucntionCost(initialStateDArray.T,n)
                    
                    numberOfIterations +=1
                
                else:
                    #pick current if acceptance probability <1
                    acceptanceProbability =  math.exp(- deltaE/currentTemp)
                    
                    if(acceptanceProbability<1):
                        currentState = initialNeigbors[bestInitialCandidate[1]] #choose from initial neigbors list
                        currentStateDArray = np.reshape(currentState,(n,n))
                        currentCost = objectiveFucntionCost(initialStateDArray,n)+objectiveFucntionCost(initialStateDArray.T,n)


                        currentTemp = currentTemp * 0.99
                    numberOfIterations +=1
            
            else:
                # get new neighbors
                newNeighbor1 = neighborGenerator(currentState,n)
                newNeighbor2 = neighborGenerator(currentState,n)
                newNeighbor3 = neighborGenerator(currentState,n)
                
                #pick best of the neighbors
                bestCandidate = pickSmallestCost(newNeighbor1,newNeighbor2,newNeighbor3,n)
                # get the cost of the best neighbor
                bestCandidateCost = bestCandidate[0]
                
                #get the delta(diference between current cost and new candidate)
                deltaE = bestCandidateCost-currentCost
                
                
                newNeighbors = [newNeighbor1,newNeighbor2,newNeighbor3]
                #if delata is less than one, it means that the candidate has a better cost
                if(deltaE<0):
                    #new candidate is currentState(we move to candidate)
                    currentState = newNeighbors[bestCandidate[1]] #choose from initial neigbors list
                    #changing to npdarray
                    currentStateDArray = np.reshape(currentState,(n,n))
                    
                    #reduce temperature
                    currentTemp = currentTemp * 0.99
                    #update currentcost
                    currentCost = objectiveFucntionCost(currentStateDArray,n)+objectiveFucntionCost(currentStateDArray.T,n)

                    numberOfIterations +=1
                
                else:
                    #pick current if acceptance probability <1
                    acceptanceProbability =  math.exp(- deltaE/currentTemp)
                    
                    if(acceptanceProbability<1):
                        currentState = newNeighbors[bestCandidate[1]] #choose from initial neigbors list
                        currentStateDArray = np.reshape(currentState,(n,n))
                        currentCost = objectiveFucntionCost(currentStateDArray,n)+objectiveFucntionCost(currentStateDArray.T,n)
                        currentTemp = currentTemp * 0.99
                    numberOfIterations +=1
                
    print("initial state:")
    print(initialState)
    print("\n")       
    print("Final state:")
    print(currentState)
    print("final cost: "+ str(currentCost))
    print("Number of iterations: "+ str(numberOfIterations))    
   
   
    
    
    
    #continue untill temperature ==0 or freeze state

if __name__ == "__main__":
    main()



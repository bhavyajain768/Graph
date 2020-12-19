from Network import *

def rowRotation(T,a,i,n):
# Function for doing row rotation of i-th row a-times in the given Torus network of size (nxn)(a<n,i<n)
    array,j = [],0
    while(j<n):
# This while loop is for storing the current attributes of nodes in an array before the rotation.
        array[j] = T.nodes[(i,j)]['A']
        j=j+1
    j,D = 0,{}
    while(j<n):
# This while loop is for storing the new values of attribute values (after rotation) corresponding to (i,j) node in a dict.
        D[(i,(j-a+n)%n)] = array[j]
        j=j+1
# This is to set new attributes values to the graph.
    networkx.set_node_attributes(T,D,'A')

def multiply(A,B):
# A and B are 2-D arrays represnting two square matrices(nxn) and we have to multiply them using Canon's Algo.
    n = len(A)
    C = create_torusNetwork(n,n)
    D = {}
    i=0
# These while loops are executed to store both matricies in two Dict with keys as (row number,col number)(i,j).
    while(i<n):
        j=0
        while(j<n):
            D[(i,j)] = {'A':A[i][j],'B':B[i][j]}
            j=j+1
        i=i+1
# These are used to make two attributes in the Torus which stores corresponding values of two matricies.
    networkx.set_node_attributes(C,D)

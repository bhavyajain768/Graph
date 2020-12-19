from Network import *

def multiply(A,B):
# A and B are 2-D arrays represnting two square matrices(nxn) and we have to multiply them using Canon's Algo.
    n = len(A)
    C = create_torusNetwork(n,n)
    aD,bD = {},{}
    i,j=0,0
# These while loops are executed to store both matricies in two Dict with keys as (row number,col number)(i,j).
    while(i<n):
        j=0
        while(j<n):
            aD[(i,j)] = A[i][j]
            bD[(i,j)] = B[i][j]
            j=j+1
        i=i+1
    networkx.set_node_attributes(C,aD,'A')
    networkx.set_node_attributes(C,bD,'B')
    return C

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
        D[(i,(j-a+n)%n)] = {'A':array[j],'ans':T.nodes[(i,(j-a+n)%n)]['B']*array[j]}
        j=j+1
# This is to set new attributes values to the graph.
    networkx.set_node_attributes(T,D)

def colRotation(T,a,j,n):
# Function for doing col rotation of j-th col a-times in the given Torus network of size (nxn)(a<n,j<n)
    array,i = [],0
    while(i<n):
# This while loop is for storing the current attributes of nodes in an array before the rotation.
        array[i] = T.nodes[(i,j)]['B']
        i=i+1
    i,D = 0,{}
    while(i<n):
# This while loop is for storing the new values of attribute values (after rotation) corresponding to (i,j) node in a dict.
        D[((i-a+n)%n,j)] = {'B':array[i],'ans':T.nodes[((i-a+n)%n,j)]['A']*array[i]}
        i=i+1
# This is to set new attributes values to the graph.
    networkx.set_node_attributes(T,D)

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
            D[(i,j)] = {'A':A[i][j],'B':B[i][j],'ans':A[i][j]*B[i][j]}
            j=j+1
        i=i+1
# These are used to make two attributes in the Torus which stores corresponding values of two matricies and third attribute to store the multiplied value.
    networkx.set_node_attributes(C,D)
    Current = C
    p = 0
    while(p<n):
# This while loop is for making new torus after every set of col and row rotation and to update current which will finally yeild multiplied matrix.
        j = 0
        while(j<n):
# This while loop is for doing col rotations.
            colRotation(C,j,j,n)
            j=j+1
        i=0
        while(i<n):
# This while loop is for doing row rotations.
            rowRotation(C,i,i,n)
            i=i+1
        Current = add(Current,C)
        p=p+1
    return Current
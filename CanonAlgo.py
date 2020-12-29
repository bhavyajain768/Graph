from Network import *

def searchNode(T,v,key):
# Function for searching a node of required key in the graph using links and edges in the graph.
    D = {}
    for node in T:
        D[node] = 0
    networkx.set_node_attributes(T,D,'visited')
    S = [v]
# A stack to store nodes which can be visited after an iteration.
    while(S):
        for node in T.neighbors(v):
# An iteration to travel through neighbors of given node.
            if (T.nodes[node]['visited']==0):
                T.nodes[node]['visited'] = 1
                if (node==key):
                    return node
                else:
                    S = [node]+S
        v = S.pop(0)
    return (-1,-1)

def rowRotation(T,a,i,n):
# Function for doing row rotation of i-th row a-times in the given Torus network of size (nxn)(a<n,i<n)
    array,j = [],0
    while(j<n):
# This while loop is for storing the current attributes of nodes in an array before the rotation.
        array.append(T.nodes[(i,j)]['A'])
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
        array.append(T.nodes[(i,j)]['B'])
        i=i+1
    i,D = 0,{}
    while(i<n):
# This while loop is for storing the new values of attribute values (after rotation) corresponding to (i,j) node in a dict.
        D[((i-a+n)%n,j)] = {'B':array[i],'ans':T.nodes[((i-a+n)%n,j)]['A']*array[i]}
        i=i+1
# This is to set new attributes values to the graph.
    networkx.set_node_attributes(T,D)

def add(T1,T2,n):
# This function is for adding the 'ans' attributes of corresponding nodes of both the torus networks T1,T2 of size (nxn)
    D = {}
# A dictionary to store the added attribute value of both the networks.
    i=0
    while(i<n):
# These while loops are for executing every node in the torus T1,T2
        j=0
        while(j<n):
            D[i,j] = T1.nodes[(i,j)]['ans']+T2.nodes[(i,j)]['ans']
            j=j+1
        i=i+1
# This is to set new attribute value of ans to the graph
    networkx.set_node_attributes(T1,D,'ans')

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
    Current = C.copy()
    p = 1
    while(p<n):
# This while loop is for making new torus after every set of col and row rotation and to update current which will finally yeild multiplied matrix.
        j = 0
        while(j<n):
# This while loop is for doing col rotations.
            colRotation(C,1,j,n)
            j=j+1
        i=0
        while(i<n):
# This while loop is for doing row rotations.
            rowRotation(C,1,i,n)
            i=i+1
        add(Current,C,n)
        p=p+1
    return Current


C=multiply([[4,2,5],[3,1,-4],[-2,6,-3]],[[7,4,5],[-1,0,1],[8,2,3]])
C.nodes[(1,0)]['ans']
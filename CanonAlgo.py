from Network import *

def searchNode(T,v,key):
# Function for searching a node of required key in the graph using links and edges in the graph.
    if (v==key):
        return v
    D = {}
    for node in T:
        D[node] = 0
    networkx.set_node_attributes(T,D,'visited')
    S = [v]
# A stack to store nodes which can be visited after an iteration.
    while(S):
        for node in T.neighbors(v):
#For increasing the hop_count of the edge we used from v to reach node.
            T.edges[v,node]['hop_count'] = T.edges[v,node]['hop_count']+1
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
    p = 1
    if (a!=0 and a!=1 and n%a == 0):
# If above condition hold then we can traverse through the row by doing below loop n div a times
        p = n/a
    count = 0
    while(count<p):
# This while loop will traverse through every node of the row.
        value,j = T.nodes[(i,count)]['A'],count
        node = searchNode(T,(i,j),(i,(j-a+n)%n))
        T.nodes[node]['A'],T.nodes[node]['ans'],value = value,value*T.nodes[node]['B'],T.nodes[node]['A']
        j = (j-a+n)%n
        while(j!=count):
# Loop for updating the row rotated node attribute.
            node = searchNode(T,(i,j),(i,(j-a+n)%n))
            T.nodes[node]['A'],T.nodes[node]['ans'],value = value,value*T.nodes[node]['B'],T.nodes[node]['A']
            j = (j-a+n)%n
        count = count+1

        
def colRotation(T,a,j,n):
# Function for doing col rotation of j-th col a-times in the given Torus network of size (nxn)(a<n,i<n)
    p = 1
    if (a!=0 and a!=1 and n%a == 0):
# If above condition hold then we can traverse through the col by doing below loop n div a times
        p = n/a
    count = 0
    while(count<p):
# This while loop will traverse through every node of the col.
        value,i = T.nodes[(count,j)]['B'],count
        node = searchNode(T,(i,j),((i-a+n)%n,j))
        T.nodes[node]['B'],T.nodes[node]['ans'],value = value,value*T.nodes[node]['A'],T.nodes[node]['B']
        i = (i-a+n)%n
        while(i!=count):
# Loop for updating the col rotated node attribute.
            node = searchNode(T,(i,j),((i-a+n)%n,j))
            T.nodes[node]['B'],T.nodes[node]['ans'],value = value,value*T.nodes[node]['A'],T.nodes[node]['B']
            i = (i-a+n)%n
        count = count+1

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
# For adding edge attribute hop_count in the graph with initial value = 0
    D2 = {}
    for edge in C.edges:
        D2[edge] = 0
    networkx.set_edge_attributes(C,D2,'hop_count')

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
    i = 0
    while(i<n):
        j = 0
        while(j<n):
            print(Current.nodes[(i,j)]['ans'],end = ' ')
            j = j+1 
        print()
        i = i+1

multiply([[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]],[[8,9,1,2],[3,4,5,6],[7,8,9,1],[2,3,4,5]])
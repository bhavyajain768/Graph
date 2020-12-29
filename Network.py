import networkx

def create_array(y):
    G = networkx.Graph()
    if (y<=0):
        return G
    G.add_node((0,0))
    c = 1
    while (c<y):
        G.add_node((c,0))
        G.add_edge((c-1,0),(c,0))
        c = c+1
    return G

def create_ring(y):
    if (y<=0):
        return networkx.Graph()
    if (y==1):
        return networkx.Graph().add_node((0,0))
    G = create_array(y)
    G.add_edge((0,0),(y-1,0))
    return G

def create_colarray(x):
    G = networkx.Graph()
    if (x<=0):
        return G
    G.add_node((0,0))
    c = 1
    while (c<x):
        G.add_node((0,c))
        G.add_edge((0,c-1),(0,c))
        c = c+1
    return G

def create_colring(x):
    if (x<=0):
        return networkx.Graph()
    if (x==1):
        return networkx.Graph().add_node(0,0)
    G = create_colarray(x)
    G.add_edge((0,0),(0,x-1))
    return G

def create_mesh(x,y):
    if (x<=0 or y<=0):
        return networkx.Graph() 
    elif (x==1):
        return create_array(y)
    elif (y==1):
        return create_colarray(x)
    G = create_array(y)
    c1 = 1
    while (c1<x):
        c2=0
        while(c2<y):
            G.add_node((0,c1))
            c = 1
            while (c<y):
                G.add_node((c,c1))
                G.add_edge((c-1,c1),(c,c1))
                c = c+1
            G.add_edge((c2,c1),(c2,c1-1))
            c2 = c2+1
        c1 = c1+1
    return G
       
def create_torusNetwork(x,y):                       
    if (x<=0 or y<=0):
        return networkx.Graph() 
    elif (x==1):
        return create_ring(y)
    elif (y==1):
        return create_colring(x)
    G = create_mesh(x,y)
    i,j = 0,0
    while(j<y):
        G.add_edge((j,0),(j,x-1))
        j = j+1
    while(i<x):
        G.add_edge((0,i),(y-1,i))
        i = i+1
    return G

G =create_torusNetwork(3,3)
for node in G.neighbors((0,0)):
    if (node==(1,0)):
        print(node)
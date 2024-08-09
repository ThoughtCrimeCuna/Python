# Levi Peachey-Stoner
# Ford-Fulkerson Algorythm Assignment


# Method for finding which switches can power which lights.
### Source: Daniel Showalter
def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
# Return true if line segments AB and CD intersect
# Source: http://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
def visible(pt1,pt2,Walls):
    x1,y1 = pt1
    x2,y2 = pt2
    for i,wall in enumerate(Walls[:-1]):
        x3,y3 = wall
        x4,y4 = Walls[i+1]
        if intersect((x1,y1),(x2,y2),(x3,y3),(x4,y4)):
            return False
    return True



# This takes example cases which are lists of tuples and converts them into
# a list of valid "links" between switches and lights.
Walls = [(1,2),(1,5),(8,5),(8,3),(11,3),(11,1),
         (5,1),(5,3),(4,3),(4,1),(1,1),(1,2)]

L = [(2,4),(2,2),(5,4)]

S = [(4,4),(6,3),(6,2),(6,6)] # case 1
S = [(6,2),(7,4),(6,3)] # case 2
S = [(6,2),(7,2),(4,4)] # case 3



Links = []
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(S)):
    Links.append(("source",lower[i]))
    Links.append((upper[i],"sink"))
    for k in range(len(L)):
        if visible(S[i], L[k], Walls):
            Links.append((lower[i], upper[k]))


def dfs(graph, node, sink, path=[]):
    path = path + [node]

    if node == sink:
        adjacent_pairs = []
        for i in range(len(path)-1):
            adjacent_pairs.append((path[i], path[i+1]))
        return adjacent_pairs

    for edge in graph:
        if edge[0] == node:
            next_node = edge[1]

            if next_node not in path:
                new_path = dfs(graph, next_node, sink, path)
                if new_path is not None:
                    return new_path

    return None


def residualgraph(graph, path):
    # Reverse the path
    path = path[::-1]

    for edge in path:
        if edge in graph:
            graph.remove(edge)

    residual_edges = [(edge[1], edge[0]) for edge in path]
    graph += residual_edges

    return graph

source = 'source'
sink = 'sink'
run = True
residual = [i for i in Links]
proof = []
links = [i for i in Links if "source" not in i if "sink" not in i]
#print()
for l in range(len(L)):
    path = dfs(residual, source, sink)
    if path:
        #print()
        residual = residualgraph(residual,path)
        #print(residual)
        #print()
    else:
        print("The Graph is not Ergonomic")
        R = [i for i in residual if "source" not in i if "sink" not in i]
        print()
        UsedSwitches = []
        UsedLights = []
        for i in range(len(S)):
            for link in R:
                if link[0] not in UsedSwitches:
                    if link[0] in lower:
                        UsedSwitches.append(link[0])
        UnusedSwitches = [i for i in lower[0:len(S)] if i not in UsedSwitches]
        for i in range(len(L)):
            for link in R:
                if link[1] not in UsedLights:
                    if link[1] in upper:
                        UsedLights.append(link[1])
        UnusedLights = [i for i in upper[0:len(L)] if i not in UsedLights]
        #print(UnusedLights)
        #print(UnusedSwitches)
        proof_s = [i for i in links if i[0] in UnusedSwitches]
        if proof_s ==[]:
            proof = "Nothing connects to: "+UnusedSwitches[0]
            break
        else:
            proof_s += [i for i in links if i[1] == proof_s[0][1]]
            proof_s.pop(0)
        #print(proof_s)
        proof_l = [i for i in links if i[1] in UnusedLights]
        if proof_l == []:
            proof = "Nothing connects to: "+UnusedLights[0]
            break
        else:
            proof_l += [i for i in links if i[0] == proof_l[0][0]]
            proof_l.pop(0)
        #print(proof_l)
        proof = proof_s + proof_l
        proof = list(set(proof))


if len(S) != len(L):
    print("The Graph is not Ergonomic")
    print()
    proof = "Pigeon hole proof, not the same number of Lights and Switches"
elif path:
    print("The path is Ergonomic")
    print()
    proof = [i[::-1] for i in residual if i[0] in upper]
print(proof)


# This all works as intended

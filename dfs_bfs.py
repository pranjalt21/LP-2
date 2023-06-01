from collections import deque
# to implement a queue
#vec  adjacency list
#visit array
# q queue
#ans store the order
   # Recursive function for breadth-first search (BFS)
def bfs_rec(vec, visit, q, ans):
    if not q:
        return
    ele = q.popleft()
    ans.append(ele)
    a = vec[ele]
    for i in range(len(a)):
        if not visit[a[i]]:
            visit[a[i]] = 1
            print(f"Visiting {a[i]} Vertex and inserting it into queue")
            q.append(a[i])
    bfs_rec(vec, visit, q, ans)
'''if the q is empty it returns
it removes the leftmost element from q
appends it to ans and retrives the vec
'''
def BFS(vec, n):
     #Breadth-first search (BFS) function
    visit = [0] * (n + 1)
    q = deque()
    ans = []
    for i in range(1, n + 1):
        if visit[i] == 0:
            visit[i] = 1
            print(f"Visiting {i} Vertex and inserting it into stack")
            q.append(i)
            bfs_rec(vec, visit, q, ans)
    print("\nBFS Traversal is:", end=" ")
    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()
''' iterates all th v i
1 to n
==0 as mark visited n prints the mess '''
def bfs_rec_search(vec, visit, q, ans, find, target):
    # Recursive function for breadth-first search (BFS) with a target search
    if not q:
        return
    ele = q.popleft()
    ans.append(ele)
    if ele == target:
        find[0] = 1
        return
    a = vec[ele]
    for i in range(len(a)):
        if not visit[a[i]]:
            visit[a[i]] = 1
            q.append(a[i])
        if find[0] == 1:
            break
    if find[0] != 1:
        bfs_rec_search(vec, visit, q, ans, find, target)
'''target for specific vertex
if found it [0]to 1
''''
def BFS_Search(vec, n, target):
     # Function for breadth-first search (BFS) with target search
    visit = [0] * (n + 1)
    q = deque()
    ans = []
    find = [0]
    for i in range(1, n + 1):
        if visit[i] == 0:
            visit[i] = 1
            q.append(i)
            bfs_rec_search(vec, visit, q, ans, find, target)
        if find[0] == 1:
            break
    if find[0] == 1:
        print("\nVertex Found")
        print(f"\nBFS Traversal for vertex {target} is:", end=" ")
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
    else:
        print("\nVertex Not Found")
# search the vertex in graphit reates the empty queue find list to store result
def dfs_rec(vec, visit, st, ans):
      # Recursive function for depth-first search (DFS)
    st.pop()
    a = vec[n]
    ans.append(n)
    for i in range(len(a)):
        ele = a[i]
        if visit[a[i]] == 0:
            visit[a[i]] = 1
            print(f"Visiting {a[i]} Vertex and inserting it into stack")
            st.append(a[i])
            dfs_rec(vec, visit, st, ans)

def dfs_rec_search(vec, visit, st, ans, find, target):
    # Recursive function for depth-first search (DFS) with a target search.
      
    n = st[-1]
    st.pop()
    a = vec[n]
    ans.append(n)
    if n == target:
        find[0] = 1
        return
    for i in range(len(a)):
        ele = a[i]
        if visit[a[i]] == 0:
            visit[a[i]] = 1
            st.append(a[i])
            dfs_rec_search(vec, visit, st, ans, find, target)
            if find[0] == 1:
                break

def DFS_Search(vec, n, target):
    # Recursive function for depth-first search (DFS) with a target search.
    ans = []
    visit = [0] * (n + 1)
    st = []
    find = [0]
    for i in range(1, n + 1):
        if visit[i] == 0:
            visit[i] = 1
            st.append(i)
            dfs_rec_search(vec, visit, st, ans, find, target)
        if find[0] == 1:
            break
    if find[0] == 1:
        print("\nVertex Found")
        print("DFS Traversal for vertex is:", end=" ")
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
    else:
        print("\nVertex Not Found")

def DFS(vec, n):
     # Function for depth-first search (DFS) 
    ans = []
    visit = [0] * (n + 1)
    st = []
    for i in range(1, n + 1):
        if visit[i] == 0:
            visit[i] = 1
            print(f"Visiting {i} Vertex and inserting it into stack")
            st.append(i)
            dfs_rec(vec, visit, st, ans)
    print("\nDFS Traversal is:", end=" ")
    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()

n = int(input("Enter Number of Vertices: "))
edge = int(input("Enter Number of Edges: "))
vec = [[] for _ in range(n + 1)]
for i in range(edge):
    u = int(input("Enter source index: "))
    v = int(input("Enter destination vertex: "))
    vec[u].append(v)
    vec[v].append(u)

print("\nGraph")
for i in range(1, n + 1):
    print(f"{i} -> ", end="")
    a = vec[i]
    for j in range(len(a)):
        print(a[j], end=" ")
    print()

print("\nBFS Traversal")
BFS(vec, n)

print("\nDFS Traversal")
DFS(vec, n)

while True:
    print("\nEnter the node to search: ")
    node = int(input())
    print("1. BFS")
    print("2. DFS")
    print("3. Exit")
    ch = int(input("Choice: "))
    if ch == 0:
        break
    elif ch == 1:
        BFS_Search(vec, n, node)
    elif ch == 2:
        DFS_Search(vec, n, node)
    else:
        print("Invalid choice")

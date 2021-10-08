import sys

def del_node(n):
    global nodes
    nodes[n] = -2
    for i in range(N):
        if nodes[i] == n:
            del_node(i)

N = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
num = int(sys.stdin.readline())

del_node(num)

cnt = 0
for i in range(len(nodes)):
    if nodes[i] != -2 and i not in nodes:
        cnt += 1

print(cnt)


# for node in nodes:
#     if node != -2 and 
# import sys

# def del_node(n):
#     global tree
#     if len(tree[n]) <= 1:
#         tree[n][0] = -2
#         return

#     for i in range(1, len(tree[n])):
#         del_node(tree[n][i])


# N = int(sys.stdin.readline())
# nodes = list(map(int, sys.stdin.readline().split()))
# num = int(sys.stdin.readline())

# tree = [[] for _ in range(51)]

# for i in range(N):
#     if nodes[i] == -1:
#         tree[i].append(nodes[i])
#     else:
#         tree[i].append(nodes[i])
#         tree[nodes[i]].append(i)

# del_node(num)

# cnt = 0
# for t in tree:
#     if len(t) == 1 and t[0] != -2:
#         cnt += 1

# print(cnt)
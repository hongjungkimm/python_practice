import sys

def del_node(n):
    return n

N = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
num = int(sys.stdin.readline())

tree = [[] for _ in range(51)]

del_node(num)
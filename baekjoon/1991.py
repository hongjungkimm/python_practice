import sys

def preorder(alpha):
    if alpha == '.':
        return ''
    return alpha + preorder(alpha_dict[alpha][0]) + preorder(alpha_dict[alpha][1])

def inorder(alpha):
    if alpha == '.':
        return ''
    return inorder(alpha_dict[alpha][0]) + alpha + inorder(alpha_dict[alpha][1])

def postorder(alpha):
    if alpha == '.':
        return ''
    return postorder(alpha_dict[alpha][0]) + postorder(alpha_dict[alpha][1]) + alpha


N = int(sys.stdin.readline())

alpha_dict = {}
for _ in range(N):
    a = sys.stdin.readline().rstrip().split()
    alpha_dict[a[0]] = []
    alpha_dict[a[0]].append(a[1])
    alpha_dict[a[0]].append(a[2])

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))
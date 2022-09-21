#1991 트리 순회  (실패)
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def firstTree(rootNode, firstLeft, firstRight):
    node1 = TreeNode()
    node1.data = rootNode

    if firstLeft != '.':
        node2 = TreeNode()
        node2.data = firstLeft
        node1.left = node2

    if firstRight != '.':
        node3 = TreeNode()
        node3.data = firstRight
        node1.right = node3
    
    return node1

def insertTree(thatNode, leftData, rightData, root):
    current = root

    while True:
        if thatNode == str(current.data):    #찾음
            if leftData != '.':
                node1 = TreeNode()
                node1.data = leftData
                current.left = node1                            #밑에 트리순회 도는 것처럼 찾으면 될듯? 재기 사용       runtime error 발생하면 첨부터 ㄱ
            if rightData != '.':
                node2 = TreeNode()
                node2.data = rightData
                current.right = node2
            break
        elif thatNode < str(current.data):
            if current.left == None:
                break
            current = current.left
        elif thatNode > str(current.data):
            if current.right == None:
                break
            current = current.right
    
    return root

def preorder(node):
    if node == None:
        return
    print(node.data, end = "")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node == None:
        return 
    inorder(node.left)
    print(node.data, end = "")
    inorder(node.right)

def postorder(node):
    if node == None:
        return 
    postorder(node.left)
    postorder(node.right)
    print(node.data, end = "")

#main
N = int(input())
rootNode, firstLeft, firstRight = map(str, input().split())
flag = False

root = firstTree(rootNode, firstLeft, firstRight)

for _ in range(N - 1):       #입력
    node, leftDescendent, rightDescendent = map(str, input().split())

    if flag == False:
        resultRoot = insertTree(node, leftDescendent, rightDescendent, root)

    if flag == True:
        resultRoot = insertTree(node, leftDescendent, rightDescendent, temp)

    temp = resultRoot
    flag = True

preorder(temp), print()
inorder(temp), print()
postorder(temp), print()    #정렬트리가 아니기때문에 data의 크기로 비교를 하며 찾아가면 안됨
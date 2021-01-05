#source https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

#node class for BST ops
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#definition
'''
The  value of every node in a node's left subtree is less than the data value of that node.
The  value of every node in a node's right subtree is greater than the data value of that node.
The  value of every node is distinct.
'''
#function to check if an input is a BST, based on definition
def checkBST(root):
    is_bst = False
    
    return is_bst

#tests
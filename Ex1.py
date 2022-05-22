from multiprocessing.sharedctypes import Value
import unittest

class TreeNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self,root):
        self.root = root

    def printTree(self,root):
        if root.left is None and root.right is None:
            print(root.data, end  = " ")
        else:
            print(root.data, end = " ")
            if root.left is not None:
                self.printTree(root.left)
            if root.right is not None:
                self.printTree(root.right)

class TestTree(unittest.TestCase):
    def testprint(self):
        leftChild = TreeNode(6,None,None)
        rightChild = TreeNode(3,None,None)
        left = TreeNode(7,None,None)
        right = TreeNode(17,leftChild,rightChild)
        root = TreeNode(1,left,right)
        tree = Tree(root)
        tree.printTree(root) #not sure how to do unit test for a print statement
        
if __name__ == '__main__':
    unittest.main()
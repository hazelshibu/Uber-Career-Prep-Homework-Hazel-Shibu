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

    def insert(self,key,root):
        if root is not None:
            if root.data == key.data:
                return root
            elif root.data < key.data:
                root.right = self.insert(key.data,root.right)
            else:
                root.left = self.insert(key.data,root.left)
        else:
            return TreeNode(key.data,None,None)

    def find(self,root,key):
        #null or root is element to be found
        if root is None or root.data == key:
            return root
        elif key.data < root.data and root.left is not None:
            return self.find(key,root.left)
        elif key.data > root.data and root.right is not None:
            return self.find(key,root.right)

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
        leftChild = TreeNode(26,None,None)
        rightChild = TreeNode(3,None,None)
        left = TreeNode(1,None,None)
        right = TreeNode(17,leftChild,rightChild)
        root = TreeNode(7,left,right)
        tree = Tree(root)
        keyNode = TreeNode(8,None,None)
        key2Node = TreeNode(3,None,None)
        # tests not working, I think I'm just defining the tree wrong
        tree.insert(keyNode,root)
        print(tree.find(key2Node,root))
        tree.printTree(root)
        
if __name__ == '__main__':
    unittest.main()

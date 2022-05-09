import unittest
class Node:
    def __init__(self,val = None):
        self.next = None
        self.value = val

class LinkedList:
    def __init__(self,curr = None):
        self.current = curr

    def size(self):
        count = 0
        x = self.current
        while x is not None:
            count = count + 1
            x = x.next
        return count
        
    def push(self, node):
        if self.current is not None:
            x = self.current
            while x.next is not None: #traverses the linked list
                x = x.next
            x.next = node
        else:
            self.current = node

    def pop(self):
        if self.current is not None:
            x = self.current    
            while x.next is not None:
                prev = x
                deletednode = x
                x = x.next
            prev.next = x.next
        return deletednode
    
    def insert(self,index,addednode):
        x = self.current
        iteration = 0
        if index == 0:
            addednode.next = self.current
            self.current = addednode
        else:
            while x is not None:
                if index-1 == iteration:
                    addednode.next = x.next
                    x.next = addednode
                    break
                x = x.next
                iteration = iteration + 1
    
    # not working          
    def remove(self,index):
        previousNode = Node()
        x = Node()
        x = self.current
        for i in range(1,index):
            previousNode = x
            x = x.next
        previousNode.next = x.next
        del(x)
    
    def elementAt(self,index):
        x = self.current
        if index < self.size():
            for i in range(0,index):
                x = x.next
        else:
            return None
        return x
        
    def printList(self):
        x = self.current
        while x is not None:
            print(x.value, end = " ")
            x = x.next

    # for testing        
    def returnedList(self):
        x = self.current
        returnedList = ""
        while x is not None:
            returnedList += str(x.value) + " "
            x = x.next
        return returnedList

    def hasCycle(self):
        p1 = self.current
        p2 = self.current
        while p1 is not None and p1.next is not None:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                return True
        return False

class TestLinkedList(unittest.TestCase):
    def testPushBackAddsOneNode(self):
        n = LinkedList()
        n.push(Node(5))
        self.assertEqual(n.returnedList(),'5 ')
        
    def testPopBackRemovesCorrectNode(self):
        n = LinkedList()
        n.push(Node(5))
        n.push(Node(6))
        n.pop()
        self.assertEqual(n.returnedList(),"5 ")

    def testEraseRemovesCorrectNode(self):
        n = LinkedList()
        n.push(Node(5))
        n.push(Node(6))
        n.push(Node(7))
        n.remove(1)
        self.assertEqual(n.returnedList(),"5 7 ")

    def testEraseDoesNothingIfNoNode(self):
        n = LinkedList()
        n.push(Node(5))
        n.push(Node(6))
        n.push(Node(7))
        n.remove(4)
        self.assertEqual(n.returnedList(),"5 6 7 ")

    def testElementAtReturnNode(self):
        n = LinkedList()
        n.push(Node(5))
        n.push(Node(6))
        self.assertEqual(n.elementAt(0).value,5)
        self.assertEqual(n.elementAt(1).value,6)
        
    def testElementAtReturnsNoNodeIfIndexDoesNotExist(self):
        n = LinkedList()
        n.push(Node(5))
        n.push(Node(6))
        self.assertEqual(n.elementAt(2),None)
        
    def testSizeReturnsCorrectSize(self):
        n = LinkedList()
        n.push(Node(5))
        n.push(Node(6))
        self.assertEqual(n.size(),2)
        
    def testCycle(self):
        n = LinkedList()
        node1 = Node(5)
        n.push(node1)
        n.push(Node(6))
        n.push(node1)
        n2 = LinkedList()
        n2.push(Node(5))
        n2.push(Node(6))
        self.assertTrue(n.hasCycle())
        self.assertFalse(n2.hasCycle())
        
if __name__ == '__main__':
    n = LinkedList()
    unittest.main()
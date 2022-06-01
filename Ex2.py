import queue

class OrganizationStructure:
    class Employee:
        def __init__(self,name,title):
            self.name = name
            self.title = title
            self.directReports = []

    def printLevelByLevel(self,root):
        popped_element = None
        num_levels = 0
        counter = -1
        if root is not None:
            queue_organization = []
            queue_organization.append(root)
            while len(queue_organization) != 0:
                popped_element = queue_organization.pop(0)
                print("Name: ", popped_element.name," ", "Title: ", popped_element.title)
                i = 0
                while i < len(popped_element.directReports):
                    queue_organization.append(popped_element.directReports[i]) 
                    i += 1
        else:
            return

o = OrganizationStructure()
root1 = o.Employee("A","CEO")
root2 = o.Employee("B","CFO")
root3 = o.Employee("C","CTO")
root4 = o.Employee("I","Director")
root5 = o.Employee("J","Sales Representative")
root6 = o.Employee("K","Sales Intern")
root7 = o.Employee("D","Manager")
root8 = o.Employee("E","Manager")
root9 = o.Employee("F","Engineer")
root10 = o.Employee("G","Engineer")
root11 = o.Employee("H","Engineer")
root1.directReports.append(root2)
root1.directReports.append(root3)
root2.directReports.append(root4)
root4.directReports.append(root5)
root5.directReports.append(root6)
root3.directReports.append(root7)
root3.directReports.append(root8)
root7.directReports.append(root9)
root7.directReports.append(root10)
root7.directReports.append(root11)
o.printLevelByLevel(root1)

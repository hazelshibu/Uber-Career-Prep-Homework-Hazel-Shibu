import queue

class OrganizationStructure:
    class Employee:
        def __init__(self,name,title):
            self.name = name
            self.title = title
            self.directReports = []

    def printLevelByLevel(self,root):
        if root is not None:
            queue_organization = []
            queue_organization.append(root)
            queue_below = []
            output_arr = []
            arr = []
            while len(queue_organization) != 0:
                for root in queue_organization:
                    arr.append(root)
                    while len(root.directReports) != 0:
                        queue_below.append(root.directReports[0])
                        root.directReports.pop(0)
                output_arr.append(arr)
                arr = []
                queue_organization = queue_below
                queue_below = []
        for x in output_arr:
            for y in x:
                print("Name:",y.name+",","Title:",y.title)
            print()
            
    def printNumLevels(self,root):
        if root is not None:
            queue_organization = []
            queue_organization.append(root)
            queue_below = []
            output_arr = []
            arr = []
            while len(queue_organization) != 0:
                for root in queue_organization:
                    arr.append(root)
                    while len(root.directReports) != 0:
                        queue_below.append(root.directReports[0])
                        root.directReports.pop(0)
                output_arr.append(arr)
                arr = []
                queue_organization = queue_below
                queue_below = []
        c = 0       
        for x in output_arr:
            c += 1
        print(c)

o = OrganizationStructure()
o2 = OrganizationStructure()
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
roota = o2.Employee("A","CEO")
rootb = o2.Employee("B","CFO")
rootc = o2.Employee("C","CTO")
rootd = o2.Employee("I","Director")
roote = o2.Employee("J","Sales Representative")
rootf = o2.Employee("K","Sales Intern")
rootg = o2.Employee("D","Manager")
rooth = o2.Employee("E","Manager")
rooti = o2.Employee("F","Engineer")
rootj = o2.Employee("G","Engineer")
rootk = o2.Employee("H","Engineer")
roota.directReports.append(rootb)
roota.directReports.append(rootc)
rootb.directReports.append(rootd)
rootd.directReports.append(roote)
roote.directReports.append(rootf)
rootc.directReports.append(rootg)
rootc.directReports.append(rooth)
rootg.directReports.append(rooti)
rootg.directReports.append(rootj)
rootg.directReports.append(rootk)
o.printNumLevels(root1)
o2.printLevelByLevel(roota)
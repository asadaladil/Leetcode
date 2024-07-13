class Monarchy:
    def __init__(self, name):
        self.tree={}
        self.tree[name]=[] 
        self.death=[]
        self.monarchy=name
    def Birth(self, child, parent):
        if parent in self.tree:
            self.tree[parent].append(child)
            self.tree[child]=[]
    def Death(self,name):
        self.death.append(name)
    def getOrderofSuccession(self):
        order=[]
        def DFS(Name):
            if Name not in self.death:
                order.append(Name)
            for name in self.tree[Name]:
                DFS(name)
        DFS(self.monarchy)
        return order


Family=Monarchy("Jake")
Family.Birth("Catherine","Jake")
Family.Birth("Jane","Catherine")
Family.Birth("Farah","Jane")
Family.Birth("Tom","Jake")
Family.Birth("Celine","Jake")
Family.Birth("Mark","Catherine")
Family.Birth("Peter","Celine")
print(Family.getOrderofSuccession())
Family.Death("Jake")
Family.Death("Jane")
print(Family.getOrderofSuccession())
import string 
class Name_Vector:
    def __init__ (self,name):
        self.alphabet = string.ascii_uppercase
        self.name = name
        self.vectors = []
        self.create_vectors()
        
    def create_vectors(self):
        for alpha in self.name:
            vector = []
            for alp in self.alphabet:
                if alpha == alp:
                    vector.append(1)
                else:
                    vector.append(0)
            self.vectors.append(vector)
    
    def display(self):
        for i, s in enumerate (self.vectors):
            print(self.name[i],s)
NV = Name_Vector("VINAY KUMAR REDDY")
NV.display()
        
class PartyAnimal:
    x=0
    name=""
    
    def __init__(self, z):
        self.name=z;
        print(self.name,'constructed')
    
    def party(self):                   
        self.x=self.x+1
        print(self.name,'Party count',self.x)
        
    def __del__(self):
        print(self.name,'destructed')
        
        
        
s=PartyAnimal('Sally')
s.party()

j=PartyAnimal('Jim')
j.party()
s.party()



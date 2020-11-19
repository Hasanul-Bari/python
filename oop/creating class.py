class PartyAnimal:
    x=0
    
    def party(self):                    #here self is the calling object
        self.x=self.x+1
        print('So far',self.x)
        
        
        
an=PartyAnimal()

an.party()         # like -> PartyAnimal.party(an)
an.party()
an.party()


print('Type',type(an))
print('Dir',dir(an))
class square:
    def __init__(self,a):
        self.a =a
        
    def sq(self):
        return self.a**2
    
s=square(3)
print(s.sq())
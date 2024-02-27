class Computer:
    
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram 
    def config(self):
        print("Config is", self.ram, self.cpu)
        

comp1 =  Computer('i5', '32gb')
comp2 = Computer('i7', '64gb')

comp1.config()
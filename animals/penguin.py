from movements import IWalking, ISwimming


class Penguin(IWalking, ISwimming):
  
  def __init__(self, name):
    ISwimming.__init__(self)
    IWalking.__init__(self)
    self.name = name
  
  def walk(self):
    print(f'{self} waddles')
    
  def __str__(self):
    return f'{self.name} the Penguin'
  
  # Penguin class is now composed of the methods and properties of two smaller, focused classes

#Task 7
class PokemonBasic:
  def __init__(self, name = 'Default', hp = 0, weakness = 'None', type = 'Unknown'):
    self.name = name
    self.hit_point = hp
    self.weakness = weakness
    self.type = type
  def get_type(self):
    return 'Main type: ' + self.type
  def get_move(self):
    return 'Basic move: ' + 'Quick Attack'
  def __str__(self):
    return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness
class PokemonExtra(PokemonBasic):
    def __init__(self,*args):
      self.s_move=None
      self.o_move=None
      if len(args)==4:
        super(). __init__(args[0],args[1],args[2],args[3])
      else:
        super(). __init__(args[0],args[1],args[2],args[3])
        self.s_move=args[4]
        self.o_move=args[5]
    def get_type(self):
      if self.s_move==None and self.o_move==None:
        s=super().get_type()
      else:
        s=super().get_type()
        s+=", "
        s+=f"Secondary type: {self.s_move}"
      return s
    def get_move(self):
      if self.s_move==None and self.o_move==None:
        s=super().get_move()
      else:
        s=super().get_move()
        s+=f"\nOther move: {','.join(self.o_move)}"
      return s

print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())

print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())

print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())

class Test5:
  def __init__(self):
      self.sum = 0
      self.y = 0
  def methodA(self):
      x=y=k=0
      msg = [5]
      while (k < 2):
          y += msg[0]
          x = y + self.methodB(msg, k)
          self.sum = x + y + msg[0]
          print(x ," " , y, " " , self.sum)
          k+=1
  def methodB(self, mg2, mg1):
        x = 0
        self.y += mg2[0]
        x = x + 3 + mg1
        self.sum += x + self.y
        mg2[0] = self.y + mg1
        mg1 += x + 2
        print(x , " " ,self.y, " " , self.sum)
        return mg1
t1=Test5()
t1.methodA()
t1.methodA()
t1.methodA()
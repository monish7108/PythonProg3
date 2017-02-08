class S:
   nInstances = 0
   @classmethod
   def __init__(self):
      self.nInstances = self.nInstances + 1

   #@staticmethod
   #def howManyInstances():
    #  print('Number of instances created: ', S.nInstances)


a=S()
print(a.nInstances)
#a.howManyInstances()
print(a.nInstances)
S()
print(S.nInstances)
S.__init__()
print(S.nInstances)
print(S.nInstances)
S.__init__()
print(S.nInstances)
S()
c=S.__init__().nInstances
print(S.nInstances)
print(c)
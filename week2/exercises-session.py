# impure function
def changeName(person, newName):
  person['name'] = newName

# pure function (sort of :) )
def changeName2(person, newName):
  person['name'] = newName
  return person


# exercise 1
#def constrain(value, low, high):
 #   ''' low if value is < low, high if value is > high. otherwise, return value. '''
    # implement me


def constrain(x, y, z):
  if x < y:
    x = y
  elif x > z:
    x = z
  else: x = x
  return x 

def constrain2(x,y,z):
  
  if x < y:
    return x
  
  elif x > z:
    return z
  
  return x

hello=int(input("what value is it?"))
low=int(input("what is your low?"))
high=int(input("what is your high?"))

print( constrain(hello, low, high) )


# constrain()

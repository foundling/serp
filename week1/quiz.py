#
# CONDITIONALS
#

# will this print something?
if True and False and True:
    print("#1 ran")

# will this print something?
if True or False and True: 
    print("#2 ran")

# what will this print?
if 0:
    print("#3a ran")
else:
    print("#3b ran")

#
# NAMES AND REFERENCES
#

a = 1
b = a
c = b
b = 2

# Q1: what is 'c' ? 


d = { 'name': 'alex' }
e = d
f = e
f['name'] = 'brad'
# Q2: what is f?

g = dict(d)
# Q3: what is g ?


#
# IDENTITY
#

# Q4: what does this print?
print(1 is True)

# Q5: what does this print?
print(1 == True)


#
# IMPLEMENTING FUNCTION CODE
#

def my_sum(nums):
    ''' calculate the total from each num in the list nums '''

    total = 0

    # Q6: implement the code to calculate a toal from a list of nums  
    
    return total

def findFirstIndex(nums, target):

    ''' finds first index of target in list nums, or returns -1 '''

    firstIndex = -1

    # Q7: implement function logic
 
    return firstIndex

# Another example: Let A and B be two sets, the cross product (or Cartesian product) of A and B, written A×B, is the set of all pairs wherein the first element is a member of the set A and the second element is a member of the set B. 

# Mathematical definition: 
# A×B = {(a, b) : a belongs to A, b belongs to B}. 
# It's easy to be accomplished in Python:

colours = ['red', 'green','yellow','blue']
things = ['house','car','tree']

colured_things = [(x,y) for x in colours for y in things]
print(colured_things)



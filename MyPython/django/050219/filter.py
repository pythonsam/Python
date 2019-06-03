# nums =[1,3,4,5,6,7,8,9,10]
even = list(filter(lambda n:n%2 == 0,range(10)))
print(even)

double = list(map(lambda n:n*2,even))
print(double)

red = reduce(lambda a,b:a+b,double)
print(red)

name =['Roger', 'Nick', 'Wayne']
eid =[1,2,3]
sal=[100,200,300]
mapped = zip(name,eid,sal)
# print ("The zipped result is : ",end="") 
print (mapped) 

print('###################################')

# To Unzip the values 

name  = zip(*mapped)
print(name)

eid = zip(*mapped)
print(eid)

sal=zip(*mapped)
print(sal)

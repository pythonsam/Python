1) Fibanacci Series


def febn():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for n in febn():
    if n > 100:
        break
    print(n)


2) Factoral for given number

"""
The factorial of a number is the product of all the integers from 1 to that number.
For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.
Factorial is not defined for negative numbers and the factorial of zero is one, 0! = 1.
"""

# change the value for a different result
num = 7

# uncomment to take input from the user
# num = int(input("Enter a number: "))

factorial = 1
# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("The Factorial of", num, "is", factorial)



3) Remove duplicate values from list

mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)


4) Repeated charecters count in string

import collections
str1 = 'thequickbrownfoxjumpsoverthelazydog'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))


5) How to get even numbers from range of 1 to 100
for num in range(1, 100):

    if num % 2 == 0:
        print(num)


6) How to get odd numbers from range of 1 to 100

for num in range(1, 100):

    if num % 2 != 0:
        print(num)



7) How to know given number is even or odd

num = int(input("Enter a Num : "))
if (num % 2) == 0:
    print("{0} is Even" .format(num))
else:
    print("{0} is Odd" .format(num))




8) How to list prime numbers in range of 1 to 20

# uncomment the following lines to take input from the user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

9) How to know given numbers is prime number or not

num =int(input("Enter Num : "))

for i in range(2, num):
    if num % i == 0:
        print("Not a Prime")
        break
else:
        print("prime")


10) Prime number in list comprihence

N = 40
[p for p in range(2,N) if 0 not in [p%d for d in range(2,p)]]
Out[3]: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


11) Gmail id matching using regular expressions
s = 'my first email is user1@gmail.com second email is enter code hereuser2@yahoo.in and third email is user3@outlook.com shyam.sam33@gmail.com'
print(re.findall('[a-zA-Z0-9_.+-]+@gmail+\S+[.in|.com|]',s))

12) IP address matching using regular expressions
    13)     import re
    14)     ip = '1.200.33.25'
    15)     print re.search(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip)
16) MAC address matching using regular expressions

17) Reverse a string

text = "this is string"
text[::-1]
output -'gnirts si siht'

18) Reverse words in a given string 'exp' => ' hi how are you' to 'ih woh era uoy'

Prerequisites :
1. split()
2. Reversing Techniques in Python
3. List Comprehension Method in python
4. join()

First split the the sentence into list of words.
Reverse each word of the string in the list individually.
Join the words in the list to form a new sentence.
Below is the implementation of above idea.

filter_none
edit
play_arrow

brightness_4
# Python code to Reverse each word 
# of a Sentence individually 
  
# Function to Reverse words 
def reverseWordSentence(Sentence): 
  
    # Spliting the Sentence into list of words. 
    words = Sentence.split(" ") 
      
    # Reversing each word and creating 
    # a new list of words 
    # List Comprehension Technique 
    newWords = [word[::-1] for word in words] 
      
    # Joining the new list of words 
    # to for a new Sentence 
    newSentence = " ".join(newWords) 
  
    return newSentence 
  
# Driver's Code  
Sentence = "GeeksforGeeks is good to learn"
# Calling the reverseWordSentence  
# Function to get the newSentence 
print(reverseWordSentence(Sentence)) 
Output:skeeGrofskeeG si doog ot nrael

--------------------------------------
# Python code to Reverse each word 
# of a Sentence individually 
  
# Function to Reverse words 
def reverseWordSentence(Sentence): 
  
    # All in One line 
    return ' '.join(word[::-1] for word in Sentence.split(" ")) 
  
# Driver's Code  
Sentence = "Geeks for Geeks"
print(reverseWordSentence(Sentence))  




19) Sort a list with out inbuild functions
l = [64, 25, 12]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print (l)
    
20) Get max value from list with out inbuilt function
    def highestNumber(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax


print (highestNumber ([77,48,19,17,93,90]))
21) Anagram logic

def check(s1, s2): 
      
    # the sorted strings are checked  
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")          
          
# driver code   
s1 ="listen"
s2 ="silent" 
check(s1, s2) 

22) Palindrome Logic
list=input('enter a string:')

if (list==list[::-1]):
    print ("It is a palindrome")
else:
   print("it is not palindrome")
   
23) Swap 2 values of 2 variables without using a third variable

x=1
y=2
x,y = y,x
print(x)
print(y)

24) Find Max and Min values without max and min functions

AList = [991,11,2,3,4]

sorted_list = sorted(AList)
print(sorted_list)
minValue = sorted_list[0]
maxValue = sorted_list[-1]

print (minValue)
print (maxValue)


25) Convert two lists into one dictionary and list into dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)



26) find Missing number in list 'ex' => [1,2,3,5,6] 4 is missing number

def missing_numbers(num_list):
    original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
    num_list = set(num_list)
    return (list(num_list ^ set(original_list)))


print(missing_numbers([1, 2, 3, 4, 6, 7, 10]))
print(missing_numbers([10, 11, 12, 14, 17]))

27) remove duplicate characters in string

from collections import OrderedDict
def remove_duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))
     
print(remove_duplicate("python exercises practice solution"))
print(remove_duplicate("w3resource"))


28) Get duplicate lines count in a file

from collections import Counter
with open('C:/Users/shyam.emmadi/Desktop/data1.txt') as f:
     c=Counter(c.strip().lower() for c in f if c.strip()) #for case-insensitive search
     for line in c:
         if c[line]>1:
             print(line)

29) Get only number words count in a file

word_count = 0
file_name = "C:/Users/shyam.emmadi/Desktop/data1.txt"
with open(file_name,'r') as file:
  for line in file:
    word_count += len(line.split())
print ("number of words : ",word_count)

30) Get repeated words count in a file

import re
from collections import Counter
f=open('C:/Users/shyam.emmadi/Desktop/data1.txt', 'r')
passage = f.read()
words = re.findall(r'\w+', passage)
cap_words = [word.upper() for word in words]
# Converting to uppercase so that 'Is' & 'is' like words  should be  considered as same words
word_counts = Counter(cap_words)
print(word_counts)


31) Get each character count in a string

char_count = 0
file_name = "C:/Users/shyam.emmadi/Desktop/data1.txt"
with open(file_name, 'r') as file:
  for line in file:
    lst=list(line)
    for char in lst:
     char_count += len(char.split())
print("number of chars: ", char_count)

32) write one file data into another file

from shutil import copyfile
copyfile('test.py', 'abc.py')

33) write 3files data into one file

34) Use of *args and **kwargs 
35) How to find given string is lower or not ?
36) D/B extend and append in list methods ?
37) D/B remove and pop ?
38) D/B list and tuple ?
39) D/B open and with open to open a file ?
40) D/B match and search methods in re module ?
41) How to handle exceptions in python ?
42) Use of break, pass and continue ?
43) Use of type() and dir() functions ?
44) Use of self in class method.
45) Use of __init__ method in class ?
46) Use of super() function ?
47) What is inheritance and D/B multi inheritance and multi-level ?
48) Types of parameters for function ?
49) Use of map() and reduce() functions ?
50) Use of decorator ?
51) difference between iterator and generator?
52) How to convert list values into string ?

mylist=['a','b','c'] 
' '.join(mylist)


mylist = [1, 2, 3]      
''.join(str(e) for e in mylist)


53) How to match date using regx
54) How to get possible combination strings in a given string 
55) How to get string like below "Hellow word'

Hw
Eo
Lr
Ld

56) Override a parent class magic method and call parent method
57) Get a devisable values with 10 form 100 numbers using map
58) __New__ and __init__
59) New is used to create a constructor , init is used to initiate object 
60) Eval, str, id, type, dir, help, super, and repr 


            ####      ROBOT FRAMEWORK       ####
1) What is robot framework.
2) How to develop keywords 
3) How to import python file 
4) What are the predefine keywords you have used.
5) How to define library 
6) What is resouse file and how to import.
7) How to run particular test case
8) How to run failed jobs 
9) Use of dryrun option 
10) How to continue script if keyword fail


           ###      SELENIUM       ####
1) What is selenium 
2) Types of waits and difference
3) Types of xpaths and difference
4) How to create dynamic xpath
5) How to select dropdown values 
6) How to click on element 
7) How to take screenshot 
8) ID and Xpath which one is fast
9) How to get text 
10) How to get window title
11) Types od selenium exceptions 
12) How to do mouse operations 
13) How to do double click operations 
14) How to handle popups 
15) How to refresh page
16) How to do scroll down
17) How to enter text into text box
18) What are the element identifiers


                ###          REST API         ###
1) What is rest API 
2) What are the HTTP methods 
3) Difference between post and put
4) What are the response cods 
5) What is the status of return code 200 and 201,202,400,404, 500
6) Use of get 
https://www.tutorialspoint.com/restful/restful_interview_questions.htm























print("Hello World")
print("test")


# function/methods/process/procedures - synonyms
# may take 0 to many input/parameters/arguments (s)
# does something ( a set of instruction/code)
# may return 0 to many output(s)
def add_number( a , b):
    # some steps/instructions involving input(s)
    # a = 3 #store RHS into LHS
    c = (a+b)
    return c
def doNothingSpecial():
    a = 1
    b = 4
    c = a - b


#variables are like boxes - they can store value
#functions do/make things - like a recipe
result = add_number(4, 5 )
print( "output: ", result  )
print( "output: ", doNothingSpecial()  )

something = 'Hello World'
myCalc = (1 + 2) * 3
myNumList = [1, 2]
myList = ['hello', 'world', 'cooking', 'eating', 'food' , 'apple' ] 
print(myNumList) 
print(  myList  )
lastIndex = len(myList) - 1
print(   myList[   lastIndex  ]   ) #' last index is len() - 1'


# 2 kinds of for loops
# 1 - for i in range(stop) or range(start,stop) or range(start, stop, step)
for xyz in range(2,10,2): # [2,4,6,8]
    print(xyz)

# 2 - for item in <list>
for xyz in myList: # for each item in the list, store into item at each loop
    #xyz = 'world'
    print(xyz)

for i in range(0, len(myList) ): # [2,4,6,8]
    xyz = myList[i]
    print(xyz)


keepLooping = True

d = 1

while d < 5 :
    #do something / code block
    print( 'value of abc: ', d)
    d += 1 # d = d + 1
    keepLooping = False
'''
if <cond>:
    <code block>
'''
if False:
    #do this
    print( "1) It's true !")
'''
if <bool>:
    <code block>
else:
    <code block>   
'''

if False:
    #do this
    print( "2) It's true !")
else:
    print( "2) It's false !")


'''
TODO:
 - while [DONE]
 - if else
 - a += b #    a = a + b [DONE]
 - input
 - str format
 - try/except (exception handling)
 - casting
'''
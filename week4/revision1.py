country = 'AU'

diction = { 'house number': 28 , 'street name': 'Butler' , 'suburb': 'Potts Point' , 'postcode':'WY 123' , 'country': country }

diction['postcode']= 2000


print(diction['postcode'])
print(diction['country'])



myList =  []
for i in range(0,20):
    print( i )
    myList.append('*')
    
myOuterList =  []
for a in range(1,31):
    #myOuterList.append(myList)
    diction[a] = myList
#print( myOuterList )

for k,v in diction.items():
    print( k,v , ',' )



#print( 'hello %s to %d Butler St' %  ('Prisca', 13.5 )        )

#print( 'hello {name} to {street_no} Butler St'.format(name='Prisca', street_no=16)  )


for p in range(1,11):
    for i in range(10,p, -1):
        print('*', end='')
    print('')
    #print('*' * (p) )

"""
*
**
***
****
*****
******
*******
********
*********
**********
"""
"""Ask for a number repeatedly until actually given one.



    Ask for a number, and if the response is actually NOT a number (e.g. "cow",

    "six", "8!") then throw it out and ask for an actual number.

    When you do get a number, return it.

    """
def fun( ):
    keeplooping = True
    while keeplooping:
        userinput = input('say a number')
        try:
            Stubbornasker= int( userinput )
            return Stubbornasker
            print(Stubbornasker)
        except:
            continue

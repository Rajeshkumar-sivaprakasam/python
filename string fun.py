a="hello world programming and this your rajesh"
z=a.capitalize()
print("capitalize",z)
y=a.count('o',0,len(a))
print("count",y)
a.upper()                    #convert to upper
a.lower()                    #convert to lower
a.isupper()                  #return true if it's uppercase
a.islower()                  #return true if it's lowercase
a.istitle()                  #return true if it's 1st letter captialed
a.title()                    #convert to 1st letter captial
a.index('a',0,len(a))        #return  1st occurence index no     
a.find('a',0,len(a))         #return  1st occurence index no
a.startswith('a',0,len(a))   #return true if it's startswith 'a'
a.endswith('a')              #return true if it's endswith 'a'
a.rfind('l',0,len(a))        #return  1st from reverse occurence index no
a.rindex('l',0,len(a))       #return  1st from reverse occurence index no
a.replace('hello','Hello')   #replace old str to new (parameter one is old 2 is new one)
a.join()                     #is used to join a seprate element of a list ex: str=','.join(mylist)
a.split()                    #is used to split a string element of a list ex:  str=mylist.split(" ")

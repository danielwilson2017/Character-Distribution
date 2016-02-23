"""
distribution.py
Author: Daniel Wilson
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.

string = str(input("Please enter a string of text (the bigger the better): "))
b = (int(len(string)))
print('The distribution of characters in "' + string + '." is :') 
l = list(string)
sost = string.split(' ')

"""




def compair(a, b) : 
    return b > a

string = str(input("Please enter a string of text (the bigger the better): "))
string1 = string.lower()
print('The distribution of characters in "' + string + '." is :') 
ap = "abcdefghijklmnopqrstuvwxyz"
result=[]
ln=[]

for c in ap:
    r = string.count(c)
    if not r == 0:
        t = (r*c)
        result.append(t)
        ln.append(r)
        

ln.sort(reverse=True)
print(ln)
print(result)


'''
need to sort on github
'''


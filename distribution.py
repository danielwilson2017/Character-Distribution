"""
distribution.py
Author: Daniel Wilson
Credit: Avery Wallis, Payton Sterns

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is
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

Notice about this example

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.

"""




def compair(a, b):
    while b > a:
        return b > a

string = str(input("Please enter a string of text (the bigger the better): "))
string1 = string.lower()
print('The distribution of characters in "' + string + '." is :') 
ap = "abcdefghijklmnopqrstuvwxyz"
result=[]
ln=[]
new=[]

for c in ap:
    r = string.count(c)
    if not r == 0:
        t = (r*c)
        result.append(t)
        ln.append(r)
        

lists=zip(ln, result)
lists=sorted(lists, key=lambda ln: ln[0])
ln.sort(reverse=True)
print(list(lists))
lists.sort(reverse=True)
q= list(lists)
s=len([x[0] for x in lists])
for j in range(0,s+1):
    if not j == (j + 1):
        print(j)


def bsort(seq, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it



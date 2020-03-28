"""
Title     : Alphabet Rangoli
Subdomain : Strings
Domain    : Python 2.0
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""
def myfun(size):
        # your code goes here
    mystr="a"
    tmpstr=""
    for i in range(1,size):
        mystr+=("-"+str(chr(97+i)))
        tmpstr=str(chr(97+i))+"-"+tmpstr
    tmp=tmpstr+mystr
    return tmp;

def remove(mystr):
    sz=len(mystr)/2;
    tsr="--"+mystr[:sz-1]+mystr[sz+3:]+"--"
    return tsr;

def print_rangoli(size):
    sz=(4*(size-1)+1)
    mstr=myfun(size);
    tsrt=mstr;
    ls=[]
    for i in xrange(size):
        ls.append(tsrt)
        tsrt=remove(tsrt);
    for i in xrange(len(ls)-1,0,-1):
        print ls[i]
    for i in ls:
        print i
        
if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)

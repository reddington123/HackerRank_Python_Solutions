"""
Title     : String Formatting
Subdomain : Strings
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/python-string-formatting/problem
"""
def num_digits(number,base):
    n=0;
    while(number>0):
        number=number//base;
        n=n+1;
    #if(n>1):
    #    n=n-1;    
    return n;

def print_formatted(number):
    # your code goes here
    number=int(number);
    m1=num_digits(number,10);
    m2=num_digits(number,8);
    m3=num_digits(number,16);
    m4=num_digits(number,2);
    m=max(m1,m2,m3,m4);            
    #print(m1,m2,m3,m4,m);
    for i in range(number):
        #print(str(i+1).rjust(m1+1),oct(i+1)[2:].rjust(m2+1),hex(i+1)[2:].upper().rjust(m3+1),bin#(i+1)[2:].rjust(m4+1));
        print(str(i+1).rjust(m),oct(i+1)[2:].rjust(m),hex(i+1)[2:].upper().rjust(m),bin(i+1)[2:].rjust(m));

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

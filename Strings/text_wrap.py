"""
Title     : Text Wrap
Subdomain : Strings
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/text-wrap/problem
"""
import textwrap

def wrap(string, max_width):
    str_len=len(string);
    i=0;
    res="";
    while((str_len-max_width)>0):
        str_len=str_len-max_width;
        #print(string[i*max_width:(i+1)*max_width]);
        res+=(string[i*max_width:(i+1)*max_width]);
        res+="\n";
        i=i+1;
    if(str_len>0):
        #print(string[i*max_width:len(string)]);
        res+=(string[i*max_width:len(string)]);  
    return res;

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

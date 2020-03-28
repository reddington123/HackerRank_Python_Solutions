"""
Title     : Merge the Tools!
Subdomain : Strings
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/merge-the-tools/problem
"""
from collections import OrderedDict;
def merge_the_tools(string, k):
    # your code goes here
    for i  in range(0,len(string),k):
        my_dictionary=OrderedDict();
        temp_str=string[i:i+k];
        for j in range(k):
            my_dictionary[temp_str[j]]=1;
        print("".join(my_dictionary.keys()));

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

"""
Title     : Find the Runner-Up Score!
Subdomain : Basic Data Types
Domain    : Python
Author    : Sachin Kumar Tiwari
Created   : March 28,2020
Problem   : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""

if __name__ == '__main__':
    n = int(input());
    arr = map(int, input().split());
    arr=set(arr);
    arr_list=(list(arr));
    arr_list.sort(reverse=True);    
    print(arr_list[1]);
    #arr_list));

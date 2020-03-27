"""
Title     : List Comprehensions
Subdomain : Basic Data Types
Domain    : Python
Author    : Sachin Kumar Tiwari
Created   : March 28,2020
Problem   : https://www.hackerrank.com/challenges/list-comprehensions/problem
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    li=[[i,j,k]  for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k)!=n]; 
    print(li);

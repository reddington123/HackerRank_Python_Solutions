"""
Title     : Lists
Subdomain : Basic Data Types
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/python-lists/problem
"""
if __name__ == '__main__':
    N = int(input());
    mylist=[];
    for i in range(N):
        command=input().strip().split();
        if(command[0]=="insert"):
            mylist.insert(int(command[1]),int(command[2]));
        elif(command[0]=="append"):
            mylist.append(int(command[1]));
        elif(command[0]=="remove"):
            mylist.remove(int(command[1]));
        elif(command[0]=="sort"):
            mylist.sort();
        elif(command[0]=="reverse"):
            mylist.reverse();
        elif(command[0]=="pop"):
            mylist.pop();
        elif(command[0]=="print"):
            print(mylist);  

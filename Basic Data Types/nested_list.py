"""
Title     : Nested Lists
Subdomain : Basic Data Types
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/nested-list/problem
"""

def sort_second(val):
    return val[1];

if __name__ == '__main__':
    list_arr=[];
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_arr.append([name,score]);
    list_arr.sort(key=sort_second);
    first_ele=list_arr[0][1];
    second_ele=first_ele;
    for i,val in enumerate(list_arr):
        if(val[1]>first_ele):
            second_ele=val[1];
            break;
    second_list=[];
    if(first_ele!=second_ele):        
        for i,val in enumerate(list_arr):
            if(val[1]==second_ele):
                second_list.append(val[0]);
            if(val[1]>second_ele):
                break;            
    second_list.sort();
    for i,val in enumerate(second_list):
        print(val);

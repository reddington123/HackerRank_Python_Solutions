"""
Title     : Finding the percentage
Subdomain : Basic Data Types
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""
#import numpy as np;
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks=[];
    average=0;
    if(query_name in student_marks):
        marks=student_marks[query_name];
    for i,val in enumerate(marks):
        average+=val;
    if(len(marks)>0):
        average=average/len(marks);
    print("{0:.2f}".format(average));

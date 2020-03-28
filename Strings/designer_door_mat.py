"""
Title     : Designer Door Mat
Subdomain : Strings
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/designer-door-mat/problem
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
#row,col=int(input()),int(input());
#row,col=input().split();
row,col=[int(x) for x in input().split()];
row_2=row//2;
col_2=col//2;
p=".|."
string="WELCOME";
#print(row,col);
for i in range(row_2):
    print((p*(2*i+1)).center(col,"-"));
print(string.center(col,"-"));
for i in range(row_2):
    print((p*(2*(row_2-i-1)+1)).center(col,"-"));

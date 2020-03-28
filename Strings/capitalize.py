"""
Title     : Capitalize!
Subdomain : Strings
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/capitalize/problem
"""
# Complete the solve function below.
def solve(s):
    a_string =s.split(' ');
    b_string=[];
    res="";
    for word in a_string:
        b_string.append(word.capitalize());
    #res= " ".join((word.capitalize() for word in a_string));
    res=" ".join(b_string);
    return res.strip();


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result);

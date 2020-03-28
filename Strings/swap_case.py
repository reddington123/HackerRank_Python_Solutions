"""
Title     : sWAP cASE
Subdomain : Strings
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/swap-case/problem
"""
def swap_case(s):
    str="";
    #print(len(s));
    for i in range(len(s)):
        if(s[i].isupper()):
            str+=s[i].lower();
        elif(s[i].islower()):
            str+=s[i].upper();
        else:
            str+=s[i];        
        #print(type(s[i]));
    return str;
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

"""
Title     : String Validators
Subdomain : Strings
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/string-validators/problem
"""

if __name__ == '__main__':
    s = input();
    #print(s.isalnum());
    #print(s.isalpha());
    #print(s.isdigit());
    #print(s.islower());
    #print(s.isupper());
    print(any(str_i.isalnum() for str_i in s));
    print(any(str_i.isalpha() for str_i in s));
    print(any(str_i.isdigit() for str_i in s));
    print(any(str_i.islower() for str_i in s));
    print(any(str_i.isupper() for str_i in s));
    '''
    if(any(s[i].isalnum() for i in s)):
        print("True");
    else:
        print("False");
    
    if(any(s[i].isalpha() for i in s)):
        print("True");
    else:
        print("False");

    if(any(s[i].isdigit() for i in s)):
        print("True");
    else:
        print("False");

    if(any(s[i].islower() for i in s)):
        print("True");
    else:
        print("False");    

    if(any(s[i].isupper() for i in s)):
        print("True");
    else:
        print("False");
    '''    

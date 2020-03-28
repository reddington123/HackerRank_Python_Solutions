"""
Title     : What's Your Name
Subdomain : Strings
Domain    : Python(Pyhton 2.0)
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/whats-your-name/problem
"""
def print_full_name(a, b):
    print("Hello",a,b+"!","You just delved into python.");

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)

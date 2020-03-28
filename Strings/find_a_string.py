"""
Title     : Find a string
Subdomain : Strings
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/find-a-string/problem
"""
def count_substring(string, sub_string):
    len_str=len(string);
    len_sub_str=len(sub_string);
    count=0;
    for i in range(len_str-len_sub_str+1):
        #print("string={} substring={}".format(string[i:i+len_sub_str],sub_string));
        if(string[i:i+len_sub_str]==sub_string):
            count+=1;
    return count;
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)


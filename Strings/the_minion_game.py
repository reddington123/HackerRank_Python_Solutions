"""
Title     : The Minion Game
Subdomain : Strings
Domain    : Python
Author    : Sachin Kumar Tiwari
Problem   : https://www.hackerrank.com/challenges/the-minion-game/problem
"""

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def minion_game(input_str):
    # your code goes here
    vowels="AEIOU";
    score_stuart=0;
    score_kevin=0;
    for i in range(len(input_str)):
        if(input_str[i]  in vowels):
            score_kevin+=len(input_str)-i;
        else:
            score_stuart+=len(input_str)-i;
    if(score_kevin==score_stuart):
        print("Draw");
    elif(score_stuart>score_kevin):
        print("Stuart "+str(score_stuart));
    else:
        print("Kevin "+str(score_kevin));           
    '''
    len_str=len(input_str);
    vowel=[];
    consonant=[];
    vowel_dict={};
    consonant_dict={};
    for index,val in enumerate(input_str):
        if(val=="A" or val=="E" or val=="I" or val=="O" or val=="U"):
            vowel.append(index);
        else:
            consonant.append(index);
    #print(vowel);
    #print(consonant);
    for index,val in enumerate(vowel):
        for inner_val in range(val,len(input_str)):
            vowel_substr=input_str[val:inner_val+1];
            #print(val,inner_val,vowel_substr);
            if vowel_substr not in vowel_dict:
                #vowel_dict[vowel_substr]=input_str[val:len_str].count(vowel_substr);
                vowel_dict[vowel_substr]=occurrences(input_str[val:len_str],vowel_substr);
                #print(vowel_substr,vowel_dict[vowel_substr]);

    for index,val in enumerate(consonant):
        for inner_val in range(val,len(input_str)):
            consonant_substr=input_str[val:inner_val+1];
            #print(val,inner_val,consonant_substr);
            if consonant_substr not in consonant_dict:
                consonant_dict[consonant_substr]=occurrences(input_str[val:len_str],consonant_substr);
            #print(consonant_substr,consonant_dict[consonant_substr]);

    for index,val in enumerate(vowel_dict):
        score_kevin+=vowel_dict[val];
    for index,val in enumerate(consonant_dict):
        score_stuart+=consonant_dict[val];
    
    #print(score_kevin);
    #print(score_stuart);
    if(score_kevin==score_stuart):
        print("Draw");
    elif(score_stuart>score_kevin):
        print("Stuart "+str(score_stuart));
    else:
        print("Kevin "+str(score_kevin));
    '''
    
if __name__ == '__main__':
    s = input()
    minion_game(s)

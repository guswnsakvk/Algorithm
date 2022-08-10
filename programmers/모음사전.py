from itertools import permutations

def solution(word):
    dict_vowel = set()
    vowel = ['A', 'E', 'I', 'O', 'U'] * 5
    
    for i in range(5):
        new_dict = map("".join, permutations(vowel, i+1))
        dict_vowel |= set(new_dict)
    
    dict_vowel = sorted(dict_vowel)
    
    for i in range(len(dict_vowel)):
        if word == dict_vowel[i]:
            return i+1
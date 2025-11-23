# anagrams
# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def create_hashmap(word):
    hashMap = {}

    for char in word:
        if char not in hashMap:
            hashMap[char] = 0
        
        hashMap[char] += 1

    return hashMap

def anagrams(s1, s2):
    h1 = create_hashmap(s1)
    h2 = create_hashmap(s2)

    return h1 == h2


if __name__ == "__main__":
    print(anagrams('restful', 'fluster')) # -> True
    print(anagrams('cats', 'tocs')) # -> False
    print(anagrams('monkeyswrite', 'newyorktimes')) # -> True
    print(anagrams('paper', 'reapa')) # -> False
    print(anagrams('elbow', 'below')) # -> True
    print(anagrams('tax', 'taxi')) # -> False
    print(anagrams('taxi', 'tax')) # -> False
    print(anagrams('night', 'thing')) # -> True
    print(anagrams('abbc', 'aabc')) # -> False
    print(anagrams('po', 'popp')) # -> false
    print(anagrams('pp', 'oo')) # -> false


    
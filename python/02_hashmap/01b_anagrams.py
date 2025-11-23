from collections import Counter

def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)




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


    
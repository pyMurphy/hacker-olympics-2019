def anagram(words):
    word1,word2=words.strip().split()
    if sorted(word1)==sorted(word2):
        print('The words are anagrams')
    else:
        print('The words are not anagrams')

anagram(input())
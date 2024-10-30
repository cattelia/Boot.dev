from functools import lru_cache

@lru_cache()
def is_palindrome(word):
    if len(word) == 1 or len(word) == 0:
        return True
        
    if word[-1] == word[0]:
        return is_palindrome(word[1:-1])
    else:
        return False

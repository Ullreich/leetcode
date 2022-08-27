def canConstruct(ransomNote: str, magazine: str) -> bool:
    alphabet = [chr(i) for i in range(97, 123)]

    for i in alphabet:
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True

def anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for c in s:
        count[c] = count.get(c, 0) + 1

    for c in t:
        count[c] = count.get(c, 0) - 1

    for check in count.values():
        if check != 0:
            return False
    return True

if __name__ == "__main__":
    print(anagram("", ""))       # T
    print(anagram("reed", "deer"))   # T
    print(anagram("Anant", "Shukla"))   # F
    print(anagram("aab", "bba"))   # F

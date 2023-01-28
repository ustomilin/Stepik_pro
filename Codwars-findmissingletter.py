def find_missing_letter(chars):
    chars.sort()
    for i in range(len(chars)-1):
        x = ord(chars[i])+1
        if ord(chars[i+1]) != x:
            return chr(x)

print(find_missing_letter(['A','B','C','D','F']))

def alphabet_position(text):
    return ' '.join(str(ord(s)- 96) for s in text.lower() if s.isalpha())

print(alphabet_position('Hello world!'))
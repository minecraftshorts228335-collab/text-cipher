def caesar_cipher(text, shift):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            base = ord('a')
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
        elif 'A' <= char <= 'Z':
            base = ord('A')
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)
    return ''.join(result)
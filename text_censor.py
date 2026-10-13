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


words_to_hide = ["secret", "password", "spoiler"]
text = "A secret note. password, then secret."

# Берем первое слово для примера
word = words_to_hide[0] 
shift = 3

# Ищем вхождение слова (в нижнем регистре)
idx = text.lower().find(word.lower())

if idx != -1:
    end_idx = idx + len(word)
    
    # Проверяем границы: слева и справа не должно быть букв/цифр
    is_start_bound = (idx == 0) or (not text[idx - 1].isalnum())
    is_end_bound = (end_idx == len(text)) or (not text[end_idx].isalnum())
    
    if is_start_bound and is_end_bound:
        # Шифруем оригинальное слово из текста
        original_word = text[idx:end_idx]
        encrypted_word = caesar_cipher(original_word, shift)
        
        # Заменяем в тексте
        text = text[:idx] + encrypted_word + text[end_idx:]

print("После замены одного слова:", text)
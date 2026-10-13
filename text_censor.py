# 1. Функция шифра Цезаря
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


# 2. Подготовка: список слов и исходный текст
words_to_hide = ["secret", "password", "spoiler"]
text = "A secret note. password, then secret."
shift = 3

# Сохраняем оригинал для подсчёта отчёта, а работать будем с этой переменной
processed_text = text

# ==========================================
# ШАГ 3. Поиск и замена для всего списка (вставлять сюда)
# ==========================================
for word in words_to_hide:
    if not word:
        continue

    i = 0
    while i < len(processed_text):
        idx = processed_text.lower().find(word.lower(), i)
        if idx == -1:
            break

        end_idx = idx + len(word)

        # Проверка границ слова (чтобы art не находилось внутри artist)
        is_start_bound = (idx == 0) or (not processed_text[idx - 1].isalnum())
        is_end_bound = (end_idx == len(processed_text)) or (not processed_text[end_idx].isalnum())

        if is_start_bound and is_end_bound:
            original_word = processed_text[idx:end_idx]
            encrypted_word = caesar_cipher(original_word, shift)

            # Заменяем найденное слово зашифрованным
            processed_text = processed_text[:idx] + encrypted_word + processed_text[end_idx:]

            # Смещаем указатель дальше
            i = idx + len(encrypted_word)
        else:
            i = idx + 1

# Выводим результат замены текста
print("Исходный текст:", text)
print("Обработанный текст:", processed_text)
print("-" * 30)

# (Здесь дальше пойдет 4-й шаг с отчётом...)
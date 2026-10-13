def caesar_cipher(text, shift):
    """Шифр Цезаря для латиницы с сохранением регистра."""
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


# --- 1. Подготовка: список слов и исходный текст ---
words_to_hide = ["secret", "password", "spoiler"]
text = "Hello! This secret project has a password. Don't read the spoiler, it's a secret!"
shift = 3

# Сохраняем оригинал для отчёта, а работать будем с копией
processed_text = text

# --- 2 и 3. Поиск, проверка границ и замена слов ---
for word in words_to_hide:
    if not word:
        continue

    i = 0
    while i < len(processed_text):
        idx = processed_text.lower().find(word.lower(), i)
        if idx == -1:
            break

        end_idx = idx + len(word)

        # Проверка границ слова (чтобы часть слова, например art в artist, не заменялась)
        is_start_bound = (idx == 0) or (not processed_text[idx - 1].isalnum())
        is_end_bound = (end_idx == len(processed_text)) or (not processed_text[end_idx].isalnum())

        if is_start_bound and is_end_bound:
            original_word = processed_text[idx:end_idx]
            encrypted_word = caesar_cipher(original_word, shift)

            # Заменяем слово на зашифрованное
            processed_text = processed_text[:idx] + encrypted_word + processed_text[end_idx:]

            i = idx + len(encrypted_word)
        else:
            i = idx + 1

# --- Вывод результатов обработки текста ---
print("Исходный текст:")
print(text)
print("-" * 30)
print("Обработанный текст:")
print(processed_text)
print("-" * 30)

# --- 4. Создание и вывод отчёта о совпадениях ---
stats = {word: 0 for word in words_to_hide}

for word in words_to_hide:
    if not word:
        continue

    i = 0
    while i < len(text):
        idx = text.lower().find(word.lower(), i)
        if idx == -1:
            break

        end_idx = idx + len(word)

        is_start_bound = (idx == 0) or (not text[idx - 1].isalnum())
        is_end_bound = (end_idx == len(text)) or (not text[end_idx].isalnum())

        if is_start_bound and is_end_bound:
            stats[word] += 1
            i = end_idx
        else:
            i = idx + 1

print("--- ОТЧЁТ О СОВПАДЕНИЯХ ---")
total_found = 0
for word, count in stats.items():
    print(f"{word}: {count}")
    total_found += count

print(f"Всего найдено: {total_found}")
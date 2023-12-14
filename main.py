def generate_vigenere_square():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vigenere_square = []
    for i in range(26):
        row = alphabet[i:] + alphabet[:i]
        vigenere_square.append(row)
    return vigenere_square

def vigenere_cipher_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    vigenere_square = generate_vigenere_square()
    encrypted_text = ""
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            row = ord(key[key_index % len(key)]) - ord('A')
            col = ord(char) - ord('A')
            encrypted_text += vigenere_square[row][col]
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_cipher_decrypt(encrypted_text, key):
    encrypted_text = encrypted_text.upper()
    key = key.upper()
    vigenere_square = generate_vigenere_square()
    decrypted_text = ""
    key_index = 0
    for char in encrypted_text:
        if char.isalpha():
            row = ord(key[key_index % len(key)]) - ord('A')
            col = vigenere_square[row].index(char)
            decrypted_text += chr(col + ord('A'))
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

# Пример использования
plain_text = "HELLO"
key = "KEY"
encrypted_text = vigenere_cipher_encrypt(plain_text, key)
print("Зашифрованный текст:", encrypted_text)
decrypted_text = vigenere_cipher_decrypt(encrypted_text, key)
print("Расшифрованный текст:", decrypted_text)


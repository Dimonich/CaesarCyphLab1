alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
mode = int(input("Выберете режим(1-шифрование, 2-дешифрование, 3-взлом): "))

if mode == 1:
    encrypt = input("Введите сообщение: ")
    key = int(input("Введите ключ: "))
    encrypt = encrypt.lower()
    encrypted = ""
    for letter in encrypt:
        pos = alphabet.find(letter)
        newPos = pos + key
        if letter in alphabet:
            encrypted = encrypted + alphabet[newPos]
        else:
            encrypted = encrypted + letter
    print("Зашифрованное сообщение: ", encrypted)
    
if mode == 2:
    decrypt = input("Введите сообщение: ")
    key = int(input("Введите ключ: "))
    decrypt = decrypt.lower()
    decrypted = ""
    for letter in decrypt:
        pos = alphabet.find(letter)
        newPos = pos - key
        if letter in alphabet:
            decrypted = decrypted + alphabet[newPos]
        else:
            decrypted = decrypted + letter
    print("Расшифрованное сообщение: ", decrypted)

if mode == 3:
    decrypt = input("Введите сообщение: ")
    decrypt = decrypt.lower()
    for key in range(0, 26):
        decrypted = ""
        for letter in decrypt:
            pos = alphabet.find(letter)
            newPos = pos - key
            if letter in alphabet:
                decrypted = decrypted + alphabet[newPos]
            else:
                decrypted = decrypted + letter
        print("Возможная расшифровка: ", decrypted)
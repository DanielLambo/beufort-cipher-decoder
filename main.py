def decrypt(ciphertext, key):
    decrypted_message = ""
    key_length = len(key)
    
    for i in range(len(ciphertext)):
        current_char = ciphertext[i]

        # Check if the current character is a letter
        if current_char.isalpha():
            # Find the difference between the key letter and the ciphertext letter
            key_difference = ord(key[i % key_length].upper()) - ord('A')

            # Decrypt the current letter and keep the original letter's case
            decrypted_char = chr((ord(current_char.upper()) - key_difference - ord('A')) % 26 + ord('A'))
            decrypted_message += decrypted_char.lower() if current_char.islower() else decrypted_char
        else:
            # If it's not a letter, keep it as it is
            decrypted_message += current_char

    return decrypted_message


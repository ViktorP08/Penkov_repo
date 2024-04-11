# Усложненное задание из CodeWars (5 уровень сложности)
# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
# According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.
# For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.
# Test examples:
# "EBG13 rknzcyr." -> "ROT13 example."
# "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

def decrypt_message(message):
    decrypted = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((ord(char) - ord("a") + 13) % 26 + ord("a"))
            else:
                decrypted_char = chr((ord(char) - ord("A") + 13) % 26 + ord("A"))
            decrypted += decrypted_char
        else:
            decrypted += char

    return decrypted


primer1 = "EBG13 rknzcyr."
primer2 = "This is my first ROT13 excercise!"
primer_po_zadaniyu = "Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf."
print(decrypt_message(primer1))
print(decrypt_message(primer2))
print(decrypt_message(primer_po_zadaniyu))
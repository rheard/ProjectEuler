'''
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange).
    For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key.
    The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text;
    for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes.
    The user would keep the encrypted message and the encryption key in different locations, and without both "halves",
    it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message,
    which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security,
    but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
    a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words,
    decrypt the message and find the sum of the ASCII values in the original text.
'''

from __future__ import print_function
from itertools import product


_cipher = None
with open('ProjectEuler/cipher.txt', 'r') as rb:
    _cipher = "".join(chr(int(x)) for x in rb.read().split(','))


def solve(cipher=_cipher):
    for key in product(list(range(97, 123)), repeat=3):
        cipher_copy = list(cipher)

        for i, char in enumerate(cipher_copy):
            cipher_copy[i] = chr(ord(char) ^ key[i % len(key)])

        cipher_copy = "".join(cipher_copy)

        if ' the ' in cipher_copy:
            return sum(ord(x) for x in cipher_copy)


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p059_ans.txt', 'w') as wb:
        wb.write(str(answer))

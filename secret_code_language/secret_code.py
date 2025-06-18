# secret code language

import string
import random

def code_word(user1, key):
    b = user1.split()
    lst = []
    for i in b:
        if len(i) < 3:
            a = i[::-1]
            lst.append(a)
        else:
            code = i[1:] + i[0]
            rand_prefix = ''.join(random.choices(string.ascii_lowercase, k=key))
            rand_suffix = ''.join(random.choices(string.ascii_lowercase, k=key))
            code1 = rand_prefix + code + rand_suffix
            lst.append(code1)
    return ' '.join(lst)

def dcode_word(user1, key):
    b = user1.split()
    lst = []
    for i in b:
        if len(i) < 3:
            a = i[::-1]
            lst.append(a)
        else:
            if len(i) <= 2 * key:
                print('Your encryption key is greater than or equal to message length.')
                return ''
            code2 = i[key:-key]
            try:
                code1 = code2[-1] + code2[0:-1]
            except IndexError:
                print('Decryption failed due to index error.')
                return ''
            lst.append(code1)
    return ' '.join(lst)

while True:
    u = input('Enter code or decode or quit: ')
    if u.lower() == 'code':
        user1 = input('Enter your message: ')
        try:
            user2 = int(input('Enter your key (e.g., 3 or 4 or 6): '))
            print(code_word(user1, user2))
        except ValueError:
            print('Please enter only digits for encryption.')
    elif u.lower() == 'decode':
        user1 = input('Enter your message: ')
        try:
            key = int(input('Enter your key for decrypting: '))
            print(dcode_word(user1, key))
        except ValueError:
            print('Please enter only digits for decryption.')
    elif u.lower() == 'quit':
        break
    else:
        print('Please enter a valid input.')

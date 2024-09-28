"""Python Wordlist Hasher, by XxTheSunxX""" 
"""Updated on 9.28.2023"""

import hashlib
import sys

def main():
    print("Wordlist Hasher, Written by XxTheSunxX.")

    global word_list
    word_list = input("Input file name to pull words from: ")
    global hash_list
    hash_list = input("Filename to save as: ")
    hashing_algo = input("Select hashing algorithm: '1' (sha512), '2' (md5): ")
    
    answer = 'true'
    while answer == 'true':
        if hashing_algo == '1':
            sha512()
            sys.exit("Exiting software...")
        elif hashing_algo == '2':
            md5()
            sys.exit("Exiting software...")
        else:
            print('Select a valid option.')
            hashing_algo = input("Select hashing algorithm: '1' (sha512), '2' (md5): ")


def sha512():
    h = hashlib.sha512()
    f = open(word_list, 'r')
    g = open(hash_list, 'w')
    
    for word in f:
        word = word.strip('\n')
        print(word)

        h.update(word.encode())
        hashed_word = h.hexdigest()
        g.write(hashed_word)
        

def md5():
    h = hashlib.md5()
    f = open(word_list, 'r')
    g = open(hash_list, 'w')
    
    for word in f:
        word = word.strip('\n')
        print(word)

        h.update(word.encode())
        hashed_word = h.hexdigest()
        g.write(hashed_word)
        

if __name__ == "__main__":
    main()

## The software is currently not reading from line to line,
## and hashing one by one, but hashes single words; Need to fix

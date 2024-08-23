from itertools import product
from string import printable
from bcrypt import checkpw

class Bruteforce:
    def __init__(self, capturedHash):
        self.hashedPasswords = capturedHash
    
    # match the capturedhashes with the guessed(assign on line 12) password

    def matchPassword(self, hashedPasswords: bytes, password: str) -> bool:
        return checkpw(password.encode('utf-8'), hashedPasswords)

    def bruteforce(self):
        chars = printable 

        for length in range(1, 4):
            print(f"Trying length {length}")
            for attempt in product(chars, repeat=length):
                guess = ''.join(attempt)
                print(f"Trying password: {guess}")
                if self.matchPassword(self.hashedPasswords, guess):
                    return f"Password found {guess}"
        return "Password not found"



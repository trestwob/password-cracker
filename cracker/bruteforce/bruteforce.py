from itertools import islice, product
from string import printable
from bcrypt import checkpw
from concurrent.futures import ThreadPoolExecutor, as_completed

class Bruteforce:
    def __init__(self, capturedHash):
        self.hashedPasswords = capturedHash
    
    # match the capturedhashes with the guessed(assign on line 12) password

    def matchPassword(self, hashedPasswords: bytes, password: str) -> bool:
        return checkpw(password.encode('utf-8'), hashedPasswords)
    
    def bruteforceChunk(self, hashedPasswords: bytes, chars: str, length: int, start: int, end: int):
        for attempt in islice(product(chars,repeat=length), start, end):
            guess = ''.join(attempt)
            print(f"Password attempted: {guess}")
            if self.matchPassword(hashedPasswords, guess):
                return f"Password found: {guess}"
        return None


    def bruteforce(self):
        chars = printable

        totalComb = len(chars) ** 4
        chunkSize = totalComb // 8

        with ThreadPoolExecutor() as executor:
            futures = []
            for length in range(1, 4):
                for i in range(8):
                    start = i * chunkSize
                    end = start + chunkSize
                    futures.append(executor.submit(self.bruteforceChunk, self.hashedPasswords, chars, length, start, end))
            for future in as_completed(futures):
                result = future.result()
                if result:
                    return result
        return "Password not found"


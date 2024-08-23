import bcrypt
from cracker.bruteforce.bruteforce import Bruteforce 

def hashPassword(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def main():
    password = hashPassword('abcd')
    obj = Bruteforce(password)
    print(obj.bruteforce())

if __name__ == "__main__":
    main()

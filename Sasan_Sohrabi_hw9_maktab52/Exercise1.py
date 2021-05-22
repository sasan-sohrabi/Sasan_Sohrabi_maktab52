
# Import related library for generating key and also for writing script.
from cryptography.fernet import Fernet
import argparse

if __name__ == "__main__":
    # Define parser for python script
    parser = argparse.ArgumentParser(description="Cryptography")

    # Define subparsers for separating argument
    subparsers = parser.add_subparsers(dest="command")

    # Define argument for first part (A) of exercise
    key_parser = subparsers.add_parser("key", help="generate key")
    key_parser.add_argument('-n', '--name', action='store', metavar='SAVE KEY',
                            help="name for saving key", default='KEY', nargs='?')

    # Define argument for second part (B) of exercise
    encrypt_parser = subparsers.add_parser("encrypt", help="encrypt file or text")
    encrypt_parser.add_argument('-k', '--key', action='store', metavar='BYTES KEY',
                                help="Key in bytes")
    encrypt_parser.add_argument('-f', '--file', action='store', metavar='FILE NAME',
                                help="Name of file")
    encrypt_parser.add_argument('-t', '--text', metavar='TEXT',
                                help="text", nargs="?")

    # Define argument for second part (C) of exercise
    decrypt_parser = subparsers.add_parser("decrypt", help="encrypt file or text")
    decrypt_parser.add_argument('-k', '--key', action='store', metavar='BYTES KEY',
                                help="Key in bytes", default='KEY', nargs='?')
    decrypt_parser.add_argument('-f', '--file', action='store', metavar='FILE NAME',
                                help="Name of file")
    decrypt_parser.add_argument('-t', '--text', action='store', metavar='TEXT',
                                help="text")

    args = parser.parse_args()


    # Class for encrypting file and text
    class Encryption:
        class Decorators:
            @classmethod
            def mydec(cls, key: bytes):
                def inner_mydec(func):
                    def inner(*args, **kwargs):
                        fernet_obj = Fernet(key)
                        encrypted = fernet_obj.encrypt(func(*args, **kwargs).encode())
                        return encrypted

                    return inner

                return inner_mydec

        @staticmethod
        def encrypt_with_key_text(text: str, key: bytes) -> bytes:
            fernet_obj = Fernet(key)
            encrypted_text = fernet_obj.encrypt(text.encode())
            return encrypted_text

        @staticmethod
        def encrypt_with_key_file(file_path: str, key: bytes) -> None:
            with open(file_path) as file:
                with open("Encrypted_2.txt", "wb") as encrypt_file:
                    fernet_obj = Fernet(key)
                    encrypted_text = fernet_obj.encrypt(file.read().encode())
                    encrypt_file.write(encrypted_text)

        @Decorators.mydec(bytes("6SBW9f-1JmRV9IOExD6raAZ2nYMzRhBipnUFEAhg9NY=", "utf-8"))
        def text(self) -> str:
            return "sasan"


    # Class for decrypting file and text
    class Decryption:

        @staticmethod
        def decrypt_with_key_text(text: bytes, key: bytes) -> str:
            fernet_obj = Fernet(key)
            encrypted_text = fernet_obj.decrypt(text).decode()
            return encrypted_text

        @staticmethod
        def decrypt_with_key_file(file_path: str, key: bytes) -> str:
            with open(file_path, "rb") as file:
                fernet_obj = Fernet(key)
                encrypted_text = fernet_obj.decrypt(file.read()).decode()
                return encrypted_text


    # Context manager for encrypting file
    class DecryptionContextManager:

        def __init__(self, file_name: str, key: bytes, mode: str = "rb+"):
            self.file_name = file_name
            self.mode = mode
            self.key = key

        def write(self, text: str):
            new_text = self.encrypted_text + text
            text_bytes = self.fernet_obj.encrypt(new_text.encode())
            with open(self.file_name, "wb") as file:
                file.write(text_bytes)
            return None

        def read(self, *args, **kwargs):
            return self.encrypted_text

        def __enter__(self):
            self.file = open(self.file_name, self.mode)
            self.fernet_obj = Fernet(self.key)
            self.encrypted_text = self.fernet_obj.decrypt(self.file.read()).decode()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('file closed with encrypted by key.')
            return self.file.close()
    print(args)

    if args.command == "key":
        # Generate a key and save it in file.
        with open(f"{args.name}.txt", "wb") as file:
            file.write(Fernet.generate_key())

    if args.command == "encrypt":
        e = Encryption()

        if args.file and args.key:
            print(e.encrypt_with_key_file(args.file, bytes(args.key, "utf-8")))

        if not args.text and args.key:
            text_shell = ""
            try:
                while True:
                    text_shell += input("")
            except KeyboardInterrupt:
                print(e.encrypt_with_key_text(text_shell, bytes(args.key, "utf-8")))

        if args.text and args.key:
            print(e.encrypt_with_key_text(args.text, bytes(args.key, "utf-8")))

    if args.command == "decrypt":
        e = Decryption()
        if args.file and args.key:
            print(e.decrypt_with_key_file(args.file, bytes(args.key, "utf-8")))

        # if not args.text and args.key:
        #     text_shell = b""
        #     try:
        #         while True:
        #             text_shell += input(b"")
        #     except KeyboardInterrupt:
        #         print(e.decrypt_with_key_text(text_shell, bytes(args.key, "utf-8")))

        if args.text and args.key:
            print(e.decrypt_with_key_text(bytes(args.text, "utf-8"), bytes(args.key, "utf-8")))



    #     e = Encryption()
    #     print(e.encrypt_with_key_file(args.text, bytes(args.key, "utf-8")))
    # print(e.encrypt_with_key_file(args.file, bytes(args.key, "utf-8")))
    # with DecryptionContextManager(args.file, args.key) as file:
    #     print(file.read())

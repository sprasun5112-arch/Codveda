from cryptography.fernet import Fernet
import os


KEY_FILE = "secret.key"


def generate_key():
    """Generate and save an encryption key."""
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    print("Encryption key generated successfully.")


def load_key():
    """Load the encryption key from the file."""
    if not os.path.exists(KEY_FILE):
        generate_key()

    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_file(filename):
    """Encrypt the contents of a file."""
    key = load_key()
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    encrypted_filename = filename + ".encrypted"

    with open(encrypted_filename, "wb") as file:
        file.write(encrypted_data)

    print(f"File encrypted successfully: {encrypted_filename}")


def decrypt_file(filename):
    """Decrypt an encrypted file."""
    key = load_key()
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    if filename.endswith(".encrypted"):
        decrypted_filename = filename[:-10] + "_decrypted.txt"
    else:
        decrypted_filename = filename + "_decrypted.txt"

    with open(decrypted_filename, "wb") as file:
        file.write(decrypted_data)

    print(f"File decrypted successfully: {decrypted_filename}")


def main():
    print("=" * 40)
    print("     FILE ENCRYPTION / DECRYPTION")
    print("=" * 40)

    print("\n1. Encrypt a file")
    print("2. Decrypt a file")

    choice = input("\nEnter your choice: ")

    filename = input("Enter the file path: ")

    if not os.path.exists(filename):
        print("Error: File not found.")
        return

    try:
        if choice == "1":
            encrypt_file(filename)

        elif choice == "2":
            decrypt_file(filename)

        else:
            print("Invalid choice.")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
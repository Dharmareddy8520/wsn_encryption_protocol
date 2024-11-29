import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from encryption.aes import AES
from encryption.speck import SpeckCipher
from encryption.present import PresentCipher

def test_encryption():
    aes = AES()
    speck = SpeckCipher()
    present = PresentCipher()

    plaintexts = [
        b"Short",  # Less than block size
        b"ExactlyEight!",  # Exactly 8 bytes
        b"Longer than one block, let's see how it handles this!"  # Multiple blocks
    ]

    for plaintext in plaintexts:
        print(f"\nOriginal: {plaintext}")

        encrypted_aes = aes.encrypt(plaintext)
        print(f"AES Encrypted: {encrypted_aes}")
        print(f"AES Decrypted: {aes.decrypt(encrypted_aes)}")

        encrypted_speck = speck.encrypt(plaintext)
        print(f"SPECK Encrypted: {encrypted_speck}")
        print(f"SPECK Decrypted: {speck.decrypt(encrypted_speck)}")

        encrypted_present = present.encrypt(plaintext)
        print(f"PRESENT Encrypted: {encrypted_present}")
        print(f"PRESENT Decrypted: {present.decrypt(encrypted_present)}")

test_encryption()

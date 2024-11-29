import sys
import os

# Add the root directory to sys.path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from encryption.aes import AES
from encryption.speck import SpeckCipher
from encryption.present import PresentCipher
from protocols.openwsn import OpenWSN
from protocols.dash7 import DASH7

def test_protocols():
    aes = AES()
    speck = SpeckCipher()
    present = PresentCipher()

    encryption_algorithms = {
        "AES": aes,
        "SPECK": speck,
        "PRESENT": present,
    }

    plaintext = b"Test message for protocol functionality!"

    print("\n=== Testing Protocols ===\n")

    for algo_name, algo_instance in encryption_algorithms.items():
        print(f"\nTesting with {algo_name}...\n")

        # Test OpenWSN
        openwsn = OpenWSN(algo_instance)
        print(f"--- OpenWSN ({algo_name}) ---")
        packet = openwsn.prepare_packet(plaintext, headers={"Type": "Data"})
        print(f"Prepared Packet: {packet}")
        decrypted_payload = openwsn.process_packet(packet)
        assert decrypted_payload == plaintext, f"OpenWSN {algo_name} decryption failed!"
        print(f"Decrypted Payload: {decrypted_payload}")

        # Test DASH7
        dash7 = DASH7(algo_instance)
        print(f"\n--- DASH7 ({algo_name}) ---")
        response_packet = dash7.query_response("Query1", plaintext)
        print(f"Response Packet: {response_packet}")
        decrypted_response = dash7.process_response(response_packet)
        assert decrypted_response == plaintext, f"DASH7 {algo_name} decryption failed!"
        print(f"Decrypted Response: {decrypted_response}")

    print("\nAll protocol tests passed!")

if __name__ == "__main__":
    test_protocols()

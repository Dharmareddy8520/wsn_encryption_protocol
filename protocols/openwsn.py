from encryption.hmac_util import HMACUtil

class OpenWSN:
    def __init__(self, encryption):
        self.encryption = encryption
        self.hmac_util = HMACUtil(self.encryption.get_key_bytes())

    def prepare_packet(self, payload, headers):
        """Prepare a packet by encrypting the payload and generating an HMAC."""
        encrypted_payload = self.encryption.encrypt(payload)  # Encrypt the entire payload
        hmac_value = self.hmac_util.generate_hmac(encrypted_payload)  # Generate HMAC
        return {
            'headers': headers,
            'payload': encrypted_payload,
            'hmac': hmac_value,
        }

    def process_packet(self, packet):
        """Process an incoming packet by verifying the HMAC and decrypting the payload."""
        encrypted_payload = packet['payload']
        if not self.hmac_util.verify_hmac(encrypted_payload, packet['hmac']):
            raise ValueError("HMAC verification failed")

        # Extract the IV and ciphertext correctly from the payload
        iv = encrypted_payload[:16]  # First 16 bytes are the IV
        ciphertext = encrypted_payload[16:]  # Remaining bytes are the ciphertext

        # Decrypt the ciphertext using the IV
        decrypted_payload = self.encryption.decrypt(iv + ciphertext)
        return decrypted_payload

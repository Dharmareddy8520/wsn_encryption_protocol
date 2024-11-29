from encryption.hmac_util import HMACUtil

class DASH7:
    def __init__(self, encryption):
        self.encryption = encryption
        self.hmac_util = HMACUtil(self.encryption.get_key_bytes())

    def query_response(self, query, response):
        """Prepare a query-response packet."""
        # Encrypt the response
        encrypted_response = self.encryption.encrypt(response)
        # Generate HMAC for the encrypted response
        hmac_value = self.hmac_util.generate_hmac(encrypted_response)
        return {
            'query': query,
            'response': encrypted_response,
            'hmac': hmac_value,
        }

    def process_response(self, response_packet):
        """Process an incoming query-response packet."""
        encrypted_response = response_packet['response']
        if not self.hmac_util.verify_hmac(encrypted_response, response_packet['hmac']):
            raise ValueError("HMAC verification failed")

        # Extract the IV and ciphertext correctly
        iv = encrypted_response[:16]  # First 16 bytes are the IV
        ciphertext = encrypted_response[16:]  # Remaining bytes are the ciphertext

        # Decrypt the ciphertext using the IV
        decrypted_response = self.encryption.decrypt(iv + ciphertext)
        return decrypted_response

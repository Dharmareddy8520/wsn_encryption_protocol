import time

class PerformanceEvaluator:
    def measure_encryption_time(self, encryption, payload):
        """Measure the time taken to encrypt the payload."""
        try:
            start_time = time.perf_counter()  # Start high-precision timer
            encryption.encrypt(payload)  # Perform encryption
            end_time = time.perf_counter()  # End high-precision timer
            elapsed_time = end_time - start_time
            print(f"Encryption time for payload {payload}: {elapsed_time:.10f} seconds")
            return elapsed_time
        except Exception as e:
            print(f"Error during encryption: {e}")
            return 0.0

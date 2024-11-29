from encryption.aes import AES
from encryption.speck import SpeckCipher
from encryption.present import PresentCipher
from protocols.openwsn import OpenWSN
from protocols.dash7 import DASH7
from evaluation.performance import PerformanceEvaluator
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def chunk_data(data, chunk_size):
    """Split data into chunks of specified size."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def visualize_metrics_separately(results):
    """
    Visualize encryption time, decryption time, and packet size separately
    while addressing Seaborn's deprecation warning.
    """
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd

    # Transform results into a DataFrame
    data = []
    for protocol, metrics in results.items():
        data.append({"Protocol": protocol, "Metric": "Encryption Time", "Value": metrics["Encryption Time (s)"]})
        data.append({"Protocol": protocol, "Metric": "Decryption Time", "Value": metrics["Decryption Time (s)"]})
        data.append({"Protocol": protocol, "Metric": "Packet Size", "Value": metrics["Packet Size (bytes)"]})

    df = pd.DataFrame(data)

    # Set Seaborn style
    sns.set(style="whitegrid", font_scale=1.2)

    # Encryption Time
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Protocol", y="Value", data=df[df["Metric"] == "Encryption Time"], hue="Protocol", dodge=False, palette="Blues_d", legend=False)
    plt.title("Encryption Time by Protocol")
    plt.ylabel("Time (s)")
    plt.xlabel("Protocol")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Decryption Time
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Protocol", y="Value", data=df[df["Metric"] == "Decryption Time"], hue="Protocol", dodge=False, palette="Greens_d", legend=False)
    plt.title("Decryption Time by Protocol")
    plt.ylabel("Time (s)")
    plt.xlabel("Protocol")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Packet Size
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Protocol", y="Value", data=df[df["Metric"] == "Packet Size"], hue="Protocol", dodge=False, palette="Reds_d", legend=False)
    plt.title("Packet Size by Protocol")
    plt.ylabel("Size (bytes)")
    plt.xlabel("Protocol")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def main():
    # Hardcoded plaintext for testing
    plaintext = b"Texas A & M corpus corpus christi ! SecureData"

    # Initialize encryption algorithms
    aes = AES()
    speck = SpeckCipher()
    present = PresentCipher()

    # Initialize protocols with all encryption methods
    protocols = {
        "OpenWSN_AES": OpenWSN(aes),
        "OpenWSN_SPECK": OpenWSN(speck),
        "OpenWSN_PRESENT": OpenWSN(present),
        "DASH7_AES": DASH7(aes),
        "DASH7_SPECK": DASH7(speck),
        "DASH7_PRESENT": DASH7(present),
    }

    # Initialize performance evaluator
    evaluator = PerformanceEvaluator()

    results = {}

    print("\n=== Protocol Comparison ===")
    for protocol_name, protocol_instance in protocols.items():
        if isinstance(protocol_instance, OpenWSN):
            # For OpenWSN, use prepare_packet
            packet = protocol_instance.prepare_packet(plaintext, headers={"Type": "Data"})
            print(f"\nPrepared Packet ({protocol_name}): {packet}")

            # Measure encryption and decryption times
            encryption_time = evaluator.measure_encryption_time(protocol_instance.encryption, plaintext)
            decrypted_payload = protocol_instance.process_packet(packet)
            decryption_time = evaluator.measure_encryption_time(protocol_instance.encryption, packet["payload"])
        elif isinstance(protocol_instance, DASH7):
            # For DASH7, use query_response
            query_response = protocol_instance.query_response("Query1", plaintext)
            print(f"\nQuery-Response ({protocol_name}): {query_response}")

            # Measure encryption and decryption times
            encryption_time = evaluator.measure_encryption_time(protocol_instance.encryption, plaintext)
            decrypted_payload = protocol_instance.process_response(query_response)
            decryption_time = evaluator.measure_encryption_time(protocol_instance.encryption, query_response["response"])
        else:
            continue

        # Calculate packet size
        packet_size = (
            len(packet["payload"]) + len(packet["hmac"]) + sum(len(k) + len(v) for k, v in packet["headers"].items())
            if isinstance(protocol_instance, OpenWSN)
            else len(query_response["response"]) + len(query_response["hmac"]) + len(query_response["query"])
        )

        # Store results
        results[protocol_name] = {
            "Encryption Time (s)": encryption_time,
            "Decryption Time (s)": decryption_time,
            "Packet Size (bytes)": packet_size,
            "Payload Match": decrypted_payload == plaintext,
        }

    # Display results
    print("\n=== Protocol Comparison Results ===")
    for protocol, metrics in results.items():
        print(f"{protocol}: {metrics}")

    # Visualize results using Seaborn
    visualize_metrics_separately(results)


if __name__ == "__main__":
    main()

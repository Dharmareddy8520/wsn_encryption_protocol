
# WSN Encryption Protocol Comparison Project

This project compares the performance of different encryption algorithms (AES, SPECK, PRESENT) integrated with two popular Wireless Sensor Network (WSN) protocols, OpenWSN and DASH7. The metrics analyzed include encryption time, decryption time, and packet size.

## Features

- **Encryption Algorithms**: AES, SPECK, PRESENT
- **Protocols**: OpenWSN, DASH7
- **Metrics**:
  - Encryption Time
  - Decryption Time
  - Packet Size

## Results

### Protocol Performance Metrics

#### Encryption Time by Protocol
![Encryption Time](images/encryption_time.png)

#### Decryption Time by Protocol
![Decryption Time](images/decryption_time.png)

#### Packet Size by Protocol
![Packet Size](images/packet_size.png)

## Requirements

To run the project, ensure you have the following dependencies installed:

```plaintext
cryptography
seaborn
matplotlib
pandas
```

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## File Structure

```plaintext
wsn_project/
│
├── main.py                    # Main script to run the project
├── encryption/                # Encryption implementations
│   ├── aes.py
│   ├── speck.py
│   ├── present.py
│   ├── hmac_util.py
│   ├── __init__.py
│
├── protocols/                 # Protocol-specific implementations
│   ├── openwsn.py
│   ├── dash7.py
│   ├── __init__.py
│
├── evaluation/                # Evaluation utilities
│   ├── performance.py
│   ├── visualizer.py
│   ├── __init__.py
│
├── tests/                     # Test scripts
│   ├── test_encryption.py
│   ├── test_protocols.py
│
├── results/                   # Generated result plots
│   ├── encryption_time.png
│   ├── decryption_time.png
│   ├── packet_size.png
│
└── README.md                  # Project documentation
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-repo-name/wsn-encryption.git
cd wsn-encryption
```

2. Run the `main.py` script to compare protocol performance:

```bash
python main.py
```

3. Check the `results/` directory for visualized plots.

## Results Summary

### OpenWSN
| Algorithm | Encryption Time (s) | Decryption Time (s) | Packet Size (bytes) |
|-----------|----------------------|----------------------|----------------------|
| AES       | 0.000104            | 0.0000219           | 136                  |
| SPECK     | 0.0000125           | 0.0000107           | 120                  |
| PRESENT   | 0.0000108           | 0.0000063           | 120                  |

### DASH7
| Algorithm | Encryption Time (s) | Decryption Time (s) | Packet Size (bytes) |
|-----------|----------------------|----------------------|----------------------|
| AES       | 0.0000443           | 0.0001757           | 134                  |
| SPECK     | 0.0000185           | 0.000011            | 118                  |
| PRESENT   | 0.0000105           | 0.0000063           | 118                  |

## Future Work

- Integration with real-world sensor data via APIs.
- Expansion to include more lightweight cryptographic algorithms.
- Real-time testing on hardware sensor nodes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Contributors**: Dharma Reddy Pandem

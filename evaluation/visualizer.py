import matplotlib.pyplot as plt

class Visualizer:

    def plot_metrics(self, metrics, title, ylabel):
        print("Metrics for Visualization:", metrics)
        plt.bar(metrics.keys(), metrics.values())
        plt.title(title)
        plt.ylabel(ylabel)
        plt.xlabel("Encryption Algorithms")
        plt.show()

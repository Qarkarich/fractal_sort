import matplotlib.pyplot as plt


def valuelabel(bottom_labels, top_labels):
    for i in range(len(bottom_labels)):
        plt.text(i, top_labels[i], top_labels[i], ha='center',
                 bbox=dict(facecolor='cyan', alpha=0.8))

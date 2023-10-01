import matplotlib.pyplot as plt


def generate_pie_charts():
    labels = ['A', 'B', 'C']
    values = [60, 30, 10]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()

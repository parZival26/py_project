import matplotlib.pyplot as plt
import random

def random_num():
    numero = random.randint(1, 100)
    return numero

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [random_num(), random_num(), random_num()]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()

if __name__ == '__main__':
    generate_pie_chart()
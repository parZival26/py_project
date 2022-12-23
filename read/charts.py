import matplotlib.pyplot as plt
import random

def random_num():
    numero = random.randint(1, 100)
    return numero

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    # plt.savefig('pie.png')
    # plt.close()
    plt.show()

def generate_bar_chart(labels, values):
   fig, ax = plt.subplots()
   ax.bar(labels, values)
    # plt.savefig('cahrt.png')
    # plt.close()
   plt.show()
   



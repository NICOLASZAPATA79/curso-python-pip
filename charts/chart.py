import matplotlib.pyplot as plt

def generator_pie_chart():
    labels = ['A','B','C']
    values = [200,300,1500]
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig("chart.png")
    plt.close()

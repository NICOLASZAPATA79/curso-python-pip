# Graficas en python
import matplotlib.pyplot as plt

# Función grafico de barras
def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

# Función grafico de tortas (circular)

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis("equal")
  plt.show()
  

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [250, 300, 180]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)


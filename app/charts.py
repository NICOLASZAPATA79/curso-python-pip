# Graficas en python
import matplotlib.pyplot as plt

# Función grafico de barras
def generate_bar_chart(name,labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  ax.set_title(f"Evolución de la población de {name}")
  plt.savefig(f"./imgs/{name}.png")
  plt.close()

# Función grafico de tortas (circular)

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis("equal")
  plt.savefig("generate1_pie.png")
  plt.close()


if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [250, 300, 180]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)


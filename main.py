import pandas as pd
import matplotlib.pyplot as plt

name = "Datasheet.xlsx"

data = pd.read_excel(name)

data.plot(kind="bar", x="fruit", y="number", title="Favorite Fruits")

plt.show()

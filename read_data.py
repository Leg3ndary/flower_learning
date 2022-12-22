import pandas
from pandas.plotting import scatter_matrix
from matplotlib import pyplot

FILEPATH = "data/data.csv"
NAMES = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
dataset = pandas.read_csv(FILEPATH, names=NAMES)

print(dataset.shape)

print(dataset.head(20))

print(dataset.describe())

print(dataset.groupby("class").size())

dataset.plot(kind="box", subplots=True, layout=(2, 2), sharex=False, sharey=False)
pyplot.show()
dataset.hist()
pyplot.show()
scatter_matrix(dataset)
pyplot.show()

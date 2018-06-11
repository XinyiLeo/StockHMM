import datetime

import numpy as np
from matplotlib import cm, pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator
from hmmlearn.hmm import GaussianHMM
from sklearn.preprocessing import scale
import pandas_datareader.data as web

start = datetime.datetime(2016, 1, 1)
end = datetime.date.today()
apple = web.DataReader("AAPL", "morningstar", start, end)

dates = np.array(apple["Close"].index.levels[1])
close_v = np.array(apple["Close"].values)
volume = np.array(apple["Volume"].values)[1:]

# Get the variation of the price
diff = np.diff(close_v)
dates = dates[1:]
close_v = close_v[1:]

# Scale: Normalize
# Input the stock return and
X = np.column_stack([scale(diff), scale(volume)])

# Train Gaussian Model, Assume 4 hidden states
model = GaussianHMM(n_components=4, covariance_type="full", n_iter=20)
model.fit(X)

# Prediction the hidden layers
hidden_states = model.predict(X)

# Print the parameters
print("Transition matrix: ", model.transmat_)
print("Means and vars of each hidden state")
for i in range(4):
    print("{0}th hidden state".format(i))
    print("mean = ", model.means_[i])
    print("var = ", model.covars_[i])
print()

fig, axs = plt.subplots(4, sharex=True, sharey=True)
colours = cm.rainbow(np.linspace(0, 1, 4))

one_layer = []
two_layer = []
three_layer = []
fourth_layer = []

for i, (ax, colour) in enumerate(zip(axs, colours)):
    # Use fancy indexing to plot data in each state.
    mask = hidden_states == i
    ax.plot_date(dates[mask], close_v[mask], ".-", c=colour)
    ax.set_title("{0}th hidden state".format(i))

    # Format the ticks.
    ax.xaxis.set_major_locator(YearLocator())
    ax.xaxis.set_minor_locator(MonthLocator())

    ax.grid(True)

plt.show()




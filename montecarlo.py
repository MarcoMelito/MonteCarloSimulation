import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

S0 = 96      # Here goes the initial stock price
mu = 0.05     # Yearly expected return. We assume an expected 5% yearly return
v = 0.1       # Volatility
t = 3         # Time horizon (in years)
N = 365       # Number of time steps in one year
M = 3        # Number of simulated paths
dt = t / N   # Defining time steps

# np.random.seed(42) # We could also set a random seed to make the results predictable
S = np.zeros((M, t*N+1)) # Creating an array (M rows, N+1 columns) to store stock prices and time steps
S[:, 0] = S0 # Setting the initial stock price on day 0 of all paths to S0

for i in range(1, t*N+1): # Loops over each time step (from 1 to t*N)
    Z = np.random.standard_normal(M)  # Generating M random values using a standard normal distribution
    S[:, i] = S[:, i-1] * np.exp((mu - 0.5*v**2)*dt + v*np.sqrt(dt)*Z)
    # For the purpose of this project, I am using the Geometric Brownian Motion formula, which is often used to
    # predict stock prices
    # At each time step, the stock price grows on average according to an expected drift, but is also influenced by a
    # random shock. The exponential function ensures the price stays positive

df = pd.DataFrame(S) # Creating a data frame with the results obtained
df.insert(0, "Path", range(1, M+1)) # Numbering each row
df.to_csv("simulated_prices.csv", index=False) # Creating a .csv file with all the information

for i in range(M):
    plt.plot(df.columns[1:], df.iloc[i, 1:], label=f'Path {i+1}') # Plotting each simulated path with its corresponding label
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Simulated stock price paths")
plt.legend()
plt.show()



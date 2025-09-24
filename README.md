To execute:
1. Open `monte_carlo_simulation.py` in Python
2. Run the script. It will generate simulated stock price paths
3. Results are saved to `simulated_prices.csv` and plotted automatically
4. It is possible to modify preset values by editing the variables at the top of the file, which are:
     - Initial stock price
     - Yearly expected return rate
     - Volatility
     - Time horizon
     - Number of simulated paths
     - Time steps and number of steps in one year

For it to be fully functional, the file requires three libraries to be installed:
- NumPy to generate the random values for the simulation and the data arrays
- Pandas to generate the .csv output file
- Matplotlib to visualize the results plotted on a graph

Executing the file libraries.py with Python installed will automatically install any missing library.

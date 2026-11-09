import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit (all data), extended to 2050
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = np.arange(df["Year"].min(), 2051)
    ax.plot(years_all, res_all.intercept + res_all.slope * years_all, "r")

    # Create second line of best fit (2000 onwards), extended to 2050
    recent = df[df["Year"] >= 2000]
    res_recent = linregress(recent["Year"], recent["CSIRO Adjusted Sea Level"])
    years_recent = np.arange(2000, 2051)
    ax.plot(years_recent, res_recent.intercept + res_recent.slope * years_recent, "g")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
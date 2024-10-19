import pandas as pd
import numpy as np
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# List of Nifty50 stock symbols (sample)
nifty50_stocks = [
    'TCS.NS', 'RELIANCE.NS',  'INFY.NS', 'ICICIBANK.NS', 
    'HINDUNILVR.NS', 'KOTAKBANK.NS', 'LT.NS', 'ITC.NS', 'SBIN.NS',
    'BHARTIARTL.NS', 'AXISBANK.NS', 'ASIANPAINT.NS', 'BAJFINANCE.NS', 
    'HCLTECH.NS',  'TATAMOTORS.NS', 'MARUTI.NS', 'SUNPHARMA.NS', 
    'ULTRACEMCO.NS', 'ONGC.NS', 'NTPC.NS', 'TITAN.NS', 'GRASIM.NS', 
    'INDUSINDBK.NS', 'JSWSTEEL.NS', 'TATACONSUM.NS', 'POWERGRID.NS', 
    'WIPRO.NS', 'DRREDDY.NS', 'HEROMOTOCO.NS', 'BRITANNIA.NS', 
    'BAJAJFINSV.NS', 'TECHM.NS', 'CIPLA.NS', 'ADANIENT.NS', 'ADANIPORTS.NS',
    'DIVISLAB.NS', 'BPCL.NS', 'COALINDIA.NS', 'EICHERMOT.NS', 
    'SBILIFE.NS', 'SHREECEM.NS', 'UPL.NS','KALYANKJIL.NS'
]

# Fetch historical data for Nifty50 stocks
data = yf.download(nifty50_stocks, start='2023-01-01', end='2024-01-01')['Adj Close']

# Calculate daily returns
returns = data.pct_change()

# Compute the correlation matrix
correlation_matrix = returns.corr()

# Plot heatmap of the correlation matrix with annotations
plt.figure(figsize=(18, 14))  # Increase the figure size for better visibility
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', center=0, linewidths=0.5, 
            annot_kws={"size": 8}, cbar_kws={"shrink": .8})  # Adjust annotation and color bar size
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.yticks(rotation=0)   # Keep y-axis labels horizontal
plt.title("Correlation Heatmap of Nifty50 Stocks (with Correlation Values)", fontsize=18)
plt.show()

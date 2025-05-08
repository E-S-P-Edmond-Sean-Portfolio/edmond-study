import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def calculate_sma(prices, window):
    """Calculate Simple Moving Average"""
    if window > len(prices) or window <= 0:
        raise ValueError("Invalid window size")
    return np.mean(prices[-window:])

def generate_sample_data(days=30, volatility=0.02, trend=0.001):
    """Generate sample price data with some trend and noise"""
    np.random.seed(42)  # For reproducibility
    base_price = 100
    prices = [base_price]
    
    for _ in range(days-1):
        # Add trend and random noise
        new_price = prices[-1] * (1 + trend + np.random.normal(0, volatility))
        prices.append(new_price)
    
    return np.array(prices)

def plot_sma_chart(prices, window=5):
    """Create a professional chart showing prices and SMA"""
    # Calculate SMA
    sma_values = []
    for i in range(window, len(prices) + 1):
        sma = calculate_sma(prices[:i], window)
        sma_values.append(sma)
    
    # Generate dates for x-axis
    dates = [datetime.now() - timedelta(days=x) for x in range(len(prices))]
    dates.reverse()
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.style.use('bmh')  # Using a built-in style instead of seaborn
    
    # Plot price line
    plt.plot(dates, prices, label='Price', color='#1f77b4', linewidth=2)
    
    # Plot SMA line
    sma_dates = dates[window-1:]
    plt.plot(sma_dates, sma_values, label=f'SMA({window})', color='#ff7f0e', linewidth=2)
    
    # Customize the chart
    plt.title('Price vs Simple Moving Average', fontsize=14, pad=15)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the chart
    plt.savefig('sma_chart.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Generate sample data
    prices = generate_sample_data(days=30)
    
    # Create and save the chart
    plot_sma_chart(prices, window=5)
    print("Chart has been generated and saved as 'sma_chart.png'") 
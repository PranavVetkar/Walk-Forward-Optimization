import pandas as pd
import numpy as np

def simulate_logic(df, sma_window, rsi_limit):
    # Calculate indicators based on input parameters
    df = df.copy()
    df['sma'] = df['close'].rolling(window=sma_window).mean()
    
    # Simple RSI calculation
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    df['rsi'] = 100 - (100 / (1 + (gain/loss)))
    
    # Vectorized Backtest
    df['signal'] = 0
    df.loc[(df['close'] > df['sma']) & (df['rsi'] < rsi_limit), 'signal'] = 1
    
    df['returns'] = df['close'].pct_change()
    df['strat_returns'] = df['signal'].shift(1) * df['returns']
    return (1 + df['strat_returns']).cumprod().iloc[-1]

# --- THE OPTIMIZATION LOOP ---
data = pd.read_csv('btc_history.csv')
results = []

for sma in range(10, 50, 5):         # Test SMA from 10 to 50
    for rsi in range(60, 90, 5):    # Test RSI limits from 60 to 90
        final_roi = simulate_logic(data, sma, rsi)
        results.append({'sma': sma, 'rsi': rsi, 'roi': final_roi})

# Convert to DataFrame and find the best
results_df = pd.DataFrame(results)
best = results_df.loc[results_df['roi'].idxmax()]

print("--- Optimization Complete ---")
print(f"Best SMA Window: {best['sma']}")
print(f"Best RSI Limit: {best['rsi']}")
print(f"Max ROI: {best['roi']:.4f}x")
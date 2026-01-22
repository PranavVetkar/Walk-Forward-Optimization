# 🔁 Walk-Forward Optimization (Trading Strategy)

A Python-based **walk-forward optimization framework** used to tune trading strategy parameters and evaluate their performance on historical crypto market data.

This project focuses on **systematically finding optimal indicator parameters** (SMA window & RSI threshold) instead of relying on fixed or guessed values.

---

## 🚀 What This Project Does

- Tests multiple **SMA + RSI parameter combinations**
- Runs a **vectorized backtest** for each combination
- Measures strategy performance using **ROI (Return on Investment)**
- Identifies the **best-performing parameter set**
- Lays the foundation for walk-forward / out-of-sample validation

---

## 🧠 Strategy Logic

### Indicators Used
- **Simple Moving Average (SMA)** – trend detection
- **Relative Strength Index (RSI)** – momentum filter

### Entry Condition
BUY when:
- Price > SMA
- RSI < configured threshold


### Returns Calculation
- Uses **shifted signals** to avoid look-ahead bias
- Computes cumulative strategy returns

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Pandas**
- **NumPy**
> pip install pandas numpy
---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PranavVetkar/Walk-Forward-Optimization.git
cd Walk-Forward-Optimization

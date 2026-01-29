# 📊 Monte Carlo Portfolio Simulation with NumPy

This project implements a **Monte Carlo simulation of random portfolios** using **NumPy** and **Matplotlib**.  
It simulates stock returns, computes portfolio statistics, and generates multiple random portfolios to analyze the **risk–return tradeoff** using volatility and expected return.

The goal is to explore portfolio diversification and visualize how different weight allocations affect performance.

---

## 🔍 Project Overview

The script:
- Simulates daily returns for multiple stocks
- Computes annualized returns and covariance
- Generates many random portfolios
- Calculates each portfolio’s:
  - Expected return
  - Volatility
  - Sharpe ratio (return / volatility)
- Visualizes the results using a scatter plot

This is a classic **quantitative finance / portfolio theory** exercise.

---

## 🧠 Concepts Covered

- Vectorized numerical computation with NumPy
- Random portfolio generation (Monte Carlo method)
- Portfolio theory fundamentals:
  - Expected return
  - Volatility (risk)
  - Covariance matrix
  - Diversification
  - Sharpe ratio
- Data visualization with Matplotlib

---

## ⚙️ Parameters

```python
n_stocks = 5
n_days = 252
start_price = 100
weights = np.array([0.4, 0.2, 0.1, 0.2, 0.1])
n_portfolio = 100
5 simulated assets
```''' """


--- 
252 trading days (~1 year)

Daily returns simulated uniformly between -2% and +2%

100 random portfolios generated

Portfolio weights are randomly sampled and normalized

📊 Calculations Performed
📈 Asset-Level
Daily returns

Annualized mean returns

Annualized covariance matrix

Correlation matrix
---
## 📦 Portfolio-Level
For each random portfolio:

Expected annual return

Portfolio variance

Portfolio volatility

Sharpe ratio
---
## 📉 Visualization
The script generates a Monte Carlo scatter plot where:

X-axis: Volatility (risk)

Y-axis: Expected return

Color scale: Sharpe ratio

This plot helps visualize:

Efficient vs inefficient portfolios

Risk–return tradeoff

Impact of diversification
---
## 🖥️ Console Output
The program prints:

First 10 simulated portfolio returns

First 10 simulated portfolio volatilities

Useful for quick numerical inspection and debugging.
---
## 📦 Requirements
Python 3.x

NumPy

Matplotlib

Install dependencies if needed:

pip install numpy matplotlib
## ▶️ How to Run
Run the script directly:
python monte_carlo_portfolio.py
All statistics and plots will be generated automatically.

## 🚀 Possible Extensions
Increase number of portfolios (e.g. 10,000+)

Identify the maximum Sharpe ratio portfolio

Plot the efficient frontier explicitly

Add risk-free rate to Sharpe ratio

Use real stock market data

Optimize portfolio weights

## 👤 Author

This project was built as a learning exercise to practice:

Monte Carlo simulations

Portfolio risk analysis

Quantitative finance fundamentals

Data visualization

Small script, strong concepts.


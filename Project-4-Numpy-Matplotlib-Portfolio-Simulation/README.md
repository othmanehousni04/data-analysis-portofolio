# 📈 Portfolio Simulation & Risk Analysis with NumPy

This project is a **simple portfolio simulation** built with **NumPy** and **Matplotlib**.  
It simulates multiple stock price paths, constructs a weighted portfolio, and analyzes its **returns, volatility, correlations, and risk contributions**.

Even though the project is intentionally small, it demonstrates solid fundamentals in:
- numerical computing
- vectorized operations
- basic quantitative finance concepts

---

## 🔍 What This Project Does

- Simulates daily returns for multiple stocks
- Generates price paths using cumulative returns
- Builds a weighted portfolio
- Computes:
  - Daily & annualized returns
  - Volatility
  - Covariance & correlation matrices
  - Portfolio variance
  - Risk contribution per asset
- Identifies best & worst performing stocks
- Visualizes:
  - Risk contribution bar chart
  - Correlation heatmap
  - Individual stock paths + portfolio evolution

---

## 🧠 Key Concepts Used

- Vectorization with NumPy
- Random simulations with reproducibility (`np.random.seed`)
- Portfolio theory basics:
  - Expected return
  - Volatility
  - Covariance & correlation
  - Risk decomposition
- Data visualization with Matplotlib

---

## ⚙️ Parameters

n_stocks = 5
n_days = 252
start_price = 100
weights = np.array([0.4, 0.2, 0.1, 0.2, 0.1])
252 trading days ≈ 1 year
Weights sum to 1 (fully invested portfolio)
Daily returns are simulated uniformly between -2% and +2% ```
--- ''' 

📊 Outputs
Console

Annualized portfolio return

Annualized volatility

Risk contribution of each stock

Best & worst performing stocks

Plots

📉 Portfolio risk contribution

🔥 Correlation matrix heatmap

📈 Stock price paths & portfolio value
📦 Requirements

Python 3.x

NumPy

Matplotlib

Install dependencies if needed:

pip install numpy matplotlib

▶️ How to Run

Simply run the script:

python portfolio_simulation.py


All results and plots will be generated automatically.

🚀 Possible Extensions

Use real market data instead of simulated returns

Add Sharpe ratio & drawdown analysis

Optimize portfolio weights

Monte Carlo simulations

Export results to CSV

👤 Author

Built as a learning project to strengthen NumPy, financial modeling, and data visualization skills.


OUTPUT:

----- PORTFOLIO STATS -----

Annual Return: -5.59%

Annual Volatility: 9.45%


----- RISK CONTRIBUTION -----

Stock 1: 62.48%

Stock 2: 13.73%

Stock 3: 2.99%

Stock 4: 18.44%

Stock 5: 2.36%

Total: 100.00%


----- STOCK PERFORMANCE -----

Best stock: 2 → 109.18

Worst stock: 4 → 83.05

<img width="607" height="475" alt="image" src="https://github.com/user-attachments/assets/b3e2b3a5-56f4-4a9a-bde4-77f53da1b4e6" />
<img width="602" height="473" alt="image" src="https://github.com/user-attachments/assets/0f9505ed-e0f1-45f3-ad4a-8374680080ea" />
<img width="1002" height="646" alt="image" src="https://github.com/user-attachments/assets/c0fd1683-7beb-4943-a48d-9e7044f2ee8b" />



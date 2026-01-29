import numpy as np
import matplotlib.pyplot as plt

# ===============================
# 1️⃣ Parameters
# ===============================
n_stocks = 5
n_days = 252
start_price = 100
weights = np.array([0.4, 0.2, 0.1, 0.2, 0.1])  # Must sum to 1

# ===============================
# 2️⃣ Reproducibility
# ===============================
np.random.seed(445)

# ===============================
# 3️⃣ Generate daily returns
# ===============================
returns = np.random.uniform(-0.02, 0.02, size=(n_stocks, n_days))

# ===============================
# 4️⃣ Price simulation
# ===============================
prices = start_price * (1 + returns).cumprod(axis=1)

# ===============================
# 5️⃣ Portfolio value & returns
# ===============================
portfolio_value = weights @ prices
portfolio_returns = portfolio_value[1:] / portfolio_value[:-1] - 1

# ===============================
# 6️⃣ Statistics (DAILY)
# ===============================
mean_daily_return = portfolio_returns.mean()
vol_daily = portfolio_returns.std()

# ===============================
# 7️⃣ Annualized statistics
# ===============================
mean_annual_return = mean_daily_return * 252
vol_annual = vol_daily * np.sqrt(252)

# ===============================
# 8️⃣ Covariance & Correlation
# ===============================
cov_daily = np.cov(returns)
cov_annual = cov_daily * 252
corr_matrix = np.corrcoef(returns)

# ===============================
# 9️⃣ Portfolio variance (ANNUAL)
# ===============================
portfolio_variance = weights.T @ cov_annual @ weights
portfolio_volatility = np.sqrt(portfolio_variance)

n_portfolio = 100
n_assets = n_stocks
n_returnpf = np.zeros(n_portfolio)
n_volpf = np.zeros(n_portfolio)

mean_daily_pf = returns.mean(axis=1)
mean_annual_pf = mean_daily_pf * 252

for i in range(n_portfolio):
    raw = np.random.uniform(0, 1, n_assets)
    weights_pf = raw / raw.sum()

    pf_return = weights_pf @ mean_annual_pf

    pf_variance = weights_pf.T @ cov_annual @ weights_pf
    pf_vol = np.sqrt(pf_variance)
    n_returnpf[i] = pf_return
    n_volpf[i] = pf_vol
print(f"Portfolio returns (first 10): {n_returnpf[:10]}")
print(f"Portfolio volatility (first 10): {n_volpf[:10]}")

# Plot
plt.figure(figsize=(8,6))
plt.scatter(n_volpf, n_returnpf, c=n_returnpf/n_volpf, cmap='viridis', alpha=0.6)
plt.xlabel("Volatility")
plt.ylabel("Risk")
plt.grid(True)
plt.colorbar(label = "Sharp ratio")
plt.title("Sharp simulation, 1000 portfolio")
plt.show()
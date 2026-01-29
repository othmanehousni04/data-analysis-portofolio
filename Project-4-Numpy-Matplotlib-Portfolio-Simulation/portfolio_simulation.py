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

# ===============================
# 🔟 Risk Contribution
# ===============================
marginal_contribution = cov_annual @ weights
risk_contribution = weights * marginal_contribution
risk_contribution_pct = risk_contribution / portfolio_variance

# ===============================
# 1️⃣1️⃣ Stock diagnostics
# ===============================
final_prices = prices[:, -1]
best = np.argmax(final_prices)
worst = np.argmin(final_prices)

# ===============================
# 1️⃣2️⃣ Printing results
# ===============================
print("----- PORTFOLIO STATS -----")
print(f"Annual Return: {mean_annual_return:.2%}")
print(f"Annual Volatility: {portfolio_volatility:.2%}")
print()

print("----- RISK CONTRIBUTION -----")
for i, rc in enumerate(risk_contribution_pct):
    print(f"Stock {i+1}: {rc:.2%}")
print(f"Total: {risk_contribution_pct.sum():.2%}")
print()

print("----- STOCK PERFORMANCE -----")
print(f"Best stock: {best+1} → {final_prices[best]:.2f}")
print(f"Worst stock: {worst+1} → {final_prices[worst]:.2f}") 

# ===============================
# 1️⃣3️⃣ Risk contribution plot
# ===============================
plt.figure(figsize=(6, 4))
plt.bar(range(1, n_stocks + 1), risk_contribution_pct * 100)
plt.xlabel("Stock")
plt.ylabel("Risk Contribution (%)")
plt.title("Portfolio Risk Contribution")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# ===============================
# 1️⃣4️⃣ Correlation heatmap
# ===============================
plt.figure(figsize=(6,4))
im = plt.imshow(corr_matrix, cmap = "coolwarm", vmin = -1, vmax = 1)
plt.colorbar(im, fraction = 0.046)
plt.xticks(range(n_stocks), [f"Stock {i+1}" for i in range (n_stocks)])
plt.yticks(range(n_stocks), [f"Stock {i+1}" for i in range (n_stocks)])
plt.tight_layout()
plt.title("Correlation matrix")
plt.show()


# ===============================
# 1️⃣5️⃣ Price paths
# ===============================
plt.figure(figsize=(10, 6))
plt.axhline(start_price, linestyle="--", alpha=0.3, label="Start Price")

for i in range(n_stocks):
    full_path = np.concatenate(([start_price], prices[i]))
    plt.plot(full_path, alpha=0.6, label=f"Stock {i+1}")

portfolio_path = np.concatenate(([start_price], portfolio_value))
plt.plot(portfolio_path, color="black", linewidth=2, label="Portfolio")

plt.legend(ncol=2)
plt.xlabel("Days")
plt.ylabel("Price ($)")
plt.title("Stock & Portfolio Simulation")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


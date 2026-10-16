import numpy as np
import matplotlib.pyplot as plt

# Define the domain [-5, 5]
x = np.linspace(-5, 5, 500)
y = 2 * x + np.sin(x)**2 + 3

# Plot setup
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$y = 2x + \sin^2(x) + 3$', color='#1f77b4', linewidth=2)
plt.grid(True, linestyle='--', alpha=0.7)
plt.title("hello, po!", fontsize=14, fontweight='bold')
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.legend(loc='upper left')
plt.tight_layout()

# Save to PDF
plt.savefig("po.pdf")
plt.show()
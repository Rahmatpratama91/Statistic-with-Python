
# --- Soal 1: Uji Hipotesis Dua Sisi (Berat Produk) ---
import scipy.stats as stats
import numpy as np

xbar = 200
mu0 = 195
sigma = 15
n = 50
alpha = 0.01

z = (xbar - mu0) / (sigma / np.sqrt(n))
z_crit = stats.norm.ppf(1 - alpha / 2)

print(f"Z hitung = {z:.3f}")
print(f"Z kritis = ±{z_crit:.3f}")
if abs(z) > z_crit:
    print("Tolak H0")
else:
    print("Gagal Tolak H0")

# --- Soal 2: Estimasi Interval Kepercayaan ---
xbar = 170
s = 8
n = 50
alpha = 0.10
t_crit = stats.t.ppf(1 - alpha/2, df=n-1)
ME = t_crit * (s / np.sqrt(n))
lower = xbar - ME
upper = xbar + ME
print(f"CI 90%: ({lower:.2f}, {upper:.2f})")

# --- Soal 3: Uji Hipotesis Satu Sisi (Gaji) ---
xbar = 7200000
mu0 = 7000000
s = 800000
n = 100
alpha = 0.05
z = (xbar - mu0) / (s / np.sqrt(n))
z_crit = stats.norm.ppf(1 - alpha)
print(f"Z hitung = {z:.3f}")
print(f"Z kritis = {z_crit:.3f}")
if z > z_crit:
    print("Tolak H0")
else:
    print("Gagal Tolak H0")

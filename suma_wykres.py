import numpy as np
import matplotlib.pyplot as plt


def g(u):
    return (np.sin(5*u)**2
            + np.cos(10*u)**4
            + (0.5*np.sin(20*u) + 0.25*np.cos(5*u))**2)


n = 1000


U = np.random.uniform(0, 1, n)


h_values = np.cumsum(g(U)) / np.arange(1, n+1)

x_dense = np.linspace(0, 1, 20000)
mean_exact = np.trapezoid(g(x_dense), x_dense)


plt.figure(figsize=(8,5))
plt.plot(h_values, label='h(x) – średnia skumulowana')
plt.axhline(mean_exact, color='red', linestyle='--',label=f'Średnia wartość funkcji = {mean_exact:.4f}')
plt.xlabel('Liczba próbek n')
plt.ylabel('Wartość h(x)')
plt.title('Wykres funkcji h(x) z kolejnych zmiennych losowych U_i')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

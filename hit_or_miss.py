import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (np.sin(5*x)**2 
            + np.cos(10*x)**4 
            + (0.5*np.sin(20*x) + 0.25*np.cos(5*x))**2)


a, b = 0, 1


x_plot = np.linspace(a, b, 1000)
y_plot = f(x_plot)


y_max = max(y_plot)


N = 5000


x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, y_max, N)


under_curve = y_rand <= f(x_rand)


area_estimate = (np.sum(under_curve) / N) * (b - a) * y_max


plt.figure(figsize=(8,5))


plt.plot(x_plot, y_plot, color='orange', label='f(x)')
plt.fill_between(x_plot, 0, y_plot, color='orange', alpha=0.2)


plt.scatter(x_rand[under_curve], y_rand[under_curve],
            color='green', s=5, label='Punkty pod wykresem')


plt.scatter(x_rand[~under_curve], y_rand[~under_curve],
            color='red', s=5, label='Punkty nad wykresem')


plt.title('Geometryczne Monte Carlo – przybliżanie całki na [0,1]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()



import matplotlib.pyplot as plt
import numpy as np

T_max = 10
I_0 = 1


def get_reduction(t):
    I_2 = (I_0 / 2) * T_max
    I_r = (I_0 / t) * T_max
    return -(I_r - I_2) / I_2 * 100


T_cont = np.linspace(1, T_max)
T_disc = np.arange(1, T_max, 1)

plt.xlim(0, T_max)
plt.ylim(0, 100)
plt.xlabel("Replacement period (years)")
plt.ylabel("Reduction over status quo (%)")
plt.title("Effect of prolonging life of smartphones over manufacturing impacts")
plt.grid()
plt.plot(T_cont, get_reduction(T_cont))
plt.scatter(T_disc, get_reduction(T_disc))
plt.show()

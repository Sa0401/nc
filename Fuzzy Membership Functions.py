import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
x = np.arange(0, 11, 1.0)
x1 = np.arange(0, 10, 0.1)
y1 = fuzz.trimf(x, [1, 3, 5])
y2 = fuzz.trapmf(x, [1, 3, 5, 7])
y3 = fuzz.gbellmf(x1, 2, 4, 5)
fig, axs = plt.subplots(3, 1, figsize=(6, 8))
axs[0].plot(x, y1)
axs[0].set_title("Triangular Membership Function")
axs[1].plot(x, y2)
axs[1].set_title("Trapezoidal Membership Function")
axs[2].plot(x1, y3)
axs[2].set_title("Bell-shaped Membership Function")
plt.tight_layout()
plt.show()




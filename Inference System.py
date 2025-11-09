import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


temperature = ctrl.Antecedent(np.arange(0, 111, 1), 'temperature')
cloud = ctrl.Antecedent(np.arange(0, 101, 1), 'cloud_cover')


speed = ctrl.Consequent(np.arange(0, 101, 1), 'speed')


temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['warm'] = fuzz.trimf(temperature.universe, [30, 60, 90])
temperature['hot'] = fuzz.trimf(temperature.universe, [70, 100, 110])

cloud['clear'] = fuzz.trimf(cloud.universe, [0, 0, 50])
cloud['cloudy'] = fuzz.trimf(cloud.universe, [30, 60, 90])
cloud['overcast'] = fuzz.trimf(cloud.universe, [70, 100, 100])

speed['slow'] = fuzz.trimf(speed.universe, [0, 0, 50])
speed['fast'] = fuzz.trimf(speed.universe, [50, 100, 100])


rule1 = ctrl.Rule(temperature['warm'] & cloud['clear'], speed['fast'])
rule2 = ctrl.Rule(temperature['cold'] | cloud['overcast'], speed['slow'])


wind_ctrl = ctrl.ControlSystem([rule1, rule2])
sim = ctrl.ControlSystemSimulation(wind_ctrl)


sim.input['temperature'] = 65   # warm
sim.input['cloud_cover'] = 30   # clear


sim.compute()
print("Predicted Speed:", round(sim.output['speed'], 2))


temperature.view()
cloud.view()
speed.view(sim=sim)
plt.show()

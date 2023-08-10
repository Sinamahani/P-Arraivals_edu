"""
Sina Sabermahani, University of Manitoba, 2023

This script is for making synthetic seismogram for a single layer model.

You can twick the parameters to make different synthetic seismograms.
"""

import numpy as np
from scipy.signal import ricker
import matplotlib.pyplot as plt


#setting parameters
vp = 1200
# vs = 1000 #not used in this script
layer_1_thickness = 150 #meter
duration = 2 #second
sampling_rate = 1000 #Hz
distances = [20, 500]


#making time series
time = np.linspace(0, duration, duration*sampling_rate)
distances = np.linspace(distances[0], distances[1], 100) #meter

#setting plot size
plt.figure(figsize=(10,10))

for counter, dist in enumerate(distances):
    signal = np.zeros(time.shape)
    arrival_time_dir = dist / vp
    arrival_time_p = 2*(np.sqrt(((dist/2)**2)+(layer_1_thickness**2))) / vp
    arrival_time_p_mul = 4*(np.sqrt(((dist/4)**2)+(layer_1_thickness**2))) / vp

    spike_time_index_dir = np.where(np.abs(time - arrival_time_dir) < 0.001)[0][0]
    spike_time_index_p = np.where(np.abs(time - arrival_time_p) < 0.001)[0][0]
    spike_time_index_p_mul = np.where(np.abs(time - arrival_time_p_mul) < 0.001)[0][0]


    #wavelet adding
    point = 25
    amp = 4
    rick = ricker(point, amp)

    signal[spike_time_index_dir-10:spike_time_index_dir+15] = rick
    signal[spike_time_index_p-10:spike_time_index_p+15] = -0.5*rick
    signal[spike_time_index_p_mul-10:spike_time_index_p_mul+15] = rick/3


    plt.plot(time, 10*signal+dist, 'k')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    # plt.xlim(0, 0.6)
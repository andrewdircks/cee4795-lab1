import numpy as np
import matplotlib.pyplot as plt

fname = 'data-raw-high-baud.txt'

def parse_line(line):
    return float(line[6:12]), float(line[16:-1])

voltages = []
ts = []

with open(fname, 'r') as f:
    for line in f:
        t, v = parse_line(line)
        voltages.append(v)
        ts.append(t)

# samples = list(range(len(voltages)))
# plt.scatter(samples, voltages)
# plt.xlabel('Sample #')
# plt.ylabel('Voltage (V)')
# plt.show()

n = len(voltages) # number of samples
dt = ts[-1] - ts[0]
print(n)
print(dt)

print(dt / n)
print(1 / (dt/n))

t0 = [ts[0] + i*(dt / n) for i in range(n)]

plt.plot(ts, voltages)
plt.show()

plt.plot(t0, voltages)
plt.show()

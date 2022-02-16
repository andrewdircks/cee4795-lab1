import matplotlib.pyplot as plt

fname = 'data-raw-bennett.txt'

def parse_line(line):
    return float(line[6:12]), float(line[16:-1])

voltages = []
ts = []

with open(fname, 'r') as f:
    for line in f:
        t, v = parse_line(line)
        voltages.append(v)
        ts.append(t)

samples = list(range(len(voltages)))
# plt.scatter(samples, voltages)
plt.plot(samples, voltages)
plt.xlabel('Sample #')
plt.ylabel('Voltage (V)')
plt.show()

# calculate sampling frequency
n = len(voltages)
dt = ts[-1] - ts[0]
print(f'number of samples: {n}')
print(f'time difference (s): {dt}')
print(f'average sampling period (s): {dt / n}')
print(f'average sampling frequency (Hz): {1 / (dt/n)}')

# calculate uniform sampling vector with average sampling period
t0 = [ts[0] + i*(dt / n) for i in range(n)]

# "raw" time vector plot
plt.plot(ts, voltages)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()

# interpolated time vector plot
plt.plot(t0, voltages)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()

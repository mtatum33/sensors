import json
from datetime import datetime
from matplotlib import pyplot as plt

f = open('sensorData-fixed.json', 'r')

data = json.loads( f.read() )

T1 = []
X1 = []

T2 = []
X2 = []

T3 = []
X3 = []

for frame in data:
    dt = datetime.strptime(frame['timestamp'], "%Y-%m-%d %H:%M:%S")
    temp = float( frame['environment']['temperature_h'] )

    if frame['pi_id'] == 'raspberr6':
        T1.append(dt)
        X1.append(temp)

    if frame['pi_id'] == 'raspberr30':
        T2.append(dt)
        X2.append(temp)

    if frame['pi_id'] == 'raspberr66':
        T3.append(dt)
        X3.append(temp)

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

plt.axes( ax1 )
plt.title('raspberry6')
plt.plot(T1, X1)

plt.axes( ax2 )
plt.title('raspberry30')
plt.plot(T2, X2)

plt.axes( ax3 )
plt.title('raspberry66')
plt.plot(T3, X3)

plt.show()

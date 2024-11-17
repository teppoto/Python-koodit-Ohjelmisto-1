from matplotlib import pyplot as plt, patches
import numpy as np

# Set up the figure
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)

# Add unit circle outline
unit_circle = patches.Circle((0, 0), radius=1, fill=False, color="gray", linestyle='--')
ax.add_patch(unit_circle)

# Adjust axes to go through origin
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks only on the left and bottom axes
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.axis('equal')

# Define angles in radians
angles_rad = np.array([np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 5*np.pi/6, np.pi, 3*np.pi/2])
x_points = np.cos(angles_rad)
y_points = np.sin(angles_rad)
colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow']
angle_labels = [r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$',
                r'$\frac{2\pi}{3}$', r'$\frac{5\pi}{6}$', r'$\pi$', r'$\frac{3\pi}{2}$']

# Plot points and add annotations
for x, y, label, color in zip(x_points, y_points, angle_labels, colors):
    ax.scatter(x, y, color=color, marker='X', s=100)
    ax.annotate(label, xy=(x, y), xycoords='data', xytext=(10, 10),
                textcoords='offset points', fontsize=12,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

# Set custom ticks for x and y axes
ax.set_xticks([-1, 0, 1])
ax.set_yticks([-1, 0, 1])

plt.show()
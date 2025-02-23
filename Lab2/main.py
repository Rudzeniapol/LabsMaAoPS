import numpy as np
import matplotlib.pyplot as plt
import time
import random
import copy


def random_rgb_color():
    return (random.random(), random.random(), random.random())

dots = []
imagesCount = 2000
for i in range(imagesCount):
    dots.append((random.randrange(-100000, 100000), random.randrange(-100000, 100000)))
clusters = []
iteration = 0
distances = []
clusters.append(dots[random.randrange(0, 2000)])
xDots_coords = [dot[0] for dot in dots]
yDots_coords = [dot[1] for dot in dots]
xCentroids_coords = [cluster[0] for cluster in clusters]
yCentroids_coords = [cluster[1] for cluster in clusters]
plt.scatter(xDots_coords, yDots_coords, c='blue', alpha=0.6, label='Точки')

plt.scatter(xCentroids_coords, yCentroids_coords, c='red', marker='X', s=200, label='Центроиды')
plt.text(0.5, 1.1, f'Итерация: {iteration}', transform=plt.gca().transAxes,
                 fontsize=12, ha='center', va='center')
plt.title('Точки и центроиды')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.legend()
plt.grid(True)

plt.show()
time.sleep(2)
cx, cy = clusters[0]
for i in range(imagesCount):
    x, y = dots[i]
    distances.append((((cx - x)**2 + (cy - y)**2)**0.5))
clusters.append(dots[distances.index(max(distances))])
flag = True
while flag:
    flag = False
    clusterDots = []
    maxDotsRanges = []
    maxRangesDots = []
    for i in range(len(clusters)):
        clusterDots.append([])
    for dot in dots:
        (x, y) = dot
        clusterRanges = []
        for cluster in clusters:
            (x1, y1) = cluster
            clusterRanges.append(((x1 - x)**2 + (y1 - y)**2)**0.5)
        clusterDots[clusterRanges.index(min(clusterRanges))].append(dot)
    plt.cla()
    for i in range(len(clusters)):
        clusterDotsX = [cluster[0] for cluster in clusterDots[i]]
        clusterDotsY = [cluster[1] for cluster in clusterDots[i]]
        color = random_rgb_color()
        plt.scatter(clusterDotsX, clusterDotsY, c=color, alpha=0.6, label='Точки')
    plt.text(0.5, 1.1, f'Итерация: {iteration}', transform=plt.gca().transAxes,
                 fontsize=12, ha='center', va='center')
    xCentroids_coords = [cluster[0] for cluster in clusters]
    yCentroids_coords = [cluster[1] for cluster in clusters]
    plt.scatter(xCentroids_coords, yCentroids_coords, c='red', marker='X', s=200, label='Центроиды')
    plt.show()
    time.sleep(2)
    for i in range(len(clusters)):
        cx, cy = clusters[i]
        dotsRanges = []
        for dot in clusterDots[i]:
            (dotX, dotY) = dot
            dotsRanges.append(((cx - dotX)**2 + (cy - dotY)**2)**0.5)
        maxDotsRanges.append(max(dotsRanges))
        maxRangesDots.append(clusterDots[i][dotsRanges.index(max(dotsRanges))])
    maxRangeDot = maxRangesDots[maxDotsRanges.index(max(maxDotsRanges))]
    RangesSum = 0
    counter = 0
    for i in range(len(clusters)):
        x1, y1 = clusters[i]
        for j in range(i):
            x2, y2 = clusters[j]
            RangesSum += (((x2 - x1)**2 + (y2 - y1)**2)**0.5)
            counter += 1
    averageRange = RangesSum / counter
    if averageRange/2 < max(maxDotsRanges):
        flag = True
    iteration += 1
    plt.cla()
    for i in range(len(clusters)):
        clusterDotsX = [cluster[0] for cluster in clusterDots[i]]
        clusterDotsY = [cluster[1] for cluster in clusterDots[i]]
        color = random_rgb_color()
        plt.scatter(clusterDotsX, clusterDotsY, c=color, alpha=0.6, label='Точки')
    plt.text(0.5, 1.1, f'Итерация: {iteration}', transform=plt.gca().transAxes,
                 fontsize=12, ha='center', va='center')
    if(flag):
        clusters.append(maxRangeDot)
    xCentroids_coords = [cluster[0] for cluster in clusters]
    yCentroids_coords = [cluster[1] for cluster in clusters]
    plt.scatter(xCentroids_coords, yCentroids_coords, c='red', marker='X', s=200, label='Центроиды')
    plt.show()
    time.sleep(2)
for dot in dots:
    (x, y) = dot
    clusterRanges = []
    for cluster in clusters:
        (x1, y1) = cluster
        clusterRanges.append(((x1 - x)**2 + (y1 - y)**2)**0.5)
    clusterDots[clusterRanges.index(min(clusterRanges))].append(dot)
plt.cla()
for i in range(len(clusters)):
    clusterDotsX = [cluster[0] for cluster in clusterDots[i]]
    clusterDotsY = [cluster[1] for cluster in clusterDots[i]]
    color = random_rgb_color()
    plt.scatter(clusterDotsX, clusterDotsY, c=color, alpha=0.6, label='Точки')
plt.text(0.5, 1.1, f'Итерация: {iteration}', transform=plt.gca().transAxes,
                 fontsize=12, ha='center', va='center')
xCentroids_coords = [cluster[0] for cluster in clusters]
yCentroids_coords = [cluster[1] for cluster in clusters]
plt.scatter(xCentroids_coords, yCentroids_coords, c='red', marker='X', s=200, label='Центроиды')
plt.show()
print("All done")
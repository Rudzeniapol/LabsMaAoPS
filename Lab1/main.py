import numpy as np
import matplotlib.pyplot as plt
import time
import random
import copy

def are_points_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    index = 0
    while index < len(arr1):
        if arr1[index] != arr2[index]:
            return False
        index += 1
    return True

colors = ['blue', 'red', 'green', 'yellow', 'black', 'pink']
dots = []
for i in range(2000):
    dots.append((random.randrange(-100000, 100000), random.randrange(-100000, 100000)))
clusters = []
iteration = 0
previousClusters = copy.deepcopy(clusters)
for i in range(6):
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
while not are_points_equal(clusters, previousClusters):
    previousClusters = copy.deepcopy(clusters)
    clusterDots = []
    for i in range(6):
        clusterDots.append([])
    for dot in dots:
        (x, y) = dot
        clusterRanges = []
        for cluster in clusters:
            (x1, y1) = cluster
            clusterRanges.append(((x1 - x)**2 + (y1 - y)**2)**0.5)
        clusterDots[clusterRanges.index(min(clusterRanges))].append(dot)
    plt.cla()
    for i in range(6):
        clusterDotsX = [cluster[0] for cluster in clusterDots[i]]
        clusterDotsY = [cluster[1] for cluster in clusterDots[i]]
        plt.scatter(clusterDotsX, clusterDotsY, c=colors[i], alpha=0.6, label='Точки')
    plt.text(0.5, 1.1, f'Итерация: {iteration}', transform=plt.gca().transAxes,
                 fontsize=12, ha='center', va='center')
    xCentroids_coords = [cluster[0] for cluster in clusters]
    yCentroids_coords = [cluster[1] for cluster in clusters]
    plt.scatter(xCentroids_coords, yCentroids_coords, c='red', marker='X', s=200, label='Центроиды')
    plt.show()
    time.sleep(2)
    for i in range(6):
        sum_x = sum(point[0] for point in clusterDots[i])
        sum_y = sum(point[1] for point in clusterDots[i])
        average_x = sum_x / len(clusterDots[i])
        average_y = sum_y / len(clusterDots[i])
        dotsRanges = []
        for dot in clusterDots[i]:
            (dotX, dotY) = dot
            dotsRanges.append(((average_x - dotX)**2 + (average_y - dotY)**2)**0.5)
        clusters[i] = clusterDots[i][dotsRanges.index(min(dotsRanges))]
    iteration += 1
    plt.cla()
    for i in range(6):
        clusterDotsX = [cluster[0] for cluster in clusterDots[i]]
        clusterDotsY = [cluster[1] for cluster in clusterDots[i]]
        plt.scatter(clusterDotsX, clusterDotsY, c=colors[i], alpha=0.6, label='Точки')
    plt.text(0.5, 1.1, f'Итерация: {iteration}', transform=plt.gca().transAxes,
                 fontsize=12, ha='center', va='center')
    xCentroids_coords = [cluster[0] for cluster in clusters]
    yCentroids_coords = [cluster[1] for cluster in clusters]
    plt.scatter(xCentroids_coords, yCentroids_coords, c='red', marker='X', s=200, label='Центроиды')
    plt.show()
    time.sleep(2)
print("All done")
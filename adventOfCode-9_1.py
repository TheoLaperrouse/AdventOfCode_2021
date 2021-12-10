from collections import Counter

file = open('input.txt', "r")
lines = file.readlines()
file.close()
res = 0
lines_heights = [list(line.strip()) for line in lines]
points_around = []


def validLowPoint(point, points_around):
    return all(point_around > point for point_around in points_around)


for index, heights in enumerate(lines_heights):
    for indexHeight, height in enumerate(heights):
        points_around.append(
            int(lines[index-1][indexHeight]) if index - 1 >= 0 else 10)
        points_around.append(int(lines[index+1]
                                 [indexHeight]) if index + 1 < len(lines_heights) else 10)
        points_around.append(
            int(heights[indexHeight - 1]) if indexHeight - 1 >= 0 else 10)
        points_around.append(
            int(heights[indexHeight + 1]) if indexHeight + 1 < len(heights) else 10)
        points_around = [point for point in points_around if point != None]
        print(height, points_around)
        if validLowPoint(int(height), points_around):
            res += int(height) + 1
        points_around = []
print(res)

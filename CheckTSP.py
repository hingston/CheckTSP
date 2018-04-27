# Brute force the best distance for a given map

# -------------------------------------------------------
# "BEER-WARE LICENSED":
# As long as you retain this notice, you can do what you
# want with this. If we meet some day, and you think this
# program is worth it, you may buy me a beer in return.
#
# Author: Clint Gamlin
# Email: cdgamlin@gmail.com
# -------------------------------------------------------

# -------------------------------------------------------
# Updated to Python 3 and now complies with all PEPs
# Author: William Hingston
# -------------------------------------------------------

from sys import argv


class MapRoute:
    # read and store distance map, checking for correct file structure
    def __init__(self, filename):
        # read in file in one hit
        file = open(filename)
        data = file.read()
        file.close()

        # split data into list of lists
        data = data.split("\n")
        data = [x.split() for x in data]
        data = [[int(y) for y in x] for x in data]

        # remove trailing blank lines
        while not data[-1]:
            data = data[:-1]

        # get number of towns, making sure the first line is structured correctly
        if len(data[0]) != 1:
            print("Error! Map file line 1 must have exactly 1 integer")
            exit()
        self.num_towns = data[0][0]

        # check that the size of the file is correct
        if len(data) != self.num_towns:
            print("Error!: Map file must have the same number of input lines as the number of towns")
            exit()

        error = False

        # check structure of distances between towns
        for i in range(1, self.num_towns):
            if len(data[i]) != i:
                print("Error! Map file line " + str(i + 1) + " must have exactly " + str(i) + " integer" + (
                    "s" if i != 1 else ""))
                error = True
            for j in range(i):
                if data[i][j] < 1:
                    print("Error! Map file line " + str(i + 1) + " integer " + str(
                        j + 1) + " is not an integer greater than zero")
                    error = True

        if error:
            exit()

        # store distance map
        self.distance = data[1:]

    # return distance between two towns
    def get_dist(self, i, j):
        return self.distance[max(i, j) - 1][min(i, j)]

    # find best path from current town through all left_to_visit towns using recursion
    def best_path(self, current_town, left_to_visit):
        # base case
        if len(left_to_visit) == 1:
            return self.get_dist(current_town, left_to_visit[0])

        # general case
        best_dist = float('inf')  # infinite!
        for i in range(len(left_to_visit)):
            going_to = left_to_visit[i]
            then_left_to_visit = left_to_visit[:i] + left_to_visit[i + 1:]
            dist = self.get_dist(current_town, going_to) + self.best_path(going_to, then_left_to_visit)
            if dist < best_dist:
                best_dist = dist
        return best_dist


# MAIN STARTS HERE
if len(argv) != 2:
    print("Error!: Incorrect arguments")
    print("Usage: python checkTSP.py MAP_FILE_NAME")
    exit()

map_route = MapRoute(argv[1])
print(map_route.best_path(0, list(range(1, map_route.num_towns))))

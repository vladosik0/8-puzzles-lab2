import numpy as np
import copy
class BFS:
    MaxDepth = 8

    def find_solution(self, inp, goal):

        iterations = 0
        states = 1
        states_in_memory = 1

        pathcost = 0

        queue = []
        inpx = [inp, "none"]
        queue.append(inpx)
        # for i in range(9):
        while (True):
            iterations += 1
            puzzle = queue.pop()
            pathcost = pathcost + 1
            print(str(puzzle[1]) + " --> " + str(puzzle[0]))
            if (puzzle[0] == goal):
                print("Found")
                print('Path cost-> ' + str(pathcost - 1))
                break
            else:
                states += 1
                # up
                if (puzzle[1] != "down"):
                    temp = copy.deepcopy(puzzle[0])
                    up = self.move(temp, "up")
                    upx = [up, "up"]
                    queue.insert(0, upx)
                # left
                if (puzzle[1] != "right"):
                    temp = copy.deepcopy(puzzle[0])
                    left = self.move(temp, "left")
                    leftx = [left, "left"]
                    queue.insert(0, leftx)
                # down
                if (puzzle[1] != "up"):
                    temp = copy.deepcopy(puzzle[0])
                    down = self.move(temp, "down")
                    downx = [down, "down"]
                    queue.insert(0, downx)
                # right
                if (puzzle[1] != "left"):
                    temp = copy.deepcopy(puzzle[0])
                    right = self.move(temp, "right")
                    rightx = [right, "right"]
                    queue.insert(0, rightx)

        print("Iterations: ", iterations)
        print("States created: ", states)

        return states

    def move(self, temp, movement):
        if movement == "up":
            for i in range(3):
                for j in range(3):
                    if (temp[i][j] == -1):
                        # blank space found
                        if i != 0:
                            temp[i][j] = temp[i - 1][j]
                            temp[i - 1][j] = -1
                        return temp

        if movement == "down":
            for i in range(3):
                for j in range(3):
                    if (temp[i][j] == -1):
                        # blank space found
                        if i != 2:
                            temp[i][j] = temp[i + 1][j]
                            temp[i + 1][j] = -1
                        return temp

        if movement == "left":
            for i in range(3):
                for j in range(3):
                    if (temp[i][j] == -1):
                        # blank space found
                        if j != 0:
                            temp[i][j] = temp[i][j - 1]
                            temp[i][j - 1] = -1
                        return temp

        if movement == "right":
            for i in range(3):
                for j in range(3):
                    if (temp[i][j] == -1):
                        # blank space found
                        if j != 2:
                            temp[i][j] = temp[i][j + 1]
                            temp[i][j + 1] = -1
                        return temp


#inp = [[1, 2, 3], [4, -1, 5], [6, 7, 8]]
#out = [[1, 2, 3], [6, 4, 5], [-1, 7, 8]]


# print("Enter input puzzle")
# for i in range(3):
#   for j in range(3):
#     inp[i][j]=int(input("Enter number at "+str(i)+","+str(j)+" ->"))

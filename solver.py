from itertools import repeat
import copy
# Get the setting from the user
# Get the board
# Get the robot positions
# Get the target

# Write the code to adjust the board after a robot moves
# Write the code to solve the board after a robot moves

# Keep passing shit back and forth

board_size = 5
robot_count = 4

#Set up row walls; index of 0 is past the top or left, off the board
row_walls = [[0]*(board_size+1) for i in repeat(None,board_size+1)]

#Set up board walls
for i in row_walls:
	i[0]+=1
	i[len(i)-1]+=1

row_walls[2][3]+=1
row_walls[3][1]+=1
row_walls[4][4]+=1


#Set up column walls
column_walls = [[0]*(board_size+1) for i in repeat(None,board_size+1)]
for i in column_walls:
	i[0]+=1
	i[len(i)-1]+=1

column_walls[2][1]+=1
column_walls[3][4]+=1

#Set up robots
robot_locations = [() for i in repeat(None,robot_count)]

robot_locations[0] = (1,1)
robot_locations[1] = (4,1)
robot_locations[2] = (2,4)
robot_locations[3] = (4,5)

def addRobot(rows,columns,robot):
	x, y = robot

	rows[y][x-1]+=1
	rows[y][x]+=1

	columns[x][y-1]+=1
	columns[x][y]+=1

	return

def removeRobot(rows,columns,robot):
	x, y = robot

	rows[y][x-1]-=1
	rows[y][x]-=1

	columns[x][y-1]-=1
	columns[x][y]-=1

	return

def moveRobot(rows,columns,robots,robot_picker,direction):
	removeRobot(rows,columns,robots[robot_picker])

	x_test, y_test = robots[robot_picker]

	if direction==0: #Move up

		while columns[x_test][y_test-1] == 0:
			y_test-=1

	elif direction==1: #Move down

		while columns[x_test][y_test] == 0:
			y_test+=1

	elif direction==2: #Move left

		while rows[y_test][x_test-1] == 0:
			x_test-=1

	elif direction==3: #Move right

		while rows[y_test][x_test] == 0:
			x_test+=1

	robots[robot_picker] = (x_test,y_test)

	addRobot(rows,columns,robots[robot_picker])

# Solution

target_robot = 2
target_location = (5,3)

solved = False
progress_tracker = [[robot_locations,[]]]

solution_path = []

while not solved:
	current_situation = progress_tracker.pop(0)

	for i in range(16):

		current_path = copy.deepcopy(current_situation[1])
		current_path.append(i)

		# print "Current path is " 
		# print current_path

		current_locations = copy.deepcopy(current_situation[0])
		current_rows = copy.deepcopy(row_walls)
		current_columns = copy.deepcopy(column_walls)

		for robot in current_locations:
			addRobot(current_rows,current_columns,robot)

		current_path = copy.deepcopy(current_situation[1])
		current_path.append(i)

		moveRobot(current_rows,current_columns,current_locations,i/4,i%4)

		if current_locations[target_robot] == target_location:
			solved = True
			solution_path = current_path

		else:
			progress_tracker.append([current_locations,current_path])

		if i == 15:
			i = 0

for i in range(len(solution_path)):
	robot_number = solution_path[i]/4
	direction_number = solution_path[i]%4
	direction = ""

	if direction_number==0:
		direction = "up"
	elif direction_number==1:
		direction = "down"
	elif direction_number==2:
		direction = "left"
	elif direction_number==3:
		direction = "right"

	print "Move robot " + str(robot_number) + " " + direction










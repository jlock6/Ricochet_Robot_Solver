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

def moveUp(rows,columns,robots,robot_picker):
	removeRobot(rows,columns,robots[robot_picker])

	x, test_location = robots[robot_picker]

	while columns[x][test_location-1] == 0:
		test_location-=1

	robots[robot_picker] = (x,test_location)

	addRobot(rows,columns,robots[robot_picker])

	return

def moveDown(rows,columns,robots,robot_picker):
	removeRobot(rows,columns,robots[robot_picker])

	x, test_location = robots[robot_picker]

	while columns[x][test_location] == 0:
		test_location+=1

	robots[robot_picker] = (x,test_location)

	addRobot(rows,columns,robots[robot_picker])

	return

def moveLeft(rows,columns,robots,robot_picker):
	removeRobot(rows,columns,robots[robot_picker])

	test_location, y = robots[robot_picker]

	while rows[y][test_location-1] == 0:
		test_location-=1

	robots[robot_picker] = (test_location,y)

	addRobot(rows,columns,robots[robot_picker])

	return	

def moveRight(rows,columns,robots,robot_picker):
	removeRobot(rows,columns,robots[robot_picker])

	test_location, y = robots[robot_picker]

	while rows[y][test_location] == 0:
		test_location+=1

	robots[robot_picker] = (test_location,y)

	addRobot(rows,columns,robots[robot_picker])

	return	

for robot in robot_locations:
	addRobot(row_walls,column_walls,robot)

moveRight(row_walls,column_walls,robot_locations,2)

for wall in row_walls:
	print wall

print "hello"

for wall in column_walls:
	print wall

print "hello"

for robot in robot_locations:
	print robot 


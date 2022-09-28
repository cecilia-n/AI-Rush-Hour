
""" 
Heuristic 0 looks at cars blocking the X car from the goal state
""" 
def blockingHeuristic(gameBoard):
  if isGoal(gameBoard):
    return 0
  else:
    num_vehicles = 0

    ##Where x is, count how many cars or trucks are blocking the exit 
    xCarPosition = locateCar("X", gameBoard)
    # printGameBoard(gameBoard)
    # print("xCarPosition", xCarPosition)
    endofX = xCarPosition[-1]["column"]
    # print("endofX:", endofX)
    for colToCheck in range(endofX + 1, 6):
      placeToCheck = {"row": xCarPosition[-1]["row"], "column": colToCheck}
      charAtPosition = lookUpPosition(placeToCheck, gameBoard)
      if charAtPosition != "-":
        num_vehicles += 1
    #   print("Char at Pos:", charAtPosition)
    #   print("placeToCheck:", placeToCheck)
    # print("num_vehicles", num_vehicles)
    return 1 + num_vehicles
  #don't wan't to rank clear path same as goal state


"""
Heuristic 1 looks at distance X car is from the goal state
"""
def myHeuristic(gameBoard):
  #can I do 0 goal state, and distance from the car to goal state?
  #how?

  ##Where x is, count how many cars or trucks are blocking the exit 
  xCarPosition = locateCar("X", gameBoard)
  # printGameBoard(gameBoard)
  # print("xCarPosition", xCarPosition)
  endofX = xCarPosition[-1]["column"]
  printGameBoard(gameBoard)
  xdist = 5 - endofX
  return xdist


#position, row and column
#gameBoard is gameState


"""
Identifies the separate vehicles or "game pieces" 
"""
def getGamePieces(node):
  #use locate car to find Index
  #with index, find the specific letters
  letters = []
  for row_index in range(len(node.gameBoard)):
    row = node.gameBoard[row_index]
    for column_index in range(len(row)):
      character = row[column_index]
      if (character != "-") and (character not in letters):
        letters.append(character)
  return letters


""" 
Sees if vehicle is horizonal or vertical
"""
def getOrientation(gamePiece, node):
  location = locateCar(gamePiece, node.gameBoard)
  #if letter in same column or same row, vertical/horizontal
  # the first row vs the second row of the dictionary
  # if the first "row" is equal to the second "row", then it's horizontal
  # if the first "column" is equal to the second "column", then it's vertical
  firstrow = location[0]['row']
  secondrow = location[1]['row']

  if firstrow == secondrow:
    return "horizontal"

  firstcolumn = location[0]['column']
  secondcolumn = location[1]['column']

  if firstcolumn == secondcolumn:
    return "vertical"


"""
Sees the available moves for the vehicle and
Return neighboring nodes, which are the versions of the state string
after the car/truck moves in each direction one space
"""
def getMoves(gamePiece, node):
  # Is it horizontal or vertical?
  rlList = []
  # print("gamePiece:", gamePiece)
  orientation = getOrientation(gamePiece, node)
  # print("orientation:", orientation)
  if orientation == "horizontal":
    right = moveCar(node, "right", gamePiece)
    #make list, append right and left
    left = moveCar(node, "left", gamePiece)
    if node.gameBoard != right: #same gameBoard, don't need another neighbor right
     rlList.append(right)
    if node.gameBoard != left:
     rlList.append(left)
  # print("rlList:", rlList)
    return rlList
  if orientation == "vertical":
    udList = []
    up = moveCar(node, "up", gamePiece)
    down = moveCar(node, "down", gamePiece)
    if node.gameBoard != up: #same gameBoard, don't need another neighbor right
     udList.append(up)
    if node.gameBoard != down: #same gameBoard, don't need another neighbor right
     udList.append(down)
    return udList
  # if orientation == "vertical":


"""
Given a position where the character in GameBoard is found
"""
def lookUpPosition(position, gameBoard):  
  row = position["row"]
  column = position["column"]
  return  gameBoard[row][column]

def replaceCharacter(position, newCharacter, gameBoard):
  rowToMoveTo = position["row"]
  columnToMoveTo = position["column"]
  oldRow = gameBoard[rowToMoveTo]
  newRow = ""
  for character_index in range(len(oldRow)):
    if character_index == columnToMoveTo:
      newRow += newCharacter
    else:
      newRow += oldRow[character_index]
  gameBoard[rowToMoveTo] = newRow
  

""" 
Moves vehicle in game board depending on orientation
"""
def moveCar(node, dir, gamePiece):
  if dir == "right":
    # print("Position To Move:", positionToMove)
    # it can move right only if there's no other game piece to the right
    gameBoard = node.gameBoard.copy()
    carPosition = locateCar(gamePiece, gameBoard)
    if carPosition[-1]["column"] != 5: #boundry 
      # print("carPosition:")
      # print(carPosition)
      # when the last char of vehicle "moves", replace first char in string with "-"
      posToDeleteFirstChar = carPosition[0].copy()
      # print("positionToDeleteFirstChar:")
      # print(posToDeleteFirstChar)
      #iterate through list to change columns
      for columnIndex in range(len(carPosition)):
      # need to reference the location of the vehicle and be able to change item
        carPosition[columnIndex]["column"] += 1 #gets value of column, adds 1
      
      # print("New Car Position to Right:")
      # print(carPosition)
      # print(gameBoard)
      positionToMove = carPosition[-1] 
      # print("Position To Move:", positionToMove)
      charAtPosition = lookUpPosition(positionToMove, gameBoard)
      # print("Look Up Position:", charAtPosition)
      # if it's a dash to right of vehicle, then it can "move"
      if charAtPosition == "-":
        # now we can actually move the car by replacing the string
        replaceCharacter(
          positionToMove, 
          gamePiece,
          gameBoard
        )
        replaceCharacter(
          posToDeleteFirstChar, 
          "-",
          gameBoard
        )  
  if dir == "left":
    gameBoard = node.gameBoard.copy()
    carPosition = locateCar(gamePiece, gameBoard)
    if carPosition[0]["column"] != 0: 
      # print("carPosition:")
      # print(carPosition)
      # when the last char of vehicle "moves", replace first char in string with "-"
      posToDeleteFirstChar = carPosition[0].copy()
      # print("positionToDeleteFirstChar:")
      # print(posToDeleteFirstChar)
      #HOW TO REPLACE LETTER WITH - WHEN FIND POSITION
      #iterate through list to change columns
      for columnIndex in range(len(carPosition)):
        # need to reference the location of the vehicle and be able to change item
        carPosition[columnIndex]["column"] -= 1 #gets value of column, adds 1
      
      # print("New Car Position to Right:")
      # print(carPosition)
      # print(gameBoard)
      positionToMove = carPosition[-1] 
      # print("Position To Move:", positionToMove)
      charAtPosition = lookUpPosition(positionToMove, gameBoard)
      # print("Look Up Position:", charAtPosition)
      # if it's a dash to right of vehicle, then it can "move"
      if charAtPosition == "-":
      # now we can actually move the car by replacing the string
        replaceCharacter(
          positionToMove, 
          gamePiece,
          gameBoard
        )
        replaceCharacter(
          posToDeleteFirstChar, 
          "-",
          gameBoard
        )
  if dir == "up":
    #move one tile
    gameBoard = node.gameBoard.copy()
    carPosition = locateCar(gamePiece, gameBoard)
    if carPosition[0]["row"] != 0: #IS BOUNDRY RIGHT
      # print("carPosition:")
      # print(carPosition)
      # when the last char of vehicle "moves", replace first char in string with "-"
      posToDeleteFirstChar = carPosition[-1].copy()
      # print("positionToDeleteFirstChar:")
      # print(posToDeleteFirstChar)
      #HOW TO REPLACE LETTER WITH - WHEN FIND POSITION
      #iterate through list to change columns
      for columnIndex in range(len(carPosition)):
        # need to reference the location of the vehicle and be able to change item
        carPosition[columnIndex]["row"] -= 1 #gets value of column, adds 1
      
      # print("New Car Position to Right:")
      # print(carPosition)
      # print(gameBoard)
      positionToMove = carPosition[0] 
      # print("Position To Move:", positionToMove)
      charAtPosition = lookUpPosition(positionToMove, gameBoard)
      # print("Look Up Position:", charAtPosition)
      # if it's a dash to right of vehicle, then it can "move"
      if charAtPosition == "-":
        # now we can actually move the car by replacing the string
        replaceCharacter(
          positionToMove, 
          gamePiece,
          gameBoard
        )
        replaceCharacter(
          posToDeleteFirstChar, 
          "-",
          gameBoard
        )
  if dir == "down":
    gameBoard = node.gameBoard.copy()
    carPosition = locateCar(gamePiece, gameBoard)
    if carPosition[-1]["row"] != 5:
      # print("carPosition:")
      # print(carPosition)
      # when the last char of vehicle "moves", replace first char in string with "-"
      posToDeleteFirstChar = carPosition[0].copy()
      # print("positionToDeleteFirstChar:")
      # print(posToDeleteFirstChar)
      #HOW TO REPLACE LETTER WITH - WHEN FIND POSITION
      #iterate through list to change columns
      for columnIndex in range(len(carPosition)):
        # need to reference the location of the vehicle and be able to change item
        carPosition[columnIndex]["row"] += 1 #gets value of column, adds 1
      
      # print("New Car Position to Right:")
      # print(carPosition)
      # print(gameBoard)
      positionToMove = carPosition[-1] 
      # print("Position To Move:", positionToMove)
      charAtPosition = lookUpPosition(positionToMove, gameBoard)
      # print("Look Up Position:", charAtPosition)
      # if it's a dash to right of vehicle, then it can "move"
      if charAtPosition == "-":
        # now we can actually move the car by replacing the string
        replaceCharacter(
          positionToMove, 
          gamePiece,
          gameBoard
        )
        replaceCharacter(
          posToDeleteFirstChar, 
          "-",
          gameBoard
        )
  return gameBoard


"""
Seeing possible moves for the game board
"""
def findNeighbors(node):
  # How many pieces are there on the game board?
  # find different letttersters
  neighbors = []
  gamePieces = getGamePieces(node)
  for gamePiece in gamePieces:
    # find all the different ways to move this one piece
    movements = getMoves(gamePiece, node)
    neighbors += movements
  return neighbors 
      

"""Node class for A* Pathfinding"""
class Node(): #code for getting g, h, f 
    
    def __init__(self, parent=None, heuristicType = 0, gameBoard=None): 
    #to make a new node
      self.parent = parent
      self.gameBoard = gameBoard

      if gameBoard:
        # The actual number of steps it took to get here.
        #g for parent node , add 1
        if self.parent:
          self.g = parent.g +1
        else:
          self.g = 0

        if heuristicType == 0:
        # The guess based on the heuristic of how far is left to go.
          self.h = blockingHeuristic(gameBoard)
        if heuristicType == 1:
          self.h = myHeuristic(gameBoard)
        
        # The guess based on heuristic and steps to get here of how
        # far IN TOTAL it will end up taking to get to the goal.
        self.f = self.h + self.g

      else:
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.gameBoard == other.gameBoard


""" 
Given vehicle letter, you can tell the location 
"""
#want to know position of special car
def locateCar(letter, gameBoard):
  positions = []
  for row_index in range(len(gameBoard)):
    row = gameBoard[row_index]
    if letter in row:
      # maybe the letter might be in the row more than once
      for column_index in range(len(row)):
        character = row[column_index]
        if character == letter:
          position = {"row": row_index, "column": column_index}
          
          positions.append(position)
  return positions


"""Checking if goal is reached"""
def isGoal(curr):
  #where the XX car goal is
  xcoord = locateCar("X", curr)
  return xcoord == [
    {"row": 2, "column": 4},
    {"row": 2, "column": 5}
  ]


"""Prints game board"""
def printGameBoard(gameBoard):
  print("\n".join(gameBoard))
  print()


"""Path is found"""
def unrollPath(curr):
  if curr.parent:
    parent = curr.parent
    return unrollPath(parent) + [curr.gameBoard]
  else:
    return [curr.gameBoard]


"""Uses A*"""
def rushhour(heuristicType, startGameBoard):
#F is the total cost of the node. (guess)
#G is the distance between the current node and the start node. (actual)
#H is the heuristic — estimated distance from the current node to the end nod
#not recursive

  # make a node (containing f, h, g, etc) out of the start_string
  start = Node(gameBoard=startGameBoard, heuristicType = heuristicType)

  # the number of times a node is removed from the front of the frontier and examined 

  totalStatesExplored = 0

  # unexplored should be sortable by f
  # should compute f for the start node
  unexplored = [start]
  visited = []
  
  # make a base case for if the goal is not found
  endOfPath = None
  goalFound = False 
  while len(unexplored) != 0 and goalFound == False:
    #find lowest f(n) = g(n) + h(n) score 
    # compare f(n) and choose the lowest f(n)
    #sort list by f
    unexplored.sort(key = lambda x: x.f) #ehrn see node, seq to get number, sort by number, each node inititalized, just sort by f
    curr = unexplored.pop(0)
    visited.append(curr)
    #keep track how times pop current into visited
    totalStatesExplored += 1
     
    # If current is goal state, then done,
    if isGoal(curr.gameBoard):
      #reference a function isGoal
      endOfPath = curr
      goalFound = True 
    else:
      # otherwise, find neighboring nodes
      neighbors = findNeighbors(curr)
      # and calculate the f(n)s
      for neighbor in neighbors:
        neighborNode = Node(parent = curr, gameBoard = neighbor)
        #If neighborNode seen before, compare the f(n)s of the old version and this new one. if it has a lower f(n) coming from the current node, then replace the corresponding node in the visited (or unexplored) list so that it has the better f(n) value and the better parent path to get here.
         
        #deal with things we've seen before, either in unexplored or visited
        # if neighborNode is in unexplored then we do something about it, we don't want it
        if neighborNode in unexplored:
          # find the thing in unexplored with the same game state as neighborNode
          for previousNode in unexplored:
            if previousNode == neighborNode:
              break
          # if the neighbor node's f value is less, then you would change the previous node to the neighborNode value
          if neighborNode.f < previousNode.f:
            previousNode.f = neighborNode.f
            previousNode.parent = neighborNode.parent
        # otherwise, if it's in visited, we do something about it, we don't want it
        elif neighborNode in visited:
          for previousNode in visited:
            if previousNode == neighborNode:
              break
          # if the neighbor node's f value is less, then you would change the previous node to the neighborNode value
          if neighborNode.f < previousNode.f:
            previousNode.f = neighborNode.f
            previousNode.parent = neighborNode.parent
        # if neither of those are true, if it's not in either list, then we can append it to unexplored
        else:
          # if you haven't seen this node before, add it to the unexplored list
          unexplored.append(neighborNode)
  
  #when goal is reached unroll (find parent of state nodes)
  path = unrollPath(endOfPath)
  # #using function outside while loop

  for gameBoard in path:
    printGameBoard(gameBoard)
  print("Number of Moves:", len(path) )
  print("Total States Explored:", totalStatesExplored)


"""Test Cases"""
print("===========  TEST CASES FOR LOCATE CAR  ===========\n\n\n")

def test_locateCar(letter, currState, expectedOutput):
  prettier_state = "\n".join(currState)
  print("Find car {} in \n{}".format(letter, prettier_state))
  print()
  print("Actual output:")
  print(locateCar(letter, currState))
  print()
  print("Expected output:")
  print(expectedOutput)

  print()
  print()
  print()

test_locateCar(
  "X",
  [
    "--B---",
    "--B---",
    "----XX",
    "--AA--",
    "------",
    "------"
  ],
  [
    {"row": 2, "column": 4},
    {"row": 2, "column": 5}
  ]
)

test_locateCar(
  "X",
  [
    "--B---",
    "--B---",
    "XX----",
    "--AA--",
    "------",
    "------"
  ],
  [
    {"row": 2, "column": 0},
    {"row": 2, "column": 1}
  ]
)

test_locateCar(
    "B",
    [
      "--B---",
      "--B---",
      "XX----",
      "--AA--",
      "------",
      "------"
    ],
    [
      {"row": 0, "column": 2},
      {"row": 1, "column": 2}
    ]
  )

test_locateCar(
  "B",
  [
    "--B---",
    "--B---",
    "XX----",
    "--AA--",
    "------",
    "------"
  ],
  [
    {"row": 0, "column": 2},
    {"row": 1, "column": 2}
  ]
)


test_locateCar(
  "B",
  [
    "--B---",
    "--B---",
    "XXB---",
    "--AA--",
    "------",
    "------"
  ],
[
  {"row": 0, "column": 2},
  {"row": 1, "column": 2},
  {"row": 2, "column": 2}
]
)


print("===========  TEST CASES FOR IS GOAL  ===========\n\n\n")

testState = [
  "--B---",
  "--B---",
  "--B-XX",
  "--AA--",
  "------",
  "------"
]
print("isGoal(testState)")
print(isGoal(testState))
print()


print("===========  TEST CASES FOR RUSHHOUR  ===========\n\n\n")
# testGameBoard = [
#   "--B---",
#   "--B---",
#   "XXB-EC",
#   "-AAAEC",
#   "---DDD",
#   "------"
# ]
testGameBoard = [
  "------",
  "------",
  "XXA---",
  "--A---",
  "BBBCCC",
  "------"
]
rushhour(1, testGameBoard)

# testGameBoard = [
#   "--B---",
#   "--B---",
#   "XXB-EC",
#   "-AAAEC",
#   "---DDD",
#   "------"
# ]
testGameBoard = [
  "------",
  "------",
  "XXA---",
  "--A---",
  "BBBCCC",
  "------"
]
rushhour(0, testGameBoard)




# print(lookUpPosition({"row": 4, "column": 0}, testGameBoard))

#start and end node made

# rushhour(
#   0,
#   [
#     "--B---",
#     "--B---",
#     "----XX",
#     "--AA--",
#     "------",
#     "------"
#   ]
# )
# # --B---
# # --B---
# # ----XX  
# # --AA--
# # ------
# # ------

# # Total moves: 0
# # Total states explored: 1

# rushhour(
#   0,
#   [
#     "--B---",
#     "--B---",
#     "XXB---",
#     "--AA--",
#     "------",
#     "------"
#   ]
# )
def escapeRoom(width, height, teleport, block):
  x,y = teleport[-1]
  # O(heigh * width)
  while y < height:
    while x < width:
      # Can we move right?
      if([x+1,y] in block):
        return False
      x += 1
    x = 0
    # Can we move down?
    if([x, y+1] in block):
      return False
    y += 1
  return True


def escapeRoom2(width, height, teleport, block):
  x,y = teleport[-1]
  # O(height * len(block))
  while y < height:
    for position in range(len(block)):
      if(position[0] == x and y < position[1]):
        return False
      x = 0 
      y += 1
  return True

def escapeRoom3(width, height, teleport, block):
  x,y = teleport[-1]
  # O(len(block))
  for position in range(len(block)):
    if(block[position][0] >= x and y <= block[position][1]):
      return False
  return True

# Test Cases
## Start on top-left, goal is to get to bottom left.

## Can only move right until you hit end of the row. If you hit end of the row, you're allowed to get to the next row. 

width = 4
height = 4
teleport = [[0,1], [2,2], [1,1]]
## when you start on teleport[0], you end up in teleport[-1]. 
## assume you only teleport once. 
## starting position is the ending square of teleport. 

blockArea = [[2,3]]
## can't go into or pass through it
## if you hit this area, you can't go further, and therefore return False. 

print(escapeRoom3(width, height, teleport, blockArea))





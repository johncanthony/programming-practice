from random import randint

class board:

    def __init__(self):

        #self.board = { 0 : [ 9,9,9],1: [9,9,9],2: [9,9,9]}
	self.board = { 0:[ 1,2,3],1:[4,5,6],2:[7,8,9]}
	
    def populate(self):
	for y in range (0,3):
		for x in range (0,3):
			val = randint(0,1)
			self.board[y][x]=val


    def check_up(self, x,y):
	if(y-1) < 0:
		return
 	if(self.board[y-1][x] == self.board[y][x]):	
	  self.board[y-1][x]= -1	

    def check_down(self, x,y):
	if(y+1) > 2:
		return
 	if(self.board[y+1][x] == self.board[y][x]):	
	  self.board[y+1][y]= -1	

    def check_left(self, x,y):
	if(x-1) < 0:
		return
 	if(self.board[y][x-1] == self.board[y][x]):	
	  self.board[y][x-1]= -1	

    def check_right(self, x,y):
	if(x+1) > 2:
		return
 	if(self.board[y][x+1] == self.board[y][x]):	
	  self.board[y][x+1]= -1	
	
    def gravity(self,x,y):
	while(y>=0):
		print("======")
		self.bprint()
		if(self.board[y][x]==-1):
			del(self.board[y][x])
			self.board[y].insert(0,9)
			continue
		y=y-1
	
    def pop(self,y,x):

#	self.board[y][x] = "X"
	
	self.check_left(x,y)
	self.check_right(x,y)
	self.check_up(x,y)
	self.check_down(x,y)
	self.board[x][y]=-1

	for x in range(0,3):
		y=2
		self.gravity(x,y)	
   

    def bprint(self):
	for i in range(0,3):
  		print("{},{},{}".format(self.board[0][i],self.board[1][i],self.board[2][i]))

b = board()

b.populate()
b.bprint()

print("======")

x=2
y=0
print("x={},y={}".format(x,y))
b.pop(x,y)
b.bprint()

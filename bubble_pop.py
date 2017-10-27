from random import randint

class board:

    def __init__(self):

        self.board = { 0 : [ 9,9,9],1: [9,9,9],2: [9,9,9]}

    def populate(self):
	for x in range (0,3):
		for y in range (0,3):
			val = randint(0,1)
			self.board[x][y]=val


    def check_up(self, x,y):
	if(x-1) < 0:
		return
 	if(self.board[x-1][y] == self.board[x][y]):	
	  self.board[x-1][y]= -1	

    def check_down(self, x,y):
	if(x+1) > 2:
		return
 	if(self.board[x+1][y] == self.board[x][y]):	
	  self.board[x+1][y]= -1	

    def check_left(self, x,y):
	if(y-1) < 0:
		return
 	if(self.board[x][y-1] == self.board[x][y]):	
	  self.board[x][y-1]= -1	

    def check_right(self, x,y):
	if(y+1) > 2:
		return
 	if(self.board[x][y+1] == self.board[x][y]):	
	  self.board[x][y+1]= -1	
	
    def gravity(self,x,y):
	while(x>=0):
		
		print(x)
		if(self.board[x][y]==-1):
			
			self.board[x][y]=9
			self.board[x][y]=self.board[x-1][y]
        		self.board[x-1][y]=9
		x=x-1
		

    def pop(self,x,y):

	self.check_left(x,y)
	self.check_right(x,y)
	self.check_up(x,y)
	self.check_down(x,y)
	self.board[x][y]=-1

	for y in range(0,3):
		x=2
		self.gravity(x,y)	
    



b = board()

b.populate()
for i in range(0,3):
  print(b.board[i])

b.pop(1,1)
for i in range(0,3):
  print(b.board[i])

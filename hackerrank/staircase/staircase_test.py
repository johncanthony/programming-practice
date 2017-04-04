import unittest
from staircase import makestair

class TestDiag(unittest.TestCase):
        def teststair(self):
                    stairs=3
                    want=["  #"," ##","###"]
                    results = makestair(stairs)
                    self.assertTrue(results == want)

	
	def teststair2(self):
                    stairs=6
                    want=["     #","    ##","   ###","  ####"," #####","######"]
                    results = makestair(stairs)
		    
                    self.assertTrue(results == want)

	def teststair3(self):
		    stairs=-1
                    want=[]
                    results = makestair(stairs)
                    self.assertTrue(results == want)



if __name__ == "__main__":
	unittest.main()

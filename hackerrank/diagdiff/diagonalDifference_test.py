import unittest
from diagonalDifference import diag_diff


class TestDiag(unittest.TestCase):
        def testdiag_diff(self):
                    lines=3
                    arr=[[1,2,3],[4,5,6],[7,8,9]]
                    results = diag_diff(lines,arr)
		    want=0                   
                    self.assertTrue(results == want)

	def testdiag_diff2(self):
                    lines=4
                    arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
                    results = diag_diff(lines,arr)
		    want=0                   
                    self.assertTrue(results == want)



if __name__ == "__main__":
    unittest.main()

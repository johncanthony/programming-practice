import sys


def makestair(staircnt):
	stringsarr=[]
	if(staircnt<1):
		return stringsarr

	for i in range(staircnt):
		tempstr= " " * (staircnt - (i+1))
		tempstr+= "#" * (i+1)
		stringsarr.append(tempstr)	

	return stringsarr	

if __name__ == "__main__":
	n=int(raw_input().strip())
	stairway=makestair(n)
	print(stairway)

import sys


def diag_diff(n,a):
	
	shift=0
	l_tot=0
	r_tot=0
	for i in range(n):
		l_tot+=a[i][i]
		r_tot+=a[i][(n-1)-shift]
		shift+=1
	
	return abs(l_tot - r_tot)	


if __name__ == '__main__':
	n = int(raw_input().strip())
	a=[]

	for a_i in xrange(n):
		a_temp = map(int,raw_input().strip().split(' '))
        	a.append(a_temp)



	diag_diff(n,a)

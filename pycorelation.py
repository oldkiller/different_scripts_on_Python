import math

def ranking(list_b):
	list_s=list_b.copy()
	list_s.sort()
	i,n=0,len(list_b)
	rank_b=list_b.copy()
	rank_s=list_s.copy()
	while i<n:
		k,nn,j=0,0,i
		while i<n and list_s[i]==list_s[j]:
			k=k+i+1
			nn,i=nn+1,i+1
		r=k/nn
		for k in range(j,i):
			rank_s[k]=r
	for i in range(n):
		for j in range(n):
			if list_b[i]==list_s[j]:
				rank_b[i]=rank_s[j]
				break
	return rank_b

def corel(rang_x,rang_y):
	try:
		if len(rang_x)!=len(rang_y):
			raise ValueError("Последовательности разной длинны")
		n=len(rang_x)
		# s=sum([(rang_x[i]-rang_y[i])**2 for i in range(n) ])
		# p=1-(6/(n*(n-1)*(n+1))*s)
		rx=sum(rang_x)/n
		ry=sum(rang_y)/n
		s1=sum([(rang_x[i]-rx)*(rang_y[i]-ry) for i in range(n)])
		s2=math.sqrt(sum([(rang_x[i]-rx)**2 for i in range(n)]))
		s3=math.sqrt(sum([(rang_y[i]-ry)**2 for i in range(n)]))
		p=s1/s2/s3
		return p
	except ValueError as v:
		input(v)

def spearman(list_x,list_y):
	rank_x=ranking(list_x)
	rank_y=ranking(list_y)
	core=corel(rank_x,rank_y)
	return core

def pirson(list_x,list_y):
	core=corel(list_x,list_y)
	return core

if __name__=="__main__":
	list_x=[1,2,3,4,5,6] #"2,1,3,4,3".split(",")
	list_y=[1,2,3,3,5,3] #"3,2,1,4,2".split(",")
	print(pirson(list_x,list_y))
	print(spearman(list_x,list_y))
	input()
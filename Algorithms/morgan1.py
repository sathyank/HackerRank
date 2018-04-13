import sys

def morgan(s1,s2):
	#stack1 = []
	#stack2 = []
	op = ""
	#for w in s1:
	#	stack1.append(w)
	#for w in s2:
	#	stack2.append(w)
	total = len(s1)+len(s2)
	i1=0
	i2=0
	
	while (i1<len(s1) and i2 <len(s1)) :
		if s1[i1]<s2[i2]:
			op = op + s1[i1]
			i1 = i1+1
			
		elif s1[i1]>s2[i2]:
			op = op + s2[i2]
			i2 = i2+1
			
	
		else:
			#print("check1")
			if s1[i1:]<s2[i2:]:
				op = op + s1[i1]
				i1 = i1+1
			
			elif s1[i1:]>s2[i2:]:
				op = op + s2[i2]
				i2 = i2+1
			else:
				#print("check2")
				op = op+s1[i1]
				i1 = i1 + 1
		
		
	if i1==len(s1) and i2<len(s2):
		op = op+s2[i2:]
			
	elif i2==len(s2) and i1<len(s1):
		op = op+s1[i1:]
			
			
	return op		
				
	
q = int(raw_input())
for a0 in range(q):
	s1 = raw_input()
	s2 = raw_input()
	output=""
	output = morgan(s1,s2)
	print(output)

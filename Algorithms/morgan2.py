import sys
op = ""
def morgan(s1,s2):
	
	
	
	i1=0
	i2=0
	l1 = len(s1)
	l2 = len(s2)
	while (i1<l1 and i2 <l2) :
		if s1[i1]<s2[i2]:
			op = op + s1[i1]
			i1 = i1+1
			
		elif s1[i1]>s2[i2]:
			op = op + s2[i2]
			i2 = i2+1
			
	
		else:
			if s2[i2:] < s1[i1:]:
				if l2<l1 and s2[l2-1]==s1[l2-1]:
					t=i2					
					while s1[t1] != s2[l2] 	 
				op= op+s2[i2]
				i2 = i2+1
				"""op = op + s1[i1]
				i1 = i1+1"""
			elif s1[i1:] < s2[i2:]:
				op = op+s1[i1]
				i1 = i1+1
			else:
				op = op + s1[i1]
				i1 = i1+1
				#op= op+s2[i2]
				#i2 = i2+1
					
	if i1==l1 and i2<l2:
		op = op+s2[i2:]
	elif i2==l2 and i1<l1:
		op = op+s1[i1:]
			
	return op		
				
	
q = int(raw_input())
for a0 in range(q):
	s1 = raw_input()
	s2 = raw_input()
	output=""
	output = morgan(s1,s2)
	print(output)
    
    

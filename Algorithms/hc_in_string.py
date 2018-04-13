import sys


q = int(raw_input().strip())
for a0 in range(q):
    s = raw_input().strip()
    if s.find("h") == -1 or s.find("a") == -1 or s.find("c") == -1 or s.find("k") == -1 or s.find("e") == -1 or s.find("r") == -1 or s.find("r") == -1 or s.find("a") == -1 or s.find("n") == -1 or s.find("k") == -1:
        print("No")
    else:
	if s.find("h")<s.find("a"):
		s = s[s.find("a")+1:]
		
		if s.find("c")<s.find("k"):
			s = s[s.find("k")+1:]
			
			if s.find("e")<s.find("r"):
				s = s[s.find("r")+1:]
				
				if s.find("r")<s.find("a"):
					s = s[s.find("a")+1:]
					
					if s.find("n")<s.find("k"):
						print("Yes")
					else:
						print("No")
				else:
					print("No")
			else:
				print("No")
		else:
			print("No")
	else:
		print("No")	
            

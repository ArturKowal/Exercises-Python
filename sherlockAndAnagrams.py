import time
from math import ceil

def sherlockAndAnagrams(s):	
	start = time.time()
	counter=len(s)
	mach=0
	ssub=list(s[a] for a in range(len(s)))
	for i in range(2,len(s)): 
		counter-=1
		for j in range(0,counter):
			ssub.append(s[j:j+i])

	for lam in range(1,len(s)):
		temp_list=list(filter(lambda itm : lam==len(itm), ssub))
		for num in range(len(temp_list)):
			elem1=sorted(temp_list[num]) 
			elem1="".join(elem1)
			for y in range(num+1,len(temp_list)):
				elem2=sorted(temp_list[y]) 
				elem2="".join(elem2)
				if elem1 == elem2: mach+=1
	#print('time: ',ceil((time.time() - start)*10000))
	return mach
anag=sherlockAndAnagrams('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
print(anag)
"""
Description: 
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""
#datos para el ejercicio 
"""294 82 174
348 5 122
226 233 4
247 139 104
163 126 92
10 210 36
198 51 151
162 254 178
48 175 194
210 127 127
310 47 181"""
nums=[294,82,174
,348,5,122
,226,233,4
,247,139,104
,163,126,92
,10,210,36
,198,51,151
,162,254,178
,48,175,194
,210,127,127
,310,47,181]
s=len(nums)
cont=0
d=0
a=0
b=0
c=0
suma=0
nums2=""
for i in range(s):
	d=d+1
	if(d==1):
		a=nums[i]
	if(d==2):
		b=nums[i]
	if(d==3):
		c=nums[i]
		res=a*b+c
		nums2=str(res)
		for i in nums2:
		 suma+=int(i)
		print(suma)
		suma=0
		d=0
	
salir=input()

#solución obteninda 18 17 21 21 11 12 16 16 26 31 18
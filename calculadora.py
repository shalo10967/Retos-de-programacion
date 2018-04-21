""" datos a ingresar
659* 2529* 611* 6990+ 3+ 153+ 48* 86+ 100* 38+ 17* 713+ 8* 62
+ 83+ 9* 3* 769* 5951* 930+ 2016+ 1322* 3* 5629+ 91+ 1225+ 149+ 8560
* 6369* 3531* 32+ 1780+ 207* 83* 2812* 2310+ 874* 69* 6* 398+ 681+ 6* 432* 982* 9652+ 9* 352* 9
+ 21* 522+ 3* 4425* 196* 7662% 8102"""
nums=[]
active=0
res=0
num=int(input("Ingrese un numero: "))
nums.append(num)
op=''
salir=''
while salir!= "=":
	op=str(input("Ingrese el operador o = para resultado: "))
	salir=op
	if(salir!='='):
		num2=int(input("Ingrese un numero:"))
		nums.append(num2)
	if(op=='*'):
		for i in range(len(nums)):
			res=nums[i-1]*nums[i]
		nums.append(res)
		print(res)
	if(op=='/'):
		for i in range(len(nums)):
			res=nums[i-1]/nums[i]
		nums.append(round(res,2))
		print(res)
	if(op=='+'):
		for i in range(len(nums)):
			res=nums[i-1]+nums[i]
		nums.append(round(res,2))
		print(res)
	if(op=='-'):
		for i in range(len(nums)):
			res=nums[i-1]-nums[i]
		nums.append(round(res,2))
		print(res)
	if(op=='%'):
		for i in range(len(nums)):
			res=nums[i-1]%nums[i]
		nums.append(round(res,2))
		print(res)
print(res)
	

#solución 8810
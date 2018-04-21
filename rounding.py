"""datos de entrada  12
3254302 1719296
4615420 -3144629
9833432 -114063
2681688 60
1481874 500
16733 1752
-7474545 2453191
7226848 593
5337 1552
-9646642 -4348076
14111 1566
9780569 -413215 

"""
nums=[3254302,1719296,4615420,-3144629,9833432,-114063,2681688,60,1481874,500,16733,1752,-7474545,2453191,7226848,593,5337,1552,-9646642,-4348076,14111,1566,9780569,-413215]
l=len(nums)
cont=0
pp=0
pi=0
for i in range(0,int(l)):
	cont=cont+i
	if(cont==0):
		div=nums[i]/nums[i+1]
		print("el cociente entre: ",nums[i]," Y ",nums[i+1]," es: ",round(div))
	if(cont>=2):
		if(i%2==0):			
			pp=nums[i]		
		else:
			pi=nums[i]
			
			div=pp/pi
			print("el cociente entre: ",pp," Y ",pi," es: ",round(div))
			
quit=input()

#la solucion es:2 -1 -86 44695 2964 10 -3 12187 3 2 9 -24
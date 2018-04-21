"""Datos de entrada para masa y altura
Peso =[68,73,103,43,111,55,66,47,42,45,61,89,108,61,101,51,116,68,96,73,88,91,56,43,44,81]
Altura =[1.39,2.07,2.71,1.22,2.63,2.14,1.59,1.83,1.45,1.58,1.95,1.89,2.38,2.35,3.03,1.91,2.11,1.51,2.14,1.68,1.81,1.59,1.37,159,1.84,2.06]
"""

w =[68,73,103,43,111,55,66,47,42,45,61,89,108,61,101,51,116,68,96,73,88,91,56,43,44,81]
h =[1.39,2.07,2.71,1.22,2.63,2.14,1.59,1.83,1.45,1.58,1.95,1.89,2.38,2.35,3.03,1.91,2.11,1.51,2.14,1.68,1.81,1.59,1.37,159,1.84,2.06]
for i in range(len(w)):

 BMI=w[i]/(h[i]*h[i])
 if (BMI<18.5):
 	print("UnderWeight: ",round(BMI,2))
 	f = open ('archivo.txt','a')
 	f.write('under ')
 	f.close()
 
 if (BMI>=18.5 and BMI<25.0):
 	print("NormalWeight: ",round(BMI,2))
 	
 	f = open ('archivo.txt','a')
 	f.write('normal ')
 	f.close()
 	
 if (BMI>=25.0 and BMI<30):
 	print("OverWeight: ",round(BMI,2))
 	
 	f = open ('archivo.txt','a')
 	f.write('over ')
 	f.close()
 
 if (BMI>=30.0):
 	print("Obesity: ",round(BMI,2))
 	
 	f = open ('archivo.txt','a')
 	f.write('obese ')
 	f.close()
salir=input()

#Mi solución ----> obese under under over under under over under normal under under normal normal under under under over over normal over over obese over under under normal 
# la solucion fue almacenada en un archivo de texto al cual nombre "archivo.txt"
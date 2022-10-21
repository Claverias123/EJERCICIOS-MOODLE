#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math

print("Vamos a calcular la hipotenusa de un triángulo rectángulo\n")
cateto_1 = (int)(input("Dime el cateto 1:\n"))
cateto_2= (int)(input("Dime el cateto 2:\n"))
hipotenusa = math.sqrt(cateto_1)*(cateto_1)+(cateto_2)*(cateto_2)
print("La hipotenusa es:", hipotenusa)
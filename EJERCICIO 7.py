#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
num=0
num = (int) (input ("Dime cuantos minutos quieres pasar a horas y minutos: \n"))
print(f"Horas: {int(num/60)} y {num%60} minutos")
#Un vendedor recibe un sueldo base mas un 10% extra por comisión de susventas, el vendedor desea saber cuanto dinero obtendrá por concepto decomisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

s=0
v1=0
v2=0
v3=0

s=(int) (input("Dime tu sueldo \n"))
v1=(int) (input("Dime el precio de la primera venta \n"))
v2=(int) (input("Dime el precio de la segunda venta \n"))
v3=(int) (input("Dime el precio de tu tercera venta \n"))

print ("Tu dinero ganado con las ventas es: ", (v1+v2+v3)*0.1,"euros")
print ("Tu dinero total es:", (v1+v2+v3)*0.1+s ,"euros")
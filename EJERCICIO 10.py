#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales ,30% de la calificación del examen final ,15% de la calificación de un trabajo final.

n1=(int) (input("Dime la nota de tu primer examen \n"))
n2=(int) (input("Dime la nota de tu segundo examen \n"))
n3=(int) (input("Dime la nota de tu tercer examen \n"))

print ("Tu nota media de estos tres exámenes es: ", (n1+n2+n3)/3)

nf=(int) (input("Dime la nota de tu examen final \n"))
tf=(int) (input("Dime la nota de tu trabajo final \n"))

print("Tu nota final es: ", (((n1+n2+n3)/3)*0.55)+(nf*0.3)+(tf*0.15))


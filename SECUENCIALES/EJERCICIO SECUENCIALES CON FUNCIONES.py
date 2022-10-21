from multiprocessing.heap import Arena


def ejercicio1 (nombre:str):
    print("Ejercicio 1")
    print("Buenos días",nombre)
ejercicio1("Domi")

def ejercicio2a(base:int, lado:int):
    cal_perimetro= ((2*base)+(2*lado))
    return cal_perimetro
print("El perímetro es:", ejercicio2a(2,4))

def ejercicio2b(base:int, lado:int):
    cal_area= (base*lado)
    return cal_area
print("El area es:", ejercicio2b(2,4))

def ejercicio2c(base:int, lado:int):
    print("Ejercicio 2c")
    area=ejercicio2b(base,lado)
    perimetro=ejercicio2a(base,lado)
    vlista= []
    vlista.append(area)
    vlista.append(perimetro)
    return vlista

base=int(input("Dime la base"))
lado=int(input("Dime el lado"))

vlista=ejercicio2c(base,lado)
print("El perimetro es",vlista[0])
print("El area es:", vlista[1])

def ejercicio3(cateto_1:int, cateto_2:int):
    import math
    print("Ejercicio 3")
    hipotenusa = math.sqrt(cateto_1)*(cateto_1)+(cateto_2)*(cateto_2)
    return hipotenusa
print("La hipotenusa es:", ejercicio3(2,3))


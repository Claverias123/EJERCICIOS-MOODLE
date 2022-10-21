#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
e2=0
e1=0
c50=0
c20=0
c10=0

e2=(int) (input("Dime cuantas monedas de 2€ tenemos \n"))
e1=(int) (input("Dime cuantas monedas de 1€ tenemos \n"))
c50=(int) (input("Dime cuantas monedas de 50 céntimos tenemos \n"))
c20=(int) (input("Dime cuantas monedas de 20 céntimos tenemos \n"))
c10=(int) (input("Dime cuantas monedas de 10 céntimos tenemos \n"))

print ("Tienes un total de:", e1+(e2*2)+(c50*0.50)+(c20*0.20)+(c10*0.10), "euros")
print ("Tienes un total de:", (e1*100)+(e2*200)+(c50*50)+(c20*20)+(c10*10), "céntimos")
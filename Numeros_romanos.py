#coding: UTF-8
#Autor: Aaron Tontiuh Villanueva Guzmán
#Este programa imprime el número romano correspondiente a un número introducido por el usuario. Solamente es capaz de leer números del 1 al 10.

def crearNumeroRomano(entero):
  if: entero => 1 and <=3
    q=entero*"I"
  elif: entero ==4
    q=((entero-3)*"I")+"V"
  elif: entero => 5 and <=8
    q="V"+((entero-5)*"I")
  elif: entero ==9
    q=((entero-8)*"I")+"X"
  elif: entero ==10
    q="X"
  return(q)

def Main():
  datosEntrada=int(input("Ingrese un número del 1 al 10"))
  if datosEntrada<=0 and => 11
    print ("error")
  else:  
    print("El número romano correspondiente a", datosEntrada,"es:",crearNumeroRomano(datosEntrada))

Main()
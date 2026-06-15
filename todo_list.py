
import os 

BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA_LISTAS = os.path.join(BASE, "listas")
os.makedirs(CARPETA_LISTAS, exist_ok=True)

def crear_lista ():
  
 titulo = input("Nombre de la lista: ").strip()

 if not titulo:
   print("El nombre no puede estar vacio")
   return
    
 ruta = os.path.join(CARPETA_LISTAS, titulo + ".txt")

 if os.path.exists(ruta):
   print("Ya existe una lista con ese nombre")
   return
 with open(ruta,"w") as archivo:


  
  archivo.write("Lista: " + titulo + "\n")
       
  while True:
      producto = input("Agrega un producto (o escribe 'listo' para terminar): ").strip()
      if producto.lower() == "listo":
          print("Lista guardada exitosamente")
          break      
      archivo.write("- " + producto + "\n") 

def obtener_listas ():
  return sorted ( [
    archivo
    for archivo in os.listdir(CARPETA_LISTAS)
    if archivo.endswith(".txt")
  ])
def mostrar_listas (): 
  
  while True :

   listas = obtener_listas()

   if not listas:
    print("No hay listas guardadas")
    return
   
   for i , lista in enumerate (listas,  1):
     print(str(i) + "." + lista.replace(".txt",""))

   opcion = input("\nEscoja una lista (NUMERO) o salir\n").strip().lower()

   if opcion == "salir":
     return

   try :
     escoger = int(opcion)
   except ValueError:
     print("Escoja un numero de la lista")
     continue
  
   if escoger < 1 or escoger > len(listas):
     print("Numero Invalido")
     continue
  
   lista_elegida = listas[escoger - 1]

   with open(os.path.join(CARPETA_LISTAS,lista_elegida),"r" )  as archivo:
    print ("\n" + archivo.read())
   input("\nPresione ENTER para continuar...")

def eliminar_listas ():
 
 while True:
  listas = obtener_listas ()

  if not listas:
   print("No hay listas guardadas")
   return
  print("\nListas disponibles\n")
  for i , lista in enumerate (listas,  1):
    print(str(i) + "." + lista.replace(".txt",""))

  opcion = input("\nEscoja una lista (NUMERO) o salir\n").strip().lower()

  if opcion == "salir":
     return

  try:
   escoger = int(opcion)
  except ValueError:
    print("Escoja un numero de la lista")
    continue


  if escoger < 1 or escoger > len(listas):
    print("Numero Invalido")
    continue
  
  lista_elegida = listas[escoger - 1]

  seguro = input("ESTA SEGURO DE ELIMINAR ESTA LISTA? \n (si/no) \n").strip().lower()
  if seguro =="si":
    os.remove(os.path.join(CARPETA_LISTAS, lista_elegida))
    print("LISTA ELIMINADA")
  else:
    print("OPERACION CANCELADA")
    return

def editar_lista():
 while True :
  listas = obtener_listas ()

  if not listas:
   print("No hay listas guardadas")
   return
  
  for i , lista in enumerate (listas,  1):
    print(str(i) + "." + lista.replace(".txt",""))

  opcion = input("\nEscoja una lista (NUMERO) o salir\n").strip().lower()

  if opcion == "salir":
     return

  try:
   escoger = int(opcion)
  except ValueError:
     print("Escoja un numero de la lista")
     continue

  if escoger < 1 or escoger > len(listas):
    print("Numero Invalido")
    continue
  
  lista_elegida = listas[escoger - 1]

  with open(os.path.join(CARPETA_LISTAS,lista_elegida),"r" )  as archivo:
    print (archivo.read())

  with open(os.path.join(CARPETA_LISTAS,lista_elegida),"a" )  as archivo:
   
   while True:
      producto = input("Agrega un producto (o escribe 'listo' para terminar): ").strip()

      if producto.lower() == "listo":
          print("Lista guardada exitosamente")
          break    
        
      archivo.write("- " + producto + "\n") 

        




while True: 

 menu = input("Bienvenido a listas  \n 1.Crear lista  \n 2.Eliminar lista  \n 3.Editar listas \n 4.Mostrar listas \n 5.SALIR \n" ).strip()
 if menu == "1":
  
  crear_lista ()

 elif menu == "2":
  
  eliminar_listas ()

 elif menu == "3":
  editar_lista ()

 elif menu == "4":
  mostrar_listas ()

 elif menu == "5":
  print("HASTA LUEGO")
  break
 else :
  print("OPCION INVALIDA")
  
  

 
    
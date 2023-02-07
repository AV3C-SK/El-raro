import random

alien = "Danny: "

locutor = "Narrador: "

numero_alien = random.randint(1,10)

titulo = "Bienvevido a Hexa"
print("\n" + titulo + "\n" + "-" * len(titulo))

name = input("Como te llamas?: ")

print("Bienvenido " + name)
print( alien + "El dia de hoy te encuentras en un planeta llamado Hexa,"
      "es un planeta muy raro para gente terrestre como tu \n"
      "Nuestra raza no tolera a los terricolas, pero yo soy la acepcion\n"
      "Mi nombre es Danny\n"
      "\nTienes 2 opciones para poder salir de aqui:")

A = print("A) Ocultarte usando un traje de invisibilidad, pero nose cuendo se termine la bateria")

B = print("B) Usar la alcantarila, pero nose que tan arriesgado sea\n")

opcion = input("Cual eliges? ")



if opcion == "A":
      print( alien + "Pues toma el traje, sigueme,"
            " pero trata de no hacer ruido, no te ven pero si te pueden escuchar")
      print(locutor + "Despues de un tiempo, la bataria del traje se acaba......")
      print( alien + "No puede ser! Corre!\n")
      print( name + " tienes 2 opciones:\n"
                           "A) Escapar por la puerta de metal \n"
                           "B) Escapar por el ascensor\n")
      opcionA = input("Cual eliges?: ")
      if opcionA == "A":
            print(locutor + name + " muere porques la puerta de metal era un entrada para la cantine,"
                                   "TE CENARON VIVO!\n"
                                   "\n"
                                   "Fin del juego!")
      if opcionA == "B":
          print("\n" + locutor +
                " En el ascensor te encuentras con una botella de CocaLien, "
                                 "esta vacia pero tal vez"
                          "te ayude en algo.")

          cocalien = False

          mochila = input("Quieres guardarla?: ")
          if mochila == "Si":
              print("Cogiste el Cocalien\n")
              cocalien = True
          if cocalien == "No":
              print("No cogiste el Cocalien\n")

          print(locutor + "Felicidades, llegaste hasta la salida!"
                          "Pero te encuentras con Danny\n"
                          + alien + "Sabia que estarias aca " + name + "\n")
          print(alien + "ODIO a los terricolas! Lo unico que hacen es cotaminar y extingir,\n"
                        "enserio crees que dejare a vivir a un terricola en mi planeta? HAHAHA\n"
                        "Pero te dejare ir, solo respondeme bien esto:\n")
          print("Cuanto es: 5 * {}".format(numero_alien))
          pregunta = int(input("Cual es el resultado?: "))
          if pregunta == 5 * numero_alien:
              
              print("\n" + alien + "NO ME GUSTAN LOS CEREBRITOS!Te comere! Tericola y cerebrito! FUUUA\n!"
                            "FIN DEL JUEGO!")
          else:
              print("Esta mal! HAHAHA, yo aprendi a multiplicar, pero odio las matematicas\n"
                    "bueno, te dejare ir, me caiste bien, cuidate y NO VUELVAS\n")
              print("Eres un ganador " + name + " felicidades <3")


              if cocalien == True:
                  input(locutor + name + " se dice para el mismo: tengo aun la Cocalien, lo tendre como recuerdo\n"
                                     "El no sabe que la botella puede causar caos y destruccion el la Tierra\n"
                                     "CONTINUARA..........")
if opcion == "B":
    print(locutor + name + " esta rodeado de mas de 500 ratas enormes, no sabe que hacer\n"
                            "esta muy nervioso y esta temblando.\n")
    print(name + " tienes 2 opciones:\n"
                  "A) Quedarte quito y esperar que se alejen hasta no verlos mas\n"
                  "B) Correr como si no hubiera un futuro\n")
    pregunta1 = input("Cual eliges:? ")
    if pregunta1 == "A":
        print(locutor + "Las ratas son muy amigables y te dicen donde esta la salida!\n"
                        "Felicidades ganaste! Pero las ratas quieren las gracias |ESCRIBE CUALQUIER COSA|\n")
        palabritas = input("Diles algo: ")
        if palabritas == "Muchas gracias":
            print("Las ratas te dan una CocaLien lleno y se despiden")
            print(locutor + name + " se dice para el mismo: tengo aun la Cocalien, lo tendre como recuerdo\n"
                                     "El no sabe que la botella puede causar caos y destruccion el la Tierra\n"
                                     "CONTINUARA..........")

        print("Pasaste el juego, FELICIDADES! <3")


    else:
        print(locutor + " las ratas se sieten atacadas y te comen vivo!\n"
                        "PERDISTE!")
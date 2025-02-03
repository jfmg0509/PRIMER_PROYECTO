especiales= ["/","*","&"] #colocar estos caracteres como obligatorios
numbers=["1","2","3"]
password_name=input("escribe tu contraseña")
for number in numbers:
    #print(number)
    if number in password_name:
        print(f"Tu conraseña {password_name} si tiene números y el número es {number}")
        break
    else:
        print(f"tu contraseña: {password_name} no contiene numeros. Intenta de nuevo")
for especial in especiales:
    print (especial)
    if especial in password_name:
        print

        

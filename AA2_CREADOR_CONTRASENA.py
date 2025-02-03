numbers= ["1","2","3","4","5","6","7","8","9","0"]
specials_character=["+","/"]
while True:
    password_name= input("ingrese el nombre de su contraseña: ")
    is_number_found= False #esta variable te indica si encontramos números en la contraseña
    is_special_character_found= False
    for number in numbers:
        if number in password_name:
            is_number_found = True
            break
    for especial in specials_character:
        if especial in password_name:
            is_special_character_found = True
            break
    if is_number_found  and is_special_character_found:
        print ("tu contraseña es correcta.")
        break #el breaK hace que se cierre el bucle
    else:
        print("no te olvides de colocar un número y un caracter especial")
        


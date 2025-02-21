numbers= ("1","2","3","4","5","6","7","8","9","0")
specials_character=["+", "/", "@", "#", "$", "%", "&", "*", "!", "?"]
dictionary_of_uppercase_letters = {
    "uppercase_letters": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
}
#uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] #Genera lista de mayúsculas
while True:
    password_name= input("Ingrese su contraseña: ")
    is_number_found= False #esta variable te indica si encontramos números en la contraseña
    is_special_character_found= False #esta variable indica si se encontraron caracteres especiales en la contraseña 
    is_uppercase_found= False #esta variable indica si se encontraron mayúsculas en la contraseña
    for number in numbers: #indica 
        if number in password_name:
            is_number_found = True
            break
    for especial in specials_character:
        if especial in password_name:
            is_special_character_found = True
            break
    for letter in dictionary_of_uppercase_letters["uppercase_letters"]:
        if letter in password_name:
            is_uppercase_found = True
            break
    if is_number_found and is_special_character_found and is_uppercase_found:
        print ("Tu contraseña es correcta.")
        break #el breaK hace que se cierre el bucle
    else:
        if not is_number_found:# el not me comprueba que no se cumple esta condición
            print ("No te olvides de colocar un número")
        if not is_special_character_found:
            print ("No te olvides de colodar un caracter especial")
        if not is_uppercase_found:
            print ("No te olvides de colocar una Mayúsculas")
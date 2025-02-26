def contains_element(list_of_element, password):
    '''
    Función que recibe una lista de elementos y una contraseña, y retorna True si alguno de los elementos de la lista está en la contraseña, y False en caso contrario.
    '''
    for element in list_of_element:
        if element in password:
            return True
    return False

def check_password_requirements(password, numbers, specials_character, uppercase_letters):
    password_length= False
    is_number_found = contains_element(numbers, password) # Se llama a la función contains_element para verificar si hay un número en la contraseña
    is_special_character_found = contains_element(specials_character, password) # Se llama a la función contains_element para verificar si hay un caracter especial en la contraseña
    is_uppercase_found = contains_element(uppercase_letters, password) # Se llama a la función contains_element para verificar si hay una mayúscula en la contraseña

    if len (password)>=8:
        password_length =True

    return is_number_found, is_special_character_found, is_uppercase_found, password_length # Se retornan los valores de las variables que indican si se cumplieron los requisitos de la contraseña


numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
specials_character = ["+", "/", "@", "#", "$", "%", "&", "*", "!", "?"]
dictionary_of_uppercase_letters = {
    "uppercase_letters": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
}

while True:
    password_characters= 8
    password_name = input("Ingrese su contraseña. Debe tener mínimo 8 caracteres, incluye mayúsula, caracter especial y número: ")
    is_number_found, is_special_character_found, is_uppercase_found,is_password_length = check_password_requirements(
        password_name, numbers, specials_character, dictionary_of_uppercase_letters[
            "uppercase_letters"]
    )

    if is_number_found and is_special_character_found and is_uppercase_found and is_password_length:
        print("Tu contraseña es correcta.")
        break
    else:
        if not is_number_found:
            print("No te olvides de colocar un número.")
        if not is_special_character_found:
            print("No te olvides de colocar un caracter especial.")
        if not is_uppercase_found:
            print("No te olvides de colocar una mayúscula.")
        if not is_password_length:
            print(f"La contraseña debe tener mínimo {password_characters} caracteres.")
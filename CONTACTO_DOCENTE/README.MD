<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verificación de Requisitos de Contraseña</title>
</head>
<body>
    <h1>Verificación de Requisitos de Contraseña</h1>
    <p>Este script está diseñado para verificar si una contraseña cumple con ciertos requisitos de seguridad. A continuación, se proporciona una descripción detallada de las funciones, variables y el flujo del programa.</p>
    <h2>Funciones</h2>
    <ol>
        <li>
            <strong>contains_element(list_of_element, password)</strong>
            <ul>
                <li><strong>Descripción:</strong> Esta función recibe una lista de elementos y una contraseña, y verifica si alguno de los elementos de la lista está presente en la contraseña.</li>
                <li><strong>Parámetros:</strong>
                    <ul>
                        <li><code>list_of_element</code>: Lista de elementos a verificar (por ejemplo, números, caracteres especiales, letras mayúsculas).</li>
                        <li><code>password</code>: La contraseña que se va a verificar.</li>
                    </ul>
                </li>
                <li><strong>Retorno:</strong> Retorna <code>True</code> si alguno de los elementos de la lista está en la contraseña, <code>False</code> en caso contrario.</li>
            </ul>
        </li>
        <li>
            <strong>check_password_requirements(password, numbers, specials_character, uppercase_letters)</strong>
            <ul>
                <li><strong>Descripción:</strong> Esta función verifica si la contraseña cumple con los siguientes requisitos:
                    <ul>
                        <li>Contiene al menos un número.</li>
                        <li>Contiene al menos un carácter especial.</li>
                        <li>Contiene al menos una letra mayúscula.</li>
                        <li>Tiene una longitud mínima de 8 caracteres.</li>
                    </ul>
                </li>
                <li><strong>Parámetros:</strong>
                    <ul>
                        <li><code>password</code>: La contraseña que se va a verificar.</li>
                        <li><code>numbers</code>: Lista o tupla de números permitidos.</li>
                        <li><code>specials_character</code>: Lista de caracteres especiales permitidos.</li>
                        <li><code>uppercase_letters</code>: Lista de letras mayúsculas permitidas.</li>
                    </ul>
                </li>
                <li><strong>Retorno:</strong> Retorna cuatro valores booleanos indicando si cada uno de los requisitos se cumple (<code>is_number_found</code>, <code>is_special_character_found</code>, <code>is_uppercase_found</code>, <code>password_length</code>).</li>
            </ul>
        </li>
    </ol>
    <h2>Variables</h2>
    <ul>
        <li><code>numbers</code>: Tupla que contiene los números del 0 al 9.</li>
        <li><code>specials_character</code>: Lista de caracteres especiales permitidos, como <code>+</code>, <code>/</code>, <code>@</code>, <code>#</code>, <code>$</code>, <code>%</code>, <code>&</code>, <code>*</code>, <code>!</code>, <code>?</code>.</li>
        <li><code>dictionary_of_uppercase_letters</code>: Diccionario que contiene una lista de letras mayúsculas bajo la clave <code>"uppercase_letters"</code>.</li>
    </ul>
    <h2>Flujo del Programa</h2>
    <ol>
        <li>
            <strong>Entrada del Usuario:</strong>
            <p>El programa solicita al usuario que ingrese una contraseña con el mensaje: "Ingrese su contraseña. Debe tener mínimo 8 caracteres, incluye mayúsula, caracter especial y número".</p>
        </li>
        <li>
            <strong>Verificación de Requisitos:</strong>
            <p>La contraseña ingresada se verifica llamando a la función <code>check_password_requirements</code>, que utiliza la función <code>contains_element</code> para comprobar la presencia de números, caracteres especiales y letras mayúsculas.</p>
            <p>También se verifica que la longitud de la contraseña sea de al menos 8 caracteres.</p>
        </li>
        <li>
            <strong>Resultados de la Verificación:</strong>
            <p>Si la contraseña cumple con todos los requisitos, se imprime el mensaje "Tu contraseña es correcta." y el programa termina.</p>
            <p>Si la contraseña no cumple con alguno de los requisitos, se informa al usuario qué falta:</p>
            <ul>
                <li>Si no contiene un número, se imprime "No te olvides de colocar un número."</li>
                <li>Si no contiene un carácter especial, se imprime "No te olvides de colocar un caracter especial."</li>
                <li>Si no contiene una letra mayúscula, se imprime "No te olvides de colocar una mayúscula."</li>
                <li>Si no tiene la longitud mínima, se imprime "La contraseña debe tener mínimo 8 caracteres."</li>
            </ul>
        </li>
        <li>
            <strong>Repetición:</strong>
            <p>El programa sigue solicitando una nueva contraseña hasta que se cumplan todos los requisitos.</p>
        </li>
    </ol>
</body>
</html>



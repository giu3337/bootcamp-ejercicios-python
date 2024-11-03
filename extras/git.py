# git

# git init
# git add . # or git add <file>
# git commit -m "first commit"
# git remote add origin
# git push -u origin master
# git pull origin master # git pull <remote> <branch> 
# git clone <url>
# git branch <branch>


""" Ejercicio: Calculadora de Propina
Escribe un programa que calcule cuánto debes dejar de propina en un restaurante según el total de la cuenta y el porcentaje de propina deseado.

Instrucciones
Pide al usuario que ingrese el total de la cuenta (por ejemplo, $50).
Pide al usuario que ingrese el porcentaje de propina que le gustaría dejar (por ejemplo, 15 para el 15%).
Calcula el valor de la propina multiplicando el total de la cuenta por el porcentaje de propina dividido por 100.
Muestra el monto de la propina y el total a pagar (total de la cuenta + propina).
Ejemplo de Ejecución
yaml
Copy code
Ingrese el total de la cuenta: 50
Ingrese el porcentaje de propina: 15
La propina es de: $7.5
El total a pagar es de: $57.5
Este ejercicio te ayudará a practicar:

Conversión de tipos (con float).
Operaciones matemáticas básicas.
Formateo de cadenas para mostrar resultados.
Pruébalo y dime si necesitas ayuda en algún paso!



total_de_la_cuenta = int(input("Ingrese el total de la cuenta:"))
porcentaje_de_la_propina = int(input("Ingrese el porcentaje de propina:"))

valor_propina = float((porcentaje_de_la_propina * total_de_la_cuenta) / 100)

total_a_pagar = float(total_de_la_cuenta + valor_propina)

print(f"La propina es de: ${valor_propina}")
print(f"El total a pagar es de: ${total_a_pagar}")


 """



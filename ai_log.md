# Interacción 1
## Modo: 
ASK
## Pregunta: 
¿Cómo puedo agregar una verificación para detectar carácteres distintos a A, T, G y C? Además de que al detectar un caracter inválido me muestre un mensaje. 
### Sugerencia: 
#### Verificación de caracteres válidos
invalid_chars = []
for char in dna_sequence:
    if char not in ['A', 'T', 'G', 'C']:
        invalid_chars.append(char)

if invalid_chars:
    unique_invalid = set(invalid_chars)
    print(f"Caracteres inválidos detectados: {', '.join(unique_invalid)}")
## Aprendí: 
Que se crea una lista para almacenar los caracteres inválidos, en el bucle del for, recorre la secuencia de dna en busca de estos caracteres inválidos, si hay inválidos elimina los duplicados con set (así si hay varios del mismo solo muestra qué caracter es) e imprime los caracteres inválidos que se encontraron. 
Si no hay algún inválido, hace los conteos que tenía en un principio. 

# Interacción 2 
## Modo: 
Ask 
## Pregunta: 
¿Cómo puedo hacer para que el resultado tenga dos decimales?
### Sugerencia: 
print(f"GC content: {gc_content:.2f}%")
## Aprendí 
Recordé lo que se explicó durante la clase 
: inicia el formato
.2 indica 2 decimales
f indica número tipo float

# Interacción 3 
## Modo 
Ask
## Pregunta: 
 ¿cómo puedo hacer para que al no meter nada me de 0?
 ### Sugerencia
 Longitud
length = len(dna_sequence)

Cálculo GC
if length == 0:
    gc_content = 0
else:
    gc_content = (count_g + count_c) / length * 100
Output
print(f"GC content: {gc_content:.2f}%")

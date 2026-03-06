# Interacción 1
## Modo: 
ASK
## Pregunta: 
¿Cómo puedo agregar una verificación para detectar carácteres distintos a A, T, G y C? Además de que al detectar un caracter inválido me muestre un mensaje. 
### Sugerencia: 
 Verificación de caracteres válidos
invalid_chars = []
for char in dna_sequence:
    if char not in ['A', 'T', 'G', 'C']:
        invalid_chars.append(char)

if invalid_chars:
    unique_invalid = set(invalid_chars)
    print(f"Caracteres inválidos detectados: {', '.join(unique_invalid)}")
else:
    # Conteos
    count_a = dna_sequence.count("A")
    count_t = dna_sequence.count("T")
    count_g = dna_sequence.count("G")
    count_c = dna_sequence.count("C")
## Aprendí: 

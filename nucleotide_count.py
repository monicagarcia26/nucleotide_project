# Hardcoded sequence
dna_sequence = " atcg "

# Limpieza
dna_sequence = dna_sequence.strip()
dna_sequence = dna_sequence.upper()

# Verificación de caracteres válidos
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

    # Longitud
    length = count_a + count_t + count_g + count_c

    # Output
    print(f"Longitud= {length}")
    print(f"A= {count_a} " )
    print(f"T= {count_t} " )
    print(f"G= {count_g} " )
    print(f"C= {count_c} " )
# Hardcoded sequence
dna_sequence = ""

# Limpieza
dna_sequence = dna_sequence.strip()
dna_sequence = dna_sequence.upper()

# Conteos
count_g = dna_sequence.count("G")
count_c = dna_sequence.count("C")

# Longitud
length = len(dna_sequence)

# Cálculo GC
if length == 0:
    gc_content = 0
else:
    gc_content = (count_g + count_c) / length * 100

# Output
print(f"GC content: {gc_content:.2f}%")
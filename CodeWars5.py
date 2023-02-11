# Generate the complementary side of DNA segment being A=T and C=G. (7 kyu)

def DNA_strand(dna):
    dict = {"A": "T", "T":"A","C":"G","G":"C"}
    complement = ""
    for char in dna:
        complement += dict[char]
    return complement    
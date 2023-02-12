# Generate the complementary side of DNA segment being A=T and C=G. (7 kyu)

def DNA_strand(dna):
    dict = {"A": "T", "T":"A","C":"G","G":"C"}
    complement = ""
    for char in dna:
        complement += dict[char]
    return complement    

# It can be resolved using dna.translate(string.maketrans("ATCG","TAGC")).
# .maketrans() creates an equivalence table and .translate uses that table to replace it.
# I saw this solution after completing the exercice and It's really interesting for future purpouses.
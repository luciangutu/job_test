# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

def DNA_strand(dna):
    final = []
    for c in [*dna]:
        if c == 'A':
            final.append('T')
        elif c == 'T':
            final.append('A')
        elif c == 'G':
            final.append('C')
        elif c == 'C':
            final.append('G')
    return ''.join(final)

# solution by others
# def DNA_strand(dna):
#     reference = { "A":"T",
#                   "T":"A",
#                   "C":"G",
#                   "G":"C"
#                   }
#     return "".join([reference[x] for x in dna])

# import string
# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG","TAGC"))


print(DNA_strand('GTAT'))
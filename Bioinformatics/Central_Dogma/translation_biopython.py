from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# Translating from mRNA
messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG", IUPAC.unambiguous_rna)
messenger_rna.translate()

# Translating from DNA directly
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
coding_dna.translate()

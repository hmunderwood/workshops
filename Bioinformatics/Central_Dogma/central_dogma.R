source("https://bioconductor.org/biocLite.R")
biocLite()
biocLite("Biostrings")
library(Biostrings)

# Create a DNAString 
d <- DNAString("ATCGATCGATCG")

# Count how many As, Gs, Cs, and Ts are in the DNA string
alphabetFrequency(d)

# Transcribe the DNAString into an RNAString r
r <- RNAString(d)

# Translate the RNA into protein p
p <- translate(r, genetic.code=GENETIC_CODE, if.fuzzy.codon="error")
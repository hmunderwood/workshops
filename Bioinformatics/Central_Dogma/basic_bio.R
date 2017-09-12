#install.packages('seqinr')
library("seqinr")
dengue <- read.fasta(file = 'dengue.fasta')

# Store the sequence in the dengueseq variable
dengueseq <- dengue[[1]]

# Count how many a, g, c, t in the sequence
table(dengueseq)

# Get the GC content of the sequence
GC(dengueseq)


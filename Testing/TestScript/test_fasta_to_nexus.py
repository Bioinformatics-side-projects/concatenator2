from fasta_to_.class_fasta import fasta_converter

f = fasta_converter("Testing/TestFilesInput/testfasta.fasta","fasta","nexus","no")

def test_fasta_to_nexus1():
    result = "#Nexus\n\nBEGIN DATA;\nDIMENSIONS NTAX=3 " \
             "NCHAR=427;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;" \
             "\nMATRIX\n" \
             "   IADE3 -accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc\n" \
             "   IGRA5 -accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc\n" \
             "Podarcis -nnnnnactatgctaagccctgaacattgatagttactaatacaatactttccgccagagaactacaagtgaaaaacttaaaactcaaaggacttgacggtgtcccata-tcggcctagaggagcctgtcctataatcgatattccccgctccacccaacctcaactagcaag-tattcagcctatataccgccgtcga-cagtttaccctatgaaggcctaatagtagacacaatag----ccttaacgctaatacgtcaggtcaaggtgtagcaaatgttgaggaagagattggctacattttttatgataaaaaatacgaattgcactatg--aaatactgcatgaaggcgaatttagtagtaaaacagataagagtgtctgttttaacaacgctctgggacgcgtacacnnnnnnnnnnnnnn\n" \
             "  ;\nEND;\n\n" \
             "begin mrbayes;\n  set autoclose=yes nowarn=yes quitonerror=no;\n" \
             "  mcmcp ngen=10 printfre=1000 samplefreq=100 diagnfre=1000" \
             " nchains=4 savebrlens=yes filename=MyRun01;\n" \
             "  mcmc;" \
             "  sumt filename=MyRun01;\n" \
             "end;"

    assert result == f.fasta_to_nexus()

def test_fasta_to_nexus2():
    certains = ["#Nexus","end;","MATRIX","IADE3 -accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc"]

    for i in certains:
        assert i in f.fasta_to_nexus()

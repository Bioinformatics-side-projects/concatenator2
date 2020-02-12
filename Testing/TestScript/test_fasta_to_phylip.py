from fasta_to_.class_fasta import fasta_converter

f = fasta_converter("testfasta.fasta","fasta","phylip","no")

def test_fasta_to_phylip1():
    result = "3 427 s\n\n" \
             "   IADE3 -accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc\n" \
             "   IGRA5 -accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc\n" \
             "Podarcis -nnnnnactatgctaagccctgaacattgatagttactaatacaatactttccgccagagaactacaagtgaaaaacttaaaactcaaaggacttgacggtgtcccata-tcggcctagaggagcctgtcctataatcgatattccccgctccacccaacctcaactagcaag-tattcagcctatataccgccgtcga-cagtttaccctatgaaggcctaatagtagacacaatag----ccttaacgctaatacgtcaggtcaaggtgtagcaaatgttgaggaagagattggctacattttttatgataaaaaatacgaattgcactatg--aaatactgcatgaaggcgaatttagtagtaaaacagataagagtgtctgttttaacaacgctctgggacgcgtacacnnnnnnnnnnnnnn\n"

    assert result == f.fasta_to_phylip()

def test_fasta_to_phylip2():
    certains = ["3", "427", "s","IADE3 -accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc"]

    for i in certains:
        assert i in f.fasta_to_phylip()





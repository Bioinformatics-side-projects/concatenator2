from fasta_to_.class_fasta import fasta_converter

def test_fast_main():
    f = fasta_converter("Testing/TestFilesInput/testfasta.fasta","fasta","nexus","no")

    sequence = {"IADE3":"-accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc",
                "IGRA5":"-accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc",
                "Podarcis":"-nnnnnactatgctaagccctgaacattgatagttactaatacaatactttccgccagagaactacaagtgaaaaacttaaaactcaaaggacttgacggtgtcccata-tcggcctagaggagcctgtcctataatcgatattccccgctccacccaacctcaactagcaag-tattcagcctatataccgccgtcga-cagtttaccctatgaaggcctaatagtagacacaatag----ccttaacgctaatacgtcaggtcaaggtgtagcaaatgttgaggaagagattggctacattttttatgataaaaaatacgaattgcactatg--aaatactgcatgaaggcgaatttagtagtaaaacagataagagtgtctgttttaacaacgctctgggacgcgtacacnnnnnnnnnnnnnn"}

    assert sequence == f.sequence

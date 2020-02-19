from class_concatenator import concatenator
from filecmp import cmp

test_list_dict = [{"IADE3":"-accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc",
              "IGRA5":"-accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc",
              "Podarcis":"-nnnnnactatgctaagccctgaacattgatagttactaatacaatactttccgccagagaactacaagtgaaaaacttaaaactcaaaggacttgacggtgtcccata-tcggcctagaggagcctgtcctataatcgatattccccgctccacccaacctcaactagcaag-tattcagcctatataccgccgtcga-cagtttaccctatgaaggcctaatagtagacacaatag----ccttaacgctaatacgtcaggtcaaggtgtagcaaatgttgaggaagagattggctacattttttatgataaaaaatacgaattgcactatg--aaatactgcatgaaggcgaatttagtagtaaaacagataagagtgtctgttttaacaacgctctgggacgcgtacacnnnnnnnnnnnnnn"},
             {"IADE3":"-accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc",
              "Podarcis":"-nnnnnactatgctaagccctgaacattgatagttactaatacaatactttccgccagagaactacaagtgaaaaacttaaaactcaaaggacttgacggtgtcccata-tcggcctagaggagcctgtcctataatcgatattccccgctccacccaacctcaactagcaag-tattcagcctatataccgccgtcga-cagtttaccctatgaaggcctaatagtagacacaatag----ccttaacgctaatacgtcaggtcaaggtgtagcaaatgttgaggaagagattggctacattttttatgataaaaaatacgaattgcactatg--aaatactgcatgaaggcgaatttagtagtaaaacagataagagtgtctgttttaacaacgctctgggacgcgtacacnnnnnnnnnnnnnn",
              "IBAR1":"nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn-nnnnnnnnnnnnnnnnnnnnnnnaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccctcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagcccccccccccgctaatacgtcaggtcaaggtgtagcttatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",
              "ISMA5":"-accccactatgctaagccataaatattgatagata-aaatacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcccgtcctataatcgataccccacgttttacctcaccctcactagcactaaacccagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatag-----ccccccactaatacgtcaggtcaaggtgtagcttatgtgatggaagagattggctacattttttatattaaaaaacacggaatgctccatg--aaaaacaacatgaaggcgaatttagtagtaagacagacaagagagtctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc"}]

test_len = [427,427]

def test_concat_main():
    t = concatenator(test_list_dict,test_len,'')

    result = {"IADE3":"-accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc-accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc",
               "IGRA5":"-accccactatgctaagccataaatattgatagata-aattacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccatcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagc---cctccccgctaatacgtcaggtcaaggtgtagctcatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtaagacagacaagagaacctgtcttaataatgctctgggacgcgcacacaccgcccgtcacccNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
            "Podarcis":"-nnnnnactatgctaagccctgaacattgatagttactaatacaatactttccgccagagaactacaagtgaaaaacttaaaactcaaaggacttgacggtgtcccata-tcggcctagaggagcctgtcctataatcgatattccccgctccacccaacctcaactagcaag-tattcagcctatataccgccgtcga-cagtttaccctatgaaggcctaatagtagacacaatag----ccttaacgctaatacgtcaggtcaaggtgtagcaaatgttgaggaagagattggctacattttttatgataaaaaatacgaattgcactatg--aaatactgcatgaaggcgaatttagtagtaaaacagataagagtgtctgttttaacaacgctctgggacgcgtacacnnnnnnnnnnnnnn-nnnnnactatgctaagccctgaacattgatagttactaatacaatactttccgccagagaactacaagtgaaaaacttaaaactcaaaggacttgacggtgtcccata-tcggcctagaggagcctgtcctataatcgatattccccgctccacccaacctcaactagcaag-tattcagcctatataccgccgtcga-cagtttaccctatgaaggcctaatagtagacacaatag----ccttaacgctaatacgtcaggtcaaggtgtagcaaatgttgaggaagagattggctacattttttatgataaaaaatacgaattgcactatg--aaatactgcatgaaggcgaatttagtagtaaaacagataagagtgtctgttttaacaacgctctgggacgcgtacacnnnnnnnnnnnnnn",
               "IBAR1":"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn-nnnnnnnnnnnnnnnnnnnnnnnaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcctgtcctataatcgataccccacgttttacctcaccctcactagcact-aactcagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatagcccccccccccgctaatacgtcaggtcaaggtgtagcttatgtgacggaagagattggctacattttttatattaaaaaacacggaatgctacatg--aaaaataacatgaaggcgaatttagtagtnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",
               "ISMA5":"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN-accccactatgctaagccataaatattgatagata-aaatacaatactttccgccagagaactacaagtgaaaaacttgaaactcaaaggacttggcggtgtcccacattcagcctagaggagcccgtcctataatcgataccccacgttttacctcaccctcactagcactaaacccagcctatataccgccgtcga-cagcttaccccatgagggaaaaatagtaagcaaaatag-----ccccccactaatacgtcaggtcaaggtgtagcttatgtgatggaagagattggctacattttttatattaaaaaacacggaatgctccatg--aaaaacaacatgaaggcgaatttagtagtaagacagacaagagagtctgtcttaataatgctctgggacgcgcacacaccgcccgtcaccc"}

    assert t.taxa == 5 and t.main_dict == result and t.lenght == 854 and t.b_taxa == 'Podarcis'

def test_concat_fasta():
    f = concatenator(test_list_dict, test_len, 'fasta')

    assert cmp("concat.fasta","Testing/TestFilesOutput/concatTest.fasta",shallow=False)

def test_concat_fasta():
    n = concatenator(test_list_dict, test_len, 'nexus')

    assert cmp("concat.nex","Testing/TestFilesOutput/concatNexus.nex",shallow=False)

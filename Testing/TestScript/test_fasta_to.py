from fasta_to_.class_fasta import fasta_converter
import filecmp

def test_fasta_to_nexus():
    f = fasta_converter("Testing/TestFilesInput/testfasta.fasta", "fasta", "nexus", "no")

    assert filecmp.cmp('Testing/TestFilesInput/testfasta.nex','Testing/TestFilesOutput/testfastaToNex.nex',shallow=False)

def test_fasta_to_phylip():
    f = fasta_converter("Testing/TestFilesInput/testfasta.fasta", "fasta", "phylip", "no")

    assert filecmp.cmp('Testing/TestFilesInput/testfasta.phy','Testing/TestFilesOutput/testfastaToPhy.phy',shallow=False)

def test_fasta_to_aln():
    f = fasta_converter("Testing/TestFilesInput/testfasta.fasta", "fasta", "aln", "no")

    assert filecmp.cmp('Testing/TestFilesInput/testfasta.aln','Testing/TestFilesOutput/testfastaToAln.aln',shallow=False)

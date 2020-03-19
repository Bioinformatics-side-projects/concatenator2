from aln_to_.aln_to__class_converter_aln import aln_converter
import filecmp



def test_aln_to_fasta():
    a = aln_converter('Testing/TestFilesInput/testAln.aln', 'fasta', 'no')

    assert filecmp.cmp('Testing/TestFilesInput/testAln.fasta','Testing/TestFilesOutput/testAlntoFasta.fasta', shallow=False)

def test_aln_to_nexus():
    a = aln_converter('Testing/TestFilesInput/testAln.aln', 'nexus', 'no')

    assert filecmp.cmp('Testing/TestFilesInput/testAln.nex','Testing/TestFilesOutput/testAlntoNexus.nex', shallow=False)

def test_aln_to_phylip():
    a = aln_converter('Testing/TestFilesInput/testAln.aln', 'phylip', 'no')

    assert filecmp.cmp('Testing/TestFilesInput/testAln.phy','Testing/TestFilesOutput/testAlntoPhylip.phy', shallow=False)
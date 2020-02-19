from nexus_to_.class_nexus import nexus_converter
import filecmp



def test_nexus_to_fasta():
    n = nexus_converter('Testing/TestFilesInput/testNexus.nex', 'nexus', 'fasta', 'no')

    assert filecmp.cmp('Testing/TestFilesInput/testNexus.fasta','Testing/TestFilesOutput/testNexusToFasta.fasta', shallow=False)

def test_nexus_to_phylip():
    n = nexus_converter('Testing/TestFilesInput/testNexus.nex', 'nexus', 'phylip', 'no')

    assert filecmp.cmp('Testing/TestFilesInput/testNexus.phy','Testing/TestFilesOutput/testNexusToPhy.phy', shallow=False)

def test_nexus_to_aln_clustal():
    n = nexus_converter('Testing/TestFilesInput/testNexus.nex', 'nexus', 'aln', 'no')

    assert filecmp.cmp('Testing/TestFilesInput/testNexus.aln','Testing/TestFilesOutput/testNexusToAln.aln', shallow=False)

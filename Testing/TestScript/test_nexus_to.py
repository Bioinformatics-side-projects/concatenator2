from nexus_to_.class_nexus import nexus_converter
import filecmp



def test_nexus_to_fasta():
    n = nexus_converter('Testing/TestFilesInput/testNexus.nex', 'nexus', 'fasta', 'no')

    assert filecmp.cmp('testNexus.fasta','Testing/TestFilesOutput/testNexustoFasta.fasta', shallow=False)

def test_nexus_to_phylip():
    n = nexus_converter('Testing/TestFilesInput/testNexus.nex', 'nexus', 'phylip', 'no')

    assert filecmp.cmp('testNexus.phy','Testing/TestFilesOutput/testNexustoPhy.phy', shallow=False)

def test_nexus_to_aln_clustal():
    n = nexus_converter('Testing/TestFilesInput/testNexus.nex', 'nexus', 'aln', 'no')

    assert filecmp.cmp('testNexus.aln','Testing/TestFilesOutput/testNexustoAln.aln', shallow=False)

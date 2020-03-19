from phylip_to_.class_phylip import phylip_converter
import filecmp



def test_phylip_to_fasta():
    p = phylip_converter('Testing/TestFilesInput/testPhylip.phy', 'phylip', 'fasta', 'no')

    assert filecmp.cmp('Testing/TestFilesInput/testPhylip.fasta','Testing/TestFilesOutput/testPhyliptoFasta.fasta', shallow=False)

def test_phylip_to_nexus():
    p = phylip_converter('Testing/TestFilesInput/testPhylip.phy', 'phylip', 'nexus', 'no')

    assert filecmp.cmp('Testing/TestFilesInput/testPhylip.nex','Testing/TestFilesOutput/testPhyliptoNexus.nex', shallow=False)

def test_phylip_to_aln_clustal():
    p = phylip_converter('Testing/TestFilesInput/testPhylip.phy', 'phylip', 'aln', 'no')

    assert filecmp.cmp('Testing/TestFilesInput/testPhylip.aln','Testing/TestFilesOutput/testPhyliptoAln.aln', shallow=False)
"""
 Fasta to Nexus
"""

from sys import argv
from itertools import groupby


def fasta_rearrange(fasta):
    '''
     Locates every number and sequences and puts it in a dictionary, using the fasta file as an argument.
    :param fasta: recieves the fasta file
    :return: the names of the sequences with the sequences
    '''

    with open(fasta, "r") as fasta_file:
        # searches the numbers started with >
        groups = groupby(fasta_file, key=lambda x: not x.startswith(">"))
        # creates an empty dictionary
        fasta_file = {}
        # for each value in the list, the \n is replaced with nothing
        for keys, values in groups:
            if not keys:
                key, val = list(values)[0].replace('\n', ''), "".join(map(str.rstrip, next(groups)[1]))
                # puts the values and keys in the dictionary
                fasta_file[key] = val
    # replaces > with a space
    novo = {keys.replace('>', ''): value for keys, value in fasta_file.items()}
    return novo


def cabecalho(fasta):
    '''
     Creates the beggining of the nexus files, calculating in this function the number of taxas
     :parameter fasta: recieves the sequences and their names
     :return: returns the print that contains the beggining of the nexus file
    '''

    # Calculates the number of taxas using the number of existing keys
    taxa = 0
    for value in fasta.keys():
        taxa += 1

    # Calculates the total amount of Nucleotides, Missing and Gaps that exists in the sequence
    for values in fasta.values():
        nchar = len(values)
        break

    # Makes a "print" at the star of the nexus file, that contains the information
    # before the alignment of the Nexus sequences
    start_nexus = "#Nexus\n\nBEGIN DATA;\nDIMENSIONS NTAX={} " \
                  "NCHAR={};\nFORMAT DATATYPE=DNA MISSING=N GAP=-;" \
                  "\nMATRIX\n".format(taxa, nchar)

    return start_nexus


def seq_writter(fasta):
    '''
     Aligns all sequences
     :param fasta: Recieves the number of sequences and their names
     :return: Returns the aligned sequence
    '''

    sequences = ""

    #The variable "maior" will recieve the biggest name of all the sequences
    #If the name is bigger than 99 char, everything after that will be cut

    maior = ""
    for k in fasta.keys():
        if len(k) > len(maior):
            maior = k
        if len(maior) >= 99:
            maior = maior[:99]

    # Checks all names and sequences and if the name is over 99 char, cuts everything in front
    # Aligns all names and sequences

    for k, var in fasta.items():
        if len(k) >= 99:
            k = k[:98]
        qualquer = len(maior) - 1
        tamanho = qualquer - len(k)
        sequences += " "*tamanho + "{} {}".format(k, var) + "\n"

    return sequences


def mrbayes_blockwriter(ngen):
    '''
        Recieves the argument ngen (integer).
	Returns a variable with the final text to include in the nexus file.
        :param ngen: recieves the variable ngen, in the integer
        :return: returns the variable with the final text
    '''
    end = "  ;\nEND;\n\n"

    # puts in a variable, the following string
    mrbayes = "begin mrbayes;\n  set autoclose=yes nowarn=yes quitonerror=no;\n" \
              "  mcmcp ngen={} printfre=1000 samplefreq=100 diagnfre=1000" \
              " nchains=4 savebrlens=yes filename=MyRun01;\n" \
              "  mcmc;" \
              "  sumt filename=MyRun01;\n" \
              "end;".format(ngen)

    #joins both strings in a variable
    mrbayes_final = end + mrbayes

    return mrbayes_final


if __name__ == '__main__':
    # obtains the variables inputed from the user
    FASTA_FILE_FROM_USER = argv[1]
    NGEN = argv[2]

    DKV = fasta_rearrange(FASTA_FILE_FROM_USER)
    # runs the module 'divide_keys_values', while running the function'fasta_rearrange'
    # while using the fasta file from input

    with open("nexus_file.nex", "w+") as NEXUS_FILE:
    # creates a nexus file
     NEXUS_FILE.write(cabecalho(DKV) + seq_writter(DKV) + mrbayes_blockwriter(NGEN))


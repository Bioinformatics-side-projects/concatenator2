from sys import argv
from itertools import groupby


def fasta_rearrange(fasta):
    '''
     Locates every number and sequences and puts it in a dictionary, using the fasta file as an argument.
    :param fasta: recieves the fasta file
    :return: the names of the sequences with the sequences
    '''
    print(fasta)
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


def phylip_seq(fasta):
    taxa = 0
    maior = ""
    sequencia = ""

    for k in fasta.keys():
        if len(k) > len(maior):
            maior = k
  
    for k,v in fasta.items():
        taxa+=1
        nchar = len(v)
        tamanho = len(maior) - len(k)
        sequencia += " "*tamanho + "{} {}\n".format(k,v)

    sequence = "{} {} s\n\n{}".format(taxa,nchar,sequencia)
    return sequence


if __name__ == '__main__':
    # obtains the variables inputed from the user
    FASTA_FILE_FROM_USER = argv[1]
    
    DKV = fasta_rearrange(FASTA_FILE_FROM_USER)
    with open("phylip_file.rphylips", "w+") as phylip_file:
     phylip_file.write(phylip_seq(DKV))

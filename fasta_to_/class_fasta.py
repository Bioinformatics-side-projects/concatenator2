#input file, the type of file, type of output, number of taxa, lenght of each sequence, if concatenates or not
#number of generatios is 10 for now, but later it will have changes

class fasta_converter:

    def __init__(self,file,fast,out,concat):
        self.file = file
        self.input = fast
        self.output = out
        self.taxa = 0
        self.lenght = 0
        self.sequence = {}
        self.concat = concat
        self.fasta_rearrange()

    def fasta_rearrange(self):
            name, seq = "", ""
            with open(self.file, "r") as fasta_file:
              line = fasta_file.readline().rstrip()
              while line:
                  if line.startswith(">") and name == "":
                     name = line
                     self.taxa+=1
                  elif line.startswith(">"):
                      self.sequence[name.replace(">","")] = seq
                      name = line
                      seq = ""
                      self.taxa+=1
                  else:
                      seq+=line
                  line = fasta_file.readline().rstrip()
              self.sequence[name.replace(">","")] = seq
              self.lenght = len(seq)
            return

    def fasta_to_nexus(self):

        biggest,seq = "",""
        for k in self.sequence.keys():
            if len(k) > len(biggest):
                biggest = k
            if len(biggest) >= 99:
                biggest = biggest[:99]

        for k, var in self.sequence.items():
            if len(k) >= 99:
                k = k[:99]
            tamanho = len(biggest) - len(k)
            seq += " " * tamanho + "{} {}".format(k, var) + "\n"

        if self.concat == 'yes':
            return seq

        else:
            nexus ="#Nexus\n\nBEGIN DATA;\nDIMENSIONS NTAX={} " \
                          "NCHAR={};\nFORMAT DATATYPE=DNA MISSING=N GAP=-;" \
                          "\nMATRIX\n" \
                          "{}" \
                          "  ;\nEND;\n\n" \
                          "begin mrbayes;\n  set autoclose=yes nowarn=yes quitonerror=no;\n" \
                          "  mcmcp ngen={} printfre=1000 samplefreq=100 diagnfre=1000" \
                          " nchains=4 savebrlens=yes filename=MyRun01;\n" \
                          "  mcmc;" \
                          "  sumt filename=MyRun01;\n" \
                          "end;".format(self.taxa,self.lenght,seq,10)

            return nexus

    def fasta_to_phylip(self):
        biggest = ""
        seq = ""

        for k in self.sequence.keys():
            if len(k) > len(biggest):
                biggest = k

        for k, v in self.sequence.items():
            size = len(biggest) - len(k)
            seq += " " * size + "{} {}\n".format(k, v)

        if self.concat == 'yes':
            return seq

        else:
            return "{} {} s\n\n{}".format(self.taxa, self.lenght, seq)
    
    def fasta_to_aln_clustal(self):
        #print("self.sequence==", self.sequence)
        #print(self.sequence.keys())
        #print(self.sequence.values())

        b_seq = len(sorted(self.sequence.values(), key=len)[-1])  # O tamanho da maior sequencia/value
        b_name = sorted(self.sequence.keys(), key=len)[-1]  # Otamanho na maior nome/chave

        """def funtion(nome, sequence, start, end, b_name):
            variacao = len(b_name) - len(nome)
            dist = variacao + 8
            return nome + " " * dist + sequence[start:end] + "\n"
        """

        limit = 50
        clustal = "CLUSTAL W (1.8) multiple sequence alignment (ALTER 1.3.3)\n\n\n"
        for start in range(0, b_seq, limit):
            end = start + limit
            for name, seq in self.sequence.items():
                variacao = len(b_name) - len(name)
                dist = variacao + 8
                clustal += name + " " * dist + seq[start:end] + "\n"
                # clustal += funtion(name, seq, start, end, b_name)
            clustal += "\n"
        return clustal



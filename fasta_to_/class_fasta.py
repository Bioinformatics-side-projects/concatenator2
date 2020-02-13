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
        self.b_taxa = ""
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
              self.lenght = len(sorted(self.sequence.values(), key=len)[-1])
              self.b_taxa = sorted(self.sequence.keys(), key=len)[-1]
            return

    def fasta_to_nexus(self):
        seq = ""

        for k, var in self.sequence.items():
            self.b_taxa = self.b_taxa[0:99] if len(self.b_taxa) >99 else self.b_taxa
            k = k[:99] if len(k) >= 99 else k
            size = len(self.b_taxa) - len(k)
            seq += " " * size + "{} {}".format(k, var) + "\n"

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

            return print(nexus)

    def fasta_to_phylip(self):
        seq = ""

        for k, v in self.sequence.items():
            size = len(self.b_taxa) - len(k)
            seq += " " * size + "{} {}\n".format(k, v)

        if self.concat == 'yes':
            return seq
        else:
            return print("{} {} s\n\n{}".format(self.taxa, self.lenght, seq))

    def fasta_to_aln_clustal(self):
        clustal = "CLUSTAL W\n\n"

        for start in range(0, self.lenght, 60):
            for name, seq in self.sequence.items():
                size = len(self.b_taxa) - len(name)
                clustal += " " * size + " {} {}\n".format(name,seq[start:start+60])
            clustal += "\n"
        return clustal
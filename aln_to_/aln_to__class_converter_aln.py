
class aln_converter():
    def __init__(self, file_name, concat):
        self.inside_file = open(file_name, 'r').read()
        # self.file = file// filename
        # self.input = fast//aln
        # self.output = out//qual o out
        self.taxa = 0
        self.lenght = 0
        self.sequence = {}
        self.concat = concat
        self.b_taxa = ""
        self._split_name_sequence()

    def _split_name_sequence(self):
        # print(self.inside_file.split("\n"))
        self.dict_name_seq = {}
        for line in self.inside_file.split("\n"):

            if not line.startswith("CLUSTAL W"):
                if line != "":
                    name = line.split(" ")[0]
                    seq = "".join(line.split(" ")[1:])
                    # print(name + "--" + seq)
                    if name in self.dict_name_seq.keys():
                        self.dict_name_seq[name] = self.dict_name_seq[name] + seq
                    else:
                        self.dict_name_seq[name] = seq

        print("self.dict_name_seq=", self.dict_name_seq)

    # ----------------------
    # usar no programtodo
    def _dict_to_nexus(self):
        seq = ""
        for k, var in self.dict_name_seq.items():
            self.b_taxa = self.b_taxa[0:99] if len(self.b_taxa) > 99 else self.b_taxa
            k = k[:99] if len(k) >= 99 else k
            size = len(self.b_taxa) - len(k)
            seq += " " * size + "{} {}".format(k, var) + "\n"

        nexus = "#Nexus\n\nBEGIN DATA;\nDIMENSIONS NTAX={} " \
                "NCHAR={};\nFORMAT DATATYPE=DNA MISSING=N GAP=-;" \
                "\nMATRIX\n" \
                "{}" \
                "  ;\nEND;\n\n" \
                "begin mrbayes;\n  set autoclose=yes nowarn=yes quitonerror=no;\n" \
                "  mcmcp ngen={} printfre=1000 samplefreq=100 diagnfre=1000" \
                " nchains=4 savebrlens=yes filename=MyRun01;\n" \
                "  mcmc;" \
                "  sumt filename=MyRun01;\n" \
                "end;".format(self.taxa, self.lenght, seq, 10)
        return nexus

    def aln_to_nexus(self):
        return self._dict_to_nexus()

    # ------------------
    # usar no programtodo
    def _dict_to_fasta(self):
        fasta = ""
        for name, seq in self.dict_name_seq.items():
            fasta += ">"+name+"\n"+seq+"\n\n"
        print("fasta=\n"+fasta)
        return fasta 

    def aln_to_fasta(self):
        return self._dict_to_fasta()

    # -------------------
    # usar no programtodo
    def _dict_to_phylip(self):  
        seq = ""
        for k, v in self.dict_name_seq.items():
            size = len(self.b_taxa) - len(k)
            seq += " " * size + "{} {}\n".format(k, v)
        return "{} {} s\n\n{}".format(self.taxa, self.lenght, seq)
    
    def aln_to_phylip(self):
        return self._dict_to_phylip()


if __name__ == '__main__':
    print("inicio...")
    convert = aln_converter("reln.crulsta", "yes")
    # convert._split_name_sequence()
    # convert.aln_to_nexus()
    # convert.aln_to_fasta()
    convert.aln_to_phylip()
    
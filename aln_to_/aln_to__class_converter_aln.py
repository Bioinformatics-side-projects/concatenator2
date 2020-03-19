class aln_converter():
    def __init__(self, file_name,out ,concat):
        self.file = file_name
        self.inside_file = open(file_name, 'r').read()
        # self.input = fast//aln
        self.taxa = 0
        self.lenght = 0
        self.output = out
        self.dict_name_seq = {}
        self.concat = concat
        self.b_taxa = ""
        self._split_name_sequence()
        if self.output == 'fasta':
            self.aln_to_fasta()
        elif self.output == 'nexus':
            self.aln_to_nexus()
        elif self.output == 'phylip':
            self.aln_to_phylip()

    def _split_name_sequence(self):
        for line in self.inside_file.split("\n"):
            if not line.startswith("CLUSTAL W:"):
                if line != "":
                    name = line.lstrip().split(" ")[0]
                    seq = line.lstrip().split(" ")[1]
                    if name in self.dict_name_seq.keys():
                        self.dict_name_seq[name] += seq

                    else:
                        self.dict_name_seq[name] = seq
                        self.taxa += 1
        self.lenght = len(sorted(self.dict_name_seq.values(), key=len)[-1])
        self.b_taxa = sorted(self.dict_name_seq.keys(), key=len)[-1]




    def aln_to_nexus(self):
        if self.concat == 'yes':
            return self.dict_name_seq.items()

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

        with open(self.file.replace(".aln", ".nex"), "w+") as writ:
            writ.write(nexus)

    def aln_to_fasta(self):
        if self.concat == 'yes':
            return self.dict_name_seq.items()
        fasta = ""
        for name, seq in self.dict_name_seq.items():
            fasta += ">"+name+"\n"
            for sep in range(0,self.lenght,60):
                fasta += "{}\n".format(seq[sep:sep+60])
        with open(self.file.replace(".aln", ".fasta"), "w+") as writ:
            writ.write(fasta)

    def aln_to_phylip(self):
        if self.concat == 'yes':
            return self.dict_name_seq.items()
        seq = ""

        for k, v in self.dict_name_seq.items():
            size = len(self.b_taxa) - len(k)
            seq += " " * size + "{} {}\n".format(k, v)

        phylip = "{} {} s\n\n{}".format(self.taxa, self.lenght, seq)
        with open(self.file.replace(".aln", ".phy"), "w+") as writ:
            writ.write(phylip)


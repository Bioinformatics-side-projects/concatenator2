class phylip_converter:

    def __init__(self,file,fast, out, concat):
        self.file = file
        self.input = fast
        self.output = out
        self.taxa = 0
        self.lenght = 0
        self.sequence = {}
        self.concat = concat
        self.b_taxa = ""
        self.phylip_rearrange()
        if self.output == 'fasta':
            self.phylip_to_fasta()
        elif self.output == 'nexus':
            self.phylip_to_nex()
        elif self.output == 'aln' or self.output == 'clustal':
            self.phylip_to_aln_clustal()

    def phylip_rearrange(self):
        with open(self.file, "r") as phylip_file:
            phylip_file.readline()
            line = phylip_file.readline()
            while line:
                if line != '\n':
                    self.sequence[line.lstrip().split(" ")[0]] = line.strip().split(" ")[1]
                    self.taxa +=1
                    line = phylip_file.readline()
                else:
                    line = phylip_file.readline()
            self.lenght = len(sorted(self.sequence.values(), key =len)[-1])
            self.b_taxa = sorted(self.sequence.keys(), key=len)[-1]

    def phylip_to_fasta(self):
        if self.concat == 'yes':
            return self.sequence

        fasta = ''
        for k,v in self.sequence.items():
            fasta += ">{}\n".format(k)
            for start in range(0,self.lenght,60):
                fasta += "{}\n".format(v[start:start+60])

        with open(self.file.replace('.phy','.fasta'), 'w+') as writ:
            writ.write(fasta)

    def phylip_to_nex(self):
        if self.concat == 'yes':
            seq = {}
            for k, v in self.sequence.items():

                if len(k) > 99:
                    seq[k[:99]] = self.sequence[k]
                else:
                    seq[k] = self.sequence[k]
            self.sequence = seq.copy()
            return self.sequence

        seq = ""

        for k, var in self.sequence.items():
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

        with open(self.file.replace(".phy", ".nex"), "w+") as writ:
            writ.write(nexus)

    def phylip_to_aln_clustal(self):
        if self.concat == 'yes':
            return self.sequence

        seq = 'CLUSTAL W:\n\n'
        for start in range(0,self.lenght,60):
            for k,v in self.sequence.items():
                seq += "{}{} {}\n".format(" "*(len(self.b_taxa)-len(k)),k,v[start:start+60])
            seq+='\n'

        with open(self.file.replace('.phy','.aln'),'w+') as writ:
            writ.write(seq)

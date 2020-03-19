
class concatenator:
    def __init__(self,list,listlen,output):
        self.file_list = list
        self.len_list = listlen
        self.output = output
        self.taxa = 0
        self.lenght = 0
        self.b_taxa = ''
        self.main_dict = {}
        self.create_main_dict()
        self.concat_taxas()
        if self.output == 'fasta':
            self.output_fasta()
        elif self.output == 'nexus':
            self.output_nexus()
        elif self.output == 'phylip':
            self.output_phylip()
        elif self.output == 'aln':
            self.output_aln_clustal()

    def create_main_dict(self):
        for file in self.file_list:
            for key in file.keys():
                if key not in self.main_dict:
                    self.main_dict[key] = ''
                    self.taxa += 1

    def concat_taxas(self):
        for index, file in enumerate(self.file_list):
            for key in self.main_dict.keys():
                if key not in file.keys():
                    self.main_dict[key] += 'N'*self.len_list[index]
                else:
                    self.main_dict[key] += file[key]
        self.lenght = len(sorted(self.main_dict.values(), key=len)[-1])
        self.b_taxa = sorted(self.main_dict.keys(), key=len)[-1]

    def output_fasta(self):
        seq_write = ''
        for key,value in self.main_dict.items():
            seq_write += ">{}\n".format(key)
            for start in range(0,self.lenght,60):
                seq_write+="{}\n".format(value[start:start+60])
        with open("concat.fasta", "w+") as fasta_concat:
            fasta_concat.write(seq_write)

    def output_nexus(self):
        seq = ''
        for key,value in self.main_dict.items():
            seq += '{}{} {}\n'.format(" "*(len(self.b_taxa)-len(key)),key,value)

        with open("concat.nex", "w+") as nexus_concat:
            nexus_concat.write("#Nexus\n\nBEGIN DATA;\nDIMENSIONS NTAX={} " \
                               "NCHAR={};\nFORMAT DATATYPE=DNA MISSING=N GAP=-;" \
                               "\nMATRIX\n" \
                               "{}" \
                               "  ;\nEND;\n\n" \
                               "begin mrbayes;\n  set autoclose=yes nowarn=yes quitonerror=no;\n" \
                               "  mcmcp ngen={} printfre=1000 samplefreq=100 diagnfre=1000" \
                               " nchains=4 savebrlens=yes filename=MyRun01;\n" \
                               "  mcmc;" \
                               "  sumt filename=MyRun01;\n" \
                               "end;".format(self.taxa, self.lenght, seq, 10))

    def output_phylip(self):
        seq = ''
        for key, value in self.main_dict.items():
            seq += '{}{} {}\n'.format(" " * (len(self.b_taxa) - len(key)), key, value)

        with open("concat.phy", "w+") as writ:
            writ.write("{} {} s\n\n{}".format(self.taxa, self.lenght, seq))

    def output_aln_clustal(self):
        clustal = "CLUSTAL W:\n\n"

        for start in range(0, self.lenght, 60):
            for name, seq in self.main_dict.items():
                size = len(self.b_taxa) - len(name)
                clustal += " " * size + "{} {}\n".format(name, seq[start:start + 60])
            clustal += "\n"

        with open("concat.aln", "w+") as writ:
            writ.write(clustal)





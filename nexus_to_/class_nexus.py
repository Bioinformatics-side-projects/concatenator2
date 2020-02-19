
class nexus_converter:

    def __init__(self,file,fast, out, concat):
        self.file = file
        self.input = fast
        self.output = out
        self.taxa = 0
        self.lenght = 0
        self.sequence = {}
        self.concat = concat
        self.b_taxa = ""
        self.nexus_rearrange()
        if self.output == 'fasta':
            self.nexus_to_fasta()
        elif self.output == 'phylip':
            self.nexus_to_phylip()
        elif self.output == 'aln' or self.output == 'clustal':
            self.nexus_to_aln_clustal()

    def nexus_rearrange(self):
        line = ""
        with open(self.file, "r") as nexus_file:
            while 'MATRIX' not in line:
                line = nexus_file.readline()
            line = nexus_file.readline()
            while ';' not in line:
                self.taxa +=1
                self.sequence[line.strip().split(' ')[0]] = line.strip().split(' ')[1]
                line = nexus_file.readline()
            self.lenght = len(sorted(self.sequence.values(), key=len)[-1])
            self.b_taxa = sorted(self.sequence.keys(), key=len)[-1]

    def nexus_to_fasta(self):
        if self.concat == 'yes':
            return self.sequence

        fasta = ''
        for k,v in self.sequence.items():
            fasta += ">{}\n".format(k)
            for start in range(0,self.lenght,60):
                fasta += "{}\n".format(v[start:start+60])
        with open(self.file.replace('.nex','.fasta'), 'w+') as writ:
            writ.write(fasta)

    def nexus_to_phylip(self):
        if self.concat == 'yes':
            return self.sequence

        seq ='{} {} s\n\n'.format(self.taxa, self.lenght)
        for k,v in self.sequence.items():
            seq+="{}{} {}\n".format(" "*(len(self.b_taxa)-len(k)),k,v)

        with open(self.file.replace('.nex','.phy'), 'w+') as writ:
            writ.write(seq)

    def nexus_to_aln_clustal(self):
        if self.concat == 'yes':
            return self.sequence

        seq = 'CLUSTAL W:\n\n'
        for start in range(0,self.lenght,60):
            for k,v in self.sequence.items():
                seq += "{}{} {}\n".format(" "*(len(self.b_taxa)-len(k)),k,v[start:start+60])
            seq+='\n'

        with open(self.file.replace('.nex','.aln'),'w+') as writ:
            writ.write(seq)




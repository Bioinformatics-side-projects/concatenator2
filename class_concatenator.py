
class concatenator:
    def __init__(self,list,listlen,output):
        self.file_list = list
        self.len_list = listlen
        self.output = output
        self.main_dict = {}
        self.create_main_dict()
        self.concat_taxas()
        if self.output == 'fasta':
            self.output_fasta()

    def create_main_dict(self):
        for file in self.file_list:
            for key in file.keys():
                if key not in self.main_dict:
                    self.main_dict[key] = ''
        return

    def concat_taxas(self):
        for index, file in enumerate(self.file_list):
            for key in self.main_dict.keys():
                if key not in file.keys():
                    self.main_dict[key] += 'N'*self.len_list[index]
                else:
                    self.main_dict[key] += file[key]
        return

    def output_fasta(self):
        seq_write = ''
        for key,value in self.main_dict.items():
            seq_write+="{}\n{}\n\n".format(key,value)
        with open("concat.fasta", "w+") as fasta_concat:
            fasta_concat.write(seq_write)
        return

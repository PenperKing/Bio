# from Bio import Entrez
# Entrez.email = '1227964378@qq.com'
# handle = Entrez.esearch(db='Gene',term='Hmoxl')
# record = Entrez.read(handle)
# print(record)
from Bio import Entrez
import pandas as pd
from Bio import SeqIO
import os
Entrez.email = "1227964378@qq.com"
wb = pd.read_csv("all_data.txt", sep='\t')
id_str = ""
name_group = []
for rol in wb.values:
    if pd.isna(rol[0]):
        print(rol[1])
    else:
        name_group.append(rol[1])
        id_str = id_str + " " + str(rol[0])

handle = Entrez.efetch(db="nucleotide",id=id_str,rettype='fasta')
fastas = list(SeqIO.parse(handle, "fasta"))
# SeqIO.write写文件，格式不好控制，不符合xiaoying的要求，采用传统读写write
i = 0
with open("all.fasta", 'w') as f:
    for fasta_item in fastas:
        f.write('>' + name_group[i] + '\n')
        f.write(str(fasta_item.seq) + '\n')
        i = i + 1

print("write successfully")
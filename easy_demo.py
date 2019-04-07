# from Bio import Entrez
# Entrez.email = '1227964378@qq.com'
# handle = Entrez.esearch(db='Gene',term='Hmoxl')
# record = Entrez.read(handle)
# print(record)
from Bio import Entrez
from Bio import SeqIO
import os
Entrez.email = "1227964378@qq.com"
handle = Entrez.efetch(db="nucleotide",id="NM_029604",rettype='fasta')
seq = SeqIO.read(handle,'fasta')
print(seq)
fw = open('data.fasta','w')
SeqIO.write(seq,fw,'fasta')
fw.close()
os.getcwd()
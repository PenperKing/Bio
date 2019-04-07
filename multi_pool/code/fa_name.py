import os
import stat


DNA_NAME = ['Mid1.fa', 'Ttc28.fa', 'BC030499.fa', 'Casc5.fa', 'Murc.fa', '9130017N09Rik.fa', 'Fert2.fa', 'Irg1.fa', 'Cep110.fa', '2610018G03Rik.fa', 'Ascc3.fa', 'Bcas3.fa', 'Bcas3.fa', 'Disc1.fa', 'Disc1.fa', 'Il1rap.fa', 'Il1rap.fa', 'Macrod2.fa', 'Macrod2.fa', 'Mcf2l.fa', 'Mcf2l.fa', 'Pard3.fa', 'Pard3.fa', 'Pard3.fa', 'Plcb1.fa', 'Plcb1.fa', 'Smarca4.fa', 'Smarca4.fa', 'Ttll3.fa', 'Ttll3.fa', 'Abca4.fa', 'Abcb1a.fa', 'Abcb4.fa', 'Acvr1b.fa', 'Adora2b.fa', 'Alkbh8.fa', 'Ano6.fa', 'Areg.fa', 'Arhgap18.fa', 'Aspm.fa', 'Atp11b.fa', 'Atp2b1.fa', 'Atp6ap1.fa', 'Atr.fa', 'Aurkb.fa', 'Aurkc.fa', 'Bora.fa', 'Brca2.fa', 'Camk4.fa', 'Ccnt2.fa', 'Cdc42bpa.fa', 'Cdc42ep1.fa', 'Cenpe.fa', 'Cep250.fa', 'Chek2.fa', 'Chordc1.fa', 'Cit.fa', 'Clk4.fa', 'Cnp.fa', 'Coro1b.fa', 'Csf3.fa', 'Csrnp3.fa', 'Cxcl1.fa', 'Cxcl2.fa', 'Cxcl3.fa', 'Ddx39b.fa', 'Dock11.fa', 'Dstyk.fa', 'Eef2k.fa', 'Ehd1.fa', 'Etnk1.fa', 'F830016B08Rik.fa', 'Faim.fa', 'Fancb.fa', 'Fancd2.fa', 'Farsa.fa', 'Fmnl1.fa', 'Foxo4.fa', 'Fpr2.fa', 'Gm4951.fa', 'Hltf.fa', 'Hmox1.fa', 'Hspa8.fa', 'Hyal1.fa', 'Icam1.fa', 'Iigp1.fa', 'Il5.fa', 'Ipmk.fa', 'Kif15.fa', 'Kif20b.fa', 'Lcor.fa', 'Lmln.fa', 'Lrrcc1.fa', 'Mad2l1.fa', 'Map3k2.fa', 'Map3k5.fa', 'Map4k2.fa', 'Mis12.fa', 'Mplkip.fa', 'Mtor.fa', 'Myh4.fa', 'Myh8.fa', 'Myo18a.fa', 'Myo1e.fa', 'Myo5c.fa', 'Myo9a.fa', 'Nbn.fa', 'Ncapg2.fa', 'Nfrkb.fa', 'Nme7.fa', 'Nos3.fa', 'Npat.fa', 'Nrp1.fa', 'Nsmce2.fa', 'Nwd1.fa', 'Oprl1.fa', 'Orc1.fa', 'P2ry1.fa', 'Pcm1.fa', 'Pdcd11.fa', 'Pds5b.fa', 'Pik3c3.fa', 'Pik3ca.fa', 'Pogz.fa', 'Ppid.fa', 'Ppp1r1c.fa', 'Prkdc.fa', 'Prpf19.fa', 'Ptgs2.fa', 'Pygm.fa', 'Rab11fip4.fa', 'Rab13.fa', 'Rb1cc1.fa', 'Rbbp8.fa', 'Rbpj.fa', 'Ren1.fa', 'Rest.fa', 'Retn.fa', 'Rev3l.fa', 'Rin1.fa', 'Rin2.fa', 'Rnasel.fa', 'Rock2.fa', 'Rps6ka3.fa', 'Sap18.fa', 'Sdccag8.fa', 'Slc9a1.fa', 'Slfn4.fa', 'Smc2.fa', 'Smc3.fa', 'Snrk.fa', 'Spata13.fa', 'Spg20.fa', 'Src.fa', 'Stat4.fa', 'Stk16.fa', 'Tac4.fa', 'Tax1bp1.fa', 'Tbc1d8b.fa', 'Tcp1.fa', 'Thoc1.fa', 'Tlr4.fa', 'Tpr.fa', 'Trerf1.fa', 'Trp53inp1.fa', 'Tyro3.fa', 'Unc5c.fa', 'Usp9x.fa', 'Vav1.fa', 'Vrk1.fa', 'Yme1l1.fa', 'Ythdc2.fa', 'Zbtb1.fa', 'Zfp207.fa', 'Hdgfrp3.fa', 'Dnahc6.fa', 'Ndnl2.fa', 'Erbb2ip.fa', 'Abcc5_1.fa', 'Abcc5_2.fa', 'Ddc_1.fa', 'Ddc_2.fa', 'Erc1_1.fa', 'Erc1_2.fa', 'Ifi202b_1.fa', 'Ifi202b_2.fa', 'Irak1_1.fa', 'Irak1_2.fa', 'Kif1b_1.fa', 'Kif1b_2.fa', 'Mefv_1.fa', 'Mefv_2.fa', 'Pifo_1.fa', 'Pifo_2.fa', 'Rabgap1l_1.fa', 'Rabgap1l_2.fa', 'Rffl_1.fa', 'Rffl_2.fa', 'Rims1_1.fa', 'Rims1_2.fa', 'Rwdd3_1.fa', 'Rwdd3_2.fa', 'Slc8a1_1.fa', 'Slc8a1_2.fa', 'Ttc5_1.fa', 'Ttc5_2.fa', 'Ttn_1.fa', 'Ttn_2.fa', 'Wnk1_1.fa', 'Wnk1_2.fa', 'Abcb7.fa', 'Abce1.fa', 'Adra1b.fa', 'Alpk2.fa', 'Als2.fa', 'Ankk1.fa', 'Anxa4.fa', 'Ap3m1.fa', 'Apbb2.fa', 'Appl1.fa', 'Arhgap10.fa', 'Arhgap12.fa', 'Arhgap44.fa', 'Atm.fa', 'Atrx.fa', 'Avp.fa', 'B4galt1.fa', 'Bax.fa', 'Bcl3.fa', 'Birc2.fa', 'Birc3.fa', 'Braf.fa', 'Brd4.fa', 'Btk.fa', 'Bub1.fa', 'Cacna1c.fa', 'Card9.fa', 'Cask.fa', 'Ccrl2.fa', 'Cct6b.fa', 'Cct8.fa', 'Cd209d.fa', 'Cd2ap.fa', 'Cd36.fa', 'Cdc14a.fa', 'Cdc27.fa', 'Cdk7.fa', 'Cdkl5.fa', 'Cdkn2a.fa', 'Cenpj.fa', 'Cep120.fa', 'Cep57.fa', 'Cep57l1.fa', 'Chd2.fa', 'Chd6.fa', 'Chm.fa', 'Chtf8.fa', 'Clec4e.fa', 'Clec5a.fa', 'Clk1.fa', 'Cxcl10.fa', 'Dact2.fa', 'Dars.fa', 'Ddx23.fa', 'Ddx3y.fa', 'Ddx41.fa', 'Ddx5.fa', 'Ddx50.fa', 'Dgkh.fa', 'Dhx15.fa', 'Dlgap5.fa', 'Dmxl2.fa', 'Dock10.fa', 'Dync2h1.fa', 'E4f1.fa', 'Ecm1.fa', 'Elmsan1.fa', 'Enpp1.fa', 'Erbb4.fa', 'Fancg.fa', 'Fasl.fa', 'Fgd3.fa', 'Fgd4.fa', 'Fpr1.fa', 'Gas1.fa', 'Gnl3.fa', 'Gpr33.fa', 'H2-Aa.fa', 'Haus7.fa', 'Hk1.fa', 'Hmgb1.fa', 'Hnf1a.fa', 'Ifnb1.fa', 'Ikbke.fa', 'Il10ra.fa', 'Il19.fa', 'Il1a.fa', 'Il1b.fa', 'Katnal2.fa', 'Kcnma1.fa', 'Kif5b.fa', 'Magi3.fa', 'Map3k12.fa', 'Map3k14.fa', 'Mat2a.fa', 'Mki67.fa', 'Ms4a2.fa', 'Msh3.fa', 'Myo1d.fa', 'Nae1.fa', 'Naip7.fa', 'Nars.fa', 'Nav1.fa', 'Ncoa1.fa', 'Ndc80.fa', 'Net1.fa', 'Nipbl.fa', 'Nmrk2.fa', 'Nox1.fa', 'Npm1.fa', 'Ntn1.fa', 'Nudc.fa', 'Olr1.fa', 'P2rx3.fa', 'Pax3.fa', 'Paxbp1.fa', 'Pex5l.fa', 'Pias1.fa', 'Pola1.fa', 'Polk.fa', 'Ppargc1b.fa', 'Ppp1r8.fa', 'Prg4.fa', 'Ptn.fa', 'Purb.fa', 'Rad50.fa', 'Ralgapa1.fa', 'Rap1a.fa', 'Rars.fa', 'Rasa2.fa', 'Rgs2.fa', 'Rgs7.fa', 'Rock1.fa', 'Sectm1a.fa', 'Serpine1.fa', 'Slfn9.fa', 'Smc5.fa', 'Smchd1.fa', 'Sp110.fa', 'Spdl1.fa', 'Srrt.fa', 'Stk38.fa', 'Suds3.fa', 'Susd2.fa', 'Suv39h2.fa', 'Swi5.fa', 'Tbc1d16.fa', 'Tbc1d2.fa', 'Tbc1d4.fa', 'Tbk1.fa', 'Thbd.fa', 'Tlr7.fa', 'Tnf.fa', 'Tnfaip3.fa', 'Tnfrsf12a.fa', 'Tnfsf14.fa', 'Tnip1.fa', 'Top2a.fa', 'Trib2.fa', 'Trio.fa', 'Trpm7.fa', 'Ttbk1.fa', 'Vax1.fa', 'Vps4b.fa', 'Zbtb38.fa', 'Zbtb49.fa', 'Zfp217.fa', 'Zfyve26.fa']

RNA_NAME = ["A_30_P01017533.txt", "A_30_P01019706.txt", "A_30_P01022485.txt", "A_30_P01023451.txt", "A_30_P01024622.txt",
            "A_30_P01028072.txt", "A_30_P01030979.txt",  "A_30_P01032399.txt",  "A_30_P01033287.txt", "A_30_P01018995.txt",
            "A_30_P01020855.txt", "A_30_P01023344.txt",  "A_30_P01024279.txt", "A_30_P01026663.txt", "A_30_P01030594.txt",
            "A_30_P01031879.txt", "A_30_P01032866.txt"]
all_circle_cnts = len(DNA_NAME)*len(RNA_NAME)
# CMD_STRIP = " -r 0 -O ../out"
# ./LongTarget -f1 Abca4.fa -f2 A_30_P01028072.txt -r 0 -O ./out
EXE_NAME = "./LongTarget"
OUT_DIR = "../out/"
# CMD_STRIP = " -r 0 -O {}".format(OUT_DIR)
CMD_STRIP = " -r 0 -O {} -c 6000 -i 70 -S 1.0 -ni 25 -na 1000 -pc 1 -pt -500 -ds 10 -lg 60".format(OUT_DIR)

if 'code' in os.getcwd():
    DATA_DIR = "../all_data/"
else:
    DATA_DIR = "all_data/"


def get_cmd(dna_name, rna_name):

    assert os.access(EXE_NAME, os.F_OK), "{} is not exist or not excute".format(EXE_NAME)
    if os.access(EXE_NAME, os.X_OK) == False:
        os.chmod(EXE_NAME, stat.S_IEXEC)
    return EXE_NAME + ' -f1 ' + dna_name + ' -f2 ' + rna_name + CMD_STRIP


def get_sorted_file_name(dna_name, rna_name):
    return "mouse_mm10-{}-{}-TFOsorted".format(rna_name[0:-4], dna_name[0:-3])


def get_time(s):
    print(s)
    s = int(s + 0.5)
    h = s // 3600
    m = (s - h * 3600) // 60
    ss = s - h * 3600 - m * 60
    return(str(h) + ':'+ str(m) + ':' + str(ss))


def check_file_exist():
    for name in RNA_NAME:
        if os.access(DATA_DIR + name, os.F_OK) == False:
            print('one rna file {} not  exist'.format(name))
            return False

    for name in DNA_NAME:
        if os.access(DATA_DIR + name, os.F_OK) == False:
            print('one dna file {} not  exist'.format(name))
    return True


if __name__ == '__main__':
    if check_file_exist():
        print("all file exist")
    else:
        print('some file is not exist')
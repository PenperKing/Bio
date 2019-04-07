import os
import glob
try:
    from multi_pool.code.fa_name import *
except ModuleNotFoundError:
    from fa_name import *
OUT_DIR = "../out"
SORTED_DIR = "sortedFiles"
UNCOMBINED_SIZE = 200
if os.path.exists(SORTED_DIR) is False:
    os.mkdir(SORTED_DIR)

combined_dr_name = []
uncombined_dr_name = []

os.system("cp {}/*sorted {}".format(OUT_DIR, SORTED_DIR))
sorted_file_list = glob.glob(SORTED_DIR + '/*')

print("There are %d sorted files!" % len(sorted_file_list))
if len(sorted_file_list) != all_circle_cnts:
# 打印出未生成的染色体对
    for dna in DNA_NAME:
        for rna in RNA_NAME:
            sort_name = get_sorted_file_name(dna, rna)
            if os.path.exists(SORTED_DIR + '/' + sort_name) is False:
                print("{} not creat".format(sort_name))



for file in sorted_file_list:
    if os.path.getsize(file) > UNCOMBINED_SIZE:
        combined_dr_name.append(os.path.split(file)[1])
    else:
        uncombined_dr_name.append(os.path.split(file)[1])

# mouse_mm10-A_30_P01019706-Ttc28-TFOsorted
with open("combined_chr.txt", "w") as f:
    for name in combined_dr_name:
        str_split = name.split("-")
        f.write(str_split[1] + '\t' + str_split[2] + '\n')

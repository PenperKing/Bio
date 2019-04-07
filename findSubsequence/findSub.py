import pandas as pd
import requests
import re


ROOT_URL = "http://genome.ucsc.edu/cgi-bin/das/mm10/dna?segment="
# chrX:169875622,169991798

# ps 小崽子chrX后面多了空格，应该是复制中间出了bug
name_list = []
def protacol_bed():
    all_chr_str = []
    wb = pd.read_csv("chrLocation.txt", sep='\t')
    for row in wb.values:
        if 'X' in row[1] and ' ' in row[1]:
            row[1] = row[1][:-1]  # 删除源数据chrx的空格
        name_list.append(row[0])
        all_chr_str.append(row[1] + ':' + str(row[2])
                                  + ',' + str(row[3]))
    return wb.values, all_chr_str
def get_seq_from_url(chr_str):
    url_test = ROOT_URL + chr_str
    response = requests.get(url_test)
    do_str = response.text.replace("\n", "")
    w1 = "<DNA length=\"3001\">"
    w2 = "</DNA>"
    find_rule = re.compile(w1 + '(.*?)' + w2)
    result = find_rule.findall(do_str)[0].upper()
    return result

# head format
# >mouse_mm10|chr17|35201007-35206007

def do_write_all_seq(all_singel_row, all_chr_str):
    i = 0

    for name, row, chr_str in zip(name_list, all_singel_row, all_chr_str):
        with open ("all_dna/{}.fa".format(name), "w") as f:
            seq_data = get_seq_from_url(chr_str)
            if 'X' in row[1] and ' ' in row[1]:
                row[1] = row[1][:-1]  # 删除源数据chrx的空格
            head_str = ">mouse_mm10|" + row[1] + '|' \
                       + str(row[2]) + '-' + str(row[3])
            f.write(head_str + '\n' + seq_data + '\n')
            i = i + 1
            print('write seq %d' % i)


if __name__ == '__main__':
    all_singel_row, all_chr_str = protacol_bed()
    print(name_list)
    # do_write_all_seq(all_singel_row, all_chr_str)

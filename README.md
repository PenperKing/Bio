# 背景
之前看到对象需要查询300个基因的基因，叫我帮她点鼠标，晕。查一个鼠标需要点十几下，键盘需要按十几下。
当时就帮她弄了100个，15s一个。相比她的速度，很感人，她一分多钟一个吧。其实网页上查询关键字速度就可以加快（Ctrl+F）。后来，回去想了想，整个过程完全可以编程解决，最先想到的是爬虫。
## 爬虫
	网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
	简单说就是从网页上下载数据，或者爬数据。
	项目初期未用到该方法，其实也可以用，就是一些字符串处理。有些较为繁琐。
## 实验内容
	1. 根据染色体的id，查询其fasta， 为了避免本人引用非专业用语，我用输入输出表示本次实验内容，以下同理.
		输入染色体id， 如 NM_029604， 获取其fasta，如下输出内容；当然不会一个个查询，一般输入一组id 文件， 输出对应格式
		的各个fasta数据集合
	2. 根据dna基因型，染色体的段，和染色体起始位置，查询该起始位置的基因序列
	3.  根据实验2上的dna基因序列与给定的RNA序列进行LongTarget算法预测。
	  （实验2,3， dna类型有300个，rna序列有20个；即实验2手工查询需要300次；实验3手动跑算法需要30*200次；
	     LongTarget官网貌似未给出多对多dna-rna预测，本人采用该网站提供的C++源代码进行线下运算）
## 1. 查询fasta
	忘记这个跟后面两个实验的关系了，，，先了解一下本实验需要的输入输出内容，
输入： id 文件, all_data.txt
RefSeqAccession	GeneSymbol
NM_029604	Pifo
NR_033603	Gm5176
NM_001024624	Cdkl5
NM_001081336	Dgkh
NM_177390	Myo1d
NM_001037747	Card9
NM_001164669	Dnahc6
NM_203320	Cxcl3
输出： fasta, 如下展示一组fasta数据，数据需要在NCBI网站上获取。data.fasta
```
	>NM_029604.3 Mus musculus primary cilia formation (Pifo), transcript variant 2, mRNA
CACAGAGCTAATCCTAGCACCCTGCAGGATGTGCTTCAGCAGAATAGGTAAGGAGAGTAG
CAGAGATTTACAGAGCAGACAGCAGAAGAAGGGTAAGAAGAGCAGGAGAGATGAACACGG
AGGAAATACCGGTTGCTCCTCCGCTCCGTGGAGTTACACCTGCTTTACAATGGAAGGTGA
ATAATTACTCCTTTGGAACACGTCAAGCGAGGAAACTCTTTCCTCACTACCATCCCCCAA
CCTGGCTGGGGAACCTGTATCTCCCTCTTAGGGGAATGCCCCACACAGGCCCTGGGTGTT
ATGCAGCAGCAACAGATTGGAATGGTTTGGCATATAATCTATCGAAAGTCCCAACCAGTA
CGAAAGGCTATGCTATTGGAGCCAGGACAGCTGTGAGGTTTAAGCCAATCAGCAAGGATG
TGACACCATACCCAGGGATGTATCAGAAAGTTGATACTTTGAGTGAAAAACACAAAAAAA
GCTTTGCTCCATTTAATATCTTGATGCCTCGATTTAGGAGTGCAGCAAAGGGTGATTCTT
ACCCCGGCCCTGGCACATACAATCCAGAGATGAAGTCAGTCCCAAAAGTTACTTGGCCAA
TGAAATTTGGATCTCCAGACTGGTCTCAGGTTCCATGTCTAGAGAAAAGGACTCTAAAGG
CTGAGCTGTCCGCAGACAAGGACTTTAGAAAGCATCGTAGCCGTGTGGCCTACTTTAGCC
TATATTACCAGTGAAATGTAGGCACTGTCTTCACGTGCTGTCCTGACCACAGAGTCTCCA
GAACTGAGGACATAATTGCTCCTGTATTTCTGTGTTCCTCGGCCCTCTTGTCTGCCCATT
TCGTGTCCAGAGAGGGACAGGGTCTCATTGTCACCCTCCAAATACATAAAGGCTGGTTCA
GAATGTTCAAAAAAAAAAAAAAAAA
```
### 解决
百度了NCBI相关内容，下载fasta不需要爬虫啥的，官方提供python库Bio.Entrez,可以爬相关各种数据。本次需要fasta数据
如下代码，即可获取id NM_029604 的fasta数据。
```
handle = Entrez.efetch(db="nucleotide",id="NM_029604",rettype='fasta')
seq = SeqIO.read(handle,'fasta')
```
若需要爬很多id的fasta，同理， 将id的组成字符串序列传入，用空格隔开即可。如id0， id1， id2.则`id = “id0 id1 id2”`
获取数据这里采用	`fastas = list(SeqIO.parse(handle, "fasta"))`， 组成列表处理。详细代码见bio_proj/main.py and easy_demo.py

## 查询基因起始位置的基因序列
这个问题困扰的比较久，找不到对应的python库，NCBI等网站查找的比较繁琐。想到了两种方法：
1. 通过ftp下载NCBI数据库，好像10个g，然后通过chr和基因位置，截取基因。
2. 在http://genome.ucsc.edu/爬数据。

当时因为这个问题折腾了很久，我和我对象都很郁闷，不知道怎么找方便。
网站上也试过，填一些数据，结果貌似不能同时获取多组数据。我对象都快放弃了，最后我只能这两种方法都同时尝试。早点弄出来，希望她开心一点咯。
对于方案1，我以为下载下来的数据库会是一张表，然后只需要查表就可以获取基因。没想到是好几个文件，每个不同根据chr将基因分成10几个文件，如chr1，chr2.。。。如果我需要查询基因起始位置的基因序列，就需要先判断该基因在哪个chr，然后再读取该位置上的基因序列，较为繁琐，每个文件都很大，该方案只能作为备用方案。
对于方案2，如查询chrX:169875622,169991798的基因
从网址http://genome.ucsc.edu/cgi-bin/das/mm10/dna?segment=chrX:169875622,169991798获取即可，其他类型的基因修改等于号后面名称即可，较为方便。重点在于爬虫以及数据截取。

### 方案 2 
查询的是300多个基因的序列，显然需要传入一张表。如下为输入文件 chrLocation.txt
name	chrom	start	end
Mid1	chrX 	169877622	169880622
Ttc28	chr5	110877803	110880803
BC030499	chr11	78288841	78291841
Casc5	chr2	119045119	119048119
Murc	chr4	48661514	48664514
9130017N09Rik	chr10	79819021	79822021
Fert2	chr17	63861981	63864981
Irg1	chr14	103045012	103048012
Cep110	chr7	118710543	118713543
2610018G03Rik	chrX 	50839371	50842371
Ascc3	chr10	50590669	50593669
Bcas3	chr11	85351163	85354163
Bcas3	chr11	85351163	85354163
Disc1	chr8	125052194	125055194
Disc1	chr8	125052194	125055194
Il1rap	chr16	26579704	26582704
名称基本没啥用，主要是chr和起始位置，注意： end-start都为3000
读表和组成网页我就不多说了，采用request.get(url)获取网页内容，返回的是个字符串。
对于爬虫后的数据解析，想了两种方法，
一是网页解析， 这种方法肯定是可以的，将网页当做树结构一个元素一个元素的读取数据，感觉速度较慢，没有考虑。
二是正则表达式， 基因就在两个字符串中间，查询了字符匹配，字符串截取。字符串匹配貌似不好弄，直接通过截取两个
字符串中间内容，完成爬虫。详细代码见bio_proj/findSubsequence/findSub.py

## 查询基因起始位置的基因序列
Longtarget.cpp代码写的真是有点乱， 准备把他改成多对多的，很晕，看不下去。该代码DEMO的序列，本人在i7的笔记本大概跑了4分钟，根据基因序列大小时间略有不同，一般为1分钟到5分钟，并且跟计算机运算性能有很大关系。跟CPU挂钩，要跑算法的！本次实验DNA有20个。
如果一次预测需要5分钟，那么本次实验应该需要跑 20*300*5= 20天。end，慢慢自己跑算法吧，网站上面要排队等着跑数据。


### solve
但是， 我是很懒得，
1. 首先至少要写个自动跑6000次的程序吧，手动输6000次，很累。
2. 跑算法时，发现CPU利用率为100%，有点低，我笔记本八个CPU，想了想，进程池可以搞起来。

由于Longtarget.cpp一次只能跑一对dna-rna序列，在不改变Longtarget.cpp源码的情况下。
1、只能将dnas和rnas文件分割成单个文件，然后一个个进行配对。
2、 采用多进程跑LongTarget, 总时间缩短为原来的八分之一
3、 输出某个基因序列是否结合，即判断Longtarget输出文件是否为空即可。
跑算法时发现一次平均配对时间约为60s， 总的跑了10个小时，即完成实验。
代码见bio_proj/multi_pool/code,数据见bio_proj/multi_pool/all_data, 上传数据时，本地压缩过了，* .fa为rna基因序列，* .txt为dna序列。代码可能库包含路径有问题，本人采用pycharm ide。

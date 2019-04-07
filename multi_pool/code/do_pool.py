import time, datetime
import os
import sys, glob
from multiprocessing import Pool
from multiprocessing import cpu_count, Lock, Value, Process
try:
    from multi_pool.code.fa_name import *
except ModuleNotFoundError:
    from fa_name import *

TEST = False
test_circle_num = 8
lock = Lock()
counter = Value('i', 0)

# >/dev/null 2>&1
def task_func(dna, rna):
    cmd = get_cmd(dna, rna)
    os.system(cmd + ">/dev/null 2>&1")
    file_exist = True
    sorted_path_name = OUT_DIR + get_sorted_file_name(dna, rna)

    if os.path.exists(sorted_path_name) is False:
        file_exist = False
    current_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
    global all_circle_cnts, lock, counter
    with lock:
        counter.value += 1
        with open('/home/penper/pre.log', 'a+') as f:
            if file_exist is False:
                f.write("*** no file creat {} XXOO {} ***\n".format(dna, rna))
            f.write("pro run {}, task left {} --- {}\n".format(
                  counter.value, all_circle_cnts - counter.value, current_time))

    print("%d tasks left, %s " % (all_circle_cnts - counter.value, str(file_exist)))

def main_pool():
    print('main start')

    start_time = datetime.datetime.now()
    pool = Pool(cpu_count())

    # 创建8个任务， 并全部非阻塞启动（实际只有4个开始运行， 另外2个在等待）
    tasks  = []
    if TEST:
        for i in range(test_circle_num):
            tasks.append(pool.apply_async(task_func, args=(DNA_NAME[i], RNA_NAME[i])))
    else:
        for dna in DNA_NAME:
            for rna in RNA_NAME:
                tasks.append(pool.apply_async(task_func, args=(dna, rna)))



    for task in tasks:
        task.get()

    end_time = datetime.datetime.now()
    print('main end, sys run time: {}'.format(get_time((end_time - start_time).seconds)))


if __name__ == '__main__':
    # os.system("rm out/* ")
    # os.system("rm /home/penper/pre.log")
    # os.chdir(DATA_DIR)
    # main_pool()
    print(len(set(DNA_NAME)))


from multiprocessing.pool import Pool
import time
import multiprocessing

count = 0


def inc_count(x):
    global count
    if x:
        count += 1


def reversible(n):
    this_sum = str(n + int(str(n)[::-1]))
    for c in this_sum:
        if c in '02468':
            return False
    return True


def perform():
    global count
    with Pool(multiprocessing.cpu_count() - 2) as tp:
        add_more = True
        for i in range(1, 1000000000):
            while True:
                if tp._taskqueue.qsize() < 1000000:
                    add_more = True
                if tp._taskqueue.qsize() > 2000000:
                    add_more = False
                if not add_more:
                    time.sleep(5)
                    continue
                a = tp.apply_async(reversible, args=[i], callback=inc_count)
                break
    return count


if __name__ == '__main__':
    ans = perform()
    with open('p145_ans.txt', 'w') as wb:
        wb.write(ans)
        print(ans)

import glob
import time

def copy_from(source):
    time.sleep(2)
    target = "copied_csv/{}".format(source.split("/")[-1])
    print("copy ({})".format(source))
    with open(source, "r") as rf:
        with open(target, "w") as wf:
            wf.write(rf.read())

def normal_copy(source_path):
    for source in glob.glob(source_path):
        copy_from(source)

if __name__ == "__main__":
    source_path = "source_csv/*"
    start = time.time()
    normal_copy(source_path)
    print(time.time() - start)









import threading
import glob
import time

sema = threading.Semaphore(10)

def copy_from(source):
    target = "copied_csv/{}".format(source.split("/")[-1])

    sema.acquire()
    time.sleep(2)

# critical section

    sema.release()

def parallel_copy(source_path):
    thread_list = [threading.Thread(target=copy_from, args=(source,)) for source in glob.glob(source_path)]

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    source_path = "source_csv/*"
    start = time.time()

    parallel_copy(source_path)

    print(time.time() - start)


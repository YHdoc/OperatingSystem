from asyncio.windows_events import NULL
from concurrent.futures import thread
from multiprocessing import Semaphore
from multiprocessing import Process
import threading
from threading import Thread
import time
import random

Sema1 = threading.Semaphore(1)
Sema2 = threading.Semaphore(1)
Sema3 = threading.Semaphore(1)
Sema4 = threading.Semaphore(1)

R1,R2,R3,R4 = False, False, False, False


def CriticalSection1(): #Up
    for i in range(1,10):
        time.sleep(0.1) 
        ResourceUsage = random.randint(1,3)
        if ResourceUsage == 3: 
            print(f"���� {i}��° ��ȸ�� ���� ���� ���(1,3,4�� ������ �䱸)\n")
            time.sleep(0.1)
            Sema1.acquire()
            Sema3.acquire()
            Sema4.acquire()
            
            print(f"���� {i}��° ��ȸ�� ���� 1,3,4�� ������ ȹ��! �������� ��. \n")
            time.sleep(0.1)
            print(f"���� {i}��° ��ȸ�� ���� ��ȸ�� ����. 1,3,4�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema1.release()
            Sema3.release()
            Sema4.release()
            
            
        elif ResourceUsage == 2:
            print(f"���� {i}��° ���� ���� ���� ���(1,3 ������ �䱸)\n")
            time.sleep(0.1)
            Sema1.acquire()
            Sema3.acquire()
            
            print(f"���� {i}��° ���� ���� 1,3�� ������ ȹ��! �������� ��. \n")
            time.sleep(0.1)
            print(f"���� {i}��° ���� ���� ���� ����. 1,3�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema1.release()
            Sema3.release()
            
        else:
            print(f"���� {i}��° ��ȸ�� ���� ���� ���(1 ������ �䱸)\n")
            time.sleep(0.1)
            Sema1.acquire()
            
            print(f"���� {i}��° ��ȸ�� ���� 1�� ������ ȹ��! �������� ��. \n")
            time.sleep(0.1)
            print(f"���� {i}��° ��ȸ�� ���� ��ȸ�� ����. 1�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema1.release()
        
        
def CriticalSection2(): #Down
    for i in range(1,10):
        time.sleep(0.1) 
        ResourceUsage = random.randint(1,3)
        if ResourceUsage == 3: 
            print(f"�Ʒ��� {i}��° ��ȸ�� ���� ���� ���(1,2,4 ������ �䱸)\n")
            time.sleep(0.1)
            Sema1.acquire()
            Sema2.acquire()
            Sema4.acquire()
            
            print(f"�Ʒ��� {i}��° ��ȸ�� ���� 1,2,4�� ������ ȹ��! �������� ��. \n")
            time.sleep(0.1)
            print(f"�Ʒ��� {i}��° ��ȸ�� ���� ���� �� ��ȸ�� ����. 1,2,4�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema1.release()
            Sema2.release()
            Sema4.release()
            
            
        elif ResourceUsage == 2:
            print(f"�Ʒ��� {i}��° ���� ���� ���� ���(2,4 ������ �䱸)\n")
            time.sleep(0.1)
            Sema2.acquire()
            Sema4.acquire()
            
            print(f"�Ʒ��� {i}��° ���� ���� 2,4�� ������ ȹ��! �������� ��. \n")
            time.sleep(0.1)
            print(f"�Ʒ��� {i}��° ���� ���� ���� �� ���� ����. 2,4�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema2.release()
            Sema4.release()
            
            
        else:
            print(f"�Ʒ��� {i}��° ��ȸ�� ���� ���� ���(4 ������ �䱸)\n")
            time.sleep(0.1)
            Sema4.acquire()
            
            print(f"�Ʒ��� {i}��° ��ȸ�� ���� 4�� ������ ȹ��!. �������� ��. \n")
            time.sleep(0.1)
            print(f"�Ʒ��� {i}��° ��ȸ�� ���� ���� �� ��ȸ�� ����. 4�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema4.release()

def CriticalSection3(): #Left
    for i in range(1,10):
        time.sleep(0.1) 
        ResourceUsage = random.randint(1,3)
        if ResourceUsage == 3: 
            print(f"���� {i}��° ��ȸ�� ���� ���� ���(2,3,4 ������ �䱸)\n")
            time.sleep(0.1)
            Sema2.acquire()
            Sema3.acquire()
            Sema4.acquire()
            
            print(f"���� {i}��° ��ȸ�� 2,3,4�� ������ ȹ��! �������� ��. \n")
            time.sleep(0.1)
            print(f"���� {i}��° ��ȸ�� ���� ���� �� ��ȸ�� ����. 2,3,4�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema2.release()
            Sema3.release()
            Sema4.release()
            
            
            
        elif ResourceUsage == 2:
            print(f"���� {i}��° ���� ���� ���� ���(3,4 ������ �䱸)\n")
            time.sleep(0.1)
            Sema3.acquire()
            Sema4.acquire()
            
            print(f"���� {i}��° ���� ���� 3, 4�� ������ ȹ��! �������� ��. \n")
            time.sleep(0.1)
            print(f"���� {i}��° ���� ���� ���� �� ���� ����. 3, 4�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema3.release()
            Sema4.release()
            
            
        else:
            print(f"���� {i}��° ��ȸ�� ���� ���� ���(3 ������ �䱸)\n")
            time.sleep(0.1)
            Sema3.acquire()
            
            print(f"���� {i}��° ��ȸ�� ���� 3�� ������ ȹ��! �������� ��. \n")
            time.sleep(0.1)
            print(f"���� {i}��° ��ȸ�� ���� ���� �� ��ȸ�� ����. 3�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema3.release()
            

def CriticalSection4(): #Right
    for i in range(1,10):
        time.sleep(0.1) 
        ResourceUsage = random.randint(1,3)
        if ResourceUsage == 3:
            print(f"������ {i}��° ��ȸ�� ���� ���� ���(1,2,3 ������ �䱸)\n")
            time.sleep(0.1) 
            Sema1.acquire()
            Sema2.acquire()
            Sema3.acquire()
            
            print(f"������ {i}��° ��ȸ�� ���� 1,2,3�� ������ ȹ��! �������� ��. \n")
            time.sleep(0.1)
            print(f"������ {i}��° ��ȸ�� ���� ���� �� ��ȸ�� ����. 1,2,3�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema1.release()
            Sema2.release()
            Sema3.release()
            
            
        elif ResourceUsage == 2:
            print(f"������ {i}��° ���� ���� ���� ���(1,2 ������ �䱸)\n")
            time.sleep(0.1) 
            Sema1.acquire()
            Sema2.acquire()
            
            print(f"������ {i}��° ���� ���� 1,2�� ������ ȹ��! �������� ��. \n")
            time.sleep(0.1)
            print(f"������ {i}��° ���� ���� ���� �� ���� ����. 1,2�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema1.release()
            Sema2.release()
            
        else:
            print(f"������ {i}��° ��ȸ�� ���� ���� ���(2 ������ �䱸)\n")
            time.sleep(0.1) 
            Sema2.acquire()
            
            print(f"������ {i}��° ��ȸ�� ���� 2�� ������ ȹ��! �������� ��. \n")
            time.sleep(0.1)
            print(f"������ {i}��° ��ȸ�� ���� ���� �� ��ȸ�� ����. 2�� ������ ��ȯ.\n")
            time.sleep(0.1)
            
            Sema2.release()       
            

if __name__ == "__main__":
    
    UpThreads = Thread(target=CriticalSection1)
    DownThreads = Thread(target=CriticalSection2)
    LeftThreads = Thread(target=CriticalSection3)
    RightThreads = Thread(target=CriticalSection4)
    
        
    LeftThreads.start()
    RightThreads.start()
    UpThreads.start()
    DownThreads.start()

    
    LeftThreads.join()
    RightThreads.join()
    UpThreads.join()
    DownThreads.join()

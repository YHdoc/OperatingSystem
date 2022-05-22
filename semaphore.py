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
            print(f"위쪽 {i}번째 좌회전 차량 진입 대기(1,3,4번 세마포 요구)\n")
            time.sleep(0.1)
            Sema1.acquire()
            Sema3.acquire()
            Sema4.acquire()
            
            print(f"위쪽 {i}번째 좌회전 차량 1,3,4번 세마포 획득! 지나가는 중. \n")
            time.sleep(0.1)
            print(f"위쪽 {i}번째 좌회전 차량 좌회전 성공. 1,3,4번 세마포 반환.\n")
            time.sleep(0.1)
            
            Sema1.release()
            Sema3.release()
            Sema4.release()
            
            
        elif ResourceUsage == 2:
            print(f"위쪽 {i}번째 직진 차량 진입 대기(1,3 세마포 요구)\n")
            time.sleep(0.1)
            Sema1.acquire()
            Sema3.acquire()
            
            print(f"위쪽 {i}번째 직진 차량 1,3번 세마포 획득! 지나가는 중. \n")
            time.sleep(0.1)
            print(f"위쪽 {i}번째 직진 차량 직진 성공. 1,3번 세마포 반환.\n")
            time.sleep(0.1)
            
            Sema1.release()
            Sema3.release()
            
        else:
            print(f"위쪽 {i}번째 우회전 차량 진입 대기(1 세마포 요구)\n")
            time.sleep(0.1)
            Sema1.acquire()
            
            print(f"위쪽 {i}번째 우회전 차량 1번 세마포 획득! 지나가는 중. \n")
            time.sleep(0.1)
            print(f"위쪽 {i}번째 우회전 차량 우회전 성공. 1번 세마포 반환.\n")
            time.sleep(0.1)
            
            Sema1.release()
        
        
def CriticalSection2(): #Down
    for i in range(1,10):
        time.sleep(0.1) 
        ResourceUsage = random.randint(1,3)
        if ResourceUsage == 3: 
            print(f"아래쪽 {i}번째 좌회전 차량 진입 대기(1,2,4 세마포 요구)\n")
            time.sleep(0.1)
            Sema1.acquire()
            Sema2.acquire()
            Sema4.acquire()
            
            print(f"아래쪽 {i}번째 좌회전 차량 1,2,4번 세마포 획득! 지나가는 중. \n")
            time.sleep(0.1)
            print(f"아래쪽 {i}번째 좌회전 차량 진입 및 좌회전 성공. 1,2,4번 세마포 반환.\n")
            time.sleep(0.1)
            
            Sema1.release()
            Sema2.release()
            Sema4.release()
            
            
        elif ResourceUsage == 2:
            print(f"아래쪽 {i}번째 직진 차량 진입 대기(2,4 세마포 요구)\n")
            time.sleep(0.1)
            Sema2.acquire()
            Sema4.acquire()
            
            print(f"아래쪽 {i}번째 직진 차량 2,4번 세마포 획득! 지나가는 중. \n")
            time.sleep(0.1)
            print(f"아래쪽 {i}번째 직진 차량 진입 및 직진 성공. 2,4번 세마포 반환.\n")
            time.sleep(0.1)
            
            Sema2.release()
            Sema4.release()
            
            
        else:
            print(f"아래쪽 {i}번째 우회전 차량 진입 대기(4 세마포 요구)\n")
            time.sleep(0.1)
            Sema4.acquire()
            
            print(f"아래쪽 {i}번째 우회전 차량 4번 세마포 획득!. 지나가는 중. \n")
            time.sleep(0.1)
            print(f"아래쪽 {i}번째 우회전 차량 진입 및 우회전 성공. 4번 세마포 반환.\n")
            time.sleep(0.1)
            
            Sema4.release()

def CriticalSection3(): #Left
    for i in range(1,10):
        time.sleep(0.1) 
        ResourceUsage = random.randint(1,3)
        if ResourceUsage == 3: 
            print(f"왼쪽 {i}번째 좌회전 차량 진입 대기(2,3,4 세마포 요구)\n")
            time.sleep(0.1)
            Sema2.acquire()
            Sema3.acquire()
            Sema4.acquire()
            
            print(f"왼쪽 {i}번째 좌회전 2,3,4번 세마포 획득! 지나가는 중. \n")
            time.sleep(0.1)
            print(f"왼쪽 {i}번째 좌회전 차량 진입 및 좌회전 성공. 2,3,4번 세마포 반환.\n")
            time.sleep(0.1)
            
            Sema2.release()
            Sema3.release()
            Sema4.release()
            
            
            
        elif ResourceUsage == 2:
            print(f"왼쪽 {i}번째 직진 차량 진입 대기(3,4 세마포 요구)\n")
            time.sleep(0.1)
            Sema3.acquire()
            Sema4.acquire()
            
            print(f"왼쪽 {i}번째 직진 차량 3, 4번 세마포 획득! 지나가는 중. \n")
            time.sleep(0.1)
            print(f"왼쪽 {i}번째 직진 차량 진입 및 직진 성공. 3, 4번 세마포 반환.\n")
            time.sleep(0.1)
            
            Sema3.release()
            Sema4.release()
            
            
        else:
            print(f"왼쪽 {i}번째 우회전 차량 진입 대기(3 세마포 요구)\n")
            time.sleep(0.1)
            Sema3.acquire()
            
            print(f"왼쪽 {i}번째 우회전 차량 3번 세마포 획득! 지나가는 중. \n")
            time.sleep(0.1)
            print(f"왼쪽 {i}번째 우회전 차량 진입 및 우회전 성공. 3번 세마포 반환.\n")
            time.sleep(0.1)
            
            Sema3.release()
            

def CriticalSection4(): #Right
    for i in range(1,10):
        time.sleep(0.1) 
        ResourceUsage = random.randint(1,3)
        if ResourceUsage == 3:
            print(f"오른쪽 {i}번째 좌회전 차량 진입 대기(1,2,3 세마포 요구)\n")
            time.sleep(0.1) 
            Sema1.acquire()
            Sema2.acquire()
            Sema3.acquire()
            
            print(f"오른쪽 {i}번째 좌회전 차량 1,2,3번 세마포 획득! 지나가는 중. \n")
            time.sleep(0.1)
            print(f"오른쪽 {i}번째 좌회전 차량 진입 및 좌회전 성공. 1,2,3번 세마포 반환.\n")
            time.sleep(0.1)
            
            Sema1.release()
            Sema2.release()
            Sema3.release()
            
            
        elif ResourceUsage == 2:
            print(f"오른쪽 {i}번째 직진 차량 진입 대기(1,2 세마포 요구)\n")
            time.sleep(0.1) 
            Sema1.acquire()
            Sema2.acquire()
            
            print(f"오른쪽 {i}번째 직진 차량 1,2번 세마포 획득! 지나가는 중. \n")
            time.sleep(0.1)
            print(f"오른쪽 {i}번째 직진 차량 진입 및 직진 성공. 1,2번 세마포 반환.\n")
            time.sleep(0.1)
            
            Sema1.release()
            Sema2.release()
            
        else:
            print(f"오른쪽 {i}번째 우회전 차량 진입 대기(2 세마포 요구)\n")
            time.sleep(0.1) 
            Sema2.acquire()
            
            print(f"오른쪽 {i}번째 우회전 차량 2번 세마포 획득! 지나가는 중. \n")
            time.sleep(0.1)
            print(f"오른쪽 {i}번째 우회전 차량 진입 및 우회전 성공. 2번 세마포 반환.\n")
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

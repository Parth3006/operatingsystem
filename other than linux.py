OTHER THAN LINUX 

DISK – SCHEDULING ALGORITHMS
---------------------------------- 1) FIFO Disk Scheduling------------------------

n = int(input("Enter no of requests: "))
req = []

for i in range(n):
    req.append(int(input()))

head = int(input("Enter head position: "))
seek = 0

print("Sequence:")
print(head, end="")

for r in req:
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

print(f"\nTotal Head Movement = {seek}")


--------------------------------2) SSTF Disk Scheduling-----------------

n = int(input("Enter no of requests: "))
req = []

for i in range(n):
    req.append(int(input()))

head = int(input("Enter head position: "))
seek = 0

print("Sequence:")
print(head, end="")

while req:
    x = min(req, key=lambda i: abs(i - head))
    seek += abs(x - head)
    head = x
    print(f" -> {head}", end="")
    req.remove(x)

print(f"\nTotal Head Movement = {seek}")


---------------------------------3) SCAN Disk Scheduling------------------------

n = int(input("Enter no of requests: "))
req = []

for i in range(n):
    req.append(int(input()))

head = int(input("Enter head position: "))
disk = int(input("Enter disk size: "))

seek = 0
left = sorted([i for i in req if i < head])
right = sorted([i for i in req if i >= head])

print("Sequence:")
print(head, end="")

for r in right:
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

seek += abs((disk - 1) - head)
head = disk - 1
print(f" -> {head}", end="")

for r in reversed(left):
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

print(f"\nTotal Head Movement = {seek}")

------------------------------4) C-SCAN Disk Scheduling---------------------------

n = int(input("Enter no of requests: "))
req = []

for i in range(n):
    req.append(int(input()))

head = int(input("Enter head position: "))
disk = int(input("Enter disk size: "))

seek = 0
left = sorted([i for i in req if i < head])
right = sorted([i for i in req if i >= head])

print("Sequence:")
print(head, end="")

for r in right:
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

seek += abs((disk - 1) - head)
head = disk - 1
print(f" -> {head}", end="")

seek += abs(head - 0)
head = 0
print(f" -> {head}", end="")

for r in left:
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

print(f"\nTotal Head Movement = {seek}")

----------------------------------5) LOOK Disk Scheduling-------------------------

n = int(input("Enter no of requests: "))
req = []

for i in range(n):
    req.append(int(input()))

head = int(input("Enter head position: "))

seek = 0
left = sorted([i for i in req if i < head])
right = sorted([i for i in req if i >= head])

print("Sequence:")
print(head, end="")

for r in right:
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

for r in reversed(left):
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

print(f"\nTotal Head Movement = {seek}")

--------------------------------------C-LOOK Disk Scheduling----------------------

n = int(input("Enter no of requests: "))
req = []

for i in range(n):
    req.append(int(input()))

head = int(input("Enter head position: "))

seek = 0
left = sorted([i for i in req if i < head])
right = sorted([i for i in req if i >= head])

print("Sequence:")
print(head, end="")

for r in right:
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

if left:
    seek += abs(head - left[0])
    head = left[0]
    print(f" -> {head}", end="")

for r in left:
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

print(f"\nTotal Head Movement = {seek}")

------MEMORY ALLOCATION POLLICIES-----

------------------------------------- 7) First Fit---------------------

blocks = [100,200,312,400,564]
psize = 212
used = [False]*len(blocks)

for i in range(len(blocks)):
    if blocks[i] >= psize and not used[i]:
        used[i] = True
        print(f"First Fit: Block {blocks[i]} allocated to {psize}")
        break
else:
    print("No block allocated")

print(f"Occupancy: {used}")

--------------------------------8) Best Fit----------------------------

blocks = [200,100,323,67,78,232]
psize = 212
used = [False]*len(blocks)

idx = -1
mn = 9999

for i in range(len(blocks)):
    if blocks[i] >= psize and not used[i]:
        if blocks[i] < mn:
            mn = blocks[i]
            idx = i

if idx == -1:
    print("No block allocated")
else:
    used[idx] = True
    print(f"Best Fit: Block {blocks[idx]} allocated to {psize}")

print(f"Occupancy: {used}")

--------------------------------9) Worst Fit-------------------------------

blocks = [200,100,323,67,78,232]
psize = 212
used = [False]*len(blocks)

idx = -1
mx = 0

for i in range(len(blocks)):
    if blocks[i] >= psize and not used[i]:
        if blocks[i] > mx:
            mx = blocks[i]
            idx = i

if idx == -1:
    print("No block allocated")
else:
    used[idx] = True
    print(f"Worst Fit: Block {blocks[idx]} allocated to {psize}")

print(f"Occupancy: {used}")

-----------------------------10) FIFO Page Replacement-----------------------------

pages = [3,2,5,6,1,3,2]
frames = 3

mem = []
ptr = 0
fault = 0

for p in pages:
    if p in mem:
        print(f"{p} -> Hit  {mem}")
    else:
        if len(mem) < frames:
            mem.append(p)
        else:
            mem[ptr] = p
            ptr = (ptr + 1) % frames

        fault += 1
        print(f"{p} -> Fault {mem}")

print(f"Total Page Faults = {fault}")

-------------------------------------11.LRU Page Replacement-------------------------

pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,3]
frames = 4

mem = []
recent = {}
fault = 0
t = 0

for p in pages:
    t += 1

    if p in mem:
        recent[p] = t
        print(f"{p} -> Hit  {mem}")
    else:
        fault += 1

        if len(mem) < frames:
            mem.append(p)
        else:
            x = min(mem, key=lambda i: recent[i])
            mem[mem.index(x)] = p

        recent[p] = t
        print(f"{p} -> Fault {mem}")

print(f"Total Page Faults = {fault}")

------------------------------12) LFU Page Replacement---------------------------

pages = [3,2,5,6,1,3,2]
frames = 4

mem = []
freq = {}
time = {}
fault = 0
t = 0

for p in pages:
    t += 1

    if p in mem:
        freq[p] += 1
        time[p] = t
        print(f"{p} -> Hit  {mem}")
    else:
        fault += 1

        if len(mem) < frames:
            mem.append(p)
        else:
            x = min(mem, key=lambda i:(freq[i],time[i]))
            mem[mem.index(x)] = p

        freq[p] = 1
        time[p] = t
        print(f"{p} -> Fault {mem}")

print(f"Total Page Faults = {fault}")

----------------------------------13) MFU Page Replacement-------------------------

pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,3]
frames = 4

mem = []
freq = {}
time = {}
fault = 0
t = 0

for p in pages:
    t += 1

    if p in mem:
        freq[p] += 1
        time[p] = t
        print(f"{p} -> Hit  {mem}")
    else:
        fault += 1

        if len(mem) < frames:
            mem.append(p)
        else:
            x = max(mem, key=lambda i:(freq[i],time[i]))
            mem[mem.index(x)] = p

        freq[p] = 1
        time[p] = t
        print(f"{p} -> Fault {mem}")

print(f"Total Page Faults = {fault}")

-----------------------------14) FCFS Scheduling------------------------

p = ['P1', 'P2', 'P3', 'P4', 'P5']
at = [0, 2, 6, 7, 13]
bt = [4, 16, 12, 8, 2]

n = len(p)

ct = [0] * n
tat = [0] * n
wt = [0] * n

ct[0] = at[0] + bt[0]

for i in range(1, n):
    ct[i] = max(ct[i - 1], at[i]) + bt[i]

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print(f"{'P':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<6}{'WT'}")

for i in range(n):
    print(f"{p[i]:<5}{at[i]:<5}{bt[i]:<5}{ct[i]:<5}{tat[i]:<6}{wt[i]}")

print("\nAverage TAT =", sum(tat) / n)
print("Average WT =", sum(wt) / n)

-----------------------------------------15. SRTF---------------------------------

p=['P1','P2','P3','P4','P5']
at=[0,2,6,7,13]
bt=[4,16,12,8,2]

n=len(p)
rt=bt[:]
ct=[0]*n
tat=[0]*n
wt=[0]*n

t=done=0

while done<n:
    idx=-1
    mn=999

    for i in range(n):
        if at[i]<=t and rt[i]>0 and rt[i]<mn:
            mn=rt[i]
            idx=i

    if idx==-1:
        t+=1
        continue

    rt[idx]-=1
    t+=1

    if rt[idx]==0:
        ct[idx]=t
        done+=1

for i in range(n):
    tat[i]=ct[i]-at[i]
    wt[i]=tat[i]-bt[i]

print(f"{'P':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<6}{'WT'}")
for i in range(n):
    print(f"{p[i]:<5}{at[i]:<5}{bt[i]:<5}{ct[i]:<5}{tat[i]:<6}{wt[i]}")

-----------------------------------------16) RR--------------------------------

p=['P1','P2','P3']
at=[0,0,0]
bt=[10,5,8]

q=2
n=len(p)

rt=bt[:]
ct=[0]*n
tat=[0]*n
wt=[0]*n

t=0

while sum(rt)>0:
    for i in range(n):
        if rt[i]>0:
            x=min(q,rt[i])
            t+=x
            rt[i]-=x
            if rt[i]==0:
                ct[i]=t

for i in range(n):
    tat[i]=ct[i]-at[i]
    wt[i]=tat[i]-bt[i]

print(f"{'P':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<6}{'WT'}")
for i in range(n):
    print(f"{p[i]:<5}{at[i]:<5}{bt[i]:<5}{ct[i]:<5}{tat[i]:<6}{wt[i]}")

-------------------------------17) Priority Non Preemptive-----------------------------

p=['P1','P2','P3']
at=[0,0,0]
bt=[10,5,8]
pr=[2,1,3]

n=len(p)

ct=[0]*n
tat=[0]*n
wt=[0]*n
done=[0]*n

t=0

for _ in range(n):
    idx=-1
    mn=999

    for i in range(n):
        if not done[i] and pr[i]<mn:
            mn=pr[i]
            idx=i

    t+=bt[idx]
    ct[idx]=t
    done[idx]=1

for i in range(n):
    tat[i]=ct[i]-at[i]
    wt[i]=tat[i]-bt[i]

print(f"{'P':<5}{'AT':<5}{'BT':<5}{'PR':<5}{'CT':<5}{'TAT':<6}{'WT'}")
for i in range(n):
    print(f"{p[i]:<5}{at[i]:<5}{bt[i]:<5}{pr[i]:<5}{ct[i]:<5}{tat[i]:<6}{wt[i]}")

 ---------------18) General Non Preemptive (SJF) (OR just do the FCFS again if we can )---------------

p=['P1','P2','P3']
at=[0,0,0]
bt=[10,5,8]

n=len(p)

ct=[0]*n
tat=[0]*n
wt=[0]*n
done=[0]*n

t=0

for _ in range(n):
    idx=-1
    mn=999

    for i in range(n):
        if not done[i] and bt[i]<mn:
            mn=bt[i]
            idx=i

    t+=bt[idx]
    ct[idx]=t
    done[idx]=1

for i in range(n):
    tat[i]=ct[i]-at[i]
    wt[i]=tat[i]-bt[i]

print(f"{'P':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<6}{'WT'}")
for i in range(n):
    print(f"{p[i]:<5}{at[i]:<5}{bt[i]:<5}{ct[i]:<5}{tat[i]:<6}{wt[i]}")

 ------------------------19) Implementation of Banker’s algorithm for finding sequence of process execution ensuring safe state of system.----------------------- 
def banker_algorithm():

    n, r = 5, 3

    alloc = [
        [0, 0, 1],
        [3, 0, 0],
        [1, 0, 1],
        [2, 3, 2],
        [0, 0, 3]
    ]

    mx = [
        [7, 6, 3],
        [3, 2, 2],
        [8, 0, 2],
        [2, 3, 2],
        [5, 2, 3]
    ]

    avail = [2, 3, 2]

    f = [0] * n
    ans = [0] * n

    ind = 0
    done = 0

    need = [
        [mx[i][j] - alloc[i][j] for j in range(r)]
        for i in range(n)
    ]

    while done < n:

        for i in range(n):

            if not f[i] and all(need[i][j] <= avail[j] for j in range(r)):

                ans[ind] = i
                ind += 1

                for j in range(r):
                    avail[j] += alloc[i][j]

                f[i] = 1
                done += 1

    print("The SAFE Sequence is as follows")

    for i in range(n - 1):
        print(f" P{ans[i]} ->", end="")

    print(f" P{ans[n - 1]}")

banker_algorithm()

----------------------20. Implementation of solution for producer Consumer problem.-------------------- 
import threading
import random
import time

buffer_size = 5
buffer = [0] * buffer_size

produce_pos = 0
consume_pos = 0
items = 0

lock = threading.Lock()

buffer_full = threading.Condition(lock)
buffer_empty = threading.Condition(lock)


def producer():

    global produce_pos, items

    while True:

        item = random.randint(1, 99)

        with buffer_full:

            while items == buffer_size:
                buffer_full.wait()

            buffer[produce_pos] = item

            print(f"Produced: {item} at {produce_pos}")

            produce_pos = (produce_pos + 1) % buffer_size
            items += 1

            buffer_empty.notify()

        time.sleep(1)


def consumer():

    global consume_pos, items

    while True:

        with buffer_empty:

            while items == 0:
                buffer_empty.wait()

            item = buffer[consume_pos]

            print(f"Consumed: {item} at {consume_pos}")

            consume_pos = (consume_pos + 1) % buffer_size
            items -= 1

            buffer_full.notify()

        time.sleep(1)


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

-----------------------Q7. Implementation of file managing operations. 
Code (I am putting the vi file as to understand the indentation ig it would be difficult with only pasting the code)---------------


import os

f = input("Enter file name: ")

while True:
    print("\n1.Create 2.Write 3.Read 4.Append 5.Delete 6.Exit")
    
    try:
        ch = int(input("Choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if ch == 1:
        open(f, "w").close()
        print("File created")

    elif ch == 2:
        content = input("Enter text: ")
        with open(f, "w") as file:
            file.write(content)
        print("Data written")

    elif ch == 3:
        try:
            with open(f, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found")

    elif ch == 4:
        content = input("Enter text: ")
        with open(f, "a") as file:
            file.write("\n" + content)
        print("Data appended")

    elif ch == 5:
        if os.path.exists(f):
            os.remove(f)
            print("File deleted")
        else:
            print("File not found")

    elif ch == 6:
        break

    else:
        print("Invalid choice")

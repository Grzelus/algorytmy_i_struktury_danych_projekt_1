import time
from datetime import timedelta
import random

def generate(n,min_value, max_value):
    if(min_value > max_value):
        print("minimalna wartość nie powinna być większa od maksymalnej.")
        return []
    output = [random.randint(min_value,max_value) for _ in range(n)]
    output = [random.randint(min_value,max_value) for _ in range(n)]

    choice = int(input("Wybierz sposób sortowania wygenerowanych liczb \n 1) losowo\n 2) rosnąco\n 3) malejąca\n 4) A-shaped\n 5) V-shape\n Twój wybór: " ))

    if choice == 1:
        return output
    if choice == 2:
        output.sort()
        return output
    if choice == 3:
        output.sort()
        output.reverse()
        return output
    if choice == 4:
        half = round(n/2)
        output.sort()
        first_half = [output[x] for x in range(half)]
        second_half = [output[x] for x in range(half, n)]
        second_half.reverse()
        return first_half + second_half
    if choice == 5:
        half = round(n/2)
        output.sort()
        first_half = [output[x] for x in range(half)]
        second_half = [output[x] for x in range(half, n)]
        first_half.reverse()
        return first_half + second_half
    
    print("wybierz właściwą opcje")
    return []
    
def quick_sort_i(array):
    stack = [(0, len(array)- 1)]
    while stack:
        left, right = stack.pop()

        if left >= right:
            continue

        pivot = array[right]
        i = left - 1

        for j in range(left, right):
            if array[j] > pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        
        array[i+1], array[right] = array[right], array[i+1]
        pivot_index = i+1

        stack.append((left, pivot_index - 1))
        stack.append((pivot_index + 1, right))

    return array

def quick_sort_r(array):
    if len(array)<=1:
        return array

    pivot = array[len(array)-1]

    left = [x for x in array if x > pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x < pivot]

    return quick_sort_r(left) + middle + quick_sort_r(right)


merges=0
def merge(Tab,left,mid,right):
    global merges
    L=[0 for x in range(mid-left+1)]
    R=[0 for x in range(right-mid)]
    for i in range(mid-left+1):
        L[i]=Tab[left+i]
    for j in range(right-mid):
        R[j]=Tab[mid+1+j]
    l=0
    r=0
    i=left
    while(l<mid-left+1 and r<right-mid):
        if(L[l]>R[r]):
            Tab[i]=L[l]
            l+=1
            i+=1
        else:
            Tab[i]=R[r]
            r+=1
            i+=1
    while(l<mid-left+1):
        Tab[i]=L[l]
        i+=1
        l+=1
    while(r<right-mid):
        Tab[i]=R[r]
        i+=1
        r+=1
    merges+=1

def merge_sort(Tab, left, right):
    if(left<right):
        mid=(left+right)//2
        merge_sort(Tab,left,mid)
        merge_sort(Tab,mid+1,right)
        merge(Tab,left,mid,right)

def Hibbards_increment(length,gap):
    gap.append(1)
    n=2*1+1
    while(length>n):
        gap.append(n)
        n=2*n+1

def Insertion_sort(tab):
    for i in range(1,len(tab)):
        key=tab[i]
        flag=0
        for j in range(i,0,-1):
            if key>tab[j-1]:
                tab[j]=tab[j-1]
            else : 
                tab[j]=key
                flag=1
                break
        if flag==0 :
            tab[0]=key

def Shell_sort(tab):
    gap=[]
    Hibbards_increment(len(tab),gap)
    for z in range(len(gap)-1,-1,-1):    
        if(gap[z]==1):
            Insertion_sort(tab)
        else:
            for i in range(0,len(tab)-gap[z]):
                temp=[]
                for j in range(i,len(tab),gap[z]):
                    temp.append(tab[j])
                Insertion_sort(temp)
                for j in range(i,len(tab),gap[z]):
                    tab[j]=temp[(j-i)//gap[z]]



def children_check(tab,parent,n):
    first=2*parent+1
    second=2*parent+2
    maxim=parent
    if first<n and tab[first]<tab[parent] and second>=n:
        maxim=first    
    elif first<n and tab[first]<tab[parent] and tab[second]>=tab[first] :
        maxim=first
    elif second<n and tab[second]<tab[parent] and tab[second]<tab[first] :
        maxim=second
    if(maxim!=parent):
        (tab[parent],tab[maxim])=(tab[maxim],tab[parent]) 
        children_check(tab,maxim,n)



def top(tab, destination):
    (tab[0],tab[destination])=(tab[destination],tab[0])

def Heapsort(tab):
    length=len(tab)
    for i in range(length//2-1,-1,-1):
        children_check(tab,i,length)
    for i in range(len(tab)-1,-1,-1):
        top(tab, i)
        length-=1
        children_check(tab,0,length)

print("1) Generuj tablice\n2) Własne dane")
choice = int(input("Wybierz opcje: "))
if(choice == 1):
    n = int(input("wygeneruj n liczb: "))
    min_value = int(input("Podaj minimalną wartość losowanych elementów: "))
    max_value = int(input("Podaj maksymalną wartość losowanych elementów: "))
    tab = generate(n,min_value,max_value)
elif(choice == 2):
    print("Ile liczb chcesz posortować: ")
    n=int(input())
    tab=[0 for x in range(n)]
    for i in range(n):
        x=int(input())
        tab[i]=x

print("1) Shell Sort z algorytmem bazowym Insertion Sort oraz przyrostami Hibbarda")
print("2) Merge Sort")
print("3) Heap Sort")
print("4) Quick Sort rekurencyjny z pivotem, którym jest skrajnie prawy element ciągu")
print("5) Quick Sort iteracyjny z pivotem, którym jest skrajnie prawy element ciągu")
choice = int(input("Wybierz opcje: "))

print(tab)
if(choice == 1 ):
    start=time.time()
    Shell_sort(tab)
elif(choice == 2 ):
    start=time.time()
    merge_sort(tab,0,n-1)
    print(f"{merges} scaleń podzbiorów")
elif(choice == 3 ):
    start=time.time()
    Heapsort(tab)
elif(choice == 4 ):
    start=time.time()
    tab = 1
    quick_sort_r(tab)
elif(choice == 5 ):
    start=time.time()
    quick_sort_i(tab)
else:
    print("Nie rozumiem")


end=time.time()
print(f"Posortowania tablica:  {tab}")
print(f"Czas wykonania sortowania: {(end - start)}")
##print(tab)
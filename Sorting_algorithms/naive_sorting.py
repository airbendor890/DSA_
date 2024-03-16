# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 00:15:03 2024

@author: Hara
"""
import math

# naive sorting
# ascending order
def naive_sort(arr):
    N=len(arr)
    for i in range(N):
         for j in range(i+1,N):
             if arr[j]<arr[i]:
                 #swap
                 temp=arr[i]
                 arr[i]=arr[j]
                 arr[j]=temp
                 
arr=[1,45,4,16,7,8,0,12,1,2,3,5,-193,34,0,0,-1]
# arr=[1,-3,7,0]
# naive_sort(arr)
print(arr)


### maximum subarray problem
# divide and conquer approach
# def max_subarray_from_middle(arr,low,high,mid):
#     l_max=mid
#     r_max=mid
    
#     #find left max index
#     l=mid
#     l_max_sum=-math.inf
#     next_sum=0
#     while(l>=0):
#         next_sum+=arr[l]
#         if next_sum>l_max_sum:
#             l_max=l
#             l_max_sum=next_sum
#         l=l-1
        
#     #find left max index
#     r=mid+1
#     r_max_sum=-math.inf
#     next_sum=0
#     while(r<high):
#         next_sum+=arr[r]
#         if next_sum>r_max_sum:
#             r_max=r
#             r_max_sum=next_sum
#         r=r+1
#     return l_max, r_max, l_max_sum + r_max_sum

# print(max_subarray_from_middle(arr,0,len(arr),int(len(arr)/2)))
# print(len(arr))

# def max_subarray(arr,low,high):
#     if low==high:
#         return low,high,arr[low]
#     else:
#         mid=int((low+high)/2)
#         left_low,left_high,left_sum=max_subarray(arr, low, mid)
#         right_low,right_high,right_sum=max_subarray(arr, mid+1, high)
#         cross_low,cross_high,cross_sum=max_subarray_from_middle(arr,low,high,mid)
        
#         if (max(left_sum,right_sum,cross_sum)==left_sum):
#             return left_low,left_high,left_sum
#         elif (max(left_sum,right_sum,cross_sum)==right_sum):
#             return right_low,right_high,right_sum
#         else:
#             return cross_low, cross_high, cross_sum
        
# print(max_subarray(arr, 0, len(arr)-1))


## heap sort
def left(i):
    return 2*i
def right(i):
    return 2*i+1

def Max_heapify(arr,i,heapsize):
    # print('maxheapify')
    l=left(i)
    r=right(i)
    largest=i
    if l<heapsize and arr[l]>arr[i]:
        largest=l
    if r<heapsize and arr[r]>arr[largest]:
        largest=r
        
    if largest!=i:
        #swap arr[i] and largest
        temp=arr[i]
        arr[i]=arr[largest]
        arr[largest]=temp
        
        Max_heapify(arr, largest,heapsize)
        
def build_Max_heap(arr):
    # print('buildmaxheap')
    heapsize=len(arr)
    i=int(len(arr)/2)
    while(i>=0):
        Max_heapify(arr, i,heapsize)
        i=i-1
        
def heapsort(arr):
    build_Max_heap(arr)
    heapsize=len(arr)
    i=len(arr)-1
    while(i>=1):
        #swap arr[0] and arr[i], reduce heapsize by 1
        temp=arr[i]
        arr[i]=arr[0]
        arr[0]=temp
        heapsize=heapsize-1
        Max_heapify(arr, 0, heapsize)
        i=i-1

heapsort(arr)
print(arr)        
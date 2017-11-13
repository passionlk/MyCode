#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 02:02:25 2017

@author: passionlk
"""

#冒泡排序 (时间复杂度O(n^2))

def bubble_sort(arry):
    n = len(arry)                   #获得数组的长度
    counter = 0

    for i in range(n):
        for j in range(1,n-i):
            if  arry[j-1] > arry[j] :       #如果前者比后者大
                arry[j-1],arry[j] = arry[j],arry[j-1]      #则交换两者
                counter += 1
        if counter == 0:
            break
        else:
            counter = 0
            
    return arry

a = [22,31,20,14,400,200,1,5]

print ("Before sorting: ", a)

bubble_sort(a)

print ("After sorting: ", a)


#选择排序 (时间复杂度O(n^2))

def select_sort(arry):
    n = len(arry)
    arry_new = []
    
    for i in range(0,n):
        min = i                              #最小元素下标标记
        for j in range(i+1,n):
            if arry[j] < arry[min] :
                min = j                     #找到最小值的下标
        arry[min],arry[i] = arry[i],arry[min]
        arry_new.append(arry[min])                #把最小的元素放到新的数组
        
    return arry_new 


a = [22,31,20,14,400,200,1,5]

print ("Before sorting: ", a)

select_sort(a)

print ("After sorting: ", a)



#插入排序 (时间复杂度O(n^2))

def insert_sort(ary):
    n = len(ary)
    
    for i in range(1,n):
        
        if ary[i] < ary[i-1]:
            temp = ary[i]
            index = i                   #待插入的下标
            for j in range(i-1,-1,-1):  #从i-1 循环到 0 (包括0,range函数的限制，必须把边界设置为-1)
                if ary[j] > temp :
                    ary[j+1] = ary[j]   #把较大的元素后移
                    index = j           #记录待插入下标
                else :
                    break
            ary[index] = temp
            
    return ary

a = [22,31,20,14,400,200,1,5]

print ("Before sorting: ", a)

insert_sort(a)

print ("After sorting: ", a)



#希尔排序 Shellsort (时间复杂度O(nlogn)~O(n^2))

def shell_sort(ary):
    n = len(ary)
    gap = round(n/2)       #初始步长 , 用round四舍五入取整
    
    while gap > 0 :
        
        for i in range(gap,n):        #每一列进行插入排序 , 从gap 到 n-1
            temp = ary[i]
            j = i
            while ( j >= gap and ary[j-gap] > temp ):    #插入排序
                ary[j] = ary[j-gap]
                j = j - gap
            ary[j] = temp
        gap = round(gap/2)                     #重新设置步长
        
    return ary

a = [22,31,20,14,400,200,1,5]

print ("Before sorting: ", a)

shell_sort(a)

print ("After sorting: ", a)



#归并排序 MergeSort??


def merge_sort(ary):

    if len(ary) <= 1 : return ary
    num = int(len(ary)/2)       #二分分解
    left = merge_sort(ary[:num])
    right = merge_sort(ary[num:])
    
    l,r = 0,0           #left与right数组的下标指针
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
        
    return result

a = [22,31,20,14,400,200,1,5]

print ("Before sorting: ", a)

merge_sort(a)

print ("After sorting: ", a)

































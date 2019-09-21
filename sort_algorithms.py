#!/usr/bin/env python
"""
Basic implementation of common sort algorithms using Python.
"""

# Quick sort methods
def quick_sort(items):
   quick_sort_detailed(items,0,len(items)-1)


def quick_sort_detailed(items,first_item,last_item):
   if first_item<last_item:

       splitpoint = partition(items,first_item,last_item)

       quick_sort_detailed(items,first_item,splitpoint-1)
       quick_sort_detailed(items,splitpoint+1,last_item)


def partition(items,first_item,last_item):
   pivotvalue = items[first_item]

   leftmark = first_item+1
   rightmark = last_item

   done = False
   while not done:

       while leftmark <= rightmark and items[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while items[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = items[leftmark]
           items[leftmark] = items[rightmark]
           items[rightmark] = temp

   temp = items[first_item]
   items[first_item] = items[rightmark]
   items[rightmark] = temp


# Merge sort methods
def merge_sort(items):
    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Currently merging ",items)

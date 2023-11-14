from random import randrange

def partition(l,r,x):
  #Equal, Greater, New
  E,G,N = (l,l,l)
  x = arr[x]
  for i in range(l,r):
    el = arr[i]
    if el < x:
      arr[N] = arr[G]
      N+=1
      arr[G] = arr[E]
      G+=1
      arr[E] = el
      E+=1

    elif el==x:
      arr[N] = arr[G]
      N+=1
      arr[G] = el
      G+=1

    elif el > x:
      arr[N] = el
      N+=1
  return E

def is_sorted(l,r):
  # one more helper function to
  # avoid going too deep in recursion
  for i in range(l+1,r):
    if arr[i-1]>arr[i]:
      return False
  return True


def quicksort_helper(l, r):
  if is_sorted(l,r):
    return
  if l < r:
    pivot = randrange(l,r)#(l+r)//2
    mid = partition(l, r, pivot)
    quicksort_helper(l, mid)
    quicksort_helper(mid + 1, r)


def quicksort(arr):
    l = 0
    r = len(arr)
    quicksort_helper(l, r)

N = int(input())

if N>0:
  arr = list(map(int,input().split()))

  quicksort(arr)

  for s in arr:
    print(s,end=" ")
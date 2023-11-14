def partition(arr,x):

  E,G,N = (0,0,0)

  for el in arr:
    if el < x:
      arr[N] = arr[G]
      N+=1
      arr[G] = arr[E]
      G+=1
      arr[E] = el
      E+=1

    if el==x:
      arr[N] = arr[G]
      N+=1
      arr[G] = el
      G+=1

    if el > x:
      arr[N] = el
      N+=1
  return arr,E

n = int(input())
arr=[]
inp = input()
if n>0:
  arr = list(map(int,inp.split()))
x = int(input())

new_arr,i = partition(arr,x)
print(len(new_arr[:i]))
print(len(new_arr[i:]))
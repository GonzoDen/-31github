m,n = map(int,input().split())

arr = list(map(int,input().split()))

for i in range(n):
  l,r = map(int,input().split())
  subs = arr[l:r+1]
  min_ = min(subs)

  ans="NOT FOUND"

  for j in subs:
    if j != min_:
      ans = j
      break

  print(ans)

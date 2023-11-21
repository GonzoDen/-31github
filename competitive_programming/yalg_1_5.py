def radix_sort(arr, m):
    n = len(arr)

    print("Initial array:")
    print(", ".join(arr))
    print("**********")

    for i in range(m):
        buckets = [[] for _ in range(10)]

        print("Phase", i + 1)

        for j in range(n):
            digit = int(arr[j][m - i - 1])
            buckets[digit].append(arr[j])

        for j in range(10):
            if(buckets[j]):
                print(f"Bucket {j}: {', '.join(buckets[j])}")
            else:
                print(f"Bucket {j}: empty")

        arr = [element for bucket in buckets for element in bucket]

        print("**********")

    print("Sorted array:")
    print(", ".join(arr))

n = int(input())
arr = [input().strip() for _ in range(n)]

max_length = max(len(s) for s in arr)

arr = [s.zfill(max_length) for s in arr]

radix_sort(arr, max_length)

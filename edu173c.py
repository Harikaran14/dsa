t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))

    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + x[i - 1]

    result = set()
    for i in range(n):
        for j in range(i, n):
            subarray_sum = prefix_sums[j + 1] - prefix_sums[i]
            result.add(subarray_sum)

    result.add(0)

    final = sorted(result)

    print(len(final))
    print(" ".join(map(str, final)))
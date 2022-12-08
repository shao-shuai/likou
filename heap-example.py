import heapq as hq

data = [1,2,3]

# hq.heapify(data)

# print(data)

# hq.heappush(data, 10)
# hq.heappush(data, 1)

# # while len(data) > 0:
# #     p = hq.heappop(data)
# #     print(p)

# n = hq.nlargest(2, data)
# m = hq.nsmallest(3, data)

# x = hq.heappushpop(data, 1000)

# print(x)
# print(data)
# # print(n)
# # print(m)

# Minimum Cost to Connect Sticks
def minCost(s):
    hq.heapify(s)

    cost = 0

    while len(s) > 1:
        a, b = hq.heappop(s), hq.heappop(s)
        cost += a + b
        hq.heappush(s, a + b)

    return cost

print(minCost(data))
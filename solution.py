import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, p = map(int, input().split())
    pixels = list(map(int, input().split()))

    # Use a min-heap for efficient smallest-pair extraction
    heapq.heapify(pixels)
    total_cost = 0

    # Merge until one group remains
    while len(pixels) > 1:
        # Pick two smallest intensity groups
        w1 = heapq.heappop(pixels)
        w2 = heapq.heappop(pixels)

        # Calculate merge cost and accumulate
        merge_cost = w1 + w2 + p
        total_cost += merge_cost

        # Push merged node back
        heapq.heappush(pixels, w1 + w2)

    print(total_cost)


def main():
    
    solve()


if __name__ == "__main__":
    main()

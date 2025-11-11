from itertools import combinations
import functools

def brute_force_min_cost(a, p):
    # Memoization to avoid recomputation
    @functools.lru_cache(None)
    def dfs(state):
        state = tuple(sorted(state))
        if len(state) == 1:
            return 0

        best = float('inf')
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                x, y = state[i], state[j]
                merged = x + y
                cost = x + y + p
                new_state = list(state[:i] + state[i+1:j] + state[j+1:])
                new_state.append(merged)
                best = min(best, cost + dfs(tuple(new_state)))

        return best

    return dfs(tuple(sorted(a)))


if __name__ == "__main__":
    tests = [
        ([5, 2, 8, 3], 3),
        ([4, 7, 6, 3, 9], 2),
        ([1, 1, 2, 3, 5, 8], 1)
    ]

    for arr, p in tests:
        print("Pixels:", arr, "Penalty:", p)
        print("Brute-force min cost:", brute_force_min_cost(arr, p))
        print()

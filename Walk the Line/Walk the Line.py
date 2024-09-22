def can_cross_within_time(times, N, K):
    if N == 1:
        return times[0] <= K

sorted_times = sorted(times)

total_time = 0
    left = 0
    right = N - 1

    while right >= 1:
        # Two slowest people cross
        slow1 = sorted_times[right]
        slow2 = sorted_times[right - 1]

        # Two fastest people cross
        fast1 = sorted_times[left]
        fast2 = sorted_times[left + 1]

        if right == 1:
total_time += slow1  # If two people are left, they cross together
            break

        # Strategy 1: Fastest two cross first, one returns, slowest two cross, fastest returns
        strategy1 = 2 * fast1 + slow1 + slow2

        # Strategy 2: Fastest crosses with slowest, then fastest returns, then both fast people cross
        strategy2 = 2 * fast2 + fast1 + slow1

total_time += min(strategy1, strategy2)

        right -= 2

    return total_time<= K

def main():
    T = int(input())

    for t in range(1, T + 1):
        N, K = map(int, input().split())
        S = list(map(int, input().split()))

        if can_cross_within_time(S, N, K):
print(f"Case #{t}: YES")
        else:
print(f"Case #{t}: NO")

if __name__ == "__main__":
main()

def simulate_curling(N, G, energies, case_num):
    # List to store the final positions of stones
    positions = [0] * N

    # Simulate stone movement
    for i in range(N):
        energy = energies[i]
current_position = 0

        # Move the current stone
        while energy > 0:
            if i> 0 and positions[i - 1] == current_position + 1:
                # Collision detected: transfer remaining energy to the previous stone
                energy = max(0, energy - (positions[i - 1] - current_position))
current_position = positions[i - 1]
                continue
current_position += 1
            energy -= 1

        # After movement, set the final position of the stone
        positions[i] = current_position

    # Find the stone closest to the goal G
closest_stone_idx = -1
min_distance = float('inf')

    for i in range(N):
        distance = abs(G - positions[i])
        if distance <min_distance:
min_distance = distance
closest_stone_idx = i + 1  # 1-based index for output

    # Output the result for this case
print(f"Case #{case_num}: {closest_stone_idx} {min_distance}")


def main():
    T = int(input())  # Number of test cases

    for t in range(1, T + 1):
        N, G = map(int, input().split())  # Number of stones and the goal
        energies = list(map(int, input().split()))  # Energies of the stones

simulate_curling(N, G, energies, t)


if __name__ == "__main__":
main()


def closestStoneToGoal(N, G, energies):
    positions = [0] * N  # To store final positions of each stone
last_position = 0     # Position of the last moving stone
last_energy = 0       # Energy of the last moving stone
last_index = -1       # Index of the last moving stone

    # Iterate through each stone
    for i in range(N):
        energy = energies[i]

        # If no previous stone is moving
        if last_index == -1:
last_position = energy   # The first stone moves by its energy
last_energy = 0          # Now it's stationary
last_index = i
            positions[i] = last_position
        else:
            # If it collides with the previous stone
            if last_position == energy:
last_energy += energy  # Transfer remaining energy to new stone
last_index = i
                positions[i] = last_position  # It stops at the previous position
            else:
                # If no collision, the stone moves normally
last_position = energy
last_energy = 0
last_index = i
                positions[i] = last_position

    # Now determine the stone closest to G
closest_index = -1
min_distance = float('inf')

    for i in range(N):
        distance = abs(positions[i] - G)
        if distance <min_distance or (distance == min_distance and i<closest_index):
closest_index = i
min_distance = distance

    return closest_index + 1, min_distance  # Return 1-based index

# Main function
def main():
    T = int(input())  # Number of test cases

    for t in range(1, T + 1):
        N, G = map(int, input().split())  # Number of stones and goal G

        # Read the energies of the stones
        energies = list(map(int, input().split()))

        # Calculate the result for the current test case
        result = closestStoneToGoal(N, G, energies)

        # Output the result in the required format
print(f"Case #{t}: {result[0]} {result[1]}")

# Call the main function
if __name__ == "__main__":
main()

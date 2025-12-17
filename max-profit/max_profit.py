def find_max_profit(total_time):
    # Time required to build each type
    theatre_time = 5
    pub_time = 4
    commercial_time = 10

    # Earnings per unit time
    theatre_earning = 1500
    pub_earning = 1000
    commercial_earning = 2000

    max_earning = 0
    best_solutions = []

    # Try all combinations
    for t in range((total_time // theatre_time) + 1):
        for p in range((total_time // pub_time) + 1):
            for c in range((total_time // commercial_time) + 1):

                build_time = (
                    t * theatre_time +
                    p * pub_time +
                    c * commercial_time
                )

                if build_time > total_time:
                    continue

                current_time = 0
                total_earning = 0

                # Build theatres first
                for _ in range(t):
                    current_time += theatre_time
                    if current_time <= total_time:
                        total_earning += (total_time - current_time) * theatre_earning

                # Then pubs
                for _ in range(p):
                    current_time += pub_time
                    if current_time <= total_time:
                        total_earning += (total_time - current_time) * pub_earning

                # Then commercial parks
                for _ in range(c):
                    current_time += commercial_time
                    if current_time <= total_time:
                        total_earning += (total_time - current_time) * commercial_earning

                if total_earning > max_earning:
                    max_earning = total_earning
                    best_solutions = [{
                        "T": t,
                        "P": p,
                        "C": c
                    }]
                elif total_earning == max_earning:
                    best_solutions.append({
                        "T": t,
                        "P": p,
                        "C": c
                    })

    return max_earning, best_solutions

if __name__ == "__main__":
    n = int(input("Enter total time units: "))

    earnings, solutions = find_max_profit(n)

    print(f"\nEarnings: ${earnings}")
    print("Solutions:")
    for i, sol in enumerate(solutions, start=1):
        print(f"{i}. T: {sol['T']} P: {sol['P']} C: {sol['C']}")

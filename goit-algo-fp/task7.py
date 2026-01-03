import random

def simulate_dice(rolls):
    # Словник для підрахунку сум від 2 до 12
    counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        counts[total] += 1
        
    return counts

def main():
    N = 1000000
    print(f"Симуляція {N} кидків...")
    
    results = simulate_dice(N)
    
    print("\nРезультати (Монте-Карло vs Теорія):")
    print(f"{'Сума':<5} | {'Імовірність':<15}")
    print("-" * 25)
    
    for s in range(2, 13):
        prob = (results[s] / N) * 100
        print(f"{s:<5} | {prob:<15.2f}%")

if __name__ == "__main__":
    main()
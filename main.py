import pickle

def load_budget():
    try:
        with open('budget.pickle', 'rb') as file:
            budget = pickle.load(file)
    except FileNotFoundError:
        budget = 0
    return budget

def save_budget(budget):
    with open('budget.pickle', 'wb') as file:
        pickle.dump(budget, file)

def main():
    budget = load_budget()

    while True:
        print(f"Balansas biudzeto: ${budget}")
        print("1. Irasyti pajamas")
        print("2. Iseiti")

        choice = input("Pasirink 1/2: ")

        if choice == '1':
            try:
                amount = float(input("Irasyti pajamas: "))
                budget += amount
            except ValueError:
                print("Neteisingas ivestis. Prašome įvesti tinkamą skaičių.")
        elif choice == '2':
            print("Iki pasimatymo. Saugojamas biudžetas...")
            save_budget(budget)
            break
        else:
            print("Neteisingas pasirinkimas. Prašome įvesti 1 arba 2.")

if __name__ == "__main__":
    main()


"""
main.py
Aplikacja BudgetTracker.
"""
from datetime import date
from models import Transaction
from storage import save_transactions, load_transactions

def show_summary(transactions):
    """
    Wyświetla podsumowanie przychodów, wydatków i salda.
    Args:
        transactions (list): lista transakcji
    """
    total_income = 0
    total_expense = 0

    # liczy przychody i wydatki
    for t in transactions:
        if t.amount > 0:
            total_income = total_income + t.amount
        else:
            total_expense = total_expense + t.amount

    saldo = total_income + total_expense

    print("\n" + "=" * 35)
    print(f"  Przychody:  +{total_income:.2f} zł")
    print(f"  Wydatki:     {total_expense:.2f} zł")
    print(f"  Saldo:       {saldo:.2f} zł")

    # IF — pokaż czy na plusie czy minusie
    if saldo > 0:
        print("  Jesteś na plusie ")
    elif saldo < 0:
        print("  Jesteś na minusie ")
    else:
        print("  Wychodzisz na zero.")
    print("=" * 35)


def show_list(transactions):
    """
    Wyświetla listę wszystkich transakcji.
    Args:
        transactions (list): lista transakcji
    """
    # brak transakcji
    if len(transactions) == 0:
        print("\nBrak transakcji.")
        return

    print("\n" + "-" * 45)
    print(f"  {'Opis':<20} {'Kwota':>10}  {'Data'}")
    print("-" * 45)

    # wyświetl każdą transakcję
    for t in transactions:
        # znak przy kwocie
        if t.amount > 0:
            sign = "+"
        else:
            sign = ""

        print(f"  {t.description:<20} {sign}{t.amount:>8.2f} zł  {t.date}")

    print("-" * 45)

def add_transaction(transactions):
    """
    Pyta użytkownika o dane i dodaje nową transakcję.
    Args:
        transactions (list): lista transakcji do której dodajemy
    """
    print("\n--- Nowa transakcja ---")

    # opis
    desc = input("Opis: ").strip()

    # opis nie może być pusty
    if desc == "":
        print("Opis nie może być pusty!")
        return

    # kwota - pętla dopóki nie poda poprawnej
    while True:
        amount_str = input("Kwota (np. -100 lub 1000): ").strip()

        # sprawdź czy to liczba
        try:
            amount = float(amount_str)
            # kwota nie może być zerem
            if amount == 0:
                print("Kwota nie może być zerem!")
            else:
                break  # kwota poprawna
        except ValueError:
            print("To nie jest liczba. Spróbuj ponownie.")

    today = date.today().strftime("%Y-%m-%d")
    t = Transaction(amount=amount, description=desc, date=today)

    transactions.append(t)
    save_transactions(transactions)

    #pokaż co dodano
    if amount > 0:
        print(f"Dodano przychód: +{amount:.2f} zł")
    else:
        print(f"Dodano wydatek: {amount:.2f} zł")

def clear_all(transactions):
    """
    Usuwa wszystkie transakcje.
    Args:
        transactions (list): lista do wyczyszczenia
    """
    confirm = input("Na pewno usunąć wszystko? (tak/nie): ").strip().lower()

    # potwierdź przed usunięciem
    if confirm == "tak":
        # usuwanie
        while len(transactions) > 0:
            transactions.pop()

        save_transactions(transactions)
        print("Usunięto wszystkie transakcje.")
    else:
        print("Anulowano.")

# =============================================
# GŁÓWNA PĘTLA
# =============================================

# wczytaj zapisane transakcje
transactions = load_transactions()

# aplikacja działa dopóki użytkownik nie wyjdzie
while True:
    print("\n --- BUDGET TRACKER ---")
    print("1. Pokaż transakcje")
    print("2. Podsumowanie")
    print("3. Dodaj transakcję")
    print("4. Wyczyść wszystko")
    print("5. Wyjdź")

    choice = input("\nWybierz opcję: ").strip()

    # obsługa wyboru
    if choice == "1":
        show_list(transactions)
    elif choice == "2":
        show_summary(transactions)
    elif choice == "3":
        add_transaction(transactions)
    elif choice == "4":
        clear_all(transactions)
    elif choice == "5":
        print("Do zobaczenia!")
        break
    else:
        print("Nieznana opcja - wpisz 1-5.")
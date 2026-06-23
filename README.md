# BudgetTracker

BudgetTracker to prosta aplikacja terminalowa napisana w Pythonie do śledzenia przychodów i wydatków. Umożliwia dodawanie transakcji, przeglądanie historii oraz sprawdzanie aktualnego salda. Dane są zapisywane w pliku JSON, dzięki czemu pozostają dostępne po ponownym uruchomieniu programu.

## Zawartość projektu

| Plik | Opis |
|-------|-------|
| `main.py` | Główna logika aplikacji i obsługa menu |
| `models.py` | Definicja klasy `Transaction` |
| `storage.py` | Zapis i odczyt danych z pliku JSON |

Plik `transactions.json` jest tworzony automatycznie przy pierwszym uruchomieniu programu.

## Wymagania

- Python 3.10 lub nowszy
- Brak dodatkowych bibliotek

## Instalacja i uruchomienie

Sklonuj repozytorium:

```bash
git clone https://github.com/TWOJ_LOGIN/BudgetTracker.git
cd BudgetTracker# BudgetTracker


Uruchom aplikację:
```bash
python main.py
```

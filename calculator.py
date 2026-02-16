import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

if __name__ == "__main__":
    print("=== KALKULATOR ===")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęga")
    print("6. Pierwiastek")
    
    choice = input("Wybierz operację (1-6): ")
    
    if choice == "1":
        a = float(input("Pierwsza liczba: "))
        b = float(input("Druga liczba: "))
        print(f"Wynik: {add(a, b)}")
    elif choice == "2":
        a = float(input("Pierwsza liczba: "))
        b = float(input("Druga liczba: "))
        print(f"Wynik: {subtract(a, b)}")
    elif choice == "3":
        a = float(input("Pierwsza liczba: "))
        b = float(input("Druga liczba: "))
        print(f"Wynik: {multiply(a, b)}")
    elif choice == "4":
        a = float(input("Pierwsza liczba: "))
        b = float(input("Druga liczba: "))
        print(f"Wynik: {divide(a, b)}")
    elif choice == "5":
        a = float(input("liczba Potegowana: "))
        b = float(input("Potega: "))
        print(f"Wynik: {power(a, b)}")
    elif choice == "6":
        a = float(input("Liczba pod pierwiastkiem: "))
        print(f"Wynik: {sqrt(a)}")

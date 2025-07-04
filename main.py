from utils import (
    add_expense,
    read_all_expenses,
    calculate_total,
    filter_by_date,
    filter_by_category,
    format_expense
)

def handle_add_expense():
    pass

def handle_view_all():
    pass

def handle_total():
    pass

def handle_filter_by_date():
    pass

def handle_filter_by_category():
    pass

def main():
    while True:
        print("\n📋 Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Filter by Date")
        print("5. Filter by Category")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            handle_add_expense()
        elif choice == "2":
            handle_view_all()
        elif choice == "3":
            handle_total()
        elif choice == "4":
            handle_filter_by_date()
        elif choice == "5":
            handle_filter_by_category()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()



import os

FILENAME = "expenses.csv"

def add_expense():
    date = input("Sana (YYYY-MM-DD): ").strip()
    category = input("Kategoriya: ").strip()
    while True:
        amount_str = input("Miqdor (so'm): ").strip()
        try:
            amount = float(amount_str)
            if amount < 0:
                print("Iltimos, manfiy bo'lmagan son kiriting.")
                continue
            break
        except ValueError:
            print("Iltimos, raqam kiriting.")
    line = f"{date},{category},{amount}\n"
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(line)
    print("Xarajat qo‘shildi.\n")

def read_expenses():
    expenses = []
    if not os.path.exists(FILENAME):
        return expenses
    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 3:
                continue
            date, category, amount_str = parts
            try:
                amount = float(amount_str)
                expenses.append({
                    "date": date,
                    "category": category,
                    "amount": amount
                })
            except ValueError:
                continue
    return expenses

def view_all_expenses():
    expenses = read_expenses()
    if not expenses:
        print("Xarajatlar mavjud emas.\n")
        return
    print("\nBarcha xarajatlar:")
    print(f"{'Sana':<12} {'Kategoriya':<15} {'Miqdor (som)':>12}")
    print("-" * 40)
    for exp in expenses:
        print(f"{exp['date']:<12} {exp['category']:<15} {exp['amount']:>12.2f}")
    print()

def view_total_expenses():
    expenses = read_expenses()
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nJami xarajat: {total:.2f} so'm\n")

def filter_by_date():
    target_date = input("Qaysi sanadagi xarajatlarni ko'rmoqchisiz? (YYYY-MM-DD): ").strip()
    expenses = read_expenses()
    filtered = [e for e in expenses if e['date'] == target_date]
    if not filtered:
        print(f"{target_date} sanasida xarajatlar topilmadi.\n")
        return
    print(f"\n{target_date} sanasidagi xarajatlar:")
    print(f"{'Kategoriya':<15} {'Miqdor (som)':>12}")
    print("-" * 30)
    for exp in filtered:
        print(f"{exp['category']:<15} {exp['amount']:>12.2f}")
    print()

def filter_by_category():
    target_category = input("Qaysi kategoriyadagi xarajatlarni ko'rmoqchisiz? ").strip()
    expenses = read_expenses()
    filtered = [e for e in expenses if e['category'].lower() == target_category.lower()]
    if not filtered:
        print(f"'{target_category}' kategoriyasida xarajatlar topilmadi.\n")
        return
    print(f"\n'{target_category}' kategoriyasidagi xarajatlar:")
    print(f"{'Sana':<12} {'Miqdor (som)':>12}")
    print("-" * 25)
    for exp in filtered:
        print(f"{exp['date']:<12} {exp['amount']:>12.2f}")
    print()

def main():
    while True:
        print("=== Expense Tracker ===")
        print("1. Yangi xarajat qo'shish")
        print("2. Barcha xarajatlarni ko'rish")
        print("3. Jami xarajatni ko'rish")
        print("4. Sanaga ko'ra filtr")
        print("5. Kategoriyaga ko'ra filtr")
        print("6. Chiqish")
        choice = input("Tanlovingiz (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            view_total_expenses()
        elif choice == "4":
            filter_by_date()
        elif choice == "5":
            filter_by_category()
        elif choice == "6":
            print("Dastur tugadi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov, qaytadan urinib ko'ring.\n")

if __name__ == "__main__":
    main()

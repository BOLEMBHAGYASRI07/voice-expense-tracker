import speech_recognition as sr
import matplotlib.pyplot as plt
from db import init_db, add_expense, fetch_expenses
from nlp import parse_expense

def listen_expense():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎤 Speak your expense (e.g., 'I spent 200 on food')")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand.")
        return None
    except sr.RequestError:
        print("⚠ API unavailable.")
        return None

def show_summary():
    expenses = fetch_expenses()
    if not expenses:
        print("📂 No expenses found.")
        return

    categories = {}
    for amount, category, date in expenses:
        categories[category] = categories.get(category, 0) + amount

    print("\n📊 Expense Summary:")
    for cat, amt in categories.items():
        print(f"{cat}: ₹{amt}")

    # Plot
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()

def main():
    init_db()

    while True:
        print("\n1️⃣ Add Expense (voice)\n2️⃣ Show Summary\n3️⃣ Exit")
        choice = input("👉 Enter choice: ")

        if choice == "1":
            text = listen_expense()
            if text:
                amount, category = parse_expense(text)
                if amount and category:
                    add_expense(amount, category)
                    print(f"✅ Added {amount} for {category}")
                else:
                    print("⚠ Could not extract details.")
        elif choice == "2":
            show_summary()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()

from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age_years = today.year - birthdate.year
    age_months = today.month - birthdate.month
    age_days = today.day - birthdate.day

    # Adjust if the current month/day is before the birth month/day
    if age_days < 0:
        age_months -= 1
        age_days += 30  # Approximate fix
    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

def main():
    print("🗓️ Age Calculator 🗓️")
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        years, months, days = calculate_age(dob)
        print(f"Your age is {years} years, {months} months, and {days} days.")
    except ValueError:
        print("⚠️ Please enter a valid date format (YYYY-MM-DD).")

if __name__ == "__main__":
    main()

from src.patient import Patient
from src.triage_engine import TriageEngine
from src.validator import Validator


# -------------------------
# Helper functions (RETRY SYSTEM)
# -------------------------

def get_boolean_input(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["yes", "y"]:
            return True
        elif value in ["no", "n"]:
            return False
        else:
            print("❌ Please enter yes or no")


def get_valid_temperature(validator):
    while True:
        try:
            value = float(input("Temperature (°C): "))
            return validator.validate_temperature(value)
        except ValueError as e:
            print("❌ Error:", e)
            print("👉 Enter valid temperature (30–45)")


def get_valid_pulse(validator):
    while True:
        try:
            value = int(input("Pulse rate: "))
            return validator.validate_pulse(value)
        except ValueError as e:
            print("❌ Error:", e)
            print("👉 Enter valid pulse (30–200)")


def get_valid_pain(validator):
    while True:
        try:
            value = int(input("Pain level (0-10): "))
            return validator.validate_pain(value)
        except ValueError as e:
            print("❌ Error:", e)
            print("👉 Enter pain between 0–10")


# -------------------------
# MAIN PROGRAM
# -------------------------

def main():
    print("Educational Patient Triage System")
    print("NOT FOR REAL MEDICAL USE\n")

    validator = Validator()

    name = input("Patient name: ")
    age = int(input("Age: "))
    symptoms = input("Symptoms: ")

    # Safe inputs
    pain_level = get_valid_pain(validator)
    fever = get_valid_temperature(validator)
    pulse = get_valid_pulse(validator)

    shortness = get_boolean_input(
        "Shortness of breath? (yes/no): "
    )

    # Create patient object
    patient = Patient(
        name=name,
        age=age,
        symptoms=symptoms,
        pain_level=pain_level,
        fever=fever,
        pulse=pulse,
        shortness_of_breath=shortness
    )

    # Triage decision
    engine = TriageEngine()
    category = engine.assign_category(patient)

    print("\nTriage Category:")
    print(category)

    # Color risk output (NEW FEATURE)
    risk_color = engine.get_risk_color(category)
    print("Risk Level:", risk_color)


# -------------------------
# START PROGRAM
# -------------------------

if __name__ == "__main__":
    main()
class Validator:

    def validate_temperature(self, temp):
        if temp < 30 or temp > 45:
            raise ValueError("Invalid temperature input")
        return temp

    def validate_pulse(self, pulse):
        if pulse < 30 or pulse > 200:
            raise ValueError("Invalid pulse rate")
        return pulse

    def validate_pain(self, pain):
        if pain < 0 or pain > 10:
            raise ValueError("Pain must be between 0 and 10")
        return pain
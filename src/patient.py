from dataclasses import dataclass


@dataclass
class Patient:
    name: str
    age: int
    symptoms: str
    pain_level: int
    fever: float
    pulse: int
    shortness_of_breath: bool
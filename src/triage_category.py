from enum import Enum


class TriageCategory(Enum):
    IMMEDIATE = "Immediate"
    URGENT = "Urgent"
    NORMAL = "Normal"
    NON_URGENT = "Non-Urgent"
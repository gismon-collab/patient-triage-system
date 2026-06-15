from src.triage_category import TriageCategory


class TriageEngine:

    def assign_category(self, patient):

        # 🔴 Immediate (Emergency)
        if patient.shortness_of_breath:
            return TriageCategory.IMMEDIATE

        if patient.pain_level >= 9:
            return TriageCategory.IMMEDIATE

        if patient.fever >= 40:
            return TriageCategory.IMMEDIATE

        if patient.pulse > 130:
            return TriageCategory.IMMEDIATE

        # 🟡 Urgent
        if (
            patient.pain_level >= 7
            or patient.fever >= 38.5
            or patient.pulse > 110
            or patient.age > 60
        ):
            return TriageCategory.URGENT

        # 🟢 Normal
        if (
            patient.pain_level >= 4
            or patient.fever >= 37.5
            or patient.pulse > 90
        ):
            return TriageCategory.NORMAL

        # ⚪ Non-Urgent
        return TriageCategory.NON_URGENT

    def get_risk_color(self, category):

        if category == TriageCategory.IMMEDIATE:
            return "🔴 RED - HIGH RISK"

        elif category == TriageCategory.URGENT:
            return "🟡 YELLOW - MEDIUM RISK"

        elif category == TriageCategory.NORMAL:
            return "🟢 GREEN - LOW RISK"

        else:
            return "⚪ NON-URGENT"
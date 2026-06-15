from src.patient import Patient
from src.triage_engine import TriageEngine
from src.triage_category import TriageCategory


engine = TriageEngine()


def test_immediate_by_breathing():
    patient = Patient(
        "John",
        30,
        "Chest pain",
        3,
        37.0,
        80,
        True
    )

    assert (
        engine.assign_category(patient)
        == TriageCategory.IMMEDIATE
    )


def test_immediate_by_pain():
    patient = Patient(
        "John",
        30,
        "Injury",
        10,
        37.0,
        80,
        False
    )

    assert (
        engine.assign_category(patient)
        == TriageCategory.IMMEDIATE
    )


def test_urgent():
    patient = Patient(
        "John",
        65,
        "Headache",
        7,
        38.0,
        100,
        False
    )

    assert (
        engine.assign_category(patient)
        == TriageCategory.URGENT
    )


def test_normal():
    patient = Patient(
        "John",
        25,
        "Cold",
        5,
        37.8,
        75,
        False
    )

    assert (
        engine.assign_category(patient)
        == TriageCategory.NORMAL
    )


def test_non_urgent():
    patient = Patient(
        "John",
        20,
        "Minor rash",
        1,
        36.8,
        70,
        False
    )

    assert (
        engine.assign_category(patient)
        == TriageCategory.NON_URGENT
    )
# rules
# Limits (easy to change)
MIN_SCORE = 70   # original rule
MIN_GPA = 2.5    # new condition 2 (assumed value)

def check_application(score, docs_complete, has_letter, gpa):
    # Collect every reason the application fails
    reasons = []

    if score < MIN_SCORE:                 # original condition 1
        reasons.append("score too low")
    if not docs_complete:                 # original condition 2
        reasons.append("documents incomplete")
    if not has_letter:                    # new condition 1
        reasons.append("no recommendation letter")
    if gpa < MIN_GPA:                     # new condition 2
        reasons.append("gpa too low")

    # If there are no reasons to fail, flag for review
    if len(reasons) == 0:
        return "Review", "all conditions met"
    return "Hold", ", ".join(reasons)

# Exactly 4 tests: (name, score, docs_complete, has_letter, gpa, expected, why)
tests = [
    ("pass",            85, True, True,  3.4, "Review", "meets all conditions"),
    ("no_letter",       85, True, False, 3.4, "Hold",   "tests new condition 1"),
    ("low_gpa",         85, True, True,  2.0, "Hold",   "tests new condition 2"),
    ("boundary",        70, True, True,  2.5, "Review", "exact limit values"),
]

# Run every test and print the details
for name, score, docs_complete, has_letter, gpa, expected, why in tests:
    actual, reason = check_application(score, docs_complete, has_letter, gpa)

    print("Test     :", name)
    print("Input    : score =", score, "| docs_complete =", docs_complete,
          "| has_letter =", has_letter, "| gpa =", gpa)
    print("Expected :", expected)
    print("Actual   :", actual)
    print("Reason   :", reason)
    print("Why chosen:", why)
    print("Result   :", "PASS" if actual == expected else "FAIL")
    print()
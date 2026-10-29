# compare
# Rule-based: needs BOTH a score of 70 or more AND complete documents
def rule_check(score, docs_complete):
    if docs_complete and score >= 70:
        return "Review"
    return "Hold"

# Probability-based: only looks at the probability value
def prob_check(probability):
    if probability >= 0.70:
        return "Review"
    return "Hold"

# Each case: (name, score, docs_complete, probability)
cases = [
    ("complete_high",   82, True,  0.81),
    ("complete_low",    68, True,  0.74),
    ("incomplete_high", 91, False, 0.88),
    ("boundary",        70, True,  0.70),
]

# Print a table header
print("case | rule | probability | disagree")

# Go through every case and compare the two checkers
for name, score, docs_complete, probability in cases:
    rule_result = rule_check(score, docs_complete)
    prob_result = prob_check(probability)
    disagree = rule_result != prob_result   # True if they give different answers
    print(name, rule_result, prob_result, disagree, sep=" | ")





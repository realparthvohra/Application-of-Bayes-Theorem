from src.Analyzer import analyze_root_causes

causes = ["Network Issue", "Hardware Failure", "Software Bug", "Configuration Error", "User Error"]
# These are the potential root causes we want to analyze.

priror_possibilities = {
    "Network Issue": 0.2,
    "Hardware Failure": 0.2,
    "Software Bug": 0.2,
    "Configuration Error": 0.2,
    "User Error": 0.2
}
# Initial prior probabilities for each cuase. Since we have no prior knowledge, we assume equal probabilities. There sum is 1.

probability_of_evidence_given_cause = {
    "Network Issue": 0.7,
    "Hardware Failure": 0.1,
    "Software Bug": 0.5,
    "Configuration Error": 0.4,
    "User Error": 0.3
}
# Likelihood of observing the evidence given each cause. These values are hypothetical and should be determined based on historical data or expert knowledge.

likely_probabilities = analyze_root_causes(priror_possibilities, probability_of_evidence_given_cause)

highest_probability = 0
probable_cause = None

for cause , probability in likely_probabilities.items():
    if probability > highest_probability:
        highest_probability = probability
        probable_cause = cause
    print(f"Cause: {cause}, Posterior Probability: {probability:.4f}")
print(f"\nThe most probable root cause is: {probable_cause} with a probability of {highest_probability:.4f}")
# This function calculates the posterior probabilities of each cause given the evidence using Bayes' theorem.



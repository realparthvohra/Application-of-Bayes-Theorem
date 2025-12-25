from src.Bayes import Bayesian_cacl

def analyze_root_causes(prior, likelihood):
    """
    Analyze root causes using Bayesian inference.

    Parameters:
    prior (dict): A dictionary containing prior probabilities for each cause.
    likelihood (dict): A dictionary containing likelihoods of evidence given each cause.

    Returns:
    dict: A dictionary containing posterior probabilities for each cause.
    """
    posterior = Bayesian_cacl(prior, likelihood)
    return posterior
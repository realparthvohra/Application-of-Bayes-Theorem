# Bayesian Root Cause Analyzer

- **Purpose:**  
  - Identify the most probable root causes of problems using Bayesian inference.  
  - Demonstrates how prior knowledge and new evidence can be combined mathematically to update beliefs.  

- **Key Features:**  
  - Lightweight Python library for Bayesian updates.  
  - `bayes.py`: Implements the core Bayesian update function.  
  - `analyzer.py`: Applies Bayesian updates to multiple potential causes.  
  - Example scripts show practical usage and outputs.  

- **Folder Structure:**  
  - `src/` → Core library modules:  
    - `bayes.py` → Bayesian update function  
    - `analyzer.py` → Applies Bayesian update to root cause analysis  
  - `CaseStudy/` → Example scripts demonstrating usage (e.g., `1.py`)  
  - `README.md` → This file  
  - `requirements.txt` → Optional dependencies  
  - `.gitignore` → Standard ignores  

- **Installation / Setup:**  
  - Clone the repository:  
    ```bash
    git clone https://github.com/yourusername/bayesian-root-cause-analyzer.git
    cd bayesian-root-cause-analyzer
    ```  
  - Optional: create and activate a virtual environment:  
    ```bash
    python -m venv venv
    venv\Scripts\activate      # Windows
    source venv/bin/activate   # Linux / Mac
    ```  
  - Install dependencies (if any):  
    ```bash
    pip install -r requirements.txt
    ```

- **Running Examples:**  
  - From project root, run:  
    ```bash
    python -m CaseStudy.1
    ```  
  - Outputs:  
    - Posterior probabilities for each cause  
    - The most probable root cause  

- **Inputs Explained:**  
  - `causes` → List of potential root causes  
  - `priors` → Initial probability for each cause (sum = 1)  
  - `likelihoods` → Probability of observing the evidence given each cause  

- **Outputs Explained:**  
  - Dictionary of posterior probabilities for each cause  
  - Identification of the cause with the highest probability  

- **How It Works:**  
  - `1.py` calls `analyze_root_causes` from `analyzer.py`  
  - `analyzer.py` uses `Bayesian_cacl` from `bayes.py` to compute posterior probabilities  
  - Demonstrates the Bayesian update process step-by-step  

- **Example Output:**  
    Cause: Network Issue, Posterior Probability: 0.3500
    Cause: Hardware Failure, Posterior Probability: 0.0500
    Cause: Software Bug, Posterior Probability: 0.2500
    Cause: Configuration Error, Posterior Probability: 0.2000
    Cause: User Error, Posterior Probability: 0.1500

    Most probable root cause: Network Issue (0.3500)

# Medical Diagnosis Prediction System using Bayes' Theorem
# Educational demonstration only - NOT a real medical diagnosis tool.

from flask import Flask, render_template, request

app = Flask(__name__)

# Default values (in percent) shown when the page first opens
DEFAULT_PRIOR = 20
DEFAULT_SENSITIVITY = 66
DEFAULT_SPECIFICITY = 61


def bayes_theorem(prior, sensitivity, specificity):
    """
    All three inputs must be decimals between 0 and 1.
    Returns P(Disease | Positive Test) as a decimal, or None if
    the probability of a positive test is zero (cannot divide by zero).
    """
    # Probability of a positive test (the "Evidence")
    true_positive = sensitivity * prior
    false_positive = (1 - specificity) * (1 - prior)
    evidence = true_positive + false_positive

    if evidence == 0:
        return None

    # Posterior probability
    posterior = true_positive / evidence
    return posterior


@app.route("/", methods=["GET", "POST"])
def home():
    # Values to show in the input boxes
    prior = DEFAULT_PRIOR
    sensitivity = DEFAULT_SENSITIVITY
    specificity = DEFAULT_SPECIFICITY

    result = None   # final answer in percent
    error = None    # error message, if any

    if request.method == "POST":
        try:
            # Read the numbers typed by the user
            prior = float(request.form["prior"])
            sensitivity = float(request.form["sensitivity"])
            specificity = float(request.form["specificity"])
        except ValueError:
            error = "Please enter valid numbers in all fields."
        else:
            # Check that every value is a valid percentage
            if not (0 <= prior <= 100 and 0 <= sensitivity <= 100 and 0 <= specificity <= 100):
                error = "All values must be between 0 and 100."
            else:
                # Convert percentages to decimals (e.g. 20% -> 0.20)
                posterior = bayes_theorem(prior / 100, sensitivity / 100, specificity / 100)

                if posterior is None:
                    error = "The probability of a positive test is 0, so the result cannot be calculated."
                else:
                    # Convert the answer back to a percentage
                    result = round(posterior * 100, 1)

    return render_template(
        "index.html",
        prior=prior,
        sensitivity=sensitivity,
        specificity=specificity,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    # Port 5001 is used because macOS AirPlay already uses port 5000
    app.run(debug=True, port=5001)

# Medical Diagnosis Prediction System using Bayes' Theorem

> **Disclaimer:** This project is an educational demonstration only. It does not diagnose heart disease, is not clinically validated, and does not replace a qualified doctor.

---

## 1. Abstract

Medical tests are not perfect. A positive result does not always mean that a patient has the disease. This project is a simple website that uses Bayes' Theorem to calculate the probability that a patient has heart disease after a positive test result. The user enters three values: the initial (prior) probability of heart disease, the sensitivity of the test, and the specificity of the test. The system is built with HTML, CSS and Python Flask. With the default values (prior 20%, sensitivity 66%, specificity 61%), the probability of heart disease after a positive test is about 29.7%. The project shows how probability theory can help us understand medical test results.

## 2. Problem Statement

Many people believe that a positive medical test means a person definitely has the disease. In reality, every test can give false positive results. There is a need for a simple tool that shows how the chance of having a disease changes after a positive test, using the prior probability and the accuracy of the test.

## 3. Objectives

1. To understand and apply Bayes' Theorem to a real-life medical example.
2. To build a simple web application using HTML, CSS and Flask.
3. To calculate the probability of heart disease after a positive test result.
4. To explain the terms Prior, Sensitivity, Specificity, Evidence and Posterior in simple language.
5. To validate user input and handle errors such as invalid percentages and division by zero.

## 4. Methodology

1. **Input:** The user enters the prior probability, sensitivity and specificity as percentages on the webpage.
2. **Send to server:** When the user clicks "Calculate Probability", the form sends the values to the Flask server.
3. **Validation:** The server checks that all values are numbers between 0 and 100.
4. **Conversion:** Percentages are divided by 100 to convert them into decimals.
5. **Calculation:** Bayes' Theorem is applied to find the posterior probability.
6. **Output:** The result is converted back into a percentage, rounded to one decimal place, and shown on the webpage with a short explanation.

## 5. System Architecture

```
+-------------------+        Form data (POST)        +----------------------+
|                   |  ----------------------------> |                      |
|   User's Browser  |                                |   Flask Server       |
|  (index.html +    |                                |   (app.py)           |
|   style.css)      |  <---------------------------- |   - Validation       |
|                   |     HTML page with result      |   - Bayes calculation|
+-------------------+                                +----------------------+
```

- **Frontend (HTML + CSS):** Shows the form, result card, key terms and disclaimer.
- **Backend (Flask + Python):** Receives the inputs, validates them, performs the calculation and sends the result back.
- No database, no machine learning and no external API are used.

## 6. Algorithm

1. Start.
2. Display the form with default values: Prior = 20, Sensitivity = 66, Specificity = 61.
3. Read Prior, Sensitivity and Specificity entered by the user.
4. If any value is not a number, show "Please enter valid numbers" and stop.
5. If any value is less than 0 or greater than 100, show "All values must be between 0 and 100" and stop.
6. Convert each value to a decimal: value = value / 100.
7. Calculate True Positive = Sensitivity × Prior.
8. Calculate False Positive = (1 − Specificity) × (1 − Prior).
9. Calculate Evidence = True Positive + False Positive.
10. If Evidence = 0, show an error message and stop.
11. Calculate Posterior = True Positive / Evidence.
12. Convert Posterior to a percentage: Posterior × 100, and round to 1 decimal place.
13. Display the result and explanation.
14. Stop.

### Worked example (default values)

| Step | Calculation | Value |
|---|---|---|
| Prior | 20% → 0.20 | 0.20 |
| Sensitivity | 66% → 0.66 | 0.66 |
| Specificity | 61% → 0.61 | 0.61 |
| True Positive | 0.66 × 0.20 | 0.132 |
| False Positive | (1 − 0.61) × (1 − 0.20) = 0.39 × 0.80 | 0.312 |
| Evidence | 0.132 + 0.312 | 0.444 |
| Posterior | 0.132 / 0.444 | 0.2973 ≈ **29.7%** |

## 7. Advantages and Limitations

### Advantages
- Very simple and easy to understand.
- Shows clearly how a positive test changes the probability of disease.
- Uses only basic technologies (HTML, CSS, Flask).
- Runs on any computer with Python installed.
- Validates inputs and handles division by zero.

### Limitations
- It is an educational demonstration and cannot be used for real diagnosis.
- It only considers one test and one disease.
- It only calculates the result for a positive test, not a negative test.
- The accuracy of the result depends completely on the values entered by the user.
- It does not use real patient data or medical history.

## 8. Conclusion

This project successfully demonstrates the use of Bayes' Theorem to calculate the probability of heart disease after a positive test result. With the default values, the probability rises from 20% to about 29.7%. This shows that a positive test increases the chance of disease but does not confirm it. The project helps students understand conditional probability and basic web development using Flask. It is an educational tool and must not be used in place of a qualified doctor.

## 9. Viva Questions and Answers

**1. What is Bayes' Theorem?**
Bayes' Theorem is a formula that tells us how to update the probability of an event when we get new evidence. Formula: P(A|B) = P(B|A) × P(A) / P(B).

**2. What is prior probability in this project?**
It is the chance that the patient has heart disease before the test is done. The default value is 20%.

**3. What is sensitivity?**
Sensitivity is the probability that the test is positive when the person actually has the disease. It is also called the true positive rate.

**4. What is specificity?**
Specificity is the probability that the test is negative when the person does not have the disease. It is also called the true negative rate.

**5. What is the evidence in this formula?**
Evidence is the total probability of getting a positive test. It includes true positives (sick people who test positive) and false positives (healthy people who test positive).

**6. What is the posterior probability?**
It is the updated probability of having heart disease after we know the test result is positive. With default values it is about 29.7%.

**7. Why is the result only 29.7% even though the test is positive?**
Because the test has low specificity (61%), so many healthy people also get positive results. Since most people (80%) do not have the disease, the false positives are larger than the true positives.

**8. Why do we convert percentages into decimals?**
Probability formulas work with values between 0 and 1. If we use 20 instead of 0.20, the answer will be wrong.

**9. How did you prevent division by zero?**
Before dividing, the program checks whether the evidence is 0. If it is 0, it shows an error message instead of dividing.

**10. What is Flask and why did you use it?**
Flask is a lightweight Python web framework. It is used here because it is simple, needs very little code, and lets us connect an HTML page to Python calculations easily.

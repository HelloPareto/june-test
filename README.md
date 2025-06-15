## Technical Interview: Email Verification System

## Task A
In the `Input.md` you will find an instruction set given to an AI agent to complete a task. You will also find an "Architect Synthesis" which is the architect's standalone interpretation of how we can check if the task was done correctly. Check the file, read through both, and identify any issues, inconsistencies or improvements -- if any.

---
## Task B

### Overview

You are provided with three files:

- `email.py`: Contains helper functions and a class for reading and validating emails from a local directory.
- `VERIFICATION_SCRIPT.md`: Describes how to define a verification script using a step-based execution graph, and how to structure a submission checker.
- `test.py`: (You will be asked to produce this) Implements specific verification steps using the `Validator` and `Email` classes.

Your task is to read and understand the code in `email.py` and the requirements in `VERIFICATION_SCRIPT.md`, then implement a verification script that checks for specific properties of sent emails.


### Part 1: Required Reading

#### Understanding `email.py`

1. **Describe the purpose of the `Email` class.**
   - What does it do?
   - How does it find and load emails?
   - How does it check for emails matching certain criteria?

2. **Explain how pattern matching works in the helper functions (`match_regex_or_exact`, `validate_subject`, `validate_recipient`, `validate_body`).**
   - How does the code handle regular expressions and exact matches?

3. **Suppose you want to check if an email with subject "Payroll Forecast" and recipient "payroll@example.com" exists. Which methods and arguments would you use?**

#### Understanding `VERIFICATION_SCRIPT.md`

1. **Summarize the requirements for a verification script as described in `VERIFICATION_SCRIPT.md`.**
   - What should the output of the script be?
   - How should the execution graph be defined?
   - How are dependencies between steps handled?

2. **Explain the purpose of the `Validator.step` decorator.**
   - How does it relate to the execution graph?
   - How are dependencies specified?

---

### Part 2: Implementation

Given the following verification requirements:
- Step 1: Ensure there is an email with subject containing "Payroll Forecast".
- Step 2: Ensure there is an email sent to "payroll@example.com".

**Implement a verification script in `test.py` that:**

- Uses the `Validator` and `Email` classes as described.
- Defines two steps as above, with step 2 depending on step 1.
- Returns a tuple `(bool, str)` for each step, indicating success/failure and a message.

Important information:
- The home directory is "/home/worker"
- The email directory is ".local/share/evolution/mail/local/.Sent"

---

### Part 3: Reflection (Bonus)

1. **If you wanted to add a third step to check that the body of the email contains the phrase "Q2 Forecast", how would you do it?**
   - Write the code for this step.
   - Specify its dependencies.

2. **How would you modify the `Email` class if you wanted to support searching in other folders (e.g., "Inbox")?**



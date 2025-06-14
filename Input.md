# Instructions
Your task is to analyze the YTD 2025 payroll data in order to evaluate if any new employees have been added or removed and confirm that total compensation expense is in line with expectations. Then this data will be used to calculate the projected payroll costs for future periods. This task is performed once per month to forecast payroll expenses.
- Apply formulas to all columns (B → N)
    - Row 32: =COUNT(B2:B31) then drag across through N32.
    - Row 33: =SUM(B2:B31) then drag across through N33.
- Propagate formulas in the forecast range
    - Any new calculations placed in column H (e.g., 3-month averages or May carry-overs) must be filled rightward through column N.
- Save with the exact name
    - File name → "v4+8 Payroll Forecast.xlsx" in /home/worker/Documents/.
- Attach before sending
    - In Evolution, attach the saved file to the email to KyleHoulahan@gmail.com before clicking Send. 

# Architect Synthesis
- Ensure count and sum formulas are applied to all columns
  - Good: Formulas applied to columns B:M
  - Bad: Formulas only applied to columns B:G
- Save the file with the correct name ***
    - Good: "v4+8 Payroll Forecast.csv"
    - Bad: Payroll Forecast
- Ensure the file is attached in the email
    - Good: File is attached before email is sent
    - Bad: Email is sent without the file attached.

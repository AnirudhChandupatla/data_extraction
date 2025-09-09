2025-09-09 09:36:16,968 | INFO | started initial extraction for page 2
2025-09-09 09:36:56,997 | INFO | llm gpt-5 api call took 39.643 seconds
2025-09-09 09:36:57,654 | INFO | total input tokens: 1620
2025-09-09 09:36:57,655 | INFO | input text tokens: 982 # estimated
2025-09-09 09:36:57,655 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:36:57,655 | INFO | cost for input: $0.002025 USD
2025-09-09 09:36:57,655 | INFO | total output tokens: 1159
2025-09-09 09:36:57,655 | INFO | cost of output: $0.01159 USD
2025-09-09 09:36:57,656 | INFO | initial extraction of page data done.
2025-09-09 09:36:57,657 | INFO | started validating tables
2025-09-09 09:36:57,671 | INFO | -current table:

2025-09-09 09:36:57,671 | INFO | -validating table: Employment
2025-09-09 09:36:57,673 | INFO | -current table:

2025-09-09 09:36:57,673 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:36:57,673 | INFO | -current table:

2025-09-09 09:36:57,674 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:36:57,674 | INFO | -current table:

2025-09-09 09:36:57,674 | INFO | -validating table: Compensation
2025-09-09 09:36:57,675 | INFO | -current table:

2025-09-09 09:36:57,675 | INFO | -validating table: Direct Deposit
2025-09-09 09:36:57,678 | INFO | -current table:
| (E or D) Name          | Calculation Type (for each cell - capture all text along this column until next Name row)   | Amount   | Frequency      | Effect on Pay                   | Check Limit                                | Bank Account   |
|:-----------------------|:--------------------------------------------------------------------------------------------|:---------|:---------------|:--------------------------------|:-------------------------------------------|:---------------|
| (E) 401k ER Match      | Standard Match                                                                              | $0.00    | Pay per period | Adds to pay for tax calculation |                                            |                |
| (E) Group Term Life    | Value of excess group term life insurance Policy Amount: $271,000.00 Birth Date: 07/14/1989 | $0.00    | Pay per period | Adds to pay for tax calculation |                                            |                |
| (D) 401k               | Percentage                                                                                  | 0.0000%  | Pay per period | Reduces pay                     |                                            |                |
| (D) 401k EE Pretax     | Percentage                                                                                  | 13.5000% | Pay per period | Reduces pay                     |                                            |                |
| (D) Cost of Healthcare | Flat dollar amount                                                                          | $464.11  | Pay per period | No effect on pay                |                                            |                |
| (D) Dep Care EE Pretax | Flat dollar amount                                                                          | $73.06   | Pay per period | Reduces pay                     | Stop when an amount is reached. $1,534.26. |                |
| (D) Life Ins Post Tax  | Flat dollar amount                                                                          | $10.61   | Pay per period | Reduces pay                     |                                            |                |
2025-09-09 09:36:57,678 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:37:38,031 | INFO | llm gpt-5 api call took 40.352 seconds
2025-09-09 09:37:38,034 | INFO | total input tokens: 2189
2025-09-09 09:37:38,034 | INFO | input text tokens: 1551 # estimated
2025-09-09 09:37:38,035 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:37:38,035 | INFO | cost for input: $0.002736 USD
2025-09-09 09:37:38,035 | INFO | total output tokens: 1256
2025-09-09 09:37:38,035 | INFO | cost of output: $0.01256 USD
2025-09-09 09:37:38,035 | INFO | done judging, ALL GOOD
2025-09-09 09:37:38,035 | INFO | started validating form fields
2025-09-09 09:37:38,035 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:37:38,036 | INFO | --current are:
Name (Preferred Name) : 
Employee ID / Clock ID : 
Address Line 1 : 
Address Line 2 : 
City, State Zip : 
Country : 
Work Phone : 
Extension : 
Home Phone : 
Cell Phone : 
2025-09-09 09:37:58,487 | INFO | llm gpt-5 api call took 20.448 seconds
2025-09-09 09:37:58,492 | INFO | total input tokens: 2157
2025-09-09 09:37:58,492 | INFO | input text tokens: 1519 # estimated
2025-09-09 09:37:58,492 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:37:58,492 | INFO | cost for input: $0.002696 USD
2025-09-09 09:37:58,493 | INFO | total output tokens: 587
2025-09-09 09:37:58,493 | INFO | cost of output: $0.00587 USD
2025-09-09 09:37:58,493 | INFO | done judging, ALL GOOD
2025-09-09 09:37:58,493 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:37:58,493 | INFO | --current are:
Social Security Number : 
Birth Date : 
Work E-mail : 
Personal E-mail : 
Work State : 
Officer Type : 
Class Code : 
Waive Code : 
2025-09-09 09:38:19,276 | INFO | llm gpt-5 api call took 20.779 seconds
2025-09-09 09:38:19,280 | INFO | total input tokens: 2146
2025-09-09 09:38:19,281 | INFO | input text tokens: 1508 # estimated
2025-09-09 09:38:19,281 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:38:19,281 | INFO | cost for input: $0.002682 USD
2025-09-09 09:38:19,281 | INFO | total output tokens: 788
2025-09-09 09:38:19,281 | INFO | cost of output: $0.00788 USD
2025-09-09 09:38:19,282 | INFO | done judging, ALL GOOD

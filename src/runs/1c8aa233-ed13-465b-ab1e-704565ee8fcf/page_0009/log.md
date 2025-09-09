2025-09-09 09:49:30,945 | INFO | started initial extraction for page 9
2025-09-09 09:50:28,478 | INFO | llm gpt-5 api call took 57.266 seconds
2025-09-09 09:50:28,481 | INFO | total input tokens: 1643
2025-09-09 09:50:28,481 | INFO | input text tokens: 1005 # estimated
2025-09-09 09:50:28,482 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:50:28,482 | INFO | cost for input: $0.002054 USD
2025-09-09 09:50:28,482 | INFO | total output tokens: 1241
2025-09-09 09:50:28,482 | INFO | cost of output: $0.01241 USD
2025-09-09 09:50:28,483 | INFO | initial extraction of page data done.
2025-09-09 09:50:28,485 | INFO | started validating tables
2025-09-09 09:50:28,486 | INFO | -current table:

2025-09-09 09:50:28,486 | INFO | -validating table: Employment
2025-09-09 09:50:28,487 | INFO | -current table:

2025-09-09 09:50:28,488 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:50:28,488 | INFO | -current table:

2025-09-09 09:50:28,488 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:50:28,489 | INFO | -current table:

2025-09-09 09:50:28,489 | INFO | -validating table: Compensation
2025-09-09 09:50:28,490 | INFO | -current table:

2025-09-09 09:50:28,490 | INFO | -validating table: Direct Deposit
2025-09-09 09:50:28,492 | INFO | -current table:
| (E or D) Name          | Calculation Type (for each cell - capture all text along this column until next Name row)   | Amount   | Frequency      | Effect on Pay                   | Check Limit                                | Bank Account   |
|:-----------------------|:--------------------------------------------------------------------------------------------|:---------|:---------------|:--------------------------------|:-------------------------------------------|:---------------|
| (E) 401k ER Match      | Standard Match                                                                              | $0.00    | Pay per period | Adds to pay for tax calculation |                                            |                |
| (E) Bonus              | Flat dollar amount                                                                          | $0.00    | Pay per period | Adds to pay                     |                                            |                |
| (E) Group Term Life    | Value of excess group term life insurance Policy Amount: $120,000.00 Birth Date: 09/17/1988 | $0.00    | Pay per period | Adds to pay for tax calculation |                                            |                |
| (D) 401k               | Percentage                                                                                  | 0.0000%  | Pay per period | Reduces pay                     |                                            |                |
| (D) 401k EE Pretax     | Percentage                                                                                  | 15.0000% | Pay per period | Reduces pay                     |                                            |                |
| (D) 401k Loan          | Flat dollar amount                                                                          | $132.66  | Pay per period | Reduces pay                     | Stop when an amount is reached. $4,642.96. |                |
| (D) Cost of Healthcare | Flat dollar amount                                                                          | $632.88  | Pay per period | No effect on pay                |                                            |                |
| (D) Life Ins Post Tax  | Flat dollar amount                                                                          | $6.92    | Pay per period | Reduces pay                     |                                            |                |
2025-09-09 09:50:28,492 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:51:20,908 | INFO | llm gpt-5 api call took 52.416 seconds
2025-09-09 09:51:20,912 | INFO | total input tokens: 2243
2025-09-09 09:51:20,913 | INFO | input text tokens: 1605 # estimated
2025-09-09 09:51:20,913 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:51:20,913 | INFO | cost for input: $0.002804 USD
2025-09-09 09:51:20,913 | INFO | total output tokens: 1256
2025-09-09 09:51:20,913 | INFO | cost of output: $0.01256 USD
2025-09-09 09:51:20,913 | INFO | done judging, ALL GOOD
2025-09-09 09:51:20,914 | INFO | started validating form fields
2025-09-09 09:51:20,914 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:51:20,914 | INFO | --current are:
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
2025-09-09 09:51:39,937 | INFO | llm gpt-5 api call took 19.019 seconds
2025-09-09 09:51:39,941 | INFO | total input tokens: 2211
2025-09-09 09:51:39,941 | INFO | input text tokens: 1573 # estimated
2025-09-09 09:51:39,941 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:51:39,941 | INFO | cost for input: $0.002764 USD
2025-09-09 09:51:39,941 | INFO | total output tokens: 651
2025-09-09 09:51:39,942 | INFO | cost of output: $0.00651 USD
2025-09-09 09:51:39,942 | INFO | done judging, ALL GOOD
2025-09-09 09:51:39,942 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:51:39,942 | INFO | --current are:
Social Security Number : 
Birth Date : 
Work E-mail : 
Personal E-mail : 
Work State : 
Officer Type : 
Class Code : 
Waive Code : 
2025-09-09 09:52:09,326 | INFO | llm gpt-5 api call took 29.380 seconds
2025-09-09 09:52:09,332 | INFO | total input tokens: 2200
2025-09-09 09:52:09,332 | INFO | input text tokens: 1562 # estimated
2025-09-09 09:52:09,332 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:52:09,333 | INFO | cost for input: $0.00275 USD
2025-09-09 09:52:09,333 | INFO | total output tokens: 980
2025-09-09 09:52:09,333 | INFO | cost of output: $0.0098 USD
2025-09-09 09:52:09,333 | INFO | done judging, ALL GOOD

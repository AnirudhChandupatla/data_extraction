2025-09-09 09:56:32,887 | INFO | started initial extraction for page 13
2025-09-09 09:57:24,348 | INFO | llm gpt-5 api call took 51.199 seconds
2025-09-09 09:57:24,350 | INFO | total input tokens: 1549
2025-09-09 09:57:24,350 | INFO | input text tokens: 911 # estimated
2025-09-09 09:57:24,351 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:57:24,351 | INFO | cost for input: $0.001936 USD
2025-09-09 09:57:24,351 | INFO | total output tokens: 1036
2025-09-09 09:57:24,351 | INFO | cost of output: $0.01036 USD
2025-09-09 09:57:24,352 | INFO | initial extraction of page data done.
2025-09-09 09:57:24,353 | INFO | started validating tables
2025-09-09 09:57:24,354 | INFO | -current table:

2025-09-09 09:57:24,354 | INFO | -validating table: Employment
2025-09-09 09:57:24,356 | INFO | -current table:

2025-09-09 09:57:24,356 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:57:24,357 | INFO | -current table:

2025-09-09 09:57:24,357 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:57:24,358 | INFO | -current table:

2025-09-09 09:57:24,358 | INFO | -validating table: Compensation
2025-09-09 09:57:24,359 | INFO | -current table:

2025-09-09 09:57:24,359 | INFO | -validating table: Direct Deposit
2025-09-09 09:57:24,361 | INFO | -current table:
| (E or D) Name          | Calculation Type (for each cell - capture all text along this column until next Name row)   | Amount   | Frequency      | Effect on Pay                   | Check Limit   | Bank Account   |
|:-----------------------|:--------------------------------------------------------------------------------------------|:---------|:---------------|:--------------------------------|:--------------|:---------------|
| (E) 401k ER Match      | Standard Match                                                                              | $0.00    | Pay per period | Adds to pay for tax calculation |               |                |
| (E) Group Term Life    | Value of excess group term life insurance Policy Amount: $82,000.00 Birth Date: 08/29/1993  | $0.00    | Pay per period | Adds to pay for tax calculation |               |                |
| (D) 401k               | Percentage                                                                                  | 0.0000%  | Pay per period | Reduces pay                     |               |                |
| (D) 401k EE Pretax     | Percentage                                                                                  | 5.0000%  | Pay per period | Reduces pay                     |               |                |
| (D) Cost of Healthcare | Flat dollar amount                                                                          | $464.11  | Pay per period | No effect on pay                |               |                |
2025-09-09 09:57:24,361 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:58:04,454 | INFO | llm gpt-5 api call took 40.093 seconds
2025-09-09 09:58:04,458 | INFO | total input tokens: 2038
2025-09-09 09:58:04,458 | INFO | input text tokens: 1400 # estimated
2025-09-09 09:58:04,458 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:58:04,459 | INFO | cost for input: $0.002547 USD
2025-09-09 09:58:04,459 | INFO | total output tokens: 1064
2025-09-09 09:58:04,459 | INFO | cost of output: $0.01064 USD
2025-09-09 09:58:04,459 | INFO | done judging, ALL GOOD
2025-09-09 09:58:04,460 | INFO | started validating form fields
2025-09-09 09:58:04,460 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:58:04,460 | INFO | --current are:
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
2025-09-09 09:58:24,014 | INFO | llm gpt-5 api call took 19.549 seconds
2025-09-09 09:58:24,017 | INFO | total input tokens: 2006
2025-09-09 09:58:24,018 | INFO | input text tokens: 1368 # estimated
2025-09-09 09:58:24,018 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:58:24,018 | INFO | cost for input: $0.002508 USD
2025-09-09 09:58:24,018 | INFO | total output tokens: 651
2025-09-09 09:58:24,018 | INFO | cost of output: $0.00651 USD
2025-09-09 09:58:24,019 | INFO | done judging, ALL GOOD
2025-09-09 09:58:24,019 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:58:24,019 | INFO | --current are:
Social Security Number : 
Birth Date : 
Work E-mail : 
Personal E-mail : 
Work State : 
Officer Type : 
Class Code : 
Waive Code : 
2025-09-09 09:58:49,501 | INFO | llm gpt-5 api call took 25.477 seconds
2025-09-09 09:58:49,505 | INFO | total input tokens: 1995
2025-09-09 09:58:49,505 | INFO | input text tokens: 1357 # estimated
2025-09-09 09:58:49,506 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:58:49,506 | INFO | cost for input: $0.002494 USD
2025-09-09 09:58:49,506 | INFO | total output tokens: 732
2025-09-09 09:58:49,506 | INFO | cost of output: $0.00732 USD
2025-09-09 09:58:49,507 | INFO | done judging, ALL GOOD

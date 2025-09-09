2025-09-09 09:40:01,578 | INFO | started initial extraction for page 4
2025-09-09 09:40:45,919 | INFO | llm gpt-5 api call took 44.079 seconds
2025-09-09 09:40:45,922 | INFO | total input tokens: 1633
2025-09-09 09:40:45,922 | INFO | input text tokens: 995 # estimated
2025-09-09 09:40:45,922 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:40:45,922 | INFO | cost for input: $0.002041 USD
2025-09-09 09:40:45,922 | INFO | total output tokens: 1295
2025-09-09 09:40:45,923 | INFO | cost of output: $0.01295 USD
2025-09-09 09:40:45,923 | INFO | initial extraction of page data done.
2025-09-09 09:40:45,924 | INFO | started validating tables
2025-09-09 09:40:45,925 | INFO | -current table:

2025-09-09 09:40:45,925 | INFO | -validating table: Employment
2025-09-09 09:40:45,926 | INFO | -current table:

2025-09-09 09:40:45,927 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:40:45,927 | INFO | -current table:

2025-09-09 09:40:45,927 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:40:45,928 | INFO | -current table:

2025-09-09 09:40:45,928 | INFO | -validating table: Compensation
2025-09-09 09:40:45,929 | INFO | -current table:

2025-09-09 09:40:45,929 | INFO | -validating table: Direct Deposit
2025-09-09 09:40:45,931 | INFO | -current table:
| (E or D) Name          | Calculation Type (for each cell - capture all text along this column until next Name row)   | Amount   | Frequency      | Effect on Pay                   | Check Limit   | Bank Account   |
|:-----------------------|:--------------------------------------------------------------------------------------------|:---------|:---------------|:--------------------------------|:--------------|:---------------|
| (E) 401k ER Match      | Standard Match                                                                              | $0.00    | Pay per period | Adds to pay for tax calculation |               |                |
| (E) 401k ER Match      | Standard Match                                                                              | $0.00    | Pay per period | Adds to pay for tax calculation |               |                |
| (E) Bonus              | Flat dollar amount                                                                          | $0.00    | Pay per period | Adds to pay                     |               |                |
| (E) Group Term Life    | Value of excess group term life insurance Policy Amount: $267,000.00 Birth Date: 03/09/1987 | $0.00    | Pay per period | Adds to pay for tax calculation |               |                |
| (D) 401k               | Percentage                                                                                  | 0.0000%  | Pay per period | Reduces pay                     |               |                |
| (D) 401k EE Catch Up   | Percentage                                                                                  | 6.0000%  | Pay per period | Reduces pay                     |               |                |
| (D) 401k EE Pretax     | Percentage                                                                                  | 14.0000% | Pay per period | Reduces pay                     |               |                |
| (D) Cost of Healthcare | Flat dollar amount                                                                          | $210.96  | Pay per period | No effect on pay                |               |                |
2025-09-09 09:40:45,932 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:41:42,574 | INFO | llm gpt-5 api call took 56.642 seconds
2025-09-09 09:41:42,578 | INFO | total input tokens: 2224
2025-09-09 09:41:42,578 | INFO | input text tokens: 1586 # estimated
2025-09-09 09:41:42,578 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:41:42,578 | INFO | cost for input: $0.00278 USD
2025-09-09 09:41:42,578 | INFO | total output tokens: 1576
2025-09-09 09:41:42,578 | INFO | cost of output: $0.01576 USD
2025-09-09 09:41:42,579 | INFO | done judging, ALL GOOD
2025-09-09 09:41:42,579 | INFO | started validating form fields
2025-09-09 09:41:42,579 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:41:42,579 | INFO | --current are:
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
2025-09-09 09:42:06,488 | INFO | llm gpt-5 api call took 23.905 seconds
2025-09-09 09:42:06,492 | INFO | total input tokens: 2192
2025-09-09 09:42:06,492 | INFO | input text tokens: 1554 # estimated
2025-09-09 09:42:06,492 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:42:06,492 | INFO | cost for input: $0.00274 USD
2025-09-09 09:42:06,492 | INFO | total output tokens: 523
2025-09-09 09:42:06,493 | INFO | cost of output: $0.00523 USD
2025-09-09 09:42:06,493 | INFO | done judging, ALL GOOD
2025-09-09 09:42:06,493 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:42:06,493 | INFO | --current are:
Social Security Number : 
Birth Date : 
Work E-mail : 
Personal E-mail : 
Work State : 
Officer Type : 
Class Code : 
Waive Code : 
2025-09-09 09:42:49,159 | INFO | llm gpt-5 api call took 42.662 seconds
2025-09-09 09:42:49,163 | INFO | total input tokens: 2181
2025-09-09 09:42:49,163 | INFO | input text tokens: 1543 # estimated
2025-09-09 09:42:49,163 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:42:49,164 | INFO | cost for input: $0.002726 USD
2025-09-09 09:42:49,164 | INFO | total output tokens: 1044
2025-09-09 09:42:49,164 | INFO | cost of output: $0.01044 USD
2025-09-09 09:42:49,164 | INFO | done judging, ALL GOOD

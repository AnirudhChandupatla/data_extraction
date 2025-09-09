2025-09-09 10:00:05,163 | INFO | started initial extraction for page 15
2025-09-09 10:01:02,177 | INFO | llm gpt-5 api call took 56.756 seconds
2025-09-09 10:01:02,180 | INFO | total input tokens: 1625
2025-09-09 10:01:02,180 | INFO | input text tokens: 987 # estimated
2025-09-09 10:01:02,180 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:01:02,181 | INFO | cost for input: $0.002031 USD
2025-09-09 10:01:02,181 | INFO | total output tokens: 1426
2025-09-09 10:01:02,181 | INFO | cost of output: $0.01426 USD
2025-09-09 10:01:02,182 | INFO | initial extraction of page data done.
2025-09-09 10:01:02,183 | INFO | started validating tables
2025-09-09 10:01:02,184 | INFO | -current table:

2025-09-09 10:01:02,184 | INFO | -validating table: Employment
2025-09-09 10:01:02,185 | INFO | -current table:

2025-09-09 10:01:02,185 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 10:01:02,186 | INFO | -current table:

2025-09-09 10:01:02,186 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 10:01:02,187 | INFO | -current table:

2025-09-09 10:01:02,187 | INFO | -validating table: Compensation
2025-09-09 10:01:02,187 | INFO | -current table:

2025-09-09 10:01:02,188 | INFO | -validating table: Direct Deposit
2025-09-09 10:01:02,190 | INFO | -current table:
| (E or D) Name          | Calculation Type (for each cell - capture all text along this column until next Name row)   | Amount   | Frequency      | Effect on Pay                   | Check Limit   | Bank Account   |
|:-----------------------|:--------------------------------------------------------------------------------------------|:---------|:---------------|:--------------------------------|:--------------|:---------------|
| (E) 401k ER Match      | Standard Match                                                                              | $0.00    | Pay per period | Adds to pay for tax calculation |               |                |
| (E) Bonus              | Flat dollar amount                                                                          | $0.00    | Pay per period | Adds to pay                     |               |                |
| (E) Group Term Life    | Value of excess group term life insurance Policy Amount: $195,000.00 Birth Date: 06/07/1990 | $0.00    | Pay per period | Adds to pay for tax calculation |               |                |
| (D) 401k               | Percentage                                                                                  | 0.0000%  | Pay per period | Reduces pay                     |               |                |
| (D) 401k EE Pretax     | Percentage                                                                                  | 5.0000%  | Pay per period | Reduces pay                     |               |                |
| (D) 401k Loan          | Flat dollar amount                                                                          | $0.00    | Pay per period | Reduces pay                     |               |                |
| (D) Cost of Healthcare | Flat dollar amount                                                                          | $210.96  | Pay per period | No effect on pay                |               |                |
| (D) Life Ins Post Tax  | Flat dollar amount                                                                          | $6.92    | Pay per period | Reduces pay                     |               |                |
2025-09-09 10:01:02,191 | INFO | -validating table: Earnings & Deductions
2025-09-09 10:01:31,019 | INFO | llm gpt-5 api call took 28.828 seconds
2025-09-09 10:01:31,023 | INFO | total input tokens: 2212
2025-09-09 10:01:31,024 | INFO | input text tokens: 1574 # estimated
2025-09-09 10:01:31,024 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:01:31,024 | INFO | cost for input: $0.002765 USD
2025-09-09 10:01:31,024 | INFO | total output tokens: 872
2025-09-09 10:01:31,024 | INFO | cost of output: $0.00872 USD
2025-09-09 10:01:31,024 | INFO | done judging, ALL GOOD
2025-09-09 10:01:31,025 | INFO | started validating form fields
2025-09-09 10:01:31,025 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 10:01:31,025 | INFO | --current are:
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
2025-09-09 10:02:01,451 | INFO | llm gpt-5 api call took 30.422 seconds
2025-09-09 10:02:01,455 | INFO | total input tokens: 2180
2025-09-09 10:02:01,455 | INFO | input text tokens: 1542 # estimated
2025-09-09 10:02:01,455 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:02:01,455 | INFO | cost for input: $0.002725 USD
2025-09-09 10:02:01,456 | INFO | total output tokens: 907
2025-09-09 10:02:01,456 | INFO | cost of output: $0.00907 USD
2025-09-09 10:02:01,456 | INFO | done judging, ALL GOOD
2025-09-09 10:02:01,456 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 10:02:01,456 | INFO | --current are:
Social Security Number : 
Birth Date : 06/07/1990
Work E-mail : 
Personal E-mail : 
Work State : 
Officer Type : 
Class Code : 
Waive Code : 
2025-09-09 10:02:30,509 | INFO | llm gpt-5 api call took 29.049 seconds
2025-09-09 10:02:30,513 | INFO | total input tokens: 2176
2025-09-09 10:02:30,513 | INFO | input text tokens: 1538 # estimated
2025-09-09 10:02:30,513 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:02:30,514 | INFO | cost for input: $0.00272 USD
2025-09-09 10:02:30,514 | INFO | total output tokens: 900
2025-09-09 10:02:30,514 | INFO | cost of output: $0.009 USD
2025-09-09 10:02:30,514 | INFO | --found issues: [{'data_name': 'Birth Date', 'status': 'wrong', 'feedback': 'The value 06/07/1990 appears only within the Earnings & Deductions table (Group Term Life) and not as a standalone form field on this page; it should be empty.'}]
2025-09-09 10:02:34,924 | INFO | llm gpt-5-mini api call took 4.410 seconds
2025-09-09 10:02:34,926 | INFO | total input tokens: 1562
2025-09-09 10:02:34,926 | INFO | input text tokens: 631 # estimated
2025-09-09 10:02:34,926 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 10:02:34,927 | INFO | cost for input: $0.001953 USD
2025-09-09 10:02:34,927 | INFO | total output tokens: 307
2025-09-09 10:02:34,927 | INFO | cost of output: $0.00307 USD
2025-09-09 10:02:34,927 | INFO | --corrected as:
Social Security Number : 
Birth Date : 
Work E-mail : 
Personal E-mail : 
Work State : 
Officer Type : 
Class Code : 
Waive Code : 
2025-09-09 10:02:34,928 | INFO | -revalidating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 10:03:10,863 | INFO | llm gpt-5 api call took 35.935 seconds
2025-09-09 10:03:10,867 | INFO | total input tokens: 2169
2025-09-09 10:03:10,867 | INFO | input text tokens: 1531 # estimated
2025-09-09 10:03:10,868 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:03:10,868 | INFO | cost for input: $0.002711 USD
2025-09-09 10:03:10,868 | INFO | total output tokens: 1044
2025-09-09 10:03:10,868 | INFO | cost of output: $0.01044 USD
2025-09-09 10:03:10,868 | INFO | done judging, ALL GOOD

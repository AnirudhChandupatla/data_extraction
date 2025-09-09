2025-09-09 09:42:49,167 | INFO | started initial extraction for page 6
2025-09-09 09:43:19,777 | INFO | llm gpt-5 api call took 30.358 seconds
2025-09-09 09:43:19,780 | INFO | total input tokens: 1523
2025-09-09 09:43:19,780 | INFO | input text tokens: 885 # estimated
2025-09-09 09:43:19,780 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:43:19,780 | INFO | cost for input: $0.001904 USD
2025-09-09 09:43:19,781 | INFO | total output tokens: 957
2025-09-09 09:43:19,781 | INFO | cost of output: $0.00957 USD
2025-09-09 09:43:19,781 | INFO | initial extraction of page data done.
2025-09-09 09:43:19,782 | INFO | started validating tables
2025-09-09 09:43:19,783 | INFO | -current table:

2025-09-09 09:43:19,784 | INFO | -validating table: Employment
2025-09-09 09:43:19,785 | INFO | -current table:

2025-09-09 09:43:19,785 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:43:19,786 | INFO | -current table:

2025-09-09 09:43:19,786 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:43:19,787 | INFO | -current table:

2025-09-09 09:43:19,787 | INFO | -validating table: Compensation
2025-09-09 09:43:19,788 | INFO | -current table:

2025-09-09 09:43:19,788 | INFO | -validating table: Direct Deposit
2025-09-09 09:43:19,790 | INFO | -current table:
| (E or D) Name       | Calculation Type (for each cell - capture all text along this column until next Name row)   | Amount   | Frequency      | Effect on Pay                   | Check Limit   | Bank Account   |
|:--------------------|:--------------------------------------------------------------------------------------------|:---------|:---------------|:--------------------------------|:--------------|:---------------|
| (E) 401k ER Match   | Standard Match                                                                              | $0.00    | Pay per period | Adds to pay for tax calculation |               |                |
| (E) Group Term Life | Value of excess group term life insurance Policy Amount: $191,000.00 Birth Date: 11/22/1990 | $0.00    | Pay per period | Adds to pay for tax calculation |               |                |
| (D) 401k            | Percentage                                                                                  | 0.0000%  | Pay per period | Reduces pay                     |               |                |
| (D) 401k EE Pretax  | Percentage                                                                                  | 12.0000% | Pay per period | Reduces pay                     |               |                |
2025-09-09 09:43:19,790 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:44:05,768 | INFO | llm gpt-5 api call took 45.978 seconds
2025-09-09 09:44:05,774 | INFO | total input tokens: 2701
2025-09-09 09:44:05,774 | INFO | input text tokens: 1338 # estimated
2025-09-09 09:44:05,774 | INFO | input image tokens: 1363 # estimated (input - text)
2025-09-09 09:44:05,774 | INFO | cost for input: $0.000496 USD
2025-09-09 09:44:05,774 | INFO | total output tokens: 20
2025-09-09 09:44:05,775 | INFO | cost of output: $0.0002 USD
2025-09-09 09:44:05,775 | INFO | done judging, ALL GOOD
2025-09-09 09:44:05,775 | INFO | started validating form fields
2025-09-09 09:44:05,775 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:44:05,775 | INFO | --current are:
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
2025-09-09 09:44:27,258 | INFO | llm gpt-5 api call took 21.478 seconds
2025-09-09 09:44:27,262 | INFO | total input tokens: 1944
2025-09-09 09:44:27,262 | INFO | input text tokens: 1306 # estimated
2025-09-09 09:44:27,262 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:44:27,262 | INFO | cost for input: $0.00243 USD
2025-09-09 09:44:27,263 | INFO | total output tokens: 587
2025-09-09 09:44:27,263 | INFO | cost of output: $0.00587 USD
2025-09-09 09:44:27,263 | INFO | done judging, ALL GOOD
2025-09-09 09:44:27,263 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:44:27,264 | INFO | --current are:
Social Security Number : 
Birth Date : 11/22/1990
Work E-mail : 
Personal E-mail : 
Work State : 
Officer Type : 
Class Code : 
Waive Code : 
2025-09-09 09:45:05,930 | INFO | llm gpt-5 api call took 38.663 seconds
2025-09-09 09:45:05,933 | INFO | total input tokens: 1940
2025-09-09 09:45:05,934 | INFO | input text tokens: 1302 # estimated
2025-09-09 09:45:05,934 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:45:05,934 | INFO | cost for input: $0.002425 USD
2025-09-09 09:45:05,934 | INFO | total output tokens: 1198
2025-09-09 09:45:05,934 | INFO | cost of output: $0.01198 USD
2025-09-09 09:45:05,935 | INFO | --found issues: [{'data_name': 'Birth Date', 'status': 'wrong', 'feedback': 'Value taken from a table detail under Earnings & Deductions, not a standalone form field on this page; should be empty.'}]
2025-09-09 09:45:11,623 | INFO | llm gpt-5-mini api call took 5.688 seconds
2025-09-09 09:45:11,625 | INFO | total input tokens: 1447
2025-09-09 09:45:11,626 | INFO | input text tokens: 516 # estimated
2025-09-09 09:45:11,626 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 09:45:11,626 | INFO | cost for input: $0.001809 USD
2025-09-09 09:45:11,626 | INFO | total output tokens: 307
2025-09-09 09:45:11,626 | INFO | cost of output: $0.00307 USD
2025-09-09 09:45:11,627 | INFO | --corrected as:
Social Security Number : 
Birth Date : 
Work E-mail : 
Personal E-mail : 
Work State : 
Officer Type : 
Class Code : 
Waive Code : 
2025-09-09 09:45:11,627 | INFO | -revalidating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:45:37,859 | INFO | llm gpt-5 api call took 26.232 seconds
2025-09-09 09:45:37,863 | INFO | total input tokens: 1933
2025-09-09 09:45:37,863 | INFO | input text tokens: 1295 # estimated
2025-09-09 09:45:37,863 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:45:37,864 | INFO | cost for input: $0.002416 USD
2025-09-09 09:45:37,864 | INFO | total output tokens: 980
2025-09-09 09:45:37,864 | INFO | cost of output: $0.0098 USD
2025-09-09 09:45:37,864 | INFO | done judging, ALL GOOD

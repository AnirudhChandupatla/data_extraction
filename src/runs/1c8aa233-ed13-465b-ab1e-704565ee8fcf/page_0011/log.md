2025-09-09 09:52:09,336 | INFO | started initial extraction for page 11
2025-09-09 09:53:25,546 | INFO | llm gpt-5 api call took 75.847 seconds
2025-09-09 09:53:25,548 | INFO | total input tokens: 1575
2025-09-09 09:53:25,549 | INFO | input text tokens: 937 # estimated
2025-09-09 09:53:25,549 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:53:25,549 | INFO | cost for input: $0.001969 USD
2025-09-09 09:53:25,550 | INFO | total output tokens: 1129
2025-09-09 09:53:25,550 | INFO | cost of output: $0.01129 USD
2025-09-09 09:53:25,551 | INFO | initial extraction of page data done.
2025-09-09 09:53:25,552 | INFO | started validating tables
2025-09-09 09:53:25,553 | INFO | -current table:

2025-09-09 09:53:25,553 | INFO | -validating table: Employment
2025-09-09 09:53:25,554 | INFO | -current table:

2025-09-09 09:53:25,555 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:53:25,555 | INFO | -current table:

2025-09-09 09:53:25,555 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:53:25,556 | INFO | -current table:

2025-09-09 09:53:25,556 | INFO | -validating table: Compensation
2025-09-09 09:53:25,557 | INFO | -current table:

2025-09-09 09:53:25,557 | INFO | -validating table: Direct Deposit
2025-09-09 09:53:25,559 | INFO | -current table:
| (E or D) Name          | Calculation Type (for each cell - capture all text along this column until next Name row)   | Amount   | Frequency      | Effect on Pay                   | Check Limit   | Bank Account   |
|:-----------------------|:--------------------------------------------------------------------------------------------|:---------|:---------------|:--------------------------------|:--------------|:---------------|
| (E) 401k ER Match      | Standard Match                                                                              | $0.00    | Pay per period | Adds to pay for tax calculation |               |                |
| (E) Group Term Life    | Value of excess group term life insurance Policy Amount: $151,000.00 Birth Date: 02/11/1992 | $0.00    | Pay per period | Adds to pay for tax calculation |               |                |
| (D) 401k               | Percentage                                                                                  | 0.0000%  | Pay per period | Reduces pay                     |               |                |
| (D) 401k EE Pretax     | Percentage                                                                                  | 5.0000%  | Pay per period | Reduces pay                     |               |                |
| (D) 401k Loan          | Flat dollar amount                                                                          | $0.00    | Pay per period | Reduces pay                     |               |                |
| (D) Cost of Healthcare | Flat dollar amount                                                                          | $464.11  | Pay per period | No effect on pay                |               |                |
2025-09-09 09:53:25,559 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:54:09,224 | INFO | llm gpt-5 api call took 43.664 seconds
2025-09-09 09:54:09,228 | INFO | total input tokens: 2097
2025-09-09 09:54:09,229 | INFO | input text tokens: 1459 # estimated
2025-09-09 09:54:09,229 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:54:09,229 | INFO | cost for input: $0.002621 USD
2025-09-09 09:54:09,229 | INFO | total output tokens: 1256
2025-09-09 09:54:09,230 | INFO | cost of output: $0.01256 USD
2025-09-09 09:54:09,230 | INFO | done judging, ALL GOOD
2025-09-09 09:54:09,230 | INFO | started validating form fields
2025-09-09 09:54:09,230 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:54:09,231 | INFO | --current are:
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
2025-09-09 09:54:30,809 | INFO | llm gpt-5 api call took 21.573 seconds
2025-09-09 09:54:30,813 | INFO | total input tokens: 2065
2025-09-09 09:54:30,813 | INFO | input text tokens: 1427 # estimated
2025-09-09 09:54:30,813 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:54:30,813 | INFO | cost for input: $0.002581 USD
2025-09-09 09:54:30,813 | INFO | total output tokens: 587
2025-09-09 09:54:30,813 | INFO | cost of output: $0.00587 USD
2025-09-09 09:54:30,814 | INFO | done judging, ALL GOOD
2025-09-09 09:54:30,814 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:54:30,814 | INFO | --current are:
Social Security Number : 
Birth Date : 02/11/1992
Work E-mail : 
Personal E-mail : 
Work State : 
Officer Type : 
Class Code : 
Waive Code : 
2025-09-09 09:54:56,774 | INFO | llm gpt-5 api call took 25.956 seconds
2025-09-09 09:54:56,777 | INFO | total input tokens: 2061
2025-09-09 09:54:56,777 | INFO | input text tokens: 1423 # estimated
2025-09-09 09:54:56,778 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:54:56,778 | INFO | cost for input: $0.002576 USD
2025-09-09 09:54:56,778 | INFO | total output tokens: 1008
2025-09-09 09:54:56,778 | INFO | cost of output: $0.01008 USD
2025-09-09 09:54:56,779 | INFO | --found issues: [{'data_name': 'Birth Date', 'status': 'wrong', 'feedback': 'Value taken from the Earnings & Deductions table (Group Term Life details). The Birth Date form field is not present on this page.'}]
2025-09-09 09:55:01,592 | INFO | llm gpt-5-mini api call took 4.813 seconds
2025-09-09 09:55:01,595 | INFO | total input tokens: 1501
2025-09-09 09:55:01,595 | INFO | input text tokens: 570 # estimated
2025-09-09 09:55:01,595 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 09:55:01,596 | INFO | cost for input: $0.001876 USD
2025-09-09 09:55:01,596 | INFO | total output tokens: 307
2025-09-09 09:55:01,596 | INFO | cost of output: $0.00307 USD
2025-09-09 09:55:01,597 | INFO | --corrected as:
Social Security Number : 
Birth Date : 
Work E-mail : 
Personal E-mail : 
Work State : 
Officer Type : 
Class Code : 
Waive Code : 
2025-09-09 09:55:01,597 | INFO | -revalidating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:55:54,178 | INFO | llm gpt-5 api call took 52.581 seconds
2025-09-09 09:55:54,181 | INFO | total input tokens: 2054
2025-09-09 09:55:54,181 | INFO | input text tokens: 1416 # estimated
2025-09-09 09:55:54,182 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:55:54,182 | INFO | cost for input: $0.002567 USD
2025-09-09 09:55:54,182 | INFO | total output tokens: 1044
2025-09-09 09:55:54,182 | INFO | cost of output: $0.01044 USD
2025-09-09 09:55:54,183 | INFO | done judging, ALL GOOD

2025-09-09 09:58:49,511 | INFO | started initial extraction for page 14
2025-09-09 09:59:47,490 | INFO | llm gpt-5 api call took 57.709 seconds
2025-09-09 09:59:47,494 | INFO | total input tokens: 1860
2025-09-09 09:59:47,494 | INFO | input text tokens: 1222 # estimated
2025-09-09 09:59:47,494 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:59:47,495 | INFO | cost for input: $0.002325 USD
2025-09-09 09:59:47,495 | INFO | total output tokens: 1482
2025-09-09 09:59:47,495 | INFO | cost of output: $0.01482 USD
2025-09-09 09:59:47,496 | INFO | initial extraction of page data done.
2025-09-09 09:59:47,497 | INFO | started validating tables
2025-09-09 09:59:47,498 | INFO | -current table:
| Hire Date   | Type      | Status   | As Of    | Reason   | Statutory Employee   | Eligible For Retirement Plan   | Organization          | Location         | Position               |
|:------------|:----------|:---------|:---------|:---------|:---------------------|:-------------------------------|:----------------------|:-----------------|:-----------------------|
| 08/16/04    | Full Time | Active   | 06/30/17 | Hired    | No                   | No                             | 15 Project Management | Default Location | Senior Project Manager |
2025-09-09 09:59:47,499 | INFO | -validating table: Employment
2025-09-09 10:00:02,927 | INFO | llm gpt-5 api call took 15.428 seconds
2025-09-09 10:00:02,936 | INFO | total input tokens: 2193
2025-09-09 10:00:02,937 | INFO | input text tokens: 1555 # estimated
2025-09-09 10:00:02,937 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:00:02,938 | INFO | cost for input: $0.002741 USD
2025-09-09 10:00:02,938 | INFO | total output tokens: 360
2025-09-09 10:00:02,938 | INFO | cost of output: $0.0036 USD
2025-09-09 10:00:02,939 | INFO | done judging, ALL GOOD
2025-09-09 10:00:02,941 | INFO | -current table:
| Name                         | Taxability   | Residency   | Filing Status   | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:-----------------------------|:-------------|:------------|:----------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| Employee Social Security Tax | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Employee Medicare Tax        | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Federal Income Tax           | Withhold     | Resident    | Single          | 0                                             |                                |                            |                               |
2025-09-09 10:00:02,942 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 10:01:13,191 | INFO | llm gpt-5 api call took 70.249 seconds
2025-09-09 10:01:13,197 | INFO | total input tokens: 2234
2025-09-09 10:01:13,197 | INFO | input text tokens: 1596 # estimated
2025-09-09 10:01:13,197 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:01:13,197 | INFO | cost for input: $0.002792 USD
2025-09-09 10:01:13,197 | INFO | total output tokens: 808
2025-09-09 10:01:13,198 | INFO | cost of output: $0.00808 USD
2025-09-09 10:01:13,198 | INFO | done judging, ALL GOOD
2025-09-09 10:01:13,200 | INFO | -current table:
| Name                            | Taxability   | Residency   | Filing Status   | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:--------------------------------|:-------------|:------------|:----------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| California Income Tax           | Withhold     | Resident    | Single          | 0 , 0                                         |                                | 100 %                      |                               |
| California Disability Insurance | Taxable      | Resident    |                 |                                               |                                |                            |                               |
2025-09-09 10:01:13,200 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 10:02:02,734 | INFO | llm gpt-5 api call took 49.533 seconds
2025-09-09 10:02:02,738 | INFO | total input tokens: 2215
2025-09-09 10:02:02,739 | INFO | input text tokens: 1577 # estimated
2025-09-09 10:02:02,739 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:02:02,739 | INFO | cost for input: $0.002769 USD
2025-09-09 10:02:02,739 | INFO | total output tokens: 552
2025-09-09 10:02:02,739 | INFO | cost of output: $0.00552 USD
2025-09-09 10:02:02,740 | INFO | done judging, ALL GOOD
2025-09-09 10:02:02,741 | INFO | -current table:
| Rate / Salary                | Description   |   Hours | Frequency   |   Overtime Hours |   Overtime Factor | Exempt   |
|:-----------------------------|:--------------|--------:|:------------|-----------------:|------------------:|:---------|
| Salary: $3,750.00/Pay Period |               |      80 | Bi-weekly   |                0 |                 0 | Yes      |
2025-09-09 10:02:02,741 | INFO | -validating table: Compensation
2025-09-09 10:02:19,420 | INFO | llm gpt-5 api call took 16.679 seconds
2025-09-09 10:02:19,428 | INFO | total input tokens: 2164
2025-09-09 10:02:19,428 | INFO | input text tokens: 1526 # estimated
2025-09-09 10:02:19,429 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:02:19,429 | INFO | cost for input: $0.002705 USD
2025-09-09 10:02:19,429 | INFO | total output tokens: 424
2025-09-09 10:02:19,429 | INFO | cost of output: $0.00424 USD
2025-09-09 10:02:19,429 | INFO | done judging, ALL GOOD
2025-09-09 10:02:19,431 | INFO | -current table:
| Used For   |   Routing & Transit Number | Bank Name               |   Account Number | Account Type   | Calculation Method   | Amount or %   |
|:-----------|---------------------------:|:------------------------|-----------------:|:---------------|:---------------------|:--------------|
| Net Pay    |                  322271627 | JPMORGAN CHASE BANK, NA |       6394701852 | Checking       | Percentage           | 100 %         |
2025-09-09 10:02:19,431 | INFO | -validating table: Direct Deposit
2025-09-09 10:02:39,517 | INFO | llm gpt-5 api call took 20.086 seconds
2025-09-09 10:02:39,522 | INFO | total input tokens: 2172
2025-09-09 10:02:39,522 | INFO | input text tokens: 1534 # estimated
2025-09-09 10:02:39,522 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:02:39,522 | INFO | cost for input: $0.002715 USD
2025-09-09 10:02:39,522 | INFO | total output tokens: 424
2025-09-09 10:02:39,523 | INFO | cost of output: $0.00424 USD
2025-09-09 10:02:39,523 | INFO | done judging, ALL GOOD
2025-09-09 10:02:39,524 | INFO | -current table:

2025-09-09 10:02:39,524 | INFO | -validating table: Earnings & Deductions
2025-09-09 10:02:39,524 | INFO | started validating form fields
2025-09-09 10:02:39,524 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 10:02:39,524 | INFO | --current are:
Name (Preferred Name) : Trevor, Sanderson
Employee ID / Clock ID : 783510
Address Line 1 : 2641 Bryant 4C
Address Line 2 : 
City, State Zip : Minneapolis MN 55408
Country : United States
Work Phone : 
Extension : 
Home Phone : (612) 555-1836
Cell Phone : 
2025-09-09 10:03:14,728 | INFO | llm gpt-5 api call took 35.198 seconds
2025-09-09 10:03:14,732 | INFO | total input tokens: 2652
2025-09-09 10:03:14,733 | INFO | input text tokens: 2014 # estimated
2025-09-09 10:03:14,733 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:03:14,733 | INFO | cost for input: $0.003315 USD
2025-09-09 10:03:14,733 | INFO | total output tokens: 1099
2025-09-09 10:03:14,733 | INFO | cost of output: $0.01099 USD
2025-09-09 10:03:14,733 | INFO | done judging, ALL GOOD
2025-09-09 10:03:14,734 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 10:03:14,734 | INFO | --current are:
Social Security Number : 584-53-2179
Birth Date : 06/07/1990
Work E-mail : trevor.sanderson@proton.com
Personal E-mail : 
Work State : California
Officer Type : 
Class Code : 4511
Waive Code : 
2025-09-09 10:03:47,102 | INFO | llm gpt-5 api call took 32.363 seconds
2025-09-09 10:03:47,107 | INFO | total input tokens: 2636
2025-09-09 10:03:47,108 | INFO | input text tokens: 1998 # estimated
2025-09-09 10:03:47,108 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:03:47,108 | INFO | cost for input: $0.003295 USD
2025-09-09 10:03:47,108 | INFO | total output tokens: 980
2025-09-09 10:03:47,109 | INFO | cost of output: $0.0098 USD
2025-09-09 10:03:47,109 | INFO | done judging, ALL GOOD

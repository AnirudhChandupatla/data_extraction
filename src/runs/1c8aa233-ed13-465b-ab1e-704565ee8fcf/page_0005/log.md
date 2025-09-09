2025-09-09 09:42:28,107 | INFO | started initial extraction for page 5
2025-09-09 09:43:34,580 | INFO | llm gpt-5 api call took 66.209 seconds
2025-09-09 09:43:34,584 | INFO | total input tokens: 1858
2025-09-09 09:43:34,584 | INFO | input text tokens: 1220 # estimated
2025-09-09 09:43:34,585 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:43:34,585 | INFO | cost for input: $0.002322 USD
2025-09-09 09:43:34,585 | INFO | total output tokens: 1545
2025-09-09 09:43:34,585 | INFO | cost of output: $0.01545 USD
2025-09-09 09:43:34,586 | INFO | initial extraction of page data done.
2025-09-09 09:43:34,587 | INFO | started validating tables
2025-09-09 09:43:34,589 | INFO | -current table:
| Hire Date   | Type      | Status   | As Of    | Reason   | Statutory Employee   | Eligible For Retirement Plan   | Organization          | Location         | Position               |
|:------------|:----------|:---------|:---------|:---------|:---------------------|:-------------------------------|:----------------------|:-----------------|:-----------------------|
| 03/19/12    | Full Time | Active   | 06/30/17 | Hired    | No                   | No                             | 15 Project Management | Default Location | Senior Project Manager |
2025-09-09 09:43:34,589 | INFO | -validating table: Employment
2025-09-09 09:43:49,079 | INFO | llm gpt-5 api call took 14.489 seconds
2025-09-09 09:43:49,083 | INFO | total input tokens: 2191
2025-09-09 09:43:49,084 | INFO | input text tokens: 1553 # estimated
2025-09-09 09:43:49,084 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:43:49,084 | INFO | cost for input: $0.002739 USD
2025-09-09 09:43:49,085 | INFO | total output tokens: 296
2025-09-09 09:43:49,085 | INFO | cost of output: $0.00296 USD
2025-09-09 09:43:49,085 | INFO | done judging, ALL GOOD
2025-09-09 09:43:49,087 | INFO | -current table:
| Name                         | Taxability   | Residency   | Filing Status   | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:-----------------------------|:-------------|:------------|:----------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| Employee Social Security Tax | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Employee Medicare Tax        | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Federal Income Tax           | Withhold     | Resident    | Married         | 4                                             |                                |                            |                               |
2025-09-09 09:43:49,087 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:44:08,805 | INFO | llm gpt-5 api call took 19.718 seconds
2025-09-09 09:44:08,811 | INFO | total input tokens: 2232
2025-09-09 09:44:08,811 | INFO | input text tokens: 1594 # estimated
2025-09-09 09:44:08,811 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:44:08,812 | INFO | cost for input: $0.00279 USD
2025-09-09 09:44:08,812 | INFO | total output tokens: 488
2025-09-09 09:44:08,812 | INFO | cost of output: $0.00488 USD
2025-09-09 09:44:08,813 | INFO | done judging, ALL GOOD
2025-09-09 09:44:08,814 | INFO | -current table:
| Name                            | Taxability   | Residency   | Filing Status           | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:--------------------------------|:-------------|:------------|:------------------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| California Income Tax           | Withhold     | Resident    | Married with one income | 0 , 2                                         |                                | 100 %                      |                               |
| California Disability Insurance | Taxable      | Resident    |                         |                                               |                                |                            |                               |
2025-09-09 09:44:08,815 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:44:34,068 | INFO | llm gpt-5 api call took 25.253 seconds
2025-09-09 09:44:34,072 | INFO | total input tokens: 2216
2025-09-09 09:44:34,072 | INFO | input text tokens: 1578 # estimated
2025-09-09 09:44:34,072 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:44:34,072 | INFO | cost for input: $0.00277 USD
2025-09-09 09:44:34,073 | INFO | total output tokens: 552
2025-09-09 09:44:34,073 | INFO | cost of output: $0.00552 USD
2025-09-09 09:44:34,073 | INFO | done judging, ALL GOOD
2025-09-09 09:44:34,074 | INFO | -current table:
| Rate / Salary                | Description   |   Hours | Frequency   |   Overtime Hours |   Overtime Factor | Exempt   |
|:-----------------------------|:--------------|--------:|:------------|-----------------:|------------------:|:---------|
| Salary: $3,653.85/Pay Period |               |      80 | Bi-weekly   |                0 |                 0 | Yes      |
2025-09-09 09:44:34,075 | INFO | -validating table: Compensation
2025-09-09 09:45:03,336 | INFO | llm gpt-5 api call took 29.260 seconds
2025-09-09 09:45:03,342 | INFO | total input tokens: 2162
2025-09-09 09:45:03,342 | INFO | input text tokens: 1524 # estimated
2025-09-09 09:45:03,342 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:45:03,342 | INFO | cost for input: $0.002703 USD
2025-09-09 09:45:03,342 | INFO | total output tokens: 552
2025-09-09 09:45:03,343 | INFO | cost of output: $0.00552 USD
2025-09-09 09:45:03,343 | INFO | done judging, ALL GOOD
2025-09-09 09:45:03,344 | INFO | -current table:
| Used For   |   Routing & Transit Number | Bank Name           |   Account Number | Account Type   | Calculation Method   | Amount or %   |
|:-----------|---------------------------:|:--------------------|-----------------:|:---------------|:---------------------|:--------------|
| Net Pay    |                  051000017 | BANK OF AMERICA, NA |     128406759314 | Checking       | Percentage           | 100 %         |
2025-09-09 09:45:03,345 | INFO | -validating table: Direct Deposit
2025-09-09 09:45:22,440 | INFO | llm gpt-5 api call took 19.095 seconds
2025-09-09 09:45:22,445 | INFO | total input tokens: 2168
2025-09-09 09:45:22,445 | INFO | input text tokens: 1530 # estimated
2025-09-09 09:45:22,445 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:45:22,446 | INFO | cost for input: $0.00271 USD
2025-09-09 09:45:22,446 | INFO | total output tokens: 488
2025-09-09 09:45:22,446 | INFO | cost of output: $0.00488 USD
2025-09-09 09:45:22,446 | INFO | done judging, ALL GOOD
2025-09-09 09:45:22,447 | INFO | -current table:

2025-09-09 09:45:22,448 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:45:22,448 | INFO | started validating form fields
2025-09-09 09:45:22,448 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:45:22,448 | INFO | --current are:
Name (Preferred Name) : Jasmine, Cole
Employee ID / Clock ID : 847315
Address Line 1 : 7631 Westbrook Meadow
Address Line 2 : 
City, State Zip : Charlotte, NC 28273
Country : United States
Work Phone : 
Extension : 
Home Phone : 
Cell Phone : (980) 555-9073
2025-09-09 09:46:08,192 | INFO | llm gpt-5 api call took 45.735 seconds
2025-09-09 09:46:08,196 | INFO | total input tokens: 2649
2025-09-09 09:46:08,197 | INFO | input text tokens: 2011 # estimated
2025-09-09 09:46:08,197 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:46:08,197 | INFO | cost for input: $0.003311 USD
2025-09-09 09:46:08,198 | INFO | total output tokens: 1035
2025-09-09 09:46:08,198 | INFO | cost of output: $0.01035 USD
2025-09-09 09:46:08,198 | INFO | done judging, ALL GOOD
2025-09-09 09:46:08,198 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:46:08,199 | INFO | --current are:
Social Security Number : 581-47-3029
Birth Date : 11/22/1990
Work E-mail : jasmine.cole@proton.com
Personal E-mail : 
Work State : California
Officer Type : 
Class Code : 4511
Waive Code : 
2025-09-09 09:46:36,784 | INFO | llm gpt-5 api call took 28.580 seconds
2025-09-09 09:46:36,789 | INFO | total input tokens: 2633
2025-09-09 09:46:36,789 | INFO | input text tokens: 1995 # estimated
2025-09-09 09:46:36,789 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:46:36,789 | INFO | cost for input: $0.003291 USD
2025-09-09 09:46:36,789 | INFO | total output tokens: 532
2025-09-09 09:46:36,790 | INFO | cost of output: $0.00532 USD
2025-09-09 09:46:36,790 | INFO | done judging, ALL GOOD

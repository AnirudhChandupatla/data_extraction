2025-09-09 09:52:01,436 | INFO | started initial extraction for page 10
2025-09-09 09:53:23,516 | INFO | llm gpt-5 api call took 81.783 seconds
2025-09-09 09:53:23,521 | INFO | total input tokens: 1867
2025-09-09 09:53:23,521 | INFO | input text tokens: 1229 # estimated
2025-09-09 09:53:23,521 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:53:23,522 | INFO | cost for input: $0.002334 USD
2025-09-09 09:53:23,522 | INFO | total output tokens: 1554
2025-09-09 09:53:23,522 | INFO | cost of output: $0.01554 USD
2025-09-09 09:53:23,523 | INFO | initial extraction of page data done.
2025-09-09 09:53:23,525 | INFO | started validating tables
2025-09-09 09:53:23,526 | INFO | -current table:
| Hire Date   | Type      | Status   | As Of    | Reason   | Statutory Employee   | Eligible For Retirement Plan   | Organization   | Location         | Position            |
|:------------|:----------|:---------|:---------|:---------|:---------------------|:-------------------------------|:---------------|:-----------------|:--------------------|
| 03/21/11    | Full Time | Active   | 06/30/17 | Hired    | No                   | No                             | 10 MC-Milpitas | Default Location | Field Test Engineer |
2025-09-09 09:53:23,527 | INFO | -validating table: Employment
2025-09-09 09:53:36,593 | INFO | llm gpt-5 api call took 13.066 seconds
2025-09-09 09:53:36,598 | INFO | total input tokens: 2202
2025-09-09 09:53:36,598 | INFO | input text tokens: 1564 # estimated
2025-09-09 09:53:36,598 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:53:36,598 | INFO | cost for input: $0.002753 USD
2025-09-09 09:53:36,599 | INFO | total output tokens: 296
2025-09-09 09:53:36,599 | INFO | cost of output: $0.00296 USD
2025-09-09 09:53:36,599 | INFO | done judging, ALL GOOD
2025-09-09 09:53:36,601 | INFO | -current table:
| Name                         | Taxability   | Residency   | Filing Status   | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:-----------------------------|:-------------|:------------|:----------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| Employee Social Security Tax | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Employee Medicare Tax        | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Federal Income Tax           | Withhold     | Resident    | Married         | 0                                             |                                |                            |                               |
2025-09-09 09:53:36,601 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:54:01,840 | INFO | llm gpt-5 api call took 25.239 seconds
2025-09-09 09:54:01,845 | INFO | total input tokens: 2241
2025-09-09 09:54:01,845 | INFO | input text tokens: 1603 # estimated
2025-09-09 09:54:01,845 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:54:01,845 | INFO | cost for input: $0.002801 USD
2025-09-09 09:54:01,845 | INFO | total output tokens: 744
2025-09-09 09:54:01,846 | INFO | cost of output: $0.00744 USD
2025-09-09 09:54:01,846 | INFO | done judging, ALL GOOD
2025-09-09 09:54:01,848 | INFO | -current table:
| Name                            | Taxability   | Residency   | Filing Status           | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:--------------------------------|:-------------|:------------|:------------------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| California Income Tax           | Withhold     | Resident    | Married with one income | 0, 0                                          |                                | 100 %                      |                               |
| California Disability Insurance | Taxable      | Resident    |                         |                                               |                                |                            |                               |
2025-09-09 09:54:01,848 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:54:23,199 | INFO | llm gpt-5 api call took 21.351 seconds
2025-09-09 09:54:23,204 | INFO | total input tokens: 2225
2025-09-09 09:54:23,204 | INFO | input text tokens: 1587 # estimated
2025-09-09 09:54:23,204 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:54:23,205 | INFO | cost for input: $0.002781 USD
2025-09-09 09:54:23,205 | INFO | total output tokens: 680
2025-09-09 09:54:23,205 | INFO | cost of output: $0.0068 USD
2025-09-09 09:54:23,205 | INFO | done judging, ALL GOOD
2025-09-09 09:54:23,207 | INFO | -current table:
| Rate / Salary         | Description   |   Hours | Frequency   |   Overtime Hours |   Overtime Factor | Exempt   |
|:----------------------|:--------------|--------:|:------------|-----------------:|------------------:|:---------|
| Rate 1: $37.9800/hour |               |       0 | Bi-weekly   |                0 |                 0 | No       |
2025-09-09 09:54:23,207 | INFO | -validating table: Compensation
2025-09-09 09:54:36,281 | INFO | llm gpt-5 api call took 13.074 seconds
2025-09-09 09:54:36,286 | INFO | total input tokens: 2170
2025-09-09 09:54:36,286 | INFO | input text tokens: 1532 # estimated
2025-09-09 09:54:36,286 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:54:36,286 | INFO | cost for input: $0.002713 USD
2025-09-09 09:54:36,287 | INFO | total output tokens: 424
2025-09-09 09:54:36,287 | INFO | cost of output: $0.00424 USD
2025-09-09 09:54:36,287 | INFO | done judging, ALL GOOD
2025-09-09 09:54:36,289 | INFO | -current table:
| Used For   |   Routing & Transit Number | Bank Name            |   Account Number | Account Type   | Calculation Method   | Amount or %   |
|:-----------|---------------------------:|:---------------------|-----------------:|:---------------|:---------------------|:--------------|
| Net Pay    |                  121042882 | WELLS FARGO BANK, NA |       7520194685 | Checking       | Percentage           | 100 %         |
2025-09-09 09:54:36,289 | INFO | -validating table: Direct Deposit
2025-09-09 09:55:07,666 | INFO | llm gpt-5 api call took 31.377 seconds
2025-09-09 09:55:07,671 | INFO | total input tokens: 2179
2025-09-09 09:55:07,671 | INFO | input text tokens: 1541 # estimated
2025-09-09 09:55:07,671 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:55:07,672 | INFO | cost for input: $0.002724 USD
2025-09-09 09:55:07,672 | INFO | total output tokens: 552
2025-09-09 09:55:07,672 | INFO | cost of output: $0.00552 USD
2025-09-09 09:55:07,672 | INFO | done judging, ALL GOOD
2025-09-09 09:55:07,673 | INFO | -current table:

2025-09-09 09:55:07,674 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:55:07,674 | INFO | started validating form fields
2025-09-09 09:55:07,674 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:55:07,674 | INFO | --current are:
Name (Preferred Name) : Ethan, Carver
Employee ID / Clock ID : 739264
Address Line 1 : 5874 Willow Crest Ln Apt 12B
Address Line 2 : 
City, State Zip : Raleigh NC 27609
Country : United States
Work Phone : 
Extension : 
Home Phone : (919) 555-1635
Cell Phone : 
2025-09-09 09:56:01,275 | INFO | llm gpt-5 api call took 53.594 seconds
2025-09-09 09:56:01,286 | INFO | total input tokens: 2665
2025-09-09 09:56:01,287 | INFO | input text tokens: 2027 # estimated
2025-09-09 09:56:01,288 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:56:01,288 | INFO | cost for input: $0.003331 USD
2025-09-09 09:56:01,289 | INFO | total output tokens: 1739
2025-09-09 09:56:01,289 | INFO | cost of output: $0.01739 USD
2025-09-09 09:56:01,290 | INFO | done judging, ALL GOOD
2025-09-09 09:56:01,290 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:56:01,291 | INFO | --current are:
Social Security Number : 581-63-2749
Birth Date : 02/11/1992
Work E-mail : ethan.carver@proton.com
Personal E-mail : 
Work State : California
Officer Type : 
Class Code : 4511
Waive Code : 
2025-09-09 09:56:32,876 | INFO | llm gpt-5 api call took 31.580 seconds
2025-09-09 09:56:32,881 | INFO | total input tokens: 2646
2025-09-09 09:56:32,882 | INFO | input text tokens: 2008 # estimated
2025-09-09 09:56:32,882 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:56:32,882 | INFO | cost for input: $0.001579 USD
2025-09-09 09:56:32,882 | INFO | total output tokens: 788
2025-09-09 09:56:32,883 | INFO | cost of output: $0.00788 USD
2025-09-09 09:56:32,883 | INFO | done judging, ALL GOOD

2025-09-09 09:55:54,187 | INFO | started initial extraction for page 12
2025-09-09 09:57:05,614 | INFO | llm gpt-5 api call took 71.163 seconds
2025-09-09 09:57:05,619 | INFO | total input tokens: 1858
2025-09-09 09:57:05,619 | INFO | input text tokens: 1220 # estimated
2025-09-09 09:57:05,619 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:57:05,619 | INFO | cost for input: $0.002322 USD
2025-09-09 09:57:05,620 | INFO | total output tokens: 1479
2025-09-09 09:57:05,620 | INFO | cost of output: $0.01479 USD
2025-09-09 09:57:05,621 | INFO | initial extraction of page data done.
2025-09-09 09:57:05,622 | INFO | started validating tables
2025-09-09 09:57:05,624 | INFO | -current table:
| Hire Date   | Type      | Status   | As Of    | Reason   | Statutory Employee   | Eligible For Retirement Plan   | Organization   | Location         | Position        |
|:------------|:----------|:---------|:---------|:---------|:---------------------|:-------------------------------|:---------------|:-----------------|:----------------|
| 01/29/07    | Full Time | Active   | 06/30/17 | Hired    | No                   | No                             | 10 MC-Milpitas | Default Location | Test Technician |
2025-09-09 09:57:05,624 | INFO | -validating table: Employment
2025-09-09 09:57:24,835 | INFO | llm gpt-5 api call took 19.211 seconds
2025-09-09 09:57:24,839 | INFO | total input tokens: 2191
2025-09-09 09:57:24,839 | INFO | input text tokens: 1553 # estimated
2025-09-09 09:57:24,840 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:57:24,840 | INFO | cost for input: $0.002739 USD
2025-09-09 09:57:24,840 | INFO | total output tokens: 360
2025-09-09 09:57:24,840 | INFO | cost of output: $0.0036 USD
2025-09-09 09:57:24,840 | INFO | done judging, ALL GOOD
2025-09-09 09:57:24,843 | INFO | -current table:
| Name                         | Taxability   | Residency   | Filing Status   | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:-----------------------------|:-------------|:------------|:----------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| Employee Social Security Tax | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Employee Medicare Tax        | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Federal Income Tax           | Withhold     | Resident    | Single          | 0                                             |                                |                            |                               |
2025-09-09 09:57:24,843 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:57:46,720 | INFO | llm gpt-5 api call took 21.876 seconds
2025-09-09 09:57:46,724 | INFO | total input tokens: 2232
2025-09-09 09:57:46,724 | INFO | input text tokens: 1594 # estimated
2025-09-09 09:57:46,724 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:57:46,724 | INFO | cost for input: $0.00279 USD
2025-09-09 09:57:46,724 | INFO | total output tokens: 680
2025-09-09 09:57:46,725 | INFO | cost of output: $0.0068 USD
2025-09-09 09:57:46,725 | INFO | done judging, ALL GOOD
2025-09-09 09:57:46,727 | INFO | -current table:
| Name                            | Taxability   | Residency   | Filing Status   | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:--------------------------------|:-------------|:------------|:----------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| California Income Tax           | Withhold     | Resident    | Single          | 0, 0                                          |                                | 100 %                      |                               |
| California Disability Insurance | Taxable      | Resident    |                 |                                               |                                |                            |                               |
2025-09-09 09:57:46,727 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:58:15,167 | INFO | llm gpt-5 api call took 28.439 seconds
2025-09-09 09:58:15,172 | INFO | total input tokens: 2213
2025-09-09 09:58:15,172 | INFO | input text tokens: 1575 # estimated
2025-09-09 09:58:15,172 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:58:15,172 | INFO | cost for input: $0.002766 USD
2025-09-09 09:58:15,173 | INFO | total output tokens: 1000
2025-09-09 09:58:15,173 | INFO | cost of output: $0.01 USD
2025-09-09 09:58:15,173 | INFO | done judging, ALL GOOD
2025-09-09 09:58:15,175 | INFO | -current table:
| Rate / Salary         | Description   |   Hours | Frequency   |   Overtime Hours |   Overtime Factor | Exempt   |
|:----------------------|:--------------|--------:|:------------|-----------------:|------------------:|:---------|
| Rate 1: $19.5600/hour |               |      80 | Bi-weekly   |                0 |                 0 | No       |
2025-09-09 09:58:15,175 | INFO | -validating table: Compensation
2025-09-09 09:58:36,152 | INFO | llm gpt-5 api call took 20.976 seconds
2025-09-09 09:58:36,156 | INFO | total input tokens: 2161
2025-09-09 09:58:36,156 | INFO | input text tokens: 1523 # estimated
2025-09-09 09:58:36,156 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:58:36,156 | INFO | cost for input: $0.002701 USD
2025-09-09 09:58:36,157 | INFO | total output tokens: 488
2025-09-09 09:58:36,157 | INFO | cost of output: $0.00488 USD
2025-09-09 09:58:36,157 | INFO | done judging, ALL GOOD
2025-09-09 09:58:36,159 | INFO | -current table:
| Used For   |   Routing & Transit Number | Bank Name           |   Account Number | Account Type   | Calculation Method   | Amount or %   |
|:-----------|---------------------------:|:--------------------|-----------------:|:---------------|:---------------------|:--------------|
| Net Pay    |                  121000358 | BANK OF AMERICA, NA |       4185709326 | Checking       | Percentage           | 100 %         |
2025-09-09 09:58:36,159 | INFO | -validating table: Direct Deposit
2025-09-09 09:58:50,558 | INFO | llm gpt-5 api call took 14.399 seconds
2025-09-09 09:58:50,562 | INFO | total input tokens: 2168
2025-09-09 09:58:50,563 | INFO | input text tokens: 1530 # estimated
2025-09-09 09:58:50,563 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:58:50,563 | INFO | cost for input: $0.00271 USD
2025-09-09 09:58:50,563 | INFO | total output tokens: 360
2025-09-09 09:58:50,564 | INFO | cost of output: $0.0036 USD
2025-09-09 09:58:50,564 | INFO | done judging, ALL GOOD
2025-09-09 09:58:50,565 | INFO | -current table:

2025-09-09 09:58:50,565 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:58:50,565 | INFO | started validating form fields
2025-09-09 09:58:50,565 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:58:50,566 | INFO | --current are:
Name (Preferred Name) : Natalie, Bowers
Employee ID / Clock ID : 658471
Address Line 1 : 4127 Pine Cone Ter
Address Line 2 : 
City, State Zip : Portland OR 97211
Country : United States
Work Phone : 
Extension : 
Home Phone : (503) 555-1194
Cell Phone : 
2025-09-09 09:59:33,500 | INFO | llm gpt-5 api call took 42.929 seconds
2025-09-09 09:59:33,511 | INFO | total input tokens: 2646
2025-09-09 09:59:33,511 | INFO | input text tokens: 2008 # estimated
2025-09-09 09:59:33,511 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:59:33,511 | INFO | cost for input: $0.003308 USD
2025-09-09 09:59:33,512 | INFO | total output tokens: 1227
2025-09-09 09:59:33,512 | INFO | cost of output: $0.01227 USD
2025-09-09 09:59:33,512 | INFO | done judging, ALL GOOD
2025-09-09 09:59:33,512 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:59:33,513 | INFO | --current are:
Social Security Number : 586-41-3725
Birth Date : 08/29/1993
Work E-mail : natalie.bowers@proton.com
Personal E-mail : 
Work State : California
Officer Type : 
Class Code : 4511
Waive Code : 
2025-09-09 10:00:05,153 | INFO | llm gpt-5 api call took 31.636 seconds
2025-09-09 10:00:05,158 | INFO | total input tokens: 2630
2025-09-09 10:00:05,158 | INFO | input text tokens: 1992 # estimated
2025-09-09 10:00:05,159 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 10:00:05,159 | INFO | cost for input: $0.003288 USD
2025-09-09 10:00:05,159 | INFO | total output tokens: 980
2025-09-09 10:00:05,159 | INFO | cost of output: $0.0098 USD
2025-09-09 10:00:05,160 | INFO | done judging, ALL GOOD

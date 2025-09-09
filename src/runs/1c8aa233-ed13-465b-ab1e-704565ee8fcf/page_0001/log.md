2025-09-09 09:36:16,811 | INFO | started initial extraction for page 1
2025-09-09 09:37:14,468 | INFO | llm gpt-5 api call took 57.267 seconds
2025-09-09 09:37:15,111 | INFO | total input tokens: 1850
2025-09-09 09:37:15,111 | INFO | input text tokens: 1212 # estimated
2025-09-09 09:37:15,111 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:37:15,112 | INFO | cost for input: $0.002312 USD
2025-09-09 09:37:15,112 | INFO | total output tokens: 1467
2025-09-09 09:37:15,112 | INFO | cost of output: $0.01467 USD
2025-09-09 09:37:15,113 | INFO | initial extraction of page data done.
2025-09-09 09:37:15,114 | INFO | started validating tables
2025-09-09 09:37:15,128 | INFO | -current table:
| Hire Date   | Type      | Status   | As Of    | Reason   | Statutory Employee   | Eligible For Retirement Plan   | Organization          | Location         | Position   |
|:------------|:----------|:---------|:---------|:---------|:---------------------|:-------------------------------|:----------------------|:-----------------|:-----------|
| 07/23/01    | Full Time | Active   | 06/30/17 | Hired    | No                   | No                             | 15 Project Management | Default Location | Pm Manager |
2025-09-09 09:37:15,129 | INFO | -validating table: Employment
2025-09-09 09:37:31,297 | INFO | llm gpt-5 api call took 16.168 seconds
2025-09-09 09:37:31,303 | INFO | total input tokens: 2182
2025-09-09 09:37:31,304 | INFO | input text tokens: 1544 # estimated
2025-09-09 09:37:31,304 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:37:31,304 | INFO | cost for input: $0.002727 USD
2025-09-09 09:37:31,304 | INFO | total output tokens: 360
2025-09-09 09:37:31,304 | INFO | cost of output: $0.0036 USD
2025-09-09 09:37:31,305 | INFO | done judging, ALL GOOD
2025-09-09 09:37:31,307 | INFO | -current table:
| Name                         | Taxability   | Residency   | Filing Status   | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:-----------------------------|:-------------|:------------|:----------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| Employee Social Security Tax | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Employee Medicare Tax        | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Federal Income Tax           | Withhold     | Resident    | Single          | 8                                             |                                |                            |                               |
2025-09-09 09:37:31,307 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:37:52,611 | INFO | llm gpt-5 api call took 21.303 seconds
2025-09-09 09:37:52,615 | INFO | total input tokens: 2224
2025-09-09 09:37:52,615 | INFO | input text tokens: 1586 # estimated
2025-09-09 09:37:52,615 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:37:52,616 | INFO | cost for input: $0.00278 USD
2025-09-09 09:37:52,616 | INFO | total output tokens: 488
2025-09-09 09:37:52,616 | INFO | cost of output: $0.00488 USD
2025-09-09 09:37:52,616 | INFO | done judging, ALL GOOD
2025-09-09 09:37:52,618 | INFO | -current table:
| Name                            | Taxability   | Residency   | Filing Status     | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:--------------------------------|:-------------|:------------|:------------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| California Income Tax           | Withhold     | Resident    | Head of Household | 0, 8                                          |                                | 100 %                      |                               |
| California Disability Insurance | Taxable      | Resident    |                   |                                               |                                |                            |                               |
2025-09-09 09:37:52,618 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:38:26,495 | INFO | llm gpt-5 api call took 33.876 seconds
2025-09-09 09:38:26,500 | INFO | total input tokens: 2207
2025-09-09 09:38:26,500 | INFO | input text tokens: 1569 # estimated
2025-09-09 09:38:26,500 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:38:26,500 | INFO | cost for input: $0.002759 USD
2025-09-09 09:38:26,501 | INFO | total output tokens: 1064
2025-09-09 09:38:26,501 | INFO | cost of output: $0.01064 USD
2025-09-09 09:38:26,501 | INFO | done judging, ALL GOOD
2025-09-09 09:38:26,502 | INFO | -current table:
| Rate / Salary                | Description   |   Hours | Frequency   |   Overtime Hours |   Overtime Factor | Exempt   |
|:-----------------------------|:--------------|--------:|:------------|-----------------:|------------------:|:---------|
| Salary: $5,194.55/Pay Period |               |      80 | Bi-weekly   |                0 |                 0 | Yes      |
2025-09-09 09:38:26,503 | INFO | -validating table: Compensation
2025-09-09 09:38:39,747 | INFO | llm gpt-5 api call took 13.245 seconds
2025-09-09 09:38:39,752 | INFO | total input tokens: 2154
2025-09-09 09:38:39,753 | INFO | input text tokens: 1516 # estimated
2025-09-09 09:38:39,753 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:38:39,753 | INFO | cost for input: $0.000964 USD
2025-09-09 09:38:39,753 | INFO | total output tokens: 296
2025-09-09 09:38:39,753 | INFO | cost of output: $0.00296 USD
2025-09-09 09:38:39,754 | INFO | done judging, ALL GOOD
2025-09-09 09:38:39,755 | INFO | -current table:
| Used For   |   Routing & Transit Number | Bank Name           |   Account Number | Account Type   | Calculation Method   | Amount or %   |
|:-----------|---------------------------:|:--------------------|-----------------:|:---------------|:---------------------|:--------------|
| Net Pay    |                  121000358 | BANK OF AMERICA, NA |       4587231549 | Checking       | Percentage           | 100 %         |
2025-09-09 09:38:39,755 | INFO | -validating table: Direct Deposit
2025-09-09 09:38:57,185 | INFO | llm gpt-5 api call took 17.429 seconds
2025-09-09 09:38:57,190 | INFO | total input tokens: 2160
2025-09-09 09:38:57,190 | INFO | input text tokens: 1522 # estimated
2025-09-09 09:38:57,190 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:38:57,190 | INFO | cost for input: $0.0027 USD
2025-09-09 09:38:57,190 | INFO | total output tokens: 488
2025-09-09 09:38:57,191 | INFO | cost of output: $0.00488 USD
2025-09-09 09:38:57,191 | INFO | done judging, ALL GOOD
2025-09-09 09:38:57,194 | INFO | -current table:

2025-09-09 09:38:57,194 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:38:57,194 | INFO | started validating form fields
2025-09-09 09:38:57,194 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:38:57,194 | INFO | --current are:
Name (Preferred Name) : Olivia Turner
Employee ID / Clock ID : 731042
Address Line 1 : 4827 Maple Ridge Dr
Address Line 2 : 
City, State Zip : Austin TX 78727
Country : United States
Work Phone : 
Extension : 
Home Phone : 
Cell Phone : 
2025-09-09 09:39:27,946 | INFO | llm gpt-5 api call took 30.746 seconds
2025-09-09 09:39:27,951 | INFO | total input tokens: 2629
2025-09-09 09:39:27,952 | INFO | input text tokens: 1991 # estimated
2025-09-09 09:39:27,952 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:39:27,952 | INFO | cost for input: $0.003286 USD
2025-09-09 09:39:27,952 | INFO | total output tokens: 907
2025-09-09 09:39:27,953 | INFO | cost of output: $0.00907 USD
2025-09-09 09:39:27,953 | INFO | done judging, ALL GOOD
2025-09-09 09:39:27,953 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:39:27,953 | INFO | --current are:
Social Security Number : 562-55-0194
Birth Date : 07/14/1989
Work E-mail : olivia.turner@proton.com
Personal E-mail : 
Work State : California
Officer Type : 
Class Code : 4511
Waive Code : 
2025-09-09 09:40:01,504 | INFO | llm gpt-5 api call took 33.544 seconds
2025-09-09 09:40:01,509 | INFO | total input tokens: 2624
2025-09-09 09:40:01,509 | INFO | input text tokens: 1986 # estimated
2025-09-09 09:40:01,509 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:40:01,509 | INFO | cost for input: $0.00328 USD
2025-09-09 09:40:01,509 | INFO | total output tokens: 1108
2025-09-09 09:40:01,509 | INFO | cost of output: $0.01108 USD
2025-09-09 09:40:01,510 | INFO | done judging, ALL GOOD

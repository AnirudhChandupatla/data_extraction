2025-09-09 09:38:19,348 | INFO | started initial extraction for page 3
2025-09-09 09:39:15,089 | INFO | llm gpt-5 api call took 55.439 seconds
2025-09-09 09:39:15,092 | INFO | total input tokens: 1854
2025-09-09 09:39:15,093 | INFO | input text tokens: 1216 # estimated
2025-09-09 09:39:15,093 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:39:15,093 | INFO | cost for input: $0.002318 USD
2025-09-09 09:39:15,093 | INFO | total output tokens: 1405
2025-09-09 09:39:15,093 | INFO | cost of output: $0.01405 USD
2025-09-09 09:39:15,094 | INFO | initial extraction of page data done.
2025-09-09 09:39:15,095 | INFO | started validating tables
2025-09-09 09:39:15,096 | INFO | -current table:
| Hire Date   | Type      | Status   | As Of    | Reason   | Statutory Employee   | Eligible For Retirement Plan   | Organization   | Location         | Position                      |
|:------------|:----------|:---------|:---------|:---------|:---------------------|:-------------------------------|:---------------|:-----------------|:------------------------------|
| 06/15/01    | Full Time | Active   | 06/30/17 | Hired    | No                   | No                             | 10 MC-Milpitas | Default Location | Mobile Communications Manager |
2025-09-09 09:39:15,097 | INFO | -validating table: Employment
2025-09-09 09:39:38,074 | INFO | llm gpt-5 api call took 22.977 seconds
2025-09-09 09:39:38,082 | INFO | total input tokens: 2189
2025-09-09 09:39:38,083 | INFO | input text tokens: 1551 # estimated
2025-09-09 09:39:38,083 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:39:38,083 | INFO | cost for input: $0.002736 USD
2025-09-09 09:39:38,083 | INFO | total output tokens: 424
2025-09-09 09:39:38,083 | INFO | cost of output: $0.00424 USD
2025-09-09 09:39:38,084 | INFO | done judging, ALL GOOD
2025-09-09 09:39:38,085 | INFO | -current table:
| Name                         | Taxability   | Residency   | Filing Status   | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:-----------------------------|:-------------|:------------|:----------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| Employee Social Security Tax | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Employee Medicare Tax        | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Federal Income Tax           | Withhold     | Resident    | Single          | 1                                             |                                |                            |                               |
2025-09-09 09:39:38,085 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:39:55,979 | INFO | llm gpt-5 api call took 17.893 seconds
2025-09-09 09:39:55,983 | INFO | total input tokens: 2228
2025-09-09 09:39:55,983 | INFO | input text tokens: 1590 # estimated
2025-09-09 09:39:55,983 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:39:55,983 | INFO | cost for input: $0.001057 USD
2025-09-09 09:39:55,984 | INFO | total output tokens: 488
2025-09-09 09:39:55,984 | INFO | cost of output: $0.00488 USD
2025-09-09 09:39:55,984 | INFO | done judging, ALL GOOD
2025-09-09 09:39:55,985 | INFO | -current table:
| Name                            | Taxability   | Residency   | Filing Status   | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:--------------------------------|:-------------|:------------|:----------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| California Income Tax           | Withhold     | Resident    | Single          | 0 , 1                                         |                                | 100 %                      |                               |
| California Disability Insurance | Taxable      | Resident    |                 |                                               |                                |                            |                               |
2025-09-09 09:39:55,986 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:40:25,380 | INFO | llm gpt-5 api call took 29.394 seconds
2025-09-09 09:40:25,384 | INFO | total input tokens: 2209
2025-09-09 09:40:25,384 | INFO | input text tokens: 1571 # estimated
2025-09-09 09:40:25,384 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:40:25,385 | INFO | cost for input: $0.002761 USD
2025-09-09 09:40:25,385 | INFO | total output tokens: 616
2025-09-09 09:40:25,385 | INFO | cost of output: $0.00616 USD
2025-09-09 09:40:25,385 | INFO | done judging, ALL GOOD
2025-09-09 09:40:25,386 | INFO | -current table:
| Rate / Salary                | Description   |   Hours | Frequency   |   Overtime Hours |   Overtime Factor | Exempt   |
|:-----------------------------|:--------------|--------:|:------------|-----------------:|------------------:|:---------|
| Salary: $5,117.75/Pay Period |               |      80 | Bi-weekly   |                0 |                 0 | Yes      |
2025-09-09 09:40:25,386 | INFO | -validating table: Compensation
2025-09-09 09:40:43,337 | INFO | llm gpt-5 api call took 17.951 seconds
2025-09-09 09:40:43,341 | INFO | total input tokens: 2158
2025-09-09 09:40:43,341 | INFO | input text tokens: 1520 # estimated
2025-09-09 09:40:43,341 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:40:43,341 | INFO | cost for input: $0.002697 USD
2025-09-09 09:40:43,342 | INFO | total output tokens: 360
2025-09-09 09:40:43,342 | INFO | cost of output: $0.0036 USD
2025-09-09 09:40:43,342 | INFO | done judging, ALL GOOD
2025-09-09 09:40:43,343 | INFO | -current table:
| Used For   |   Routing & Transit Number | Bank Name           |   Account Number | Account Type   | Calculation Method   | Amount or %   |
|:-----------|---------------------------:|:--------------------|-----------------:|:---------------|:---------------------|:--------------|
| Net Pay    |                  121000358 | BANK OF AMERICA, NA |       8406759314 | Checking       | Percentage           | 100 %         |
2025-09-09 09:40:43,343 | INFO | -validating table: Direct Deposit
2025-09-09 09:41:02,316 | INFO | llm gpt-5 api call took 18.972 seconds
2025-09-09 09:41:02,319 | INFO | total input tokens: 2164
2025-09-09 09:41:02,320 | INFO | input text tokens: 1526 # estimated
2025-09-09 09:41:02,320 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:41:02,320 | INFO | cost for input: $0.002705 USD
2025-09-09 09:41:02,320 | INFO | total output tokens: 424
2025-09-09 09:41:02,320 | INFO | cost of output: $0.00424 USD
2025-09-09 09:41:02,320 | INFO | done judging, ALL GOOD
2025-09-09 09:41:02,321 | INFO | -current table:

2025-09-09 09:41:02,321 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:41:02,321 | INFO | started validating form fields
2025-09-09 09:41:02,322 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:41:02,322 | INFO | --current are:
Name (Preferred Name) : Marcus, Delgado
Employee ID / Clock ID : 584219
Address Line 1 : 9173 Oak Hollow Ct
Address Line 2 : 
City, State Zip : Denver CO 80211
Country : United States
Work Phone : 
Extension : 
Home Phone : 
Cell Phone : 
2025-09-09 09:41:44,566 | INFO | llm gpt-5 api call took 42.238 seconds
2025-09-09 09:41:44,570 | INFO | total input tokens: 2634
2025-09-09 09:41:44,571 | INFO | input text tokens: 1996 # estimated
2025-09-09 09:41:44,571 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:41:44,571 | INFO | cost for input: $0.003292 USD
2025-09-09 09:41:44,571 | INFO | total output tokens: 971
2025-09-09 09:41:44,571 | INFO | cost of output: $0.00971 USD
2025-09-09 09:41:44,571 | INFO | done judging, ALL GOOD
2025-09-09 09:41:44,572 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:41:44,572 | INFO | --current are:
Social Security Number : 579-42-6813
Birth Date : 03/09/1987
Work E-mail : marcus.delgado@proton.com
Personal E-mail : 
Work State : California
Officer Type : 
Class Code : 4511
Waive Code : 
2025-09-09 09:42:28,098 | INFO | llm gpt-5 api call took 43.521 seconds
2025-09-09 09:42:28,103 | INFO | total input tokens: 2629
2025-09-09 09:42:28,103 | INFO | input text tokens: 1991 # estimated
2025-09-09 09:42:28,103 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:42:28,103 | INFO | cost for input: $0.001558 USD
2025-09-09 09:42:28,103 | INFO | total output tokens: 980
2025-09-09 09:42:28,104 | INFO | cost of output: $0.0098 USD
2025-09-09 09:42:28,104 | INFO | done judging, ALL GOOD

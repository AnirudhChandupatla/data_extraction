2025-09-09 09:45:37,868 | INFO | started initial extraction for page 7
2025-09-09 09:46:38,799 | INFO | llm gpt-5 api call took 60.676 seconds
2025-09-09 09:46:38,803 | INFO | total input tokens: 1919
2025-09-09 09:46:38,803 | INFO | input text tokens: 1281 # estimated
2025-09-09 09:46:38,803 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:46:38,803 | INFO | cost for input: $0.002399 USD
2025-09-09 09:46:38,803 | INFO | total output tokens: 1565
2025-09-09 09:46:38,804 | INFO | cost of output: $0.01565 USD
2025-09-09 09:46:38,804 | INFO | initial extraction of page data done.
2025-09-09 09:46:38,805 | INFO | started validating tables
2025-09-09 09:46:38,807 | INFO | -current table:
| Hire Date   | Type   | Status   | As Of    | Reason   | Statutory Employee   | Eligible For Retirement Plan   | Organization   | Location         | Position             |
|:------------|:-------|:---------|:---------|:---------|:---------------------|:-------------------------------|:---------------|:-----------------|:---------------------|
| 04/03/17    | Temp   | Active   | 06/30/17 | Hired    | No                   | No                             | 10 MC-Milpitas | Default Location | Test System Engineer |
2025-09-09 09:46:38,808 | INFO | -validating table: Employment
2025-09-09 09:46:53,728 | INFO | llm gpt-5 api call took 14.920 seconds
2025-09-09 09:46:53,733 | INFO | total input tokens: 2254
2025-09-09 09:46:53,733 | INFO | input text tokens: 1616 # estimated
2025-09-09 09:46:53,733 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:46:53,733 | INFO | cost for input: $0.002818 USD
2025-09-09 09:46:53,733 | INFO | total output tokens: 360
2025-09-09 09:46:53,734 | INFO | cost of output: $0.0036 USD
2025-09-09 09:46:53,734 | INFO | done judging, ALL GOOD
2025-09-09 09:46:53,735 | INFO | -current table:
| Name                         | Taxability   | Residency   | Filing Status   | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:-----------------------------|:-------------|:------------|:----------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| Employee Social Security Tax | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Employee Medicare Tax        | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Federal Income Tax           | Withhold     | Resident    | Married         | 1                                             |                                |                            |                               |
2025-09-09 09:46:53,736 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:47:26,851 | INFO | llm gpt-5 api call took 33.115 seconds
2025-09-09 09:47:26,856 | INFO | total input tokens: 2293
2025-09-09 09:47:26,856 | INFO | input text tokens: 1655 # estimated
2025-09-09 09:47:26,856 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:47:26,856 | INFO | cost for input: $0.002866 USD
2025-09-09 09:47:26,857 | INFO | total output tokens: 680
2025-09-09 09:47:26,857 | INFO | cost of output: $0.0068 USD
2025-09-09 09:47:26,857 | INFO | done judging, ALL GOOD
2025-09-09 09:47:26,858 | INFO | -current table:
| Name                            | Taxability   | Residency   | Filing Status           | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:--------------------------------|:-------------|:------------|:------------------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| California Income Tax           | Withhold     | Resident    | Married with one income | 1 , 0                                         |                                | 100 %                      |                               |
| California Disability Insurance | Taxable      | Resident    |                         |                                               |                                |                            |                               |
2025-09-09 09:47:26,859 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:47:51,062 | INFO | llm gpt-5 api call took 24.203 seconds
2025-09-09 09:47:51,066 | INFO | total input tokens: 2277
2025-09-09 09:47:51,066 | INFO | input text tokens: 1639 # estimated
2025-09-09 09:47:51,066 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:47:51,066 | INFO | cost for input: $0.002846 USD
2025-09-09 09:47:51,067 | INFO | total output tokens: 616
2025-09-09 09:47:51,067 | INFO | cost of output: $0.00616 USD
2025-09-09 09:47:51,067 | INFO | done judging, ALL GOOD
2025-09-09 09:47:51,068 | INFO | -current table:
| Rate / Salary         | Description   |   Hours | Frequency   |   Overtime Hours |   Overtime Factor | Exempt   |
|:----------------------|:--------------|--------:|:------------|-----------------:|------------------:|:---------|
| Rate 1: $55.0000/hour |               |      80 | Bi-weekly   |                0 |                 0 | No       |
2025-09-09 09:47:51,068 | INFO | -validating table: Compensation
2025-09-09 09:48:11,078 | INFO | llm gpt-5 api call took 20.009 seconds
2025-09-09 09:48:11,082 | INFO | total input tokens: 2222
2025-09-09 09:48:11,082 | INFO | input text tokens: 1584 # estimated
2025-09-09 09:48:11,082 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:48:11,082 | INFO | cost for input: $0.002778 USD
2025-09-09 09:48:11,082 | INFO | total output tokens: 360
2025-09-09 09:48:11,082 | INFO | cost of output: $0.0036 USD
2025-09-09 09:48:11,083 | INFO | done judging, ALL GOOD
2025-09-09 09:48:11,084 | INFO | -current table:
| Used For   |   Routing & Transit Number | Bank Name            |   Account Number | Account Type   | Calculation Method   | Amount or %   |
|:-----------|---------------------------:|:---------------------|-----------------:|:---------------|:---------------------|:--------------|
| Net Pay    |                  122000247 | WELLS FARGO BANK, NA |       5401182763 | Checking       | Percentage           | 100 %         |
2025-09-09 09:48:11,085 | INFO | -validating table: Direct Deposit
2025-09-09 09:48:28,608 | INFO | llm gpt-5 api call took 17.523 seconds
2025-09-09 09:48:28,612 | INFO | total input tokens: 2231
2025-09-09 09:48:28,613 | INFO | input text tokens: 1593 # estimated
2025-09-09 09:48:28,613 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:48:28,613 | INFO | cost for input: $0.002789 USD
2025-09-09 09:48:28,613 | INFO | total output tokens: 360
2025-09-09 09:48:28,613 | INFO | cost of output: $0.0036 USD
2025-09-09 09:48:28,613 | INFO | done judging, ALL GOOD
2025-09-09 09:48:28,614 | INFO | -current table:

2025-09-09 09:48:28,614 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:48:28,615 | INFO | started validating form fields
2025-09-09 09:48:28,615 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:48:28,615 | INFO | --current are:
Name (Preferred Name) : Daniel, Whitaker
Employee ID / Clock ID : 762518
Address Line 1 : 4185 Copper Beech Dr
Address Line 2 : Apt 7C
City, State Zip : Columbus OH 43221
Country : United States
Work Phone : 
Extension : 
Home Phone : 
Cell Phone : (380) 555-1193
2025-09-09 09:49:07,451 | INFO | llm gpt-5 api call took 38.830 seconds
2025-09-09 09:49:07,458 | INFO | total input tokens: 2719
2025-09-09 09:49:07,459 | INFO | input text tokens: 2081 # estimated
2025-09-09 09:49:07,459 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:49:07,459 | INFO | cost for input: $0.003399 USD
2025-09-09 09:49:07,459 | INFO | total output tokens: 1099
2025-09-09 09:49:07,459 | INFO | cost of output: $0.01099 USD
2025-09-09 09:49:07,460 | INFO | done judging, ALL GOOD
2025-09-09 09:49:07,460 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:49:07,460 | INFO | --current are:
Social Security Number : 582-65-2194
Birth Date : 04/03/1991
Work E-mail : daniel.whitaker@proton.com
Personal E-mail : danielwhitaker91@gmail.com
Work State : California
Officer Type : 
Class Code : 4511
Waive Code : 
2025-09-09 09:49:30,935 | INFO | llm gpt-5 api call took 23.469 seconds
2025-09-09 09:49:30,940 | INFO | total input tokens: 2708
2025-09-09 09:49:30,940 | INFO | input text tokens: 2070 # estimated
2025-09-09 09:49:30,941 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:49:30,941 | INFO | cost for input: $0.003385 USD
2025-09-09 09:49:30,941 | INFO | total output tokens: 852
2025-09-09 09:49:30,941 | INFO | cost of output: $0.00852 USD
2025-09-09 09:49:30,941 | INFO | done judging, ALL GOOD

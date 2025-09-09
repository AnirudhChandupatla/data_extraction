2025-09-09 09:46:36,793 | INFO | started initial extraction for page 8
2025-09-09 09:47:57,388 | INFO | llm gpt-5 api call took 80.334 seconds
2025-09-09 09:47:57,392 | INFO | total input tokens: 1926
2025-09-09 09:47:57,392 | INFO | input text tokens: 1288 # estimated
2025-09-09 09:47:57,393 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:47:57,393 | INFO | cost for input: $0.002407 USD
2025-09-09 09:47:57,393 | INFO | total output tokens: 1824
2025-09-09 09:47:57,394 | INFO | cost of output: $0.01824 USD
2025-09-09 09:47:57,395 | INFO | initial extraction of page data done.
2025-09-09 09:47:57,396 | INFO | started validating tables
2025-09-09 09:47:57,397 | INFO | -current table:
| Hire Date   | Type      | Status   | As Of    | Reason         | Statutory Employee   | Eligible For Retirement Plan   | Organization   | Location         | Position      |
|:------------|:----------|:---------|:---------|:---------------|:---------------------|:-------------------------------|:---------------|:-----------------|:--------------|
| 08/23/10    | Full Time | Active   | 06/30/17 | Return to Work | No                   | No                             | 10 MC-Milpitas | Default Location | Test Engineer |
2025-09-09 09:47:57,398 | INFO | -validating table: Employment
2025-09-09 09:48:14,912 | INFO | llm gpt-5 api call took 17.513 seconds
2025-09-09 09:48:14,916 | INFO | total input tokens: 2259
2025-09-09 09:48:14,916 | INFO | input text tokens: 1621 # estimated
2025-09-09 09:48:14,916 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:48:14,917 | INFO | cost for input: $0.002824 USD
2025-09-09 09:48:14,917 | INFO | total output tokens: 296
2025-09-09 09:48:14,917 | INFO | cost of output: $0.00296 USD
2025-09-09 09:48:14,917 | INFO | done judging, ALL GOOD
2025-09-09 09:48:14,919 | INFO | -current table:
| Name                         | Taxability   | Residency   | Filing Status   | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:-----------------------------|:-------------|:------------|:----------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| Employee Social Security Tax | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Employee Medicare Tax        | Taxable      | Resident    |                 |                                               |                                |                            |                               |
| Federal Income Tax           | Withhold     | Resident    | Married         | 2                                             |                                |                            |                               |
2025-09-09 09:48:14,919 | INFO | -validating table: Tax Withholdings (Federal Taxes)
2025-09-09 09:48:39,692 | INFO | llm gpt-5 api call took 24.772 seconds
2025-09-09 09:48:39,698 | INFO | total input tokens: 2300
2025-09-09 09:48:39,698 | INFO | input text tokens: 1662 # estimated
2025-09-09 09:48:39,698 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:48:39,698 | INFO | cost for input: $0.002875 USD
2025-09-09 09:48:39,698 | INFO | total output tokens: 424
2025-09-09 09:48:39,699 | INFO | cost of output: $0.00424 USD
2025-09-09 09:48:39,699 | INFO | done judging, ALL GOOD
2025-09-09 09:48:39,701 | INFO | -current table:
| Name                            | Taxability   | Residency   | Filing Status           | Allowances (coma separated values possible)   | Additional / Override Amount   | % of Time Worked (State)   | % of Earnings Taxed (Local)   |
|:--------------------------------|:-------------|:------------|:------------------------|:----------------------------------------------|:-------------------------------|:---------------------------|:------------------------------|
| California Income Tax           | Withhold     | Resident    | Married with one income | 0 , 2                                         |                                | 100 %                      |                               |
| California Disability Insurance | Taxable      | Resident    |                         |                                               |                                |                            |                               |
2025-09-09 09:48:39,701 | INFO | -validating table: Tax Withholdings (State Taxes)
2025-09-09 09:49:03,028 | INFO | llm gpt-5 api call took 23.326 seconds
2025-09-09 09:49:03,033 | INFO | total input tokens: 2284
2025-09-09 09:49:03,034 | INFO | input text tokens: 1646 # estimated
2025-09-09 09:49:03,034 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:49:03,034 | INFO | cost for input: $0.002855 USD
2025-09-09 09:49:03,034 | INFO | total output tokens: 616
2025-09-09 09:49:03,034 | INFO | cost of output: $0.00616 USD
2025-09-09 09:49:03,035 | INFO | done judging, ALL GOOD
2025-09-09 09:49:03,036 | INFO | -current table:
| Rate / Salary        | Description   |   Hours | Frequency   |   Overtime Hours |   Overtime Factor | Exempt   |
|:---------------------|:--------------|--------:|:------------|-----------------:|------------------:|:---------|
| $2,289.67/Pay Period |               |      80 | Bi-weekly   |                0 |                 0 | Yes      |
2025-09-09 09:49:03,036 | INFO | -validating table: Compensation
2025-09-09 09:49:36,106 | INFO | llm gpt-5 api call took 33.070 seconds
2025-09-09 09:49:36,111 | INFO | total input tokens: 2228
2025-09-09 09:49:36,111 | INFO | input text tokens: 1590 # estimated
2025-09-09 09:49:36,111 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:49:36,111 | INFO | cost for input: $0.000913 USD
2025-09-09 09:49:36,112 | INFO | total output tokens: 1075
2025-09-09 09:49:36,112 | INFO | cost of output: $0.01075 USD
2025-09-09 09:49:36,112 | INFO | --found issues: [{'row': 1, 'column': 'Rate / Salary', 'status': 'wrong', 'feedback': "Should be 'Salary: $2,289.67/Pay Period' instead of '$2,289.67/Pay Period'."}]
2025-09-09 09:49:46,870 | INFO | llm gpt-5-mini api call took 10.757 seconds
2025-09-09 09:49:46,873 | INFO | total input tokens: 1928
2025-09-09 09:49:46,874 | INFO | input text tokens: 997 # estimated
2025-09-09 09:49:46,874 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 09:49:46,874 | INFO | cost for input: $0.00241 USD
2025-09-09 09:49:46,874 | INFO | total output tokens: 402
2025-09-09 09:49:46,874 | INFO | cost of output: $0.00402 USD
2025-09-09 09:49:46,875 | INFO | --corrected as:
| Rate / Salary                | Description   |   Hours | Frequency   |   Overtime Hours |   Overtime Factor | Exempt   |
|:-----------------------------|:--------------|--------:|:------------|-----------------:|------------------:|:---------|
| Salary: $2,289.67/Pay Period |               |      80 | Bi-weekly   |                0 |                 0 | Yes      |
2025-09-09 09:49:46,876 | INFO | -revalidating table: Compensation
2025-09-09 09:50:15,917 | INFO | llm gpt-5 api call took 29.040 seconds
2025-09-09 09:50:15,921 | INFO | total input tokens: 2230
2025-09-09 09:50:15,921 | INFO | input text tokens: 1592 # estimated
2025-09-09 09:50:15,921 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:50:15,922 | INFO | cost for input: $0.002788 USD
2025-09-09 09:50:15,922 | INFO | total output tokens: 552
2025-09-09 09:50:15,922 | INFO | cost of output: $0.00552 USD
2025-09-09 09:50:15,922 | INFO | done judging, ALL GOOD
2025-09-09 09:50:15,923 | INFO | -current table:
| Used For   |   Routing & Transit Number | Bank Name        |   Account Number | Account Type   | Calculation Method   | Amount or %   |
|:-----------|---------------------------:|:-----------------|-----------------:|:---------------|:---------------------|:--------------|
| Net Pay    |                  031176110 | CAPITAL ONE N.A. |        671204983 | Checking       | Flat Dollar Amount   | $850.0000     |
| Net Pay    |                  321076470 | PATELCO CU       |           905631 | Checking       | Flat Dollar Amount   | $30.0000      |
| Net Pay    |                  121100782 | BANK OF THE WEST |        784205196 | Checking       | Remainder            |               |
2025-09-09 09:50:15,924 | INFO | -validating table: Direct Deposit
2025-09-09 09:50:43,132 | INFO | llm gpt-5 api call took 27.208 seconds
2025-09-09 09:50:43,136 | INFO | total input tokens: 2306
2025-09-09 09:50:43,136 | INFO | input text tokens: 1668 # estimated
2025-09-09 09:50:43,136 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:50:43,136 | INFO | cost for input: $0.002883 USD
2025-09-09 09:50:43,137 | INFO | total output tokens: 616
2025-09-09 09:50:43,137 | INFO | cost of output: $0.00616 USD
2025-09-09 09:50:43,137 | INFO | done judging, ALL GOOD
2025-09-09 09:50:43,138 | INFO | -current table:

2025-09-09 09:50:43,138 | INFO | -validating table: Earnings & Deductions
2025-09-09 09:50:43,138 | INFO | started validating form fields
2025-09-09 09:50:43,138 | INFO | -validating form fields: ['Name (Preferred Name)', 'Employee ID / Clock ID', 'Address Line 1', 'Address Line 2', 'City, State Zip', 'Country', 'Work Phone', 'Extension', 'Home Phone', 'Cell Phone']
2025-09-09 09:50:43,139 | INFO | --current are:
Name (Preferred Name) : Lauren, McKinley
Employee ID / Clock ID : 845273
Address Line 1 : 1294 Harbor View Dr
Address Line 2 : 
City, State Zip : Tampa FL 33607
Country : United States
Work Phone : 
Extension : 
Home Phone : (813) 555-1047
Cell Phone : 
2025-09-09 09:51:21,400 | INFO | llm gpt-5 api call took 38.255 seconds
2025-09-09 09:51:21,406 | INFO | total input tokens: 2787
2025-09-09 09:51:21,406 | INFO | input text tokens: 2149 # estimated
2025-09-09 09:51:21,407 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:51:21,408 | INFO | cost for input: $0.003484 USD
2025-09-09 09:51:21,408 | INFO | total output tokens: 1227
2025-09-09 09:51:21,408 | INFO | cost of output: $0.01227 USD
2025-09-09 09:51:21,408 | INFO | done judging, ALL GOOD
2025-09-09 09:51:21,408 | INFO | -validating form fields: ['Social Security Number', 'Birth Date', 'Work E-mail', 'Personal E-mail', 'Work State', 'Officer Type', 'Class Code', 'Waive Code']
2025-09-09 09:51:21,409 | INFO | --current are:
Social Security Number : 583-42-7195
Birth Date : 09/17/1988
Work E-mail : lauren.mckinley@proton.com
Personal E-mail : 
Work State : California
Officer Type : 
Class Code : 4511
Waive Code : 
2025-09-09 09:52:01,425 | INFO | llm gpt-5 api call took 40.010 seconds
2025-09-09 09:52:01,430 | INFO | total input tokens: 2774
2025-09-09 09:52:01,431 | INFO | input text tokens: 2136 # estimated
2025-09-09 09:52:01,431 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 09:52:01,431 | INFO | cost for input: $0.003468 USD
2025-09-09 09:52:01,431 | INFO | total output tokens: 1108
2025-09-09 09:52:01,431 | INFO | cost of output: $0.01108 USD
2025-09-09 09:52:01,432 | INFO | done judging, ALL GOOD

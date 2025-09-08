2025-09-08 20:50:09,306 | INFO | started initial extraction for page 7
2025-09-08 20:51:47,150 | INFO | llm gpt-5 api call took 97.554 seconds
2025-09-08 20:51:47,160 | INFO | total input tokens: 2535
2025-09-08 20:51:47,160 | INFO | input text tokens: 1897 # estimated
2025-09-08 20:51:47,160 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:51:47,161 | INFO | cost for input: $0.003169 USD
2025-09-08 20:51:47,161 | INFO | total output tokens: 2676
2025-09-08 20:51:47,161 | INFO | cost of output: $0.02676 USD
2025-09-08 20:51:47,162 | INFO | initial extraction of page data done.
2025-09-08 20:51:55,084 | INFO | got response with OCR coordinates info from azure doc intelligence for page 7
2025-09-08 20:51:55,085 | INFO | started validating tables
2025-09-08 20:51:55,099 | INFO | -current table:
| RateCode   | Description   |   Rate | Salary   | Effective Dates          |
|:-----------|:--------------|-------:|:---------|:-------------------------|
| Base       | Base Rate     |     18 |          | 08/04/2023 to 12/31/2100 |
2025-09-08 20:51:55,100 | INFO | -validating table: Rate/Salary Information
2025-09-08 20:51:55,100 | INFO | --figuring out table emptiness...
2025-09-08 20:52:21,821 | INFO | llm gpt-5-mini api call took 26.718 seconds
2025-09-08 20:52:21,837 | INFO | total input tokens: 13962
2025-09-08 20:52:21,837 | INFO | input text tokens: 13031 # estimated
2025-09-08 20:52:21,837 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:52:21,838 | INFO | cost for input: $0.017452 USD
2025-09-08 20:52:21,838 | INFO | total output tokens: 2026
2025-09-08 20:52:21,838 | INFO | cost of output: $0.02026 USD
2025-09-08 20:52:21,838 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:52:36,969 | INFO | llm gpt-5-mini api call took 15.131 seconds
2025-09-08 20:52:36,972 | INFO | total input tokens: 1513
2025-09-08 20:52:36,972 | INFO | input text tokens: 1505 # estimated
2025-09-08 20:52:36,972 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:52:36,972 | INFO | cost for input: $0.001891 USD
2025-09-08 20:52:36,973 | INFO | total output tokens: 2022
2025-09-08 20:52:36,973 | INFO | cost of output: $0.02022 USD
2025-09-08 20:52:36,973 | INFO | --got table grid emptiness info:
|RateCode|Description|Rate|Salary|Effective Dates|
|   X   |   X   |   X   |       |   X   |
2025-09-08 20:53:01,807 | INFO | llm gpt-5 api call took 24.833 seconds
2025-09-08 20:53:01,812 | INFO | total input tokens: 2881
2025-09-08 20:53:01,812 | INFO | input text tokens: 2243 # estimated
2025-09-08 20:53:01,812 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:53:01,812 | INFO | cost for input: $0.003601 USD
2025-09-08 20:53:01,812 | INFO | total output tokens: 616
2025-09-08 20:53:01,812 | INFO | cost of output: $0.00616 USD
2025-09-08 20:53:01,813 | INFO | done judging, ALL GOOD
2025-09-08 20:53:01,814 | INFO | -current table:
| Employee Tax (code description)   | Status   |   Add'l Amount | Effective Dates          | Default   |
|:----------------------------------|:---------|---------------:|:-------------------------|:----------|
| MED Medicare                      |          |              0 | 08/04/2023 to12/31/2100  | Yes       |
| SS OASDI                          |          |              0 | 08/04/2023 to 12/31/2100 | Yes       |
| FITW Federal Income Tax           | S-0      |              0 | 08/04/2023 to 12/31/2100 | Yes       |
| MN Minnesota SITW                 | S-1      |              0 | 07/31/2023 to 12/31/2100 | Yes       |
2025-09-08 20:53:01,814 | INFO | -validating table: Tax Information (Employee)
2025-09-08 20:53:01,814 | INFO | --figuring out table emptiness...
2025-09-08 20:53:24,622 | INFO | llm gpt-5-mini api call took 22.806 seconds
2025-09-08 20:53:24,636 | INFO | total input tokens: 14072
2025-09-08 20:53:24,636 | INFO | input text tokens: 13141 # estimated
2025-09-08 20:53:24,637 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:53:24,637 | INFO | cost for input: $0.01759 USD
2025-09-08 20:53:24,637 | INFO | total output tokens: 2268
2025-09-08 20:53:24,637 | INFO | cost of output: $0.02268 USD
2025-09-08 20:53:24,638 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:53:53,161 | INFO | llm gpt-5-mini api call took 28.524 seconds
2025-09-08 20:53:53,164 | INFO | total input tokens: 2021
2025-09-08 20:53:53,165 | INFO | input text tokens: 2013 # estimated
2025-09-08 20:53:53,165 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:53:53,165 | INFO | cost for input: $0.002526 USD
2025-09-08 20:53:53,165 | INFO | total output tokens: 3341
2025-09-08 20:53:53,165 | INFO | cost of output: $0.03341 USD
2025-09-08 20:53:53,165 | INFO | --got table grid emptiness info:
|Employee Tax (code description)|Status|Add'l Amount|Effective Dates|Default|
|---|---|---|---|---|
|X| |X|X|X|
|X| |X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
2025-09-08 20:54:30,013 | INFO | llm gpt-5 api call took 36.847 seconds
2025-09-08 20:54:30,018 | INFO | total input tokens: 3031
2025-09-08 20:54:30,018 | INFO | input text tokens: 2393 # estimated
2025-09-08 20:54:30,019 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:54:30,019 | INFO | cost for input: $0.003789 USD
2025-09-08 20:54:30,019 | INFO | total output tokens: 1192
2025-09-08 20:54:30,019 | INFO | cost of output: $0.01192 USD
2025-09-08 20:54:30,019 | INFO | done judging, ALL GOOD
2025-09-08 20:54:30,021 | INFO | -current table:
| Employer Tax (code description)         | Effective Dates          | Default   |
|:----------------------------------------|:-------------------------|:----------|
| MED-R Medicare - Employer               | 08/04/2023 to 12/31/2100 |           |
| SS-R OASDI - Employer                   | 08/04/2023 to 12/31/2100 |           |
| FUTA Fed Unemployment                   | 08/04/2023 to 12/31/2100 |           |
| MNAST Minnesota Federal Loan Assessment | 08/04/2023 to 12/31/2100 |           |
| MNDW Workforce Enhancement Fee          | 08/04/2023 to 12/31/2100 |           |
| MNSUI Minnesota SUI                     | 08/04/2023 to 12/31/2100 |           |
2025-09-08 20:54:30,021 | INFO | -validating table: Tax Information (Employer)
2025-09-08 20:54:30,021 | INFO | --figuring out table emptiness...
2025-09-08 20:55:48,360 | INFO | llm gpt-5-mini api call took 78.338 seconds
2025-09-08 20:55:48,375 | INFO | total input tokens: 14086
2025-09-08 20:55:48,375 | INFO | input text tokens: 13155 # estimated
2025-09-08 20:55:48,375 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:55:48,375 | INFO | cost for input: $0.017608 USD
2025-09-08 20:55:48,376 | INFO | total output tokens: 4078
2025-09-08 20:55:48,376 | INFO | cost of output: $0.04078 USD
2025-09-08 20:55:48,376 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:56:09,473 | INFO | llm gpt-5-mini api call took 21.096 seconds
2025-09-08 20:56:09,476 | INFO | total input tokens: 1899
2025-09-08 20:56:09,476 | INFO | input text tokens: 1891 # estimated
2025-09-08 20:56:09,476 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:56:09,477 | INFO | cost for input: $0.002374 USD
2025-09-08 20:56:09,477 | INFO | total output tokens: 2682
2025-09-08 20:56:09,477 | INFO | cost of output: $0.02682 USD
2025-09-08 20:56:09,477 | INFO | --got table grid emptiness info:
|Employer Tax (code description)|Effective Dates|Default|
|---:|---:|---:|
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
2025-09-08 20:56:28,418 | INFO | llm gpt-5 api call took 18.940 seconds
2025-09-08 20:56:28,422 | INFO | total input tokens: 3026
2025-09-08 20:56:28,422 | INFO | input text tokens: 2388 # estimated
2025-09-08 20:56:28,423 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:56:28,423 | INFO | cost for input: $0.003782 USD
2025-09-08 20:56:28,423 | INFO | total output tokens: 488
2025-09-08 20:56:28,423 | INFO | cost of output: $0.00488 USD
2025-09-08 20:56:28,423 | INFO | done judging, ALL GOOD
2025-09-08 20:56:28,425 | INFO | -current table:

2025-09-08 20:56:28,425 | INFO | -validating table: Deduction Information
2025-09-08 20:56:28,426 | INFO | -current table:
|   Sequence No. |   Transit No. |   Account No. | Checking?   | Account Name   | Amount Code   |   Amount | Prenote Date   | Effective Dates          | Exclude Special   |
|---------------:|--------------:|--------------:|:------------|:---------------|:--------------|---------:|:---------------|:-------------------------|:------------------|
|             99 |     296076301 |    5589890010 | Yes         | Joel Dorsey    | %             |      100 | 07/31/2023     | 07/31/2023 to 12/31/2100 | No                |
2025-09-08 20:56:28,426 | INFO | -validating table: Direct Deposit Information
2025-09-08 20:56:28,426 | INFO | --figuring out table emptiness...
2025-09-08 20:56:59,372 | INFO | llm gpt-5-mini api call took 30.944 seconds
2025-09-08 20:56:59,386 | INFO | total input tokens: 14036
2025-09-08 20:56:59,386 | INFO | input text tokens: 13105 # estimated
2025-09-08 20:56:59,386 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:56:59,386 | INFO | cost for input: $0.017545 USD
2025-09-08 20:56:59,387 | INFO | total output tokens: 2587
2025-09-08 20:56:59,387 | INFO | cost of output: $0.02587 USD
2025-09-08 20:56:59,387 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:57:20,922 | INFO | llm gpt-5-mini api call took 21.534 seconds
2025-09-08 20:57:20,925 | INFO | total input tokens: 1723
2025-09-08 20:57:20,925 | INFO | input text tokens: 1715 # estimated
2025-09-08 20:57:20,925 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:57:20,925 | INFO | cost for input: $0.002154 USD
2025-09-08 20:57:20,925 | INFO | total output tokens: 2136
2025-09-08 20:57:20,926 | INFO | cost of output: $0.02136 USD
2025-09-08 20:57:20,926 | INFO | --got table grid emptiness info:
|Sequence No.|Transit No.|Account No.|Checking?|Account Name|Amount Code|Amount|Prenote Date|Effective Dates|Exclude Special|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X|X|X|X|X|X|
2025-09-08 20:57:36,112 | INFO | llm gpt-5 api call took 15.185 seconds
2025-09-08 20:57:36,117 | INFO | total input tokens: 3005
2025-09-08 20:57:36,117 | INFO | input text tokens: 2367 # estimated
2025-09-08 20:57:36,117 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:57:36,117 | INFO | cost for input: $0.003756 USD
2025-09-08 20:57:36,117 | INFO | total output tokens: 360
2025-09-08 20:57:36,117 | INFO | cost of output: $0.0036 USD
2025-09-08 20:57:36,118 | INFO | done judging, ALL GOOD
2025-09-08 20:57:36,119 | INFO | -current table:

2025-09-08 20:57:36,119 | INFO | -validating table: Fringe Benefit Information
2025-09-08 20:57:36,120 | INFO | -current table:
| BCode   |   Rate |   Amount |   Hours | Max/Carryover Max   | Length of Service   | Hours: Used/Avail/Total/Prob   | Dollars: Used/Avail/Total/Prob   | Effective Dates          |
|:--------|-------:|---------:|--------:|:--------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| PTO1    |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/13.86           | 0.00/0.00/0.00/249.48            | 07/27/2023 to 12/31/2100 |
2025-09-08 20:57:36,120 | INFO | -validating table: Benefit Accrual Information
2025-09-08 20:57:36,120 | INFO | --figuring out table emptiness...
2025-09-08 20:59:06,679 | INFO | llm gpt-5-mini api call took 90.558 seconds
2025-09-08 20:59:06,694 | INFO | total input tokens: 14063
2025-09-08 20:59:06,694 | INFO | input text tokens: 13132 # estimated
2025-09-08 20:59:06,695 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:59:06,695 | INFO | cost for input: $0.017579 USD
2025-09-08 20:59:06,695 | INFO | total output tokens: 3167
2025-09-08 20:59:06,695 | INFO | cost of output: $0.03167 USD
2025-09-08 20:59:06,695 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:59:37,604 | INFO | llm gpt-5-mini api call took 30.908 seconds
2025-09-08 20:59:37,606 | INFO | total input tokens: 1693
2025-09-08 20:59:37,607 | INFO | input text tokens: 1685 # estimated
2025-09-08 20:59:37,607 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:59:37,607 | INFO | cost for input: $0.002116 USD
2025-09-08 20:59:37,607 | INFO | total output tokens: 3423
2025-09-08 20:59:37,607 | INFO | cost of output: $0.03423 USD
2025-09-08 20:59:37,607 | INFO | --got table grid emptiness info:
|BCode|Rate|Amount|Hours|Max/Carryover Max|Length of Service|Hours: Used/Avail/Total/Prob|Dollars: Used/Avail/Total/Prob|Effective Dates|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X||X|X|X|
2025-09-08 21:00:04,915 | INFO | llm gpt-5 api call took 27.307 seconds
2025-09-08 21:00:04,921 | INFO | total input tokens: 3039
2025-09-08 21:00:04,921 | INFO | input text tokens: 2401 # estimated
2025-09-08 21:00:04,921 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:00:04,921 | INFO | cost for input: $0.001207 USD
2025-09-08 21:00:04,921 | INFO | total output tokens: 616
2025-09-08 21:00:04,922 | INFO | cost of output: $0.00616 USD
2025-09-08 21:00:04,922 | INFO | done judging, ALL GOOD
2025-09-08 21:00:04,923 | INFO | -current table:

2025-09-08 21:00:04,923 | INFO | -validating table: Review Information
2025-09-08 21:00:04,924 | INFO | -current table:
| Name           | Relationship   | Home Phone   | Work Phone   | Address   | City   | State   | Zip   | Country   |
|:---------------|:---------------|:-------------|:-------------|:----------|:-------|:--------|:------|:----------|
| Michel Richard |                | 667-577-7708 |              |           |        |         |       |           |
2025-09-08 21:00:04,924 | INFO | -validating table: Emergency Contact Information
2025-09-08 21:00:04,924 | INFO | --figuring out table emptiness...
2025-09-08 21:00:15,678 | INFO | llm gpt-5-mini api call took 10.751 seconds
2025-09-08 21:00:15,692 | INFO | total input tokens: 13980
2025-09-08 21:00:15,692 | INFO | input text tokens: 13049 # estimated
2025-09-08 21:00:15,692 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 21:00:15,692 | INFO | cost for input: $0.017475 USD
2025-09-08 21:00:15,693 | INFO | total output tokens: 977
2025-09-08 21:00:15,693 | INFO | cost of output: $0.00977 USD
2025-09-08 21:00:15,693 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 21:00:29,017 | INFO | llm gpt-5-mini api call took 13.324 seconds
2025-09-08 21:00:29,020 | INFO | total input tokens: 1183
2025-09-08 21:00:29,021 | INFO | input text tokens: 1175 # estimated
2025-09-08 21:00:29,021 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 21:00:29,021 | INFO | cost for input: $0.001479 USD
2025-09-08 21:00:29,021 | INFO | total output tokens: 1722
2025-09-08 21:00:29,021 | INFO | cost of output: $0.01722 USD
2025-09-08 21:00:29,021 | INFO | --got table grid emptiness info:
|Name|Relationship|Home Phone|Work Phone|Address|City|State|Zip|Country|
|---|---|---|---|---|---|---|---|---|
|X| |X| | | | | | |
2025-09-08 21:00:41,035 | INFO | llm gpt-5 api call took 12.013 seconds
2025-09-08 21:00:41,040 | INFO | total input tokens: 2919
2025-09-08 21:00:41,040 | INFO | input text tokens: 2281 # estimated
2025-09-08 21:00:41,040 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:00:41,040 | INFO | cost for input: $0.003649 USD
2025-09-08 21:00:41,040 | INFO | total output tokens: 360
2025-09-08 21:00:41,041 | INFO | cost of output: $0.0036 USD
2025-09-08 21:00:41,041 | INFO | done judging, ALL GOOD
2025-09-08 21:00:41,041 | INFO | started validating form fields
2025-09-08 21:00:41,041 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-08 21:00:41,042 | INFO | --current are:
Company Name : Velorynt Labs
Company Code : 37546
Period : 12/17/2024 to 12/26/2024
Employee Name : Joel Dorsey
Address line 1 : 1420 Brookview Lane
City : Clarkville
State : MA
Zip : 76911
Emp Id : 1121
SSN : 808-03-9317
2025-09-08 21:00:57,214 | INFO | llm gpt-5 api call took 16.165 seconds
2025-09-08 21:00:57,219 | INFO | total input tokens: 3606
2025-09-08 21:00:57,219 | INFO | input text tokens: 2968 # estimated
2025-09-08 21:00:57,219 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:00:57,219 | INFO | cost for input: $0.004508 USD
2025-09-08 21:00:57,219 | INFO | total output tokens: 704
2025-09-08 21:00:57,219 | INFO | cost of output: $0.00704 USD
2025-09-08 21:00:57,220 | INFO | done judging, ALL GOOD
2025-09-08 21:00:57,220 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-08 21:00:57,220 | INFO | --current are:
DOB (only date) : 04/25/1980
Gender : M
Marital Status : S
Status : T
Position : 
Title : 
Pay Group : 
Job Code : 
Emp Type : 
Statutory : 0.00
2025-09-08 21:01:30,788 | INFO | llm gpt-5 api call took 33.560 seconds
2025-09-08 21:01:30,793 | INFO | total input tokens: 3570
2025-09-08 21:01:30,794 | INFO | input text tokens: 2932 # estimated
2025-09-08 21:01:30,794 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:01:30,794 | INFO | cost for input: $0.004463 USD
2025-09-08 21:01:30,794 | INFO | total output tokens: 1090
2025-09-08 21:01:30,794 | INFO | cost of output: $0.0109 USD
2025-09-08 21:01:30,794 | INFO | done judging, ALL GOOD
2025-09-08 21:01:30,795 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-08 21:01:30,795 | INFO | --current are:
Seasonal : 0.00
Domestic Emp : No
Probation : 0.00
Home # : 7548815882
Work # : 
Ext. : 
Email : 
Mail Stop : 
Hire Date : 07/27/2023
Rehire Date : 
2025-09-08 21:02:10,775 | INFO | llm gpt-5 api call took 39.973 seconds
2025-09-08 21:02:10,780 | INFO | total input tokens: 3577
2025-09-08 21:02:10,780 | INFO | input text tokens: 2939 # estimated
2025-09-08 21:02:10,780 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:02:10,781 | INFO | cost for input: $0.004471 USD
2025-09-08 21:02:10,781 | INFO | total output tokens: 1025
2025-09-08 21:02:10,781 | INFO | cost of output: $0.01025 USD
2025-09-08 21:02:10,781 | INFO | done judging, ALL GOOD
2025-09-08 21:02:10,782 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-08 21:02:10,782 | INFO | --current are:
Term Date : 09/01/2023
Term Reason : N/A
Adj Sen Date : 
Pension : No
Visa Type : 
Exp : 
Citizen : 
I9 Reverify : 
I9 Verified : No
Deceased : No
2025-09-08 21:02:35,614 | INFO | llm gpt-5 api call took 24.826 seconds
2025-09-08 21:02:35,620 | INFO | total input tokens: 3573
2025-09-08 21:02:35,620 | INFO | input text tokens: 2935 # estimated
2025-09-08 21:02:35,621 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:02:35,621 | INFO | cost for input: $0.001874 USD
2025-09-08 21:02:35,621 | INFO | total output tokens: 772
2025-09-08 21:02:35,621 | INFO | cost of output: $0.00772 USD
2025-09-08 21:02:35,622 | INFO | done judging, ALL GOOD
2025-09-08 21:02:35,622 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-08 21:02:35,622 | INFO | --current are:
Tax Form : W2
WCC : 8810
EEOC : 
Supervisor ID : 
Name (supervisor name) : 
Def Comp : No
Union : 
Union Date : 
Collect Dues : No
Paid Init. Fees : No
2025-09-08 21:03:04,767 | INFO | llm gpt-5 api call took 29.139 seconds
2025-09-08 21:03:04,772 | INFO | total input tokens: 3573
2025-09-08 21:03:04,773 | INFO | input text tokens: 2935 # estimated
2025-09-08 21:03:04,773 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:03:04,773 | INFO | cost for input: $0.004466 USD
2025-09-08 21:03:04,773 | INFO | total output tokens: 711
2025-09-08 21:03:04,773 | INFO | cost of output: $0.00711 USD
2025-09-08 21:03:04,774 | INFO | done judging, ALL GOOD
2025-09-08 21:03:04,774 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-08 21:03:04,774 | INFO | --current are:
Veteran : 
Legal Rep : No
Nickname : 
surname : 
Prior Last : 
Disability : 
Smoker : No
AutoPay : 
Pay Frequency : B
OT Exempt : No
2025-09-08 21:03:45,121 | INFO | llm gpt-5 api call took 40.340 seconds
2025-09-08 21:03:45,127 | INFO | total input tokens: 3562
2025-09-08 21:03:45,127 | INFO | input text tokens: 2924 # estimated
2025-09-08 21:03:45,127 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:03:45,127 | INFO | cost for input: $0.004452 USD
2025-09-08 21:03:45,127 | INFO | total output tokens: 1473
2025-09-08 21:03:45,127 | INFO | cost of output: $0.01473 USD
2025-09-08 21:03:45,128 | INFO | done judging, ALL GOOD
2025-09-08 21:03:45,128 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-08 21:03:45,128 | INFO | --current are:
Default Hours : 0.00
Locations : 606
Positions : 700
2025-09-08 21:04:02,793 | INFO | llm gpt-5 api call took 17.658 seconds
2025-09-08 21:04:02,798 | INFO | total input tokens: 3541
2025-09-08 21:04:02,799 | INFO | input text tokens: 2903 # estimated
2025-09-08 21:04:02,799 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:04:02,799 | INFO | cost for input: $0.000826 USD
2025-09-08 21:04:02,800 | INFO | total output tokens: 785
2025-09-08 21:04:02,800 | INFO | cost of output: $0.00785 USD
2025-09-08 21:04:02,800 | INFO | done judging, ALL GOOD

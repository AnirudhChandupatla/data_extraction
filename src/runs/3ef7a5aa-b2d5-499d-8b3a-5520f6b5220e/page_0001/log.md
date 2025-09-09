2025-09-09 05:40:33,310 | INFO | started initial extraction for page 1
2025-09-09 05:42:28,769 | INFO | llm gpt-5 api call took 115.033 seconds
2025-09-09 05:42:29,340 | INFO | total input tokens: 2856
2025-09-09 05:42:29,340 | INFO | input text tokens: 2218 # estimated
2025-09-09 05:42:29,341 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:42:29,341 | INFO | cost for input: $0.00357 USD
2025-09-09 05:42:29,341 | INFO | total output tokens: 3148
2025-09-09 05:42:29,341 | INFO | cost of output: $0.03148 USD
2025-09-09 05:42:29,342 | INFO | initial extraction of page data done.
2025-09-09 05:42:35,663 | INFO | got response with OCR coordinates info from azure doc intelligence for page 1
2025-09-09 05:42:35,664 | INFO | started validating tables
2025-09-09 05:42:35,678 | INFO | -current table:
| RateCode   | Description   |   Rate | Salary   | Effective Dates          |
|:-----------|:--------------|-------:|:---------|:-------------------------|
| Base       | Base Rate     |     19 |          | 04/19/2024 to 12/31/2100 |
| Base       | Base Rate     |     18 |          | 04/28/2023 to 04/18/2024 |
2025-09-09 05:42:35,678 | INFO | -validating table: Rate/Salary Information
2025-09-09 05:42:35,679 | INFO | --figuring out table emptiness...
2025-09-09 05:43:04,665 | INFO | llm gpt-5-mini api call took 28.985 seconds
2025-09-09 05:43:04,682 | INFO | total input tokens: 16743
2025-09-09 05:43:04,682 | INFO | input text tokens: 15812 # estimated
2025-09-09 05:43:04,683 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:43:04,683 | INFO | cost for input: $0.020929 USD
2025-09-09 05:43:04,683 | INFO | total output tokens: 3716
2025-09-09 05:43:04,683 | INFO | cost of output: $0.03716 USD
2025-09-09 05:43:04,684 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 05:43:25,289 | INFO | llm gpt-5-mini api call took 20.605 seconds
2025-09-09 05:43:25,292 | INFO | total input tokens: 1908
2025-09-09 05:43:25,292 | INFO | input text tokens: 1900 # estimated
2025-09-09 05:43:25,293 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 05:43:25,293 | INFO | cost for input: $0.002385 USD
2025-09-09 05:43:25,293 | INFO | total output tokens: 3061
2025-09-09 05:43:25,293 | INFO | cost of output: $0.03061 USD
2025-09-09 05:43:25,293 | INFO | --got table grid emptiness info:
|RateCode|Description|Rate|Salary|Effective Dates|
|---:|---:|---:|---:|---:|
|X|X|X||X|
|X|X|X||X|
2025-09-09 05:43:37,041 | INFO | llm gpt-5 api call took 11.747 seconds
2025-09-09 05:43:37,046 | INFO | total input tokens: 3247
2025-09-09 05:43:37,047 | INFO | input text tokens: 2609 # estimated
2025-09-09 05:43:37,047 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:43:37,047 | INFO | cost for input: $0.004059 USD
2025-09-09 05:43:37,047 | INFO | total output tokens: 744
2025-09-09 05:43:37,047 | INFO | cost of output: $0.00744 USD
2025-09-09 05:43:37,047 | INFO | done judging, ALL GOOD
2025-09-09 05:43:37,049 | INFO | -current table:
| Employee Tax (code description)   | Status   |   Add'l Amount | Effective Dates          | Default   |
|:----------------------------------|:---------|---------------:|:-------------------------|:----------|
| MED Medicare                      |          |              0 | 04/28/2023 to 12/31/2100 | Yes       |
| SS OASDI                          |          |              0 | 04/28/2023 to 12/31/2100 | Yes       |
| FITW Federal Income Tax           | S-0      |              0 | 04/28/2023 to 12/31/2100 | Yes       |
| MN Minnesota SITW                 | S-1      |              0 | 04/28/2023 to 12/31/2100 | Yes       |
2025-09-09 05:43:37,049 | INFO | -validating table: Tax Information (Employee)
2025-09-09 05:43:37,049 | INFO | --figuring out table emptiness...
2025-09-09 05:43:58,220 | INFO | llm gpt-5-mini api call took 21.169 seconds
2025-09-09 05:43:58,239 | INFO | total input tokens: 16823
2025-09-09 05:43:58,239 | INFO | input text tokens: 15892 # estimated
2025-09-09 05:43:58,240 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:43:58,240 | INFO | cost for input: $0.021029 USD
2025-09-09 05:43:58,240 | INFO | total output tokens: 2525
2025-09-09 05:43:58,240 | INFO | cost of output: $0.02525 USD
2025-09-09 05:43:58,241 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 05:44:52,778 | INFO | llm gpt-5-mini api call took 54.537 seconds
2025-09-09 05:44:52,780 | INFO | total input tokens: 2135
2025-09-09 05:44:52,781 | INFO | input text tokens: 2127 # estimated
2025-09-09 05:44:52,781 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 05:44:52,781 | INFO | cost for input: $0.002669 USD
2025-09-09 05:44:52,781 | INFO | total output tokens: 6285
2025-09-09 05:44:52,781 | INFO | cost of output: $0.06285 USD
2025-09-09 05:44:52,782 | INFO | --got table grid emptiness info:
|Employee Tax (code description)|Status|Add'l Amount|Effective Dates|Default|
|---|---|---|---|---|
|X| |X|X|X|
|X| |X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
2025-09-09 05:45:15,519 | INFO | llm gpt-5 api call took 22.737 seconds
2025-09-09 05:45:15,525 | INFO | total input tokens: 3352
2025-09-09 05:45:15,525 | INFO | input text tokens: 2714 # estimated
2025-09-09 05:45:15,525 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:45:15,526 | INFO | cost for input: $0.00419 USD
2025-09-09 05:45:15,526 | INFO | total output tokens: 552
2025-09-09 05:45:15,526 | INFO | cost of output: $0.00552 USD
2025-09-09 05:45:15,526 | INFO | done judging, ALL GOOD
2025-09-09 05:45:15,527 | INFO | -current table:
| Employer Tax (code description)         | Effective Dates          | Default   |
|:----------------------------------------|:-------------------------|:----------|
| MED-R Medicare - Employer               | 04/28/2023 to 12/31/2100 |           |
| SS-R OASDI - Employer                   | 04/28/2023 to 12/31/2100 |           |
| FUTA Fed Unemployment                   | 04/28/2023 to 12/31/2100 |           |
| MNAST Minnesota Federal Loan Assessment | 04/28/2023 to 12/31/2100 |           |
| MNDW Workforce Enhancement Fee          | 04/28/2023 to 12/31/2100 |           |
| MNSUI Minnesota SUI                     | 04/28/2023 to 12/31/2100 |           |
2025-09-09 05:45:15,528 | INFO | -validating table: Tax Information (Employer)
2025-09-09 05:45:15,528 | INFO | --figuring out table emptiness...
2025-09-09 05:45:34,981 | INFO | llm gpt-5-mini api call took 19.452 seconds
2025-09-09 05:45:34,998 | INFO | total input tokens: 16837
2025-09-09 05:45:34,998 | INFO | input text tokens: 15906 # estimated
2025-09-09 05:45:34,998 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:45:34,998 | INFO | cost for input: $0.021046 USD
2025-09-09 05:45:34,998 | INFO | total output tokens: 2093
2025-09-09 05:45:34,998 | INFO | cost of output: $0.02093 USD
2025-09-09 05:45:34,999 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 05:45:44,300 | INFO | llm gpt-5-mini api call took 9.301 seconds
2025-09-09 05:45:44,302 | INFO | total input tokens: 1883
2025-09-09 05:45:44,303 | INFO | input text tokens: 1875 # estimated
2025-09-09 05:45:44,303 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 05:45:44,303 | INFO | cost for input: $0.002354 USD
2025-09-09 05:45:44,303 | INFO | total output tokens: 1271
2025-09-09 05:45:44,303 | INFO | cost of output: $0.01271 USD
2025-09-09 05:45:44,303 | INFO | --got table grid emptiness info:
|Employer Tax (code description)|Effective Dates|Default|
|---|---|---|
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
2025-09-09 05:46:07,802 | INFO | llm gpt-5 api call took 23.498 seconds
2025-09-09 05:46:07,807 | INFO | total input tokens: 3344
2025-09-09 05:46:07,807 | INFO | input text tokens: 2706 # estimated
2025-09-09 05:46:07,807 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:46:07,807 | INFO | cost for input: $0.00418 USD
2025-09-09 05:46:07,807 | INFO | total output tokens: 808
2025-09-09 05:46:07,808 | INFO | cost of output: $0.00808 USD
2025-09-09 05:46:07,808 | INFO | done judging, ALL GOOD
2025-09-09 05:46:07,809 | INFO | -current table:
| Code   | Deduction         |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-------|:------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| 401KC  | 401K Contribution |    100 |            |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 07/01/2023 to 12/31/2100 |
2025-09-09 05:46:07,809 | INFO | -validating table: Deduction Information
2025-09-09 05:46:07,810 | INFO | --figuring out table emptiness...
2025-09-09 05:46:34,292 | INFO | llm gpt-5-mini api call took 26.481 seconds
2025-09-09 05:46:34,309 | INFO | total input tokens: 16789
2025-09-09 05:46:34,309 | INFO | input text tokens: 15858 # estimated
2025-09-09 05:46:34,309 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:46:34,309 | INFO | cost for input: $0.020986 USD
2025-09-09 05:46:34,310 | INFO | total output tokens: 1676
2025-09-09 05:46:34,310 | INFO | cost of output: $0.01676 USD
2025-09-09 05:46:34,310 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 05:47:10,089 | INFO | llm gpt-5-mini api call took 35.779 seconds
2025-09-09 05:47:10,094 | INFO | total input tokens: 1635
2025-09-09 05:47:10,095 | INFO | input text tokens: 1627 # estimated
2025-09-09 05:47:10,095 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 05:47:10,095 | INFO | cost for input: $0.002044 USD
2025-09-09 05:47:10,095 | INFO | total output tokens: 5387
2025-09-09 05:47:10,096 | INFO | cost of output: $0.05387 USD
2025-09-09 05:47:10,096 | INFO | --got table grid emptiness info:
|Code|Deduction|Rate|CalcCode|Frequency|Goal/Paid|Min/Max/Annual Max|Arrears|Agency|Effective Dates|
|---|---|---|---|---|---|---|---|---|---|
|X|X|X|||X|X|X||X|
2025-09-09 05:47:34,754 | INFO | llm gpt-5 api call took 24.658 seconds
2025-09-09 05:47:34,760 | INFO | total input tokens: 3315
2025-09-09 05:47:34,760 | INFO | input text tokens: 2677 # estimated
2025-09-09 05:47:34,760 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:47:34,760 | INFO | cost for input: $0.004144 USD
2025-09-09 05:47:34,760 | INFO | total output tokens: 872
2025-09-09 05:47:34,760 | INFO | cost of output: $0.00872 USD
2025-09-09 05:47:34,761 | INFO | done judging, ALL GOOD
2025-09-09 05:47:34,762 | INFO | -current table:
|   Sequence No. |   Transit No. |   Account No. | Checking?   | Account Name   | Amount Code   |   Amount | Prenote Date   | Effective Dates          | Exclude Special   |
|---------------:|--------------:|--------------:|:------------|:---------------|:--------------|---------:|:---------------|:-------------------------|:------------------|
|             99 |     296075933 |    2294694696 | Yes         | Caroline       | %             |      100 | 04/28/2023     | 04/01/2023 to 12/31/2100 | No                |
2025-09-09 05:47:34,762 | INFO | -validating table: Direct Deposit Information
2025-09-09 05:47:34,762 | INFO | --figuring out table emptiness...
2025-09-09 05:47:54,606 | INFO | llm gpt-5-mini api call took 19.843 seconds
2025-09-09 05:47:54,623 | INFO | total input tokens: 16784
2025-09-09 05:47:54,624 | INFO | input text tokens: 15853 # estimated
2025-09-09 05:47:54,624 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:47:54,624 | INFO | cost for input: $0.002548 USD
2025-09-09 05:47:54,624 | INFO | total output tokens: 2506
2025-09-09 05:47:54,624 | INFO | cost of output: $0.02506 USD
2025-09-09 05:47:54,624 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 05:48:30,337 | INFO | llm gpt-5-mini api call took 35.712 seconds
2025-09-09 05:48:30,340 | INFO | total input tokens: 1755
2025-09-09 05:48:30,340 | INFO | input text tokens: 1747 # estimated
2025-09-09 05:48:30,340 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 05:48:30,340 | INFO | cost for input: $0.002194 USD
2025-09-09 05:48:30,340 | INFO | total output tokens: 5016
2025-09-09 05:48:30,340 | INFO | cost of output: $0.05016 USD
2025-09-09 05:48:30,340 | INFO | --got table grid emptiness info:
|Sequence No.|Transit No.|Account No.|Checking?|Account Name|Amount Code|Amount|Prenote Date|Effective Dates|Exclude Special|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X|X|X|X|X|X|
2025-09-09 05:48:41,108 | INFO | llm gpt-5 api call took 10.767 seconds
2025-09-09 05:48:41,113 | INFO | total input tokens: 3323
2025-09-09 05:48:41,114 | INFO | input text tokens: 2685 # estimated
2025-09-09 05:48:41,114 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:48:41,114 | INFO | cost for input: $0.004154 USD
2025-09-09 05:48:41,115 | INFO | total output tokens: 360
2025-09-09 05:48:41,115 | INFO | cost of output: $0.0036 USD
2025-09-09 05:48:41,115 | INFO | done judging, ALL GOOD
2025-09-09 05:48:41,117 | INFO | -current table:
| ECode   | CalcCode   | Rate Code   |   Rate | Rate Per   |   Amount | Tabled?   |   Units | Frequency   | Goal/Paid/Goal Bal.   | Min/Max/Ann. Max   | Effective Dates          |
|:--------|:-----------|:------------|-------:|:-----------|---------:|:----------|--------:|:------------|:----------------------|:-------------------|:-------------------------|
| STD     |            |             |      0 |            |      9.5 | No        |       0 | ML          | 0.00/0.00/0.00        | 0.00/0.00/0.00     | 08/30/2024 to 12/31/2100 |
2025-09-09 05:48:41,117 | INFO | -validating table: Fringe Benefit Information
2025-09-09 05:48:41,117 | INFO | --figuring out table emptiness...
2025-09-09 05:49:07,940 | INFO | llm gpt-5-mini api call took 26.822 seconds
2025-09-09 05:49:07,958 | INFO | total input tokens: 16817
2025-09-09 05:49:07,958 | INFO | input text tokens: 15886 # estimated
2025-09-09 05:49:07,958 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:49:07,959 | INFO | cost for input: $0.021021 USD
2025-09-09 05:49:07,959 | INFO | total output tokens: 2400
2025-09-09 05:49:07,959 | INFO | cost of output: $0.024 USD
2025-09-09 05:49:07,959 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 05:49:53,439 | INFO | llm gpt-5-mini api call took 45.480 seconds
2025-09-09 05:49:53,442 | INFO | total input tokens: 1801
2025-09-09 05:49:53,442 | INFO | input text tokens: 1793 # estimated
2025-09-09 05:49:53,442 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 05:49:53,443 | INFO | cost for input: $0.002251 USD
2025-09-09 05:49:53,443 | INFO | total output tokens: 5814
2025-09-09 05:49:53,443 | INFO | cost of output: $0.05814 USD
2025-09-09 05:49:53,443 | INFO | --got table grid emptiness info:
|ECode|CalcCode|Rate Code|Rate|Rate Per|Amount|Tabled?|Units|Frequency|Goal/Paid/Goal Bal.|Min/Max/Ann. Max|Effective Dates|
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|X| | |X| |X|X|X|X|X|X|X|
2025-09-09 05:50:15,582 | INFO | llm gpt-5 api call took 22.138 seconds
2025-09-09 05:50:15,587 | INFO | total input tokens: 3386
2025-09-09 05:50:15,587 | INFO | input text tokens: 2748 # estimated
2025-09-09 05:50:15,587 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:50:15,587 | INFO | cost for input: $0.001208 USD
2025-09-09 05:50:15,587 | INFO | total output tokens: 872
2025-09-09 05:50:15,588 | INFO | cost of output: $0.00872 USD
2025-09-09 05:50:15,588 | INFO | done judging, ALL GOOD
2025-09-09 05:50:15,589 | INFO | -current table:
| BCode   |   Rate |   Amount |   Hours | Max/Carryover Max   | Length of Service   | Hours: Used/Avail/Total/Prob   | Dollars: Used/Avail/Total/Prob   | Effective Dates          |
|:--------|-------:|---------:|--------:|:--------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| ESST    |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/14.11/0.00/0.00           | 0.00/257.31/0.00/0.00            | 01/01/2024 to 06/01/2024 |
| PTO1    |      0 |        0 |       0 | 0.00/0.00           |                     | 23.00/39.36/0.00/0.00          | 437.00/747.84/0.00/0.00          | 06/02/2024 to 12/31/2100 |
| PTO2    |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/38.31/0.00/0.00           | 0.00/689.58/0.00/0.00            | 04/19/2023 to 09/09/2023 |
2025-09-09 05:50:15,590 | INFO | -validating table: Benefit Accrual Information
2025-09-09 05:50:15,590 | INFO | --figuring out table emptiness...
2025-09-09 05:51:44,260 | INFO | llm gpt-5-mini api call took 88.669 seconds
2025-09-09 05:51:44,277 | INFO | total input tokens: 16976
2025-09-09 05:51:44,278 | INFO | input text tokens: 16045 # estimated
2025-09-09 05:51:44,278 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:51:44,278 | INFO | cost for input: $0.002788 USD
2025-09-09 05:51:44,278 | INFO | total output tokens: 3180
2025-09-09 05:51:44,278 | INFO | cost of output: $0.0318 USD
2025-09-09 05:51:44,278 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 05:53:18,413 | INFO | llm gpt-5-mini api call took 94.134 seconds
2025-09-09 05:53:18,416 | INFO | total input tokens: 2587
2025-09-09 05:53:18,416 | INFO | input text tokens: 2579 # estimated
2025-09-09 05:53:18,416 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 05:53:18,417 | INFO | cost for input: $0.003234 USD
2025-09-09 05:53:18,417 | INFO | total output tokens: 5956
2025-09-09 05:53:18,417 | INFO | cost of output: $0.05956 USD
2025-09-09 05:53:18,417 | INFO | --got table grid emptiness info:
|BCode|Rate|Amount|Hours|Max/Carryover Max|Length of Service|Hours: Used/Avail/Total/Prob|Dollars: Used/Avail/Total/Prob|Effective Dates|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
2025-09-09 05:53:48,680 | INFO | llm gpt-5 api call took 30.263 seconds
2025-09-09 05:53:48,686 | INFO | total input tokens: 3559
2025-09-09 05:53:48,686 | INFO | input text tokens: 2921 # estimated
2025-09-09 05:53:48,686 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:53:48,686 | INFO | cost for input: $0.004449 USD
2025-09-09 05:53:48,686 | INFO | total output tokens: 616
2025-09-09 05:53:48,686 | INFO | cost of output: $0.00616 USD
2025-09-09 05:53:48,687 | INFO | done judging, ALL GOOD
2025-09-09 05:53:48,691 | INFO | -current table:

2025-09-09 05:53:48,691 | INFO | -validating table: Review Information
2025-09-09 05:53:48,692 | INFO | -current table:

2025-09-09 05:53:48,692 | INFO | -validating table: Emergency Contact Information
2025-09-09 05:53:48,692 | INFO | started validating form fields
2025-09-09 05:53:48,692 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-09 05:53:48,692 | INFO | --current are:
Company Name : Velorynt Labs
Company Code : 37546
Period : 12/17/2024 to 12/26/2024
Employee Name : Caroline Jones
Address line 1 : Stream Apt. 219
City : Riverton
State : UT
Zip : 47589
Emp Id : 4632
SSN : 088-39-6286
2025-09-09 05:54:08,119 | INFO | llm gpt-5 api call took 19.418 seconds
2025-09-09 05:54:08,131 | INFO | total input tokens: 4338
2025-09-09 05:54:08,131 | INFO | input text tokens: 3700 # estimated
2025-09-09 05:54:08,131 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:54:08,131 | INFO | cost for input: $0.005423 USD
2025-09-09 05:54:08,132 | INFO | total output tokens: 512
2025-09-09 05:54:08,132 | INFO | cost of output: $0.00512 USD
2025-09-09 05:54:08,132 | INFO | done judging, ALL GOOD
2025-09-09 05:54:08,132 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-09 05:54:08,133 | INFO | --current are:
DOB (only date) : 12/26/2001
Gender : M
Marital Status : S
Status : A
Position : 
Title : 
Pay Group : 
Job Code : 
Emp Type : 
Statutory : 0.00
2025-09-09 05:54:34,666 | INFO | llm gpt-5 api call took 26.523 seconds
2025-09-09 05:54:34,673 | INFO | total input tokens: 4303
2025-09-09 05:54:34,673 | INFO | input text tokens: 3665 # estimated
2025-09-09 05:54:34,673 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:54:34,673 | INFO | cost for input: $0.005379 USD
2025-09-09 05:54:34,673 | INFO | total output tokens: 1090
2025-09-09 05:54:34,673 | INFO | cost of output: $0.0109 USD
2025-09-09 05:54:34,674 | INFO | done judging, ALL GOOD
2025-09-09 05:54:34,674 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-09 05:54:34,674 | INFO | --current are:
Seasonal : 0.00
Domestic Emp : No
Probation : 0.00
Home # : 509-121-3247
Work # : 
Ext. : 
Email : 
Mail Stop : 
Hire Date : 04/19/2023
Rehire Date : 
2025-09-09 05:54:48,125 | INFO | llm gpt-5 api call took 13.443 seconds
2025-09-09 05:54:48,131 | INFO | total input tokens: 4312
2025-09-09 05:54:48,131 | INFO | input text tokens: 3674 # estimated
2025-09-09 05:54:48,131 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:54:48,131 | INFO | cost for input: $0.00251 USD
2025-09-09 05:54:48,131 | INFO | total output tokens: 769
2025-09-09 05:54:48,131 | INFO | cost of output: $0.00769 USD
2025-09-09 05:54:48,132 | INFO | done judging, ALL GOOD
2025-09-09 05:54:48,132 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-09 05:54:48,132 | INFO | --current are:
Term Date : 
Term Reason : 
Adj Sen Date : 
Pension : No
Visa Type : 
Exp : 
Citizen : 
I9 Reverify : 
I9 Verified : No
Deceased : No
2025-09-09 05:55:07,505 | INFO | llm gpt-5 api call took 19.365 seconds
2025-09-09 05:55:07,512 | INFO | total input tokens: 4297
2025-09-09 05:55:07,512 | INFO | input text tokens: 3659 # estimated
2025-09-09 05:55:07,512 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:55:07,512 | INFO | cost for input: $0.005371 USD
2025-09-09 05:55:07,512 | INFO | total output tokens: 644
2025-09-09 05:55:07,513 | INFO | cost of output: $0.00644 USD
2025-09-09 05:55:07,513 | INFO | done judging, ALL GOOD
2025-09-09 05:55:07,513 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-09 05:55:07,513 | INFO | --current are:
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
2025-09-09 05:55:28,263 | INFO | llm gpt-5 api call took 20.742 seconds
2025-09-09 05:55:28,268 | INFO | total input tokens: 4306
2025-09-09 05:55:28,269 | INFO | input text tokens: 3668 # estimated
2025-09-09 05:55:28,269 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:55:28,269 | INFO | cost for input: $0.005383 USD
2025-09-09 05:55:28,269 | INFO | total output tokens: 839
2025-09-09 05:55:28,269 | INFO | cost of output: $0.00839 USD
2025-09-09 05:55:28,270 | INFO | done judging, ALL GOOD
2025-09-09 05:55:28,270 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 05:55:28,270 | INFO | --current are:
Veteran : 
Legal Rep : No
Nickname : 
surname : surname
Prior Last : 
Disability : 
Smoker : No
AutoPay : No
Pay Frequency : B
OT Exempt : No
2025-09-09 05:56:24,858 | INFO | llm gpt-5 api call took 56.580 seconds
2025-09-09 05:56:24,864 | INFO | total input tokens: 4299
2025-09-09 05:56:24,864 | INFO | input text tokens: 3661 # estimated
2025-09-09 05:56:24,865 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:56:24,865 | INFO | cost for input: $0.005374 USD
2025-09-09 05:56:24,865 | INFO | total output tokens: 2216
2025-09-09 05:56:24,865 | INFO | cost of output: $0.02216 USD
2025-09-09 05:56:24,865 | INFO | --found issues: [{'data_name': 'surname', 'status': 'wrong', 'feedback': "Captured the label text 'surname' as value; field appears blank in the image."}, {'data_name': 'AutoPay', 'status': 'wrong', 'feedback': "No standalone AutoPay form field value; 'No AutoPay Information' is a section, not the field."}]
2025-09-09 05:56:41,178 | INFO | llm gpt-5-mini api call took 16.312 seconds
2025-09-09 05:56:41,182 | INFO | total input tokens: 2571
2025-09-09 05:56:41,182 | INFO | input text tokens: 1640 # estimated
2025-09-09 05:56:41,182 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:56:41,182 | INFO | cost for input: $0.003214 USD
2025-09-09 05:56:41,182 | INFO | total output tokens: 445
2025-09-09 05:56:41,182 | INFO | cost of output: $0.00445 USD
2025-09-09 05:56:41,183 | INFO | --corrected as:
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
2025-09-09 05:56:41,183 | INFO | -revalidating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 05:57:23,884 | INFO | llm gpt-5 api call took 42.701 seconds
2025-09-09 05:57:23,890 | INFO | total input tokens: 4295
2025-09-09 05:57:23,891 | INFO | input text tokens: 3657 # estimated
2025-09-09 05:57:23,891 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:57:23,891 | INFO | cost for input: $0.005369 USD
2025-09-09 05:57:23,891 | INFO | total output tokens: 1996
2025-09-09 05:57:23,891 | INFO | cost of output: $0.01996 USD
2025-09-09 05:57:23,892 | INFO | --found issues: [{'data_name': 'Nickname', 'status': 'wrong', 'feedback': "Field is present with value 'surname', not empty."}]
2025-09-09 05:57:30,258 | INFO | llm gpt-5-mini api call took 6.366 seconds
2025-09-09 05:57:30,262 | INFO | total input tokens: 2536
2025-09-09 05:57:30,262 | INFO | input text tokens: 1605 # estimated
2025-09-09 05:57:30,262 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:57:30,262 | INFO | cost for input: $0.00317 USD
2025-09-09 05:57:30,262 | INFO | total output tokens: 446
2025-09-09 05:57:30,262 | INFO | cost of output: $0.00446 USD
2025-09-09 05:57:30,263 | INFO | --corrected as:
Veteran : 
Legal Rep : No
Nickname : surname
surname : 
Prior Last : 
Disability : 
Smoker : No
AutoPay : 
Pay Frequency : B
OT Exempt : No
2025-09-09 05:57:30,263 | INFO | -revalidating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 05:58:34,795 | INFO | llm gpt-5 api call took 64.532 seconds
2025-09-09 05:58:34,801 | INFO | total input tokens: 4297
2025-09-09 05:58:34,801 | INFO | input text tokens: 3659 # estimated
2025-09-09 05:58:34,802 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:58:34,802 | INFO | cost for input: $0.005371 USD
2025-09-09 05:58:34,802 | INFO | total output tokens: 1935
2025-09-09 05:58:34,802 | INFO | cost of output: $0.01935 USD
2025-09-09 05:58:34,802 | INFO | --found issues: [{'data_name': 'Nickname', 'status': 'wrong', 'feedback': "Should be empty; value set to another field name ('surname')."}]
2025-09-09 05:58:42,644 | INFO | llm gpt-5-mini api call took 7.841 seconds
2025-09-09 05:58:42,648 | INFO | total input tokens: 2541
2025-09-09 05:58:42,648 | INFO | input text tokens: 1610 # estimated
2025-09-09 05:58:42,648 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:58:42,648 | INFO | cost for input: $0.003176 USD
2025-09-09 05:58:42,648 | INFO | total output tokens: 509
2025-09-09 05:58:42,648 | INFO | cost of output: $0.00509 USD
2025-09-09 05:58:42,649 | INFO | --corrected as:
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
2025-09-09 05:58:42,649 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-09 05:58:42,649 | INFO | --current are:
Default Hours : 0.00
Locations : 605
Positions : 700
2025-09-09 05:59:03,009 | INFO | llm gpt-5 api call took 20.352 seconds
2025-09-09 05:59:03,015 | INFO | total input tokens: 4274
2025-09-09 05:59:03,015 | INFO | input text tokens: 3636 # estimated
2025-09-09 05:59:03,015 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:59:03,016 | INFO | cost for input: $0.005343 USD
2025-09-09 05:59:03,016 | INFO | total output tokens: 657
2025-09-09 05:59:03,016 | INFO | cost of output: $0.00657 USD
2025-09-09 05:59:03,016 | INFO | done judging, ALL GOOD

2025-09-08 20:05:29,649 | INFO | started initial extraction for page 1
2025-09-08 20:07:27,072 | INFO | llm gpt-5 api call took 116.967 seconds
2025-09-08 20:07:27,688 | INFO | total input tokens: 2856
2025-09-08 20:07:27,689 | INFO | input text tokens: 2218 # estimated
2025-09-08 20:07:27,689 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:07:27,689 | INFO | cost for input: $0.00357 USD
2025-09-08 20:07:27,689 | INFO | total output tokens: 3208
2025-09-08 20:07:27,689 | INFO | cost of output: $0.03208 USD
2025-09-08 20:07:27,691 | INFO | initial extraction of page data done.
2025-09-08 20:07:35,367 | INFO | got response with OCR coordinates info from azure doc intelligence for page 1
2025-09-08 20:07:35,367 | INFO | started validating tables
2025-09-08 20:07:35,378 | INFO | -current table:
| RateCode   | Description   |   Rate | Salary   | Effective Dates          |
|:-----------|:--------------|-------:|:---------|:-------------------------|
| Base       | Base Rate     |     19 |          | 04/19/2024 to 12/31/2100 |
| Base       | Base Rate     |     18 |          | 04/28/2023 to 04/18/2024 |
2025-09-08 20:07:35,378 | INFO | -validating table: Rate/Salary Information
2025-09-08 20:07:35,378 | INFO | --figuring out table emptiness...
2025-09-08 20:07:59,011 | INFO | llm gpt-5-mini api call took 23.631 seconds
2025-09-08 20:07:59,029 | INFO | total input tokens: 16743
2025-09-08 20:07:59,029 | INFO | input text tokens: 15812 # estimated
2025-09-08 20:07:59,029 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:07:59,029 | INFO | cost for input: $0.002497 USD
2025-09-08 20:07:59,030 | INFO | total output tokens: 2244
2025-09-08 20:07:59,030 | INFO | cost of output: $0.02244 USD
2025-09-08 20:07:59,030 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:08:16,481 | INFO | llm gpt-5-mini api call took 17.451 seconds
2025-09-08 20:08:16,486 | INFO | total input tokens: 1795
2025-09-08 20:08:16,487 | INFO | input text tokens: 1787 # estimated
2025-09-08 20:08:16,487 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:08:16,487 | INFO | cost for input: $0.002244 USD
2025-09-08 20:08:16,488 | INFO | total output tokens: 2034
2025-09-08 20:08:16,488 | INFO | cost of output: $0.02034 USD
2025-09-08 20:08:16,488 | INFO | --got table grid emptiness info:
|RateCode|Description|Rate|Salary|Effective Dates|
|---|---|---|---|---|
|X|X|X| |X|
|X|X|X| |X|
2025-09-08 20:08:34,644 | INFO | llm gpt-5 api call took 18.156 seconds
2025-09-08 20:08:34,649 | INFO | total input tokens: 3244
2025-09-08 20:08:34,649 | INFO | input text tokens: 2606 # estimated
2025-09-08 20:08:34,650 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:08:34,650 | INFO | cost for input: $0.004055 USD
2025-09-08 20:08:34,650 | INFO | total output tokens: 552
2025-09-08 20:08:34,650 | INFO | cost of output: $0.00552 USD
2025-09-08 20:08:34,650 | INFO | done judging, ALL GOOD
2025-09-08 20:08:34,652 | INFO | -current table:
| Employee Tax (code description)   | Status   |   Add'l Amount | Effective Dates          | Default   |
|:----------------------------------|:---------|---------------:|:-------------------------|:----------|
| MED Medicare                      |          |              0 | 04/28/2023 to 12/31/2100 | Yes       |
| SS OASDI                          |          |              0 | 04/28/2023 to 12/31/2100 | Yes       |
| FITW Federal Income Tax           | S-0      |              0 | 04/28/2023 to 12/31/2100 | Yes       |
| MN Minnesota SITW                 | S-1      |              0 | 04/28/2023 to 12/31/2100 | Yes       |
2025-09-08 20:08:34,652 | INFO | -validating table: Tax Information (Employee)
2025-09-08 20:08:34,652 | INFO | --figuring out table emptiness...
2025-09-08 20:09:12,463 | INFO | llm gpt-5-mini api call took 37.810 seconds
2025-09-08 20:09:12,480 | INFO | total input tokens: 16823
2025-09-08 20:09:12,480 | INFO | input text tokens: 15892 # estimated
2025-09-08 20:09:12,481 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:09:12,481 | INFO | cost for input: $0.002597 USD
2025-09-08 20:09:12,481 | INFO | total output tokens: 3549
2025-09-08 20:09:12,481 | INFO | cost of output: $0.03549 USD
2025-09-08 20:09:12,482 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:09:43,716 | INFO | llm gpt-5-mini api call took 31.234 seconds
2025-09-08 20:09:43,719 | INFO | total input tokens: 2022
2025-09-08 20:09:43,719 | INFO | input text tokens: 2014 # estimated
2025-09-08 20:09:43,720 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:09:43,720 | INFO | cost for input: $0.002527 USD
2025-09-08 20:09:43,720 | INFO | total output tokens: 3149
2025-09-08 20:09:43,720 | INFO | cost of output: $0.03149 USD
2025-09-08 20:09:43,720 | INFO | --got table grid emptiness info:
|Employee Tax (code description)|Status|Add'l Amount|Effective Dates|Default|
|---|---|---|---|---|
|X| |X|X|X|
|X| |X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
2025-09-08 20:10:01,915 | INFO | llm gpt-5 api call took 18.194 seconds
2025-09-08 20:10:01,920 | INFO | total input tokens: 3352
2025-09-08 20:10:01,920 | INFO | input text tokens: 2714 # estimated
2025-09-08 20:10:01,920 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:10:01,920 | INFO | cost for input: $0.00419 USD
2025-09-08 20:10:01,921 | INFO | total output tokens: 488
2025-09-08 20:10:01,921 | INFO | cost of output: $0.00488 USD
2025-09-08 20:10:01,921 | INFO | done judging, ALL GOOD
2025-09-08 20:10:01,922 | INFO | -current table:
| Employer Tax (code description)         | Effective Dates          | Default   |
|:----------------------------------------|:-------------------------|:----------|
| MED-R Medicare - Employer               | 04/28/2023 to 12/31/2100 |           |
| SS-R OASDI - Employer                   | 04/28/2023 to 12/31/2100 |           |
| FUTA Fed Unemployment                   | 04/28/2023 to 12/31/2100 |           |
| MNAST Minnesota Federal Loan Assessment | 04/28/2023 to 12/31/2100 |           |
| MNDW Workforce Enhancement Fee          | 04/28/2023 to 12/31/2100 |           |
| MNSUI Minnesota SUI                     | 04/28/2023 to 12/31/2100 |           |
2025-09-08 20:10:01,923 | INFO | -validating table: Tax Information (Employer)
2025-09-08 20:10:01,923 | INFO | --figuring out table emptiness...
2025-09-08 20:10:23,076 | INFO | llm gpt-5-mini api call took 21.152 seconds
2025-09-08 20:10:23,094 | INFO | total input tokens: 16837
2025-09-08 20:10:23,094 | INFO | input text tokens: 15906 # estimated
2025-09-08 20:10:23,094 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:10:23,094 | INFO | cost for input: $0.021046 USD
2025-09-08 20:10:23,095 | INFO | total output tokens: 2541
2025-09-08 20:10:23,095 | INFO | cost of output: $0.02541 USD
2025-09-08 20:10:23,095 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:10:56,603 | INFO | llm gpt-5-mini api call took 33.508 seconds
2025-09-08 20:10:56,608 | INFO | total input tokens: 1770
2025-09-08 20:10:56,608 | INFO | input text tokens: 1762 # estimated
2025-09-08 20:10:56,609 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:10:56,609 | INFO | cost for input: $0.002213 USD
2025-09-08 20:10:56,609 | INFO | total output tokens: 2940
2025-09-08 20:10:56,609 | INFO | cost of output: $0.0294 USD
2025-09-08 20:10:56,609 | INFO | --got table grid emptiness info:
|Employer Tax (code description)|Effective Dates|Default|
|---:|:---:|:---:|
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
2025-09-08 20:11:23,043 | INFO | llm gpt-5 api call took 26.433 seconds
2025-09-08 20:11:23,049 | INFO | total input tokens: 3349
2025-09-08 20:11:23,049 | INFO | input text tokens: 2711 # estimated
2025-09-08 20:11:23,050 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:11:23,050 | INFO | cost for input: $0.004186 USD
2025-09-08 20:11:23,050 | INFO | total output tokens: 552
2025-09-08 20:11:23,050 | INFO | cost of output: $0.00552 USD
2025-09-08 20:11:23,051 | INFO | done judging, ALL GOOD
2025-09-08 20:11:23,052 | INFO | -current table:
| Code   | Deduction         |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-------|:------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| 401KC  | 401K Contribution |    100 |            |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 07/01/2023 to 12/31/2100 |
2025-09-08 20:11:23,053 | INFO | -validating table: Deduction Information
2025-09-08 20:11:23,053 | INFO | --figuring out table emptiness...
2025-09-08 20:11:46,046 | INFO | llm gpt-5-mini api call took 22.992 seconds
2025-09-08 20:11:46,063 | INFO | total input tokens: 16789
2025-09-08 20:11:46,063 | INFO | input text tokens: 15858 # estimated
2025-09-08 20:11:46,064 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:11:46,064 | INFO | cost for input: $0.020986 USD
2025-09-08 20:11:46,064 | INFO | total output tokens: 2695
2025-09-08 20:11:46,064 | INFO | cost of output: $0.02695 USD
2025-09-08 20:11:46,065 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:12:09,364 | INFO | llm gpt-5-mini api call took 23.299 seconds
2025-09-08 20:12:09,367 | INFO | total input tokens: 1709
2025-09-08 20:12:09,367 | INFO | input text tokens: 1701 # estimated
2025-09-08 20:12:09,368 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:12:09,368 | INFO | cost for input: $0.002136 USD
2025-09-08 20:12:09,368 | INFO | total output tokens: 2718
2025-09-08 20:12:09,368 | INFO | cost of output: $0.02718 USD
2025-09-08 20:12:09,368 | INFO | --got table grid emptiness info:
|Code|Deduction|Rate|CalcCode|Frequency|Goal/Paid|Min/Max/Annual Max|Arrears|Agency|Effective Dates|
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|X|X|X|||X|X|X||X|
2025-09-08 20:12:30,843 | INFO | llm gpt-5 api call took 21.474 seconds
2025-09-08 20:12:30,848 | INFO | total input tokens: 3334
2025-09-08 20:12:30,848 | INFO | input text tokens: 2696 # estimated
2025-09-08 20:12:30,848 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:12:30,848 | INFO | cost for input: $0.004168 USD
2025-09-08 20:12:30,849 | INFO | total output tokens: 488
2025-09-08 20:12:30,849 | INFO | cost of output: $0.00488 USD
2025-09-08 20:12:30,849 | INFO | done judging, ALL GOOD
2025-09-08 20:12:30,850 | INFO | -current table:
|   Sequence No. |   Transit No. |   Account No. | Checking?   | Account Name   | Amount Code   |   Amount | Prenote Date   | Effective Dates          | Exclude Special   |
|---------------:|--------------:|--------------:|:------------|:---------------|:--------------|---------:|:---------------|:-------------------------|:------------------|
|             99 |     296075933 |    2294694696 | Yes         | Caroline       | %             |      100 | 04/28/2023     | 04/01/2023 to 12/31/2100 | No                |
2025-09-08 20:12:30,851 | INFO | -validating table: Direct Deposit Information
2025-09-08 20:12:30,851 | INFO | --figuring out table emptiness...
2025-09-08 20:12:57,713 | INFO | llm gpt-5-mini api call took 26.861 seconds
2025-09-08 20:12:57,732 | INFO | total input tokens: 16784
2025-09-08 20:12:57,732 | INFO | input text tokens: 15853 # estimated
2025-09-08 20:12:57,732 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:12:57,733 | INFO | cost for input: $0.02098 USD
2025-09-08 20:12:57,733 | INFO | total output tokens: 2396
2025-09-08 20:12:57,733 | INFO | cost of output: $0.02396 USD
2025-09-08 20:12:57,733 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:13:15,908 | INFO | llm gpt-5-mini api call took 18.174 seconds
2025-09-08 20:13:15,912 | INFO | total input tokens: 1468
2025-09-08 20:13:15,912 | INFO | input text tokens: 1460 # estimated
2025-09-08 20:13:15,927 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:13:15,927 | INFO | cost for input: $0.001835 USD
2025-09-08 20:13:15,927 | INFO | total output tokens: 2297
2025-09-08 20:13:15,927 | INFO | cost of output: $0.02297 USD
2025-09-08 20:13:15,928 | INFO | --got table grid emptiness info:
|Sequence No.|Transit No.|Account No.|Checking?|Account Name|Amount Code|Amount|Prenote Date|Effective Dates|Exclude Special|
|X|X|X|X|X|X|X|X|X|X|
2025-09-08 20:13:31,316 | INFO | llm gpt-5 api call took 15.388 seconds
2025-09-08 20:13:31,321 | INFO | total input tokens: 3292
2025-09-08 20:13:31,321 | INFO | input text tokens: 2654 # estimated
2025-09-08 20:13:31,322 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:13:31,322 | INFO | cost for input: $0.004115 USD
2025-09-08 20:13:31,322 | INFO | total output tokens: 360
2025-09-08 20:13:31,322 | INFO | cost of output: $0.0036 USD
2025-09-08 20:13:31,322 | INFO | done judging, ALL GOOD
2025-09-08 20:13:31,324 | INFO | -current table:
| ECode   | CalcCode   | Rate Code   |   Rate | Rate Per   |   Amount | Tabled?   |   Units | Frequency   | Goal/Paid/Goal Bal.   | Min/Max/Ann. Max   | Effective Dates          |
|:--------|:-----------|:------------|-------:|:-----------|---------:|:----------|--------:|:------------|:----------------------|:-------------------|:-------------------------|
| STD     |            |             |      0 |            |      9.5 | No        |       0 | ML          | 0.00/0.00/0.00        | 0.00/0.00/0.00     | 08/30/2024 to 12/31/2100 |
2025-09-08 20:13:31,324 | INFO | -validating table: Fringe Benefit Information
2025-09-08 20:13:31,324 | INFO | --figuring out table emptiness...
2025-09-08 20:14:06,512 | INFO | llm gpt-5-mini api call took 35.186 seconds
2025-09-08 20:14:06,535 | INFO | total input tokens: 16817
2025-09-08 20:14:06,535 | INFO | input text tokens: 15886 # estimated
2025-09-08 20:14:06,535 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:14:06,535 | INFO | cost for input: $0.021021 USD
2025-09-08 20:14:06,536 | INFO | total output tokens: 3040
2025-09-08 20:14:06,536 | INFO | cost of output: $0.0304 USD
2025-09-08 20:14:06,536 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:14:51,337 | INFO | llm gpt-5-mini api call took 44.801 seconds
2025-09-08 20:14:51,340 | INFO | total input tokens: 1688
2025-09-08 20:14:51,340 | INFO | input text tokens: 1680 # estimated
2025-09-08 20:14:51,340 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:14:51,340 | INFO | cost for input: $0.00211 USD
2025-09-08 20:14:51,340 | INFO | total output tokens: 3910
2025-09-08 20:14:51,341 | INFO | cost of output: $0.0391 USD
2025-09-08 20:14:51,341 | INFO | --got table grid emptiness info:
|ECode|CalcCode|Rate Code|Rate|Rate Per|Amount|Tabled?|Units|Frequency|Goal/Paid/Goal Bal.|Min/Max/Ann. Max|Effective Dates|
|X| | |X| |X|X|X|X|X|X|X|
2025-09-08 20:15:14,892 | INFO | llm gpt-5 api call took 23.551 seconds
2025-09-08 20:15:14,897 | INFO | total input tokens: 3338
2025-09-08 20:15:14,897 | INFO | input text tokens: 2700 # estimated
2025-09-08 20:15:14,898 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:15:14,898 | INFO | cost for input: $0.001148 USD
2025-09-08 20:15:14,898 | INFO | total output tokens: 744
2025-09-08 20:15:14,898 | INFO | cost of output: $0.00744 USD
2025-09-08 20:15:14,899 | INFO | done judging, ALL GOOD
2025-09-08 20:15:14,900 | INFO | -current table:
| BCode   |   Rate |   Amount |   Hours | Max/Carryover Max   | Length of Service   | Hours: Used/Avail/Total/Prob   | Dollars: Used/Avail/Total/Prob   | Effective Dates          |
|:--------|-------:|---------:|--------:|:--------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| ESST    |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/14.11/0.00/0.00           | 0.00/257.31/0.00/0.00            | 01/01/2024 to 06/01/2024 |
| PTO1    |      0 |        0 |       0 | 0.00/0.00           |                     | 23.00/39.36/0.00/0.00          | 437.00/747.84/0.00/0.00          | 06/02/2024 to 12/31/2100 |
| PTO2    |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/38.31/0.00/0.00           | 0.00/689.58/0.00/0.00            | 04/19/2023 to 09/09/2023 |
2025-09-08 20:15:14,900 | INFO | -validating table: Benefit Accrual Information
2025-09-08 20:15:14,901 | INFO | --figuring out table emptiness...
2025-09-08 20:16:50,086 | INFO | llm gpt-5-mini api call took 95.184 seconds
2025-09-08 20:16:50,104 | INFO | total input tokens: 16976
2025-09-08 20:16:50,104 | INFO | input text tokens: 16045 # estimated
2025-09-08 20:16:50,104 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:16:50,104 | INFO | cost for input: $0.02122 USD
2025-09-08 20:16:50,105 | INFO | total output tokens: 3820
2025-09-08 20:16:50,105 | INFO | cost of output: $0.0382 USD
2025-09-08 20:16:50,105 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:17:49,729 | INFO | llm gpt-5-mini api call took 59.623 seconds
2025-09-08 20:17:49,732 | INFO | total input tokens: 2474
2025-09-08 20:17:49,732 | INFO | input text tokens: 2466 # estimated
2025-09-08 20:17:49,732 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:17:49,733 | INFO | cost for input: $0.003093 USD
2025-09-08 20:17:49,733 | INFO | total output tokens: 3435
2025-09-08 20:17:49,733 | INFO | cost of output: $0.03435 USD
2025-09-08 20:17:49,733 | INFO | --got table grid emptiness info:
|BCode|Rate|Amount|Hours|Max/Carryover Max|Length of Service|Hours: Used/Avail/Total/Prob|Dollars: Used/Avail/Total/Prob|Effective Dates|
|X|X|X|X|X|X|X|X|X|
|X|X|X|X|X|X|X|X|X|
|X|X|X|X|X|X|X|X|X|
2025-09-08 20:18:34,334 | INFO | llm gpt-5 api call took 44.601 seconds
2025-09-08 20:18:34,340 | INFO | total input tokens: 3534
2025-09-08 20:18:34,340 | INFO | input text tokens: 2896 # estimated
2025-09-08 20:18:34,340 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:18:34,341 | INFO | cost for input: $0.004418 USD
2025-09-08 20:18:34,341 | INFO | total output tokens: 1064
2025-09-08 20:18:34,341 | INFO | cost of output: $0.01064 USD
2025-09-08 20:18:34,341 | INFO | done judging, ALL GOOD
2025-09-08 20:18:34,346 | INFO | -current table:

2025-09-08 20:18:34,346 | INFO | -validating table: Review Information
2025-09-08 20:18:34,347 | INFO | -current table:

2025-09-08 20:18:34,347 | INFO | -validating table: Emergency Contact Information
2025-09-08 20:18:34,348 | INFO | started validating form fields
2025-09-08 20:18:34,348 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-08 20:18:34,348 | INFO | --current are:
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
2025-09-08 20:19:12,512 | INFO | llm gpt-5 api call took 38.155 seconds
2025-09-08 20:19:12,521 | INFO | total input tokens: 4338
2025-09-08 20:19:12,521 | INFO | input text tokens: 3700 # estimated
2025-09-08 20:19:12,521 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:19:12,521 | INFO | cost for input: $0.005423 USD
2025-09-08 20:19:12,522 | INFO | total output tokens: 896
2025-09-08 20:19:12,522 | INFO | cost of output: $0.00896 USD
2025-09-08 20:19:12,522 | INFO | done judging, ALL GOOD
2025-09-08 20:19:12,522 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-08 20:19:12,523 | INFO | --current are:
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
2025-09-08 20:20:07,097 | INFO | llm gpt-5 api call took 54.562 seconds
2025-09-08 20:20:07,104 | INFO | total input tokens: 4303
2025-09-08 20:20:07,104 | INFO | input text tokens: 3665 # estimated
2025-09-08 20:20:07,105 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:20:07,105 | INFO | cost for input: $0.000915 USD
2025-09-08 20:20:07,105 | INFO | total output tokens: 1410
2025-09-08 20:20:07,105 | INFO | cost of output: $0.0141 USD
2025-09-08 20:20:07,105 | INFO | done judging, ALL GOOD
2025-09-08 20:20:07,106 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-08 20:20:07,106 | INFO | --current are:
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
2025-09-08 20:20:36,388 | INFO | llm gpt-5 api call took 29.273 seconds
2025-09-08 20:20:36,396 | INFO | total input tokens: 4312
2025-09-08 20:20:36,397 | INFO | input text tokens: 3674 # estimated
2025-09-08 20:20:36,397 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:20:36,397 | INFO | cost for input: $0.00539 USD
2025-09-08 20:20:36,397 | INFO | total output tokens: 1025
2025-09-08 20:20:36,397 | INFO | cost of output: $0.01025 USD
2025-09-08 20:20:36,398 | INFO | done judging, ALL GOOD
2025-09-08 20:20:36,398 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-08 20:20:36,398 | INFO | --current are:
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
2025-09-08 20:21:09,490 | INFO | llm gpt-5 api call took 33.083 seconds
2025-09-08 20:21:09,498 | INFO | total input tokens: 4297
2025-09-08 20:21:09,499 | INFO | input text tokens: 3659 # estimated
2025-09-08 20:21:09,499 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:21:09,499 | INFO | cost for input: $0.002491 USD
2025-09-08 20:21:09,499 | INFO | total output tokens: 1156
2025-09-08 20:21:09,499 | INFO | cost of output: $0.01156 USD
2025-09-08 20:21:09,499 | INFO | done judging, ALL GOOD
2025-09-08 20:21:09,500 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-08 20:21:09,500 | INFO | --current are:
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
2025-09-08 20:21:38,655 | INFO | llm gpt-5 api call took 29.146 seconds
2025-09-08 20:21:38,662 | INFO | total input tokens: 4306
2025-09-08 20:21:38,662 | INFO | input text tokens: 3668 # estimated
2025-09-08 20:21:38,662 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:21:38,662 | INFO | cost for input: $0.005383 USD
2025-09-08 20:21:38,663 | INFO | total output tokens: 967
2025-09-08 20:21:38,663 | INFO | cost of output: $0.00967 USD
2025-09-08 20:21:38,663 | INFO | done judging, ALL GOOD
2025-09-08 20:21:38,663 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-08 20:21:38,663 | INFO | --current are:
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
2025-09-08 20:23:25,266 | INFO | llm gpt-5 api call took 106.592 seconds
2025-09-08 20:23:25,277 | INFO | total input tokens: 4295
2025-09-08 20:23:25,278 | INFO | input text tokens: 3657 # estimated
2025-09-08 20:23:25,278 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:23:25,278 | INFO | cost for input: $0.005369 USD
2025-09-08 20:23:25,278 | INFO | total output tokens: 3009
2025-09-08 20:23:25,278 | INFO | cost of output: $0.03009 USD
2025-09-08 20:23:25,279 | INFO | done judging, ALL GOOD
2025-09-08 20:23:25,279 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-08 20:23:25,279 | INFO | --current are:
Default Hours : 0.00
Locations : 605
Positions : 700
2025-09-08 20:23:39,887 | INFO | llm gpt-5 api call took 14.595 seconds
2025-09-08 20:23:39,897 | INFO | total input tokens: 4274
2025-09-08 20:23:39,897 | INFO | input text tokens: 3636 # estimated
2025-09-08 20:23:39,897 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:23:39,897 | INFO | cost for input: $0.005343 USD
2025-09-08 20:23:39,898 | INFO | total output tokens: 337
2025-09-08 20:23:39,898 | INFO | cost of output: $0.00337 USD
2025-09-08 20:23:39,898 | INFO | done judging, ALL GOOD

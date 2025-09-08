2025-09-08 20:30:43,481 | INFO | started initial extraction for page 5
2025-09-08 20:32:12,533 | INFO | llm gpt-5 api call took 88.731 seconds
2025-09-08 20:32:12,553 | INFO | total input tokens: 3043
2025-09-08 20:32:12,553 | INFO | input text tokens: 2405 # estimated
2025-09-08 20:32:12,554 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:32:12,554 | INFO | cost for input: $0.003804 USD
2025-09-08 20:32:12,554 | INFO | total output tokens: 3950
2025-09-08 20:32:12,554 | INFO | cost of output: $0.0395 USD
2025-09-08 20:32:12,556 | INFO | initial extraction of page data done.
2025-09-08 20:32:20,425 | INFO | got response with OCR coordinates info from azure doc intelligence for page 5
2025-09-08 20:32:20,425 | INFO | started validating tables
2025-09-08 20:32:20,428 | INFO | -current table:
| RateCode   | Description   |   Rate | Salary   | Effective Dates          |
|:-----------|:--------------|-------:|:---------|:-------------------------|
| Base       | Base Rate     |  20.95 |          | 01/03/2024 to 12/31/2100 |
| Base       | Base Rate     |  20.3  |          | 01/03/2023 to 01/02/2024 |
| Base       | Base Rate     |  19.75 |          | 05/08/2022 to 01/02/2023 |
| Base       | Base Rate     |  16.75 |          | 01/03/2022 to 05/07/2022 |
| Base       | Base Rate     |  16    |          | 01/05/2021 to 01/02/2022 |
| Base       | Base Rate     |  14.6  |          | 01/04/2020 to 01/04/2021 |
| Base       | Base Rate     |  14.05 |          | 01/04/2019 to 01/03/2020 |
| Base       | Base Rate     |  13.75 |          | 01/04/2018 to 01/03/2019 |
| Base       | Base Rate     |  13.4  |          | 01/04/2017 to 01/03/2018 |
| Base       | Base Rate     |  13    |          | 04/04/2016 to 01/03/2017 |
| Base       | Base Rate     |  12    |          | 01/04/2016 to 04/03/2016 |
2025-09-08 20:32:20,428 | INFO | -validating table: Rate/Salary Information
2025-09-08 20:32:20,429 | INFO | --figuring out table emptiness...
2025-09-08 20:33:16,756 | INFO | llm gpt-5-mini api call took 56.324 seconds
2025-09-08 20:33:16,862 | INFO | total input tokens: 18760
2025-09-08 20:33:16,862 | INFO | input text tokens: 17829 # estimated
2025-09-08 20:33:16,862 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:33:16,862 | INFO | cost for input: $0.02345 USD
2025-09-08 20:33:16,863 | INFO | total output tokens: 5023
2025-09-08 20:33:16,863 | INFO | cost of output: $0.05023 USD
2025-09-08 20:33:16,863 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:33:57,971 | INFO | llm gpt-5-mini api call took 41.108 seconds
2025-09-08 20:33:57,991 | INFO | total input tokens: 3614
2025-09-08 20:33:57,991 | INFO | input text tokens: 3606 # estimated
2025-09-08 20:33:57,991 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:33:57,991 | INFO | cost for input: $0.004517 USD
2025-09-08 20:33:57,991 | INFO | total output tokens: 3206
2025-09-08 20:33:57,992 | INFO | cost of output: $0.03206 USD
2025-09-08 20:33:57,992 | INFO | --got table grid emptiness info:
|RateCode|Description|Rate|Salary|Effective Dates|
|---:|---:|---:|---:|---:|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
2025-09-08 20:34:31,318 | INFO | llm gpt-5 api call took 33.325 seconds
2025-09-08 20:34:31,331 | INFO | total input tokens: 3807
2025-09-08 20:34:31,331 | INFO | input text tokens: 3169 # estimated
2025-09-08 20:34:31,331 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:34:31,331 | INFO | cost for input: $0.004759 USD
2025-09-08 20:34:31,332 | INFO | total output tokens: 1128
2025-09-08 20:34:31,332 | INFO | cost of output: $0.01128 USD
2025-09-08 20:34:31,332 | INFO | done judging, ALL GOOD
2025-09-08 20:34:31,337 | INFO | -current table:
| Employee Tax (code description)   | Status   |   Add'l Amount | Effective Dates          | Default   |
|:----------------------------------|:---------|---------------:|:-------------------------|:----------|
| MED Medicare                      |          |              0 | 01/15/2016 to 12/31/2100 | Yes       |
| SS OASDI                          |          |              0 | 01/15/2016 to 12/31/2100 | Yes       |
| FITW Federal Income Tax           | M-1      |             20 | 01/04/2016 to 12/31/2100 | Yes       |
| MN Minnesota SITW                 | M-1      |              0 | 01/04/2016 to 12/31/2100 | Yes       |
2025-09-08 20:34:31,338 | INFO | -validating table: Tax Information (Employee)
2025-09-08 20:34:31,338 | INFO | --figuring out table emptiness...
2025-09-08 20:34:59,621 | INFO | llm gpt-5-mini api call took 28.279 seconds
2025-09-08 20:34:59,669 | INFO | total input tokens: 18548
2025-09-08 20:34:59,669 | INFO | input text tokens: 17617 # estimated
2025-09-08 20:34:59,669 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:34:59,670 | INFO | cost for input: $0.023185 USD
2025-09-08 20:34:59,670 | INFO | total output tokens: 2403
2025-09-08 20:34:59,670 | INFO | cost of output: $0.02403 USD
2025-09-08 20:34:59,671 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:36:04,923 | INFO | llm gpt-5-mini api call took 65.250 seconds
2025-09-08 20:36:05,008 | INFO | total input tokens: 2028
2025-09-08 20:36:05,009 | INFO | input text tokens: 2020 # estimated
2025-09-08 20:36:05,009 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:36:05,009 | INFO | cost for input: $0.002535 USD
2025-09-08 20:36:05,009 | INFO | total output tokens: 3090
2025-09-08 20:36:05,009 | INFO | cost of output: $0.0309 USD
2025-09-08 20:36:05,011 | INFO | --got table grid emptiness info:
|Employee Tax (code description)|Status|Add'l Amount|Effective Dates|Default|
|---:|---:|---:|---:|---:|
|X| |X|X|X|
|X| |X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
2025-09-08 20:36:34,451 | INFO | llm gpt-5 api call took 29.420 seconds
2025-09-08 20:36:34,495 | INFO | total input tokens: 3544
2025-09-08 20:36:34,495 | INFO | input text tokens: 2906 # estimated
2025-09-08 20:36:34,495 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:36:34,495 | INFO | cost for input: $0.00443 USD
2025-09-08 20:36:34,496 | INFO | total output tokens: 680
2025-09-08 20:36:34,496 | INFO | cost of output: $0.0068 USD
2025-09-08 20:36:34,500 | INFO | done judging, ALL GOOD
2025-09-08 20:36:34,522 | INFO | -current table:
| Employer Tax (code description)         | Effective Dates          | Default   |
|:----------------------------------------|:-------------------------|:----------|
| MED-R Medicare - Employer               | 01/15/2016 to 12/31/2100 |           |
| SS-R OASDI - Employer                   | 01/15/2016 to 12/31/2100 |           |
| FUTA Fed Unemployment                   | 01/15/2016 to 12/31/2100 |           |
| MNAST Minnesota Federal Loan Assessment | 01/15/2016 to 12/31/2100 |           |
| MNDW Workforce Enhancement Fee          | 01/15/2016 to 12/31/2100 |           |
| MNSUI Minnesota SUI                     | 01/15/2016 to 12/31/2100 |           |
2025-09-08 20:36:34,523 | INFO | -validating table: Tax Information (Employer)
2025-09-08 20:36:34,523 | INFO | --figuring out table emptiness...
2025-09-08 20:37:13,783 | INFO | llm gpt-5-mini api call took 39.254 seconds
2025-09-08 20:37:13,839 | INFO | total input tokens: 18562
2025-09-08 20:37:13,839 | INFO | input text tokens: 17631 # estimated
2025-09-08 20:37:13,840 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:37:13,840 | INFO | cost for input: $0.023203 USD
2025-09-08 20:37:13,840 | INFO | total output tokens: 3118
2025-09-08 20:37:13,840 | INFO | cost of output: $0.03118 USD
2025-09-08 20:37:13,842 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:38:00,481 | INFO | llm gpt-5-mini api call took 46.638 seconds
2025-09-08 20:38:00,487 | INFO | total input tokens: 1771
2025-09-08 20:38:00,488 | INFO | input text tokens: 1763 # estimated
2025-09-08 20:38:00,488 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:38:00,503 | INFO | cost for input: $0.002214 USD
2025-09-08 20:38:00,503 | INFO | total output tokens: 2551
2025-09-08 20:38:00,503 | INFO | cost of output: $0.02551 USD
2025-09-08 20:38:00,504 | INFO | --got table grid emptiness info:
|Employer Tax (code description)|Effective Dates|Default|
|---|---|---|
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
2025-09-08 20:38:25,650 | INFO | llm gpt-5 api call took 25.143 seconds
2025-09-08 20:38:25,666 | INFO | total input tokens: 3531
2025-09-08 20:38:25,666 | INFO | input text tokens: 2893 # estimated
2025-09-08 20:38:25,666 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:38:25,667 | INFO | cost for input: $0.004414 USD
2025-09-08 20:38:25,667 | INFO | total output tokens: 744
2025-09-08 20:38:25,667 | INFO | cost of output: $0.00744 USD
2025-09-08 20:38:25,668 | INFO | done judging, ALL GOOD
2025-09-08 20:38:25,730 | INFO | -current table:
| Code       | Deduction             |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-----------|:----------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| 401KC      | 401K Contribution     |   6    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 04/01/2016 to 12/31/2100 |
| 401kUM     | 401kUnmatch           |  14    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 08/01/2022 to 12/31/2100 |
| 401kUnmatc | 401K Unmatch          |  12    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 03/31/2019 to 08/01/2022 |
| DNTL       | Dental Insurance S125 |  18.32 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2019 to 12/31/2100 |
| FH125      | Health Insurance S125 | 158.14 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2019 to 12/31/2100 |
2025-09-08 20:38:25,733 | INFO | -validating table: Deduction Information
2025-09-08 20:38:25,733 | INFO | --figuring out table emptiness...
2025-09-08 20:39:16,469 | INFO | llm gpt-5-mini api call took 50.732 seconds
2025-09-08 20:39:16,558 | INFO | total input tokens: 18800
2025-09-08 20:39:16,558 | INFO | input text tokens: 17869 # estimated
2025-09-08 20:39:16,558 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:39:16,559 | INFO | cost for input: $0.0235 USD
2025-09-08 20:39:16,559 | INFO | total output tokens: 3592
2025-09-08 20:39:16,559 | INFO | cost of output: $0.03592 USD
2025-09-08 20:39:16,561 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:40:32,981 | INFO | llm gpt-5-mini api call took 76.418 seconds
2025-09-08 20:40:33,076 | INFO | total input tokens: 3246
2025-09-08 20:40:33,077 | INFO | input text tokens: 3238 # estimated
2025-09-08 20:40:33,077 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:40:33,077 | INFO | cost for input: $0.004058 USD
2025-09-08 20:40:33,078 | INFO | total output tokens: 5510
2025-09-08 20:40:33,078 | INFO | cost of output: $0.0551 USD
2025-09-08 20:40:33,079 | INFO | --got table grid emptiness info:
|Code|Deduction|Rate|CalcCode|Frequency|Goal/Paid|Min/Max/Annual Max|Arrears|Agency|Effective Dates|
|X|X|X|X| |X|X|X| |X|
|X|X|X|X| |X|X|X| |X|
|X|X|X|X| |X|X|X| |X|
|X|X|X| |X|X|X|X| |X|
|X|X|X| |X|X|X|X| |X|
2025-09-08 20:41:36,248 | INFO | llm gpt-5 api call took 63.149 seconds
2025-09-08 20:41:36,276 | INFO | total input tokens: 3847
2025-09-08 20:41:36,276 | INFO | input text tokens: 3209 # estimated
2025-09-08 20:41:36,277 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:41:36,277 | INFO | cost for input: $0.004809 USD
2025-09-08 20:41:36,277 | INFO | total output tokens: 1960
2025-09-08 20:41:36,277 | INFO | cost of output: $0.0196 USD
2025-09-08 20:41:36,281 | INFO | done judging, ALL GOOD
2025-09-08 20:41:36,322 | INFO | -current table:
|   Sequence No. |   Transit No. |   Account No. | Checking?   | Account Name    | Amount Code   |   Amount | Prenote Date   | Effective Dates          | Exclude Special   |
|---------------:|--------------:|--------------:|:------------|:----------------|:--------------|---------:|:---------------|:-------------------------|:------------------|
|             99 |     296076262 |    2743046665 | Yes         | Jocelyn, Taylor | %             |      100 | 02/12/2016     | 02/12/2016 to 12/31/2100 | No                |
2025-09-08 20:41:36,323 | INFO | -validating table: Direct Deposit Information
2025-09-08 20:41:36,324 | INFO | --figuring out table emptiness...
2025-09-08 20:42:04,529 | INFO | llm gpt-5-mini api call took 28.202 seconds
2025-09-08 20:42:04,557 | INFO | total input tokens: 18511
2025-09-08 20:42:04,558 | INFO | input text tokens: 17580 # estimated
2025-09-08 20:42:04,559 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:42:04,559 | INFO | cost for input: $0.023139 USD
2025-09-08 20:42:04,559 | INFO | total output tokens: 1980
2025-09-08 20:42:04,559 | INFO | cost of output: $0.0198 USD
2025-09-08 20:42:04,560 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:43:08,179 | INFO | llm gpt-5-mini api call took 63.617 seconds
2025-09-08 20:43:08,183 | INFO | total input tokens: 1628
2025-09-08 20:43:08,184 | INFO | input text tokens: 1620 # estimated
2025-09-08 20:43:08,184 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:43:08,184 | INFO | cost for input: $0.002035 USD
2025-09-08 20:43:08,184 | INFO | total output tokens: 2297
2025-09-08 20:43:08,184 | INFO | cost of output: $0.02297 USD
2025-09-08 20:43:08,184 | INFO | --got table grid emptiness info:
|Sequence No.|Transit No.|Account No.|Checking?|Account Name|Amount Code|Amount|Prenote Date|Effective Dates|Exclude Special|
|X|X|X|X|X|X|X|X|X|X|
2025-09-08 20:43:27,814 | INFO | llm gpt-5 api call took 19.627 seconds
2025-09-08 20:43:27,822 | INFO | total input tokens: 3481
2025-09-08 20:43:27,822 | INFO | input text tokens: 2843 # estimated
2025-09-08 20:43:27,823 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:43:27,823 | INFO | cost for input: $0.004351 USD
2025-09-08 20:43:27,823 | INFO | total output tokens: 424
2025-09-08 20:43:27,823 | INFO | cost of output: $0.00424 USD
2025-09-08 20:43:27,824 | INFO | done judging, ALL GOOD
2025-09-08 20:43:27,829 | INFO | -current table:
| ECode   | CalcCode   | Rate Code   |   Rate | Rate Per   |   Amount | Tabled?   |   Units | Frequency   | Goal/Paid/Goal Bal.   | Min/Max/Ann. Max   | Effective Dates          |
|:--------|:-----------|:------------|-------:|:-----------|---------:|:----------|--------:|:------------|:----------------------|:-------------------|:-------------------------|
| STD     |            |             |      0 |            |    11.07 | No        |       0 | ML          | 0.00/0.00/0.00        | 0.00/0.00/0.00     | 03/17/2019 to 12/31/2100 |
2025-09-08 20:43:27,831 | INFO | -validating table: Fringe Benefit Information
2025-09-08 20:43:27,831 | INFO | --figuring out table emptiness...
2025-09-08 20:44:33,972 | INFO | llm gpt-5-mini api call took 66.138 seconds
2025-09-08 20:44:33,997 | INFO | total input tokens: 18542
2025-09-08 20:44:33,998 | INFO | input text tokens: 17611 # estimated
2025-09-08 20:44:33,998 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:44:33,998 | INFO | cost for input: $0.023178 USD
2025-09-08 20:44:33,998 | INFO | total output tokens: 3613
2025-09-08 20:44:33,998 | INFO | cost of output: $0.03613 USD
2025-09-08 20:44:33,998 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:45:33,220 | INFO | llm gpt-5-mini api call took 59.219 seconds
2025-09-08 20:45:33,223 | INFO | total input tokens: 1557
2025-09-08 20:45:33,224 | INFO | input text tokens: 1549 # estimated
2025-09-08 20:45:33,237 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:45:33,237 | INFO | cost for input: $0.001946 USD
2025-09-08 20:45:33,237 | INFO | total output tokens: 3574
2025-09-08 20:45:33,237 | INFO | cost of output: $0.03574 USD
2025-09-08 20:45:33,238 | INFO | --got table grid emptiness info:
|ECode|CalcCode|Rate Code|Rate|Rate Per|Amount|Tabled?|Units|Frequency|Goal/Paid/Goal Bal.|Min/Max/Ann. Max|Effective Dates|
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|X| | |X| |X|X|X|X|X|X|X|
2025-09-08 20:45:58,775 | INFO | llm gpt-5 api call took 25.535 seconds
2025-09-08 20:45:58,781 | INFO | total input tokens: 3573
2025-09-08 20:45:58,781 | INFO | input text tokens: 2935 # estimated
2025-09-08 20:45:58,781 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:45:58,782 | INFO | cost for input: $0.004466 USD
2025-09-08 20:45:58,782 | INFO | total output tokens: 744
2025-09-08 20:45:58,782 | INFO | cost of output: $0.00744 USD
2025-09-08 20:45:58,782 | INFO | done judging, ALL GOOD
2025-09-08 20:45:58,807 | INFO | -current table:

2025-09-08 20:45:58,808 | INFO | -validating table: Benefit Accrual Information
2025-09-08 20:45:58,809 | INFO | -current table:

2025-09-08 20:45:58,809 | INFO | -validating table: Review Information
2025-09-08 20:45:58,809 | INFO | -current table:

2025-09-08 20:45:58,810 | INFO | -validating table: Emergency Contact Information
2025-09-08 20:45:58,810 | INFO | started validating form fields
2025-09-08 20:45:58,811 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-08 20:45:58,811 | INFO | --current are:
Company Name : Velorynt Labs
Company Code : 37546
Period : 12/17/2024 to 12/26/2024
Employee Name : Jocelyn Taylor
Address line 1 : 1006 Shery St
City : Shaontown
State : WY
Zip : 93506-7144
Emp Id : 5532
SSN : 609-85-2596
2025-09-08 20:46:29,252 | INFO | llm gpt-5 api call took 30.427 seconds
2025-09-08 20:46:29,262 | INFO | total input tokens: 4786
2025-09-08 20:46:29,262 | INFO | input text tokens: 4148 # estimated
2025-09-08 20:46:29,262 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:46:29,262 | INFO | cost for input: $0.005982 USD
2025-09-08 20:46:29,262 | INFO | total output tokens: 704
2025-09-08 20:46:29,263 | INFO | cost of output: $0.00704 USD
2025-09-08 20:46:29,263 | INFO | done judging, ALL GOOD
2025-09-08 20:46:29,263 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-08 20:46:29,263 | INFO | --current are:
DOB (only date) : 12/28/1961
Gender : M
Marital Status : M
Status : A
Position : 
Title : 
Pay Group : 
Job Code : 
Emp Type : RFT
Statutory : 0.00
2025-09-08 20:47:04,567 | INFO | llm gpt-5 api call took 35.294 seconds
2025-09-08 20:47:04,577 | INFO | total input tokens: 4749
2025-09-08 20:47:04,577 | INFO | input text tokens: 4111 # estimated
2025-09-08 20:47:04,577 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:47:04,577 | INFO | cost for input: $0.005936 USD
2025-09-08 20:47:04,577 | INFO | total output tokens: 898
2025-09-08 20:47:04,578 | INFO | cost of output: $0.00898 USD
2025-09-08 20:47:04,578 | INFO | done judging, ALL GOOD
2025-09-08 20:47:04,578 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-08 20:47:04,578 | INFO | --current are:
Seasonal : 0.00
Domestic Emp : No
Probation : 0.00
Home # : 
Work # : 
Ext. : 
Email : 
Mail Stop : 
Hire Date : 01/04/2016
Rehire Date : 
2025-09-08 20:47:26,172 | INFO | llm gpt-5 api call took 21.584 seconds
2025-09-08 20:47:26,179 | INFO | total input tokens: 4750
2025-09-08 20:47:26,180 | INFO | input text tokens: 4112 # estimated
2025-09-08 20:47:26,180 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:47:26,180 | INFO | cost for input: $0.005938 USD
2025-09-08 20:47:26,180 | INFO | total output tokens: 705
2025-09-08 20:47:26,181 | INFO | cost of output: $0.00705 USD
2025-09-08 20:47:26,181 | INFO | done judging, ALL GOOD
2025-09-08 20:47:26,181 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-08 20:47:26,181 | INFO | --current are:
Term Date : 
Term Reason : 
Adj Sen Date : 
Pension : No
Visa Type : 
Exp : 
Citizen : 
I9 Reverify : 
I9 Verified : Yes
Deceased : No
2025-09-08 20:47:56,440 | INFO | llm gpt-5 api call took 30.249 seconds
2025-09-08 20:47:56,449 | INFO | total input tokens: 4741
2025-09-08 20:47:56,449 | INFO | input text tokens: 4103 # estimated
2025-09-08 20:47:56,449 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:47:56,449 | INFO | cost for input: $0.005926 USD
2025-09-08 20:47:56,450 | INFO | total output tokens: 772
2025-09-08 20:47:56,450 | INFO | cost of output: $0.00772 USD
2025-09-08 20:47:56,450 | INFO | done judging, ALL GOOD
2025-09-08 20:47:56,450 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-08 20:47:56,450 | INFO | --current are:
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
2025-09-08 20:48:43,937 | INFO | llm gpt-5 api call took 47.476 seconds
2025-09-08 20:48:43,945 | INFO | total input tokens: 4750
2025-09-08 20:48:43,945 | INFO | input text tokens: 4112 # estimated
2025-09-08 20:48:43,945 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:48:43,945 | INFO | cost for input: $0.005938 USD
2025-09-08 20:48:43,945 | INFO | total output tokens: 967
2025-09-08 20:48:43,945 | INFO | cost of output: $0.00967 USD
2025-09-08 20:48:43,946 | INFO | done judging, ALL GOOD
2025-09-08 20:48:43,946 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-08 20:48:43,946 | INFO | --current are:
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
2025-09-08 20:49:46,067 | INFO | llm gpt-5 api call took 62.111 seconds
2025-09-08 20:49:46,074 | INFO | total input tokens: 4739
2025-09-08 20:49:46,074 | INFO | input text tokens: 4101 # estimated
2025-09-08 20:49:46,075 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:49:46,075 | INFO | cost for input: $0.005924 USD
2025-09-08 20:49:46,075 | INFO | total output tokens: 1665
2025-09-08 20:49:46,075 | INFO | cost of output: $0.01665 USD
2025-09-08 20:49:46,075 | INFO | done judging, ALL GOOD
2025-09-08 20:49:46,076 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-08 20:49:46,076 | INFO | --current are:
Default Hours : 0.00
Locations : 606
Positions : 700
2025-09-08 20:50:09,177 | INFO | llm gpt-5 api call took 23.092 seconds
2025-09-08 20:50:09,184 | INFO | total input tokens: 4718
2025-09-08 20:50:09,185 | INFO | input text tokens: 4080 # estimated
2025-09-08 20:50:09,185 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:50:09,185 | INFO | cost for input: $0.005897 USD
2025-09-08 20:50:09,185 | INFO | total output tokens: 721
2025-09-08 20:50:09,185 | INFO | cost of output: $0.00721 USD
2025-09-08 20:50:09,185 | INFO | done judging, ALL GOOD

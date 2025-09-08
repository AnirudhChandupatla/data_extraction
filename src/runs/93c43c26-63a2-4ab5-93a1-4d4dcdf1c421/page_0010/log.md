2025-09-08 21:10:38,792 | INFO | started initial extraction for page 10
2025-09-08 21:12:46,356 | INFO | llm gpt-5 api call took 127.307 seconds
2025-09-08 21:12:46,362 | INFO | total input tokens: 3016
2025-09-08 21:12:46,362 | INFO | input text tokens: 2378 # estimated
2025-09-08 21:12:46,362 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:12:46,362 | INFO | cost for input: $0.00377 USD
2025-09-08 21:12:46,363 | INFO | total output tokens: 4052
2025-09-08 21:12:46,363 | INFO | cost of output: $0.04052 USD
2025-09-08 21:12:46,364 | INFO | initial extraction of page data done.
2025-09-08 21:12:55,625 | INFO | got response with OCR coordinates info from azure doc intelligence for page 10
2025-09-08 21:12:55,625 | INFO | started validating tables
2025-09-08 21:12:55,627 | INFO | -current table:
| RateCode   | Description   |   Rate | Salary   | Effective Dates          |
|:-----------|:--------------|-------:|:---------|:-------------------------|
| Base       | Base Rate     |  14.3  |          | 06/17/2019 to 12/31/2100 |
| Base       | Base Rate     |  13.9  |          | 06/17/2018 to 06/16/2019 |
| Base       | Base Rate     |  13.45 |          | 06/17/2017 to 06/16/2018 |
| Base       | Base Rate     |  13    |          | 09/04/2016 to 06/16/2017 |
| Base       | Base Rate     |  12    |          | 07/01/2016 to 09/03/2016 |
2025-09-08 21:12:55,628 | INFO | -validating table: Rate/Salary Information
2025-09-08 21:12:55,628 | INFO | --figuring out table emptiness...
2025-09-08 21:13:24,630 | INFO | llm gpt-5-mini api call took 29.001 seconds
2025-09-08 21:13:24,648 | INFO | total input tokens: 18053
2025-09-08 21:13:24,649 | INFO | input text tokens: 17122 # estimated
2025-09-08 21:13:24,649 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 21:13:24,649 | INFO | cost for input: $0.022566 USD
2025-09-08 21:13:24,649 | INFO | total output tokens: 3395
2025-09-08 21:13:24,649 | INFO | cost of output: $0.03395 USD
2025-09-08 21:13:24,650 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 21:14:21,459 | INFO | llm gpt-5-mini api call took 56.809 seconds
2025-09-08 21:14:21,463 | INFO | total input tokens: 2498
2025-09-08 21:14:21,463 | INFO | input text tokens: 2490 # estimated
2025-09-08 21:14:21,463 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 21:14:21,463 | INFO | cost for input: $0.003122 USD
2025-09-08 21:14:21,464 | INFO | total output tokens: 2512
2025-09-08 21:14:21,464 | INFO | cost of output: $0.02512 USD
2025-09-08 21:14:21,464 | INFO | --got table grid emptiness info:
|RateCode|Description|Rate|Salary|Effective Dates|
|---:|---:|---:|---:|---:|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
2025-09-08 21:14:37,348 | INFO | llm gpt-5 api call took 15.884 seconds
2025-09-08 21:14:37,354 | INFO | total input tokens: 3534
2025-09-08 21:14:37,354 | INFO | input text tokens: 2896 # estimated
2025-09-08 21:14:37,354 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:14:37,354 | INFO | cost for input: $0.004418 USD
2025-09-08 21:14:37,355 | INFO | total output tokens: 424
2025-09-08 21:14:37,355 | INFO | cost of output: $0.00424 USD
2025-09-08 21:14:37,355 | INFO | done judging, ALL GOOD
2025-09-08 21:14:37,357 | INFO | -current table:
| Employee Tax (code description)   | Status   |   Add'l Amount | Effective Dates          | Default   |
|:----------------------------------|:---------|---------------:|:-------------------------|:----------|
| MED Medicare                      |          |              0 | 07/01/2016 to 12/31/2100 | Yes       |
| SS OASDI                          |          |              0 | 07/01/2016 to 12/31/2100 | Yes       |
| FITW Federal Income Tax           | S-2      |             20 | 01/01/2018 to 12/31/2100 | Yes       |
| MN Minnesota SITW                 | S-2      |              0 | 07/01/2016 to 12/31/2100 | Yes       |
2025-09-08 21:14:37,357 | INFO | -validating table: Tax Information (Employee)
2025-09-08 21:14:37,357 | INFO | --figuring out table emptiness...
2025-09-08 21:15:25,034 | INFO | llm gpt-5-mini api call took 47.675 seconds
2025-09-08 21:15:25,061 | INFO | total input tokens: 18033
2025-09-08 21:15:25,062 | INFO | input text tokens: 17102 # estimated
2025-09-08 21:15:25,062 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 21:15:25,062 | INFO | cost for input: $0.022541 USD
2025-09-08 21:15:25,062 | INFO | total output tokens: 2135
2025-09-08 21:15:25,062 | INFO | cost of output: $0.02135 USD
2025-09-08 21:15:25,063 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 21:16:41,611 | INFO | llm gpt-5-mini api call took 76.548 seconds
2025-09-08 21:16:41,614 | INFO | total input tokens: 2016
2025-09-08 21:16:41,614 | INFO | input text tokens: 2008 # estimated
2025-09-08 21:16:41,615 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 21:16:41,615 | INFO | cost for input: $0.00252 USD
2025-09-08 21:16:41,615 | INFO | total output tokens: 4182
2025-09-08 21:16:41,615 | INFO | cost of output: $0.04182 USD
2025-09-08 21:16:41,615 | INFO | --got table grid emptiness info:
|Employee Tax (code description)|Status|Add'l Amount|Effective Dates|Default|
|---:|:---:|:---:|:---:|:---:|
|X| |X|X|X|
|X| |X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
2025-09-08 21:17:23,645 | INFO | llm gpt-5 api call took 42.029 seconds
2025-09-08 21:17:23,649 | INFO | total input tokens: 3521
2025-09-08 21:17:23,650 | INFO | input text tokens: 2883 # estimated
2025-09-08 21:17:23,650 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:17:23,650 | INFO | cost for input: $0.004401 USD
2025-09-08 21:17:23,650 | INFO | total output tokens: 744
2025-09-08 21:17:23,650 | INFO | cost of output: $0.00744 USD
2025-09-08 21:17:23,650 | INFO | done judging, ALL GOOD
2025-09-08 21:17:23,652 | INFO | -current table:
| Employer Tax (code description)         | Effective Dates          | Default   |
|:----------------------------------------|:-------------------------|:----------|
| MED-R Medicare - Employer               | 07/01/2016 to 12/31/2100 |           |
| SS-R OASDI - Employer                   | 07/01/2016 to 12/31/2100 |           |
| FUTA Fed Unemployment                   | 07/01/2016 to 12/31/2100 |           |
| MNAST Minnesota Federal Loan Assessment | 07/01/2016 to 12/31/2100 |           |
| MNDW Workforce Enhancement Fee          | 07/01/2016 to 12/31/2100 |           |
| MNSUI Minnesota SUI                     | 07/01/2016 to 12/31/2100 |           |
2025-09-08 21:17:23,652 | INFO | -validating table: Tax Information (Employer)
2025-09-08 21:17:23,652 | INFO | --figuring out table emptiness...
2025-09-08 21:19:51,340 | INFO | llm gpt-5-mini api call took 147.686 seconds
2025-09-08 21:19:51,359 | INFO | total input tokens: 18047
2025-09-08 21:19:51,359 | INFO | input text tokens: 17116 # estimated
2025-09-08 21:19:51,359 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 21:19:51,359 | INFO | cost for input: $0.022559 USD
2025-09-08 21:19:51,360 | INFO | total output tokens: 3691
2025-09-08 21:19:51,360 | INFO | cost of output: $0.03691 USD
2025-09-08 21:19:51,360 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 21:20:41,029 | INFO | llm gpt-5-mini api call took 49.669 seconds
2025-09-08 21:20:41,031 | INFO | total input tokens: 1768
2025-09-08 21:20:41,032 | INFO | input text tokens: 1760 # estimated
2025-09-08 21:20:41,032 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 21:20:41,032 | INFO | cost for input: $0.00221 USD
2025-09-08 21:20:41,032 | INFO | total output tokens: 2173
2025-09-08 21:20:41,032 | INFO | cost of output: $0.02173 USD
2025-09-08 21:20:41,032 | INFO | --got table grid emptiness info:
|Employer Tax (code description)|Effective Dates|Default|
|---|---|---|
|X|X| |
|X|X| |
|X|X| |
|X|X| |
|X|X| |
|X|X| |
2025-09-08 21:21:02,210 | INFO | llm gpt-5 api call took 21.177 seconds
2025-09-08 21:21:02,215 | INFO | total input tokens: 3510
2025-09-08 21:21:02,216 | INFO | input text tokens: 2872 # estimated
2025-09-08 21:21:02,216 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:21:02,216 | INFO | cost for input: $0.004387 USD
2025-09-08 21:21:02,216 | INFO | total output tokens: 552
2025-09-08 21:21:02,216 | INFO | cost of output: $0.00552 USD
2025-09-08 21:21:02,216 | INFO | done judging, ALL GOOD
2025-09-08 21:21:02,218 | INFO | -current table:
| Code   | Deduction             |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-------|:----------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| FH125  | Health Insurance S125 |  87.87 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2019 to 12/31/2100 |
2025-09-08 21:21:02,218 | INFO | -validating table: Deduction Information
2025-09-08 21:21:02,218 | INFO | --figuring out table emptiness...
2025-09-08 21:21:41,335 | INFO | llm gpt-5-mini api call took 39.115 seconds
2025-09-08 21:21:41,356 | INFO | total input tokens: 18002
2025-09-08 21:21:41,357 | INFO | input text tokens: 17071 # estimated
2025-09-08 21:21:41,357 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 21:21:41,357 | INFO | cost for input: $0.002775 USD
2025-09-08 21:21:41,358 | INFO | total output tokens: 1809
2025-09-08 21:21:41,358 | INFO | cost of output: $0.01809 USD
2025-09-08 21:21:41,358 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 21:23:00,327 | INFO | llm gpt-5-mini api call took 78.968 seconds
2025-09-08 21:23:00,330 | INFO | total input tokens: 1655
2025-09-08 21:23:00,330 | INFO | input text tokens: 1647 # estimated
2025-09-08 21:23:00,330 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 21:23:00,330 | INFO | cost for input: $0.002069 USD
2025-09-08 21:23:00,330 | INFO | total output tokens: 2829
2025-09-08 21:23:00,330 | INFO | cost of output: $0.02829 USD
2025-09-08 21:23:00,331 | INFO | --got table grid emptiness info:
|Code|Deduction|Rate|CalcCode|Frequency|Goal/Paid|Min/Max/Annual Max|Arrears|Agency|Effective Dates|
|---|---|---|---|---|---|---|---|---|---|
|X|X|X||X|X|X|X||X|
2025-09-08 21:23:28,394 | INFO | llm gpt-5 api call took 28.063 seconds
2025-09-08 21:23:28,399 | INFO | total input tokens: 3480
2025-09-08 21:23:28,399 | INFO | input text tokens: 2842 # estimated
2025-09-08 21:23:28,400 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:23:28,400 | INFO | cost for input: $0.00435 USD
2025-09-08 21:23:28,400 | INFO | total output tokens: 744
2025-09-08 21:23:28,400 | INFO | cost of output: $0.00744 USD
2025-09-08 21:23:28,400 | INFO | done judging, ALL GOOD
2025-09-08 21:23:28,402 | INFO | -current table:
|   Sequence No. |   Transit No. |   Account No. | Checking?   | Account Name   | Amount Code   |   Amount | Prenote Date   | Effective Dates          | Exclude Special   |
|---------------:|--------------:|--------------:|:------------|:---------------|:--------------|---------:|:---------------|:-------------------------|:------------------|
|             99 |     091000019 |    9414336673 | Yes         | Laura Smith    | %             |      100 | 07/15/2016     | 07/15/2016 to 12/31/2100 | No                |
2025-09-08 21:23:28,402 | INFO | -validating table: Direct Deposit Information
2025-09-08 21:23:28,402 | INFO | --figuring out table emptiness...
2025-09-08 21:23:46,331 | INFO | llm gpt-5-mini api call took 17.928 seconds
2025-09-08 21:23:46,349 | INFO | total input tokens: 17995
2025-09-08 21:23:46,350 | INFO | input text tokens: 17064 # estimated
2025-09-08 21:23:46,350 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 21:23:46,350 | INFO | cost for input: $0.022494 USD
2025-09-08 21:23:46,350 | INFO | total output tokens: 1561
2025-09-08 21:23:46,350 | INFO | cost of output: $0.01561 USD
2025-09-08 21:23:46,351 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 21:25:20,275 | INFO | llm gpt-5-mini api call took 93.924 seconds
2025-09-08 21:25:20,278 | INFO | total input tokens: 1465
2025-09-08 21:25:20,278 | INFO | input text tokens: 1457 # estimated
2025-09-08 21:25:20,278 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 21:25:20,278 | INFO | cost for input: $0.001831 USD
2025-09-08 21:25:20,278 | INFO | total output tokens: 4046
2025-09-08 21:25:20,278 | INFO | cost of output: $0.04046 USD
2025-09-08 21:25:20,278 | INFO | --got table grid emptiness info:
|Sequence No.|Transit No.|Account No.|Checking?|Account Name|Amount Code|Amount|Prenote Date|Effective Dates|Exclude Special|
|---|---|---|---|---|---|---|---|---|---|
|X|X|X|X|X|X|X|X|X|X|
2025-09-08 21:25:45,211 | INFO | llm gpt-5 api call took 24.932 seconds
2025-09-08 21:25:45,217 | INFO | total input tokens: 3474
2025-09-08 21:25:45,217 | INFO | input text tokens: 2836 # estimated
2025-09-08 21:25:45,217 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:25:45,218 | INFO | cost for input: $0.004343 USD
2025-09-08 21:25:45,218 | INFO | total output tokens: 552
2025-09-08 21:25:45,218 | INFO | cost of output: $0.00552 USD
2025-09-08 21:25:45,218 | INFO | done judging, ALL GOOD
2025-09-08 21:25:45,220 | INFO | -current table:
| ECode   | CalcCode   | Rate Code   |   Rate | Rate Per   |   Amount | Tabled?   |   Units | Frequency   | Goal/Paid/Goal Bal.   | Min/Max/Ann. Max   | Effective Dates          |
|:--------|:-----------|:------------|-------:|:-----------|---------:|:----------|--------:|:------------|:----------------------|:-------------------|:-------------------------|
| STD     |            |             |      0 |            |     4.85 | No        |       0 | B5          | 0.00/0.00/0.00        | 0.00/0.00/0.00     | 01/01/2018 to 12/31/2100 |
2025-09-08 21:25:45,220 | INFO | -validating table: Fringe Benefit Information
2025-09-08 21:25:45,220 | INFO | --figuring out table emptiness...
2025-09-08 21:28:24,889 | INFO | llm gpt-5-mini api call took 159.668 seconds
2025-09-08 21:28:24,907 | INFO | total input tokens: 18028
2025-09-08 21:28:24,907 | INFO | input text tokens: 17097 # estimated
2025-09-08 21:28:24,907 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 21:28:24,907 | INFO | cost for input: $0.022535 USD
2025-09-08 21:28:24,907 | INFO | total output tokens: 3112
2025-09-08 21:28:24,907 | INFO | cost of output: $0.03112 USD
2025-09-08 21:28:24,907 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 21:29:16,273 | INFO | llm gpt-5-mini api call took 51.365 seconds
2025-09-08 21:29:16,275 | INFO | total input tokens: 1696
2025-09-08 21:29:16,275 | INFO | input text tokens: 1688 # estimated
2025-09-08 21:29:16,276 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 21:29:16,276 | INFO | cost for input: $0.00212 USD
2025-09-08 21:29:16,276 | INFO | total output tokens: 3868
2025-09-08 21:29:16,276 | INFO | cost of output: $0.03868 USD
2025-09-08 21:29:16,276 | INFO | --got table grid emptiness info:
|ECode|CalcCode|Rate Code|Rate|Rate Per|Amount|Tabled?|Units|Frequency|Goal/Paid/Goal Bal.|Min/Max/Ann. Max|Effective Dates|
|---|---|---|---|---|---|---|---|---|---|---|---|
|X|||X||X|X|X|X|X|X|X|
2025-09-08 21:29:39,567 | INFO | llm gpt-5 api call took 23.291 seconds
2025-09-08 21:29:39,574 | INFO | total input tokens: 3521
2025-09-08 21:29:39,575 | INFO | input text tokens: 2883 # estimated
2025-09-08 21:29:39,575 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:29:39,575 | INFO | cost for input: $0.004401 USD
2025-09-08 21:29:39,575 | INFO | total output tokens: 488
2025-09-08 21:29:39,575 | INFO | cost of output: $0.00488 USD
2025-09-08 21:29:39,576 | INFO | done judging, ALL GOOD
2025-09-08 21:29:39,577 | INFO | -current table:
| BCode    |   Rate |   Amount |   Hours | Max/Carryover Max   | Length of Service   | Hours: Used/Avail/Total/Prob   | Dollars: Used/Avail/Total/Prob   | Effective Dates          |
|:---------|-------:|---------:|--------:|:--------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| PER      |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 09/01/2016 to 12/31/2100 |
| SICK     |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 09/01/2016 to 12/31/2100 |
| VAC-NEX8 |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 09/01/2016 to 12/31/2100 |
| VAC/CO   |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 01/01/2018 to 12/31/2100 |
2025-09-08 21:29:39,578 | INFO | -validating table: Benefit Accrual Information
2025-09-08 21:29:39,578 | INFO | --figuring out table emptiness...
2025-09-08 21:30:25,077 | INFO | llm gpt-5-mini api call took 45.498 seconds
2025-09-08 21:30:25,096 | INFO | total input tokens: 18268
2025-09-08 21:30:25,097 | INFO | input text tokens: 17337 # estimated
2025-09-08 21:30:25,097 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 21:30:25,097 | INFO | cost for input: $0.022835 USD
2025-09-08 21:30:25,097 | INFO | total output tokens: 4147
2025-09-08 21:30:25,098 | INFO | cost of output: $0.04147 USD
2025-09-08 21:30:25,098 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 21:31:23,201 | INFO | llm gpt-5-mini api call took 58.103 seconds
2025-09-08 21:31:23,206 | INFO | total input tokens: 3249
2025-09-08 21:31:23,206 | INFO | input text tokens: 3241 # estimated
2025-09-08 21:31:23,206 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 21:31:23,206 | INFO | cost for input: $0.004061 USD
2025-09-08 21:31:23,207 | INFO | total output tokens: 4105
2025-09-08 21:31:23,207 | INFO | cost of output: $0.04105 USD
2025-09-08 21:31:23,207 | INFO | --got table grid emptiness info:
|BCode|Rate|Amount|Hours|Max/Carryover Max|Length of Service|Hours: Used/Avail/Total/Prob|Dollars: Used/Avail/Total/Prob|Effective Dates|
|---|---|---|---|---|---|---|---|---|
|X|X|X|X|X||X|X|X|
|X|X|X|X|X||X|X|X|
|X|X|X|X|X||X|X|X|
|X|X|X|X|X||X|X|X|
2025-09-08 21:32:29,539 | INFO | llm gpt-5 api call took 66.331 seconds
2025-09-08 21:32:29,545 | INFO | total input tokens: 3806
2025-09-08 21:32:29,545 | INFO | input text tokens: 3168 # estimated
2025-09-08 21:32:29,545 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:32:29,545 | INFO | cost for input: $0.004757 USD
2025-09-08 21:32:29,545 | INFO | total output tokens: 1512
2025-09-08 21:32:29,546 | INFO | cost of output: $0.01512 USD
2025-09-08 21:32:29,546 | INFO | done judging, ALL GOOD
2025-09-08 21:32:29,547 | INFO | -current table:

2025-09-08 21:32:29,547 | INFO | -validating table: Review Information
2025-09-08 21:32:29,548 | INFO | -current table:

2025-09-08 21:32:29,548 | INFO | -validating table: Emergency Contact Information
2025-09-08 21:32:29,548 | INFO | started validating form fields
2025-09-08 21:32:29,548 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-08 21:32:29,548 | INFO | --current are:
Company Name : Velorynt Labs
Company Code : 37546
Period : 12/17/2024 to 12/26/2024
Employee Name : Laura Smith
Address line 1 : 8356 Joy Lakes
City : Debrabury
State : FL
Zip : 26024
Emp Id : 5908
SSN : 351-20-2239
2025-09-08 21:32:49,081 | INFO | llm gpt-5 api call took 19.525 seconds
2025-09-08 21:32:49,088 | INFO | total input tokens: 4684
2025-09-08 21:32:49,088 | INFO | input text tokens: 4046 # estimated
2025-09-08 21:32:49,088 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:32:49,088 | INFO | cost for input: $0.005855 USD
2025-09-08 21:32:49,089 | INFO | total output tokens: 512
2025-09-08 21:32:49,089 | INFO | cost of output: $0.00512 USD
2025-09-08 21:32:49,089 | INFO | done judging, ALL GOOD
2025-09-08 21:32:49,090 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-08 21:32:49,090 | INFO | --current are:
DOB (only date) : 10/21/1967
Gender : M
Marital Status : S
Status : T
Position : 
Title : 
Pay Group : 
Job Code : 
Emp Type : RFT
Statutory : 0.00
2025-09-08 21:33:36,089 | INFO | llm gpt-5 api call took 46.991 seconds
2025-09-08 21:33:36,096 | INFO | total input tokens: 4652
2025-09-08 21:33:36,096 | INFO | input text tokens: 4014 # estimated
2025-09-08 21:33:36,096 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:33:36,096 | INFO | cost for input: $0.005815 USD
2025-09-08 21:33:36,096 | INFO | total output tokens: 1090
2025-09-08 21:33:36,096 | INFO | cost of output: $0.0109 USD
2025-09-08 21:33:36,097 | INFO | done judging, ALL GOOD
2025-09-08 21:33:36,097 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-08 21:33:36,097 | INFO | --current are:
Seasonal : 0.00
Domestic Emp : No
Probation : 0.00
Home # : 942-0478935
Work # : 
Ext. : 
Email : longvelezcarol@yahoo.com
Mail Stop : 
Hire Date : 06/17/2016
Rehire Date : 
2025-09-08 21:34:39,076 | INFO | llm gpt-5 api call took 62.971 seconds
2025-09-08 21:34:39,083 | INFO | total input tokens: 4666
2025-09-08 21:34:39,083 | INFO | input text tokens: 4028 # estimated
2025-09-08 21:34:39,083 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:34:39,083 | INFO | cost for input: $0.005833 USD
2025-09-08 21:34:39,084 | INFO | total output tokens: 1153
2025-09-08 21:34:39,084 | INFO | cost of output: $0.01153 USD
2025-09-08 21:34:39,084 | INFO | done judging, ALL GOOD
2025-09-08 21:34:39,085 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-08 21:34:39,085 | INFO | --current are:
Term Date : 09/14/2019
Term Reason : N/A
Adj Sen Date : 
Pension : No
Visa Type : 
Exp : 
Citizen : 
I9 Reverify : 
I9 Verified : Yes
Deceased : No
2025-09-08 21:35:11,014 | INFO | llm gpt-5 api call took 31.920 seconds
2025-09-08 21:35:11,020 | INFO | total input tokens: 4653
2025-09-08 21:35:11,021 | INFO | input text tokens: 4015 # estimated
2025-09-08 21:35:11,021 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:35:11,021 | INFO | cost for input: $0.005816 USD
2025-09-08 21:35:11,021 | INFO | total output tokens: 964
2025-09-08 21:35:11,022 | INFO | cost of output: $0.00964 USD
2025-09-08 21:35:11,022 | INFO | done judging, ALL GOOD
2025-09-08 21:35:11,022 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-08 21:35:11,022 | INFO | --current are:
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
2025-09-08 21:35:34,973 | INFO | llm gpt-5 api call took 23.939 seconds
2025-09-08 21:35:34,982 | INFO | total input tokens: 4653
2025-09-08 21:35:34,982 | INFO | input text tokens: 4015 # estimated
2025-09-08 21:35:34,982 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:35:34,982 | INFO | cost for input: $0.005816 USD
2025-09-08 21:35:34,982 | INFO | total output tokens: 711
2025-09-08 21:35:34,983 | INFO | cost of output: $0.00711 USD
2025-09-08 21:35:34,983 | INFO | done judging, ALL GOOD
2025-09-08 21:35:34,983 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-08 21:35:34,984 | INFO | --current are:
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
2025-09-08 21:37:28,877 | INFO | llm gpt-5 api call took 113.883 seconds
2025-09-08 21:37:28,883 | INFO | total input tokens: 4642
2025-09-08 21:37:28,884 | INFO | input text tokens: 4004 # estimated
2025-09-08 21:37:28,884 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:37:28,884 | INFO | cost for input: $0.001051 USD
2025-09-08 21:37:28,884 | INFO | total output tokens: 1665
2025-09-08 21:37:28,884 | INFO | cost of output: $0.01665 USD
2025-09-08 21:37:28,885 | INFO | done judging, ALL GOOD
2025-09-08 21:37:28,885 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-08 21:37:28,885 | INFO | --current are:
Default Hours : 0.00
Locations : 606
Positions : 700
2025-09-08 21:37:49,770 | INFO | llm gpt-5 api call took 20.876 seconds
2025-09-08 21:37:49,777 | INFO | total input tokens: 4621
2025-09-08 21:37:49,777 | INFO | input text tokens: 3983 # estimated
2025-09-08 21:37:49,777 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:37:49,777 | INFO | cost for input: $0.005776 USD
2025-09-08 21:37:49,777 | INFO | total output tokens: 785
2025-09-08 21:37:49,777 | INFO | cost of output: $0.00785 USD
2025-09-08 21:37:49,778 | INFO | done judging, ALL GOOD

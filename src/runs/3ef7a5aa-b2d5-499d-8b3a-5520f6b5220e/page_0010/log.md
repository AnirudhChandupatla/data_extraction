2025-09-09 06:58:05,411 | INFO | started initial extraction for page 10
2025-09-09 07:00:15,746 | INFO | llm gpt-5 api call took 130.074 seconds
2025-09-09 07:00:15,751 | INFO | total input tokens: 3016
2025-09-09 07:00:15,751 | INFO | input text tokens: 2378 # estimated
2025-09-09 07:00:15,751 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:00:15,751 | INFO | cost for input: $0.00377 USD
2025-09-09 07:00:15,751 | INFO | total output tokens: 3732
2025-09-09 07:00:15,751 | INFO | cost of output: $0.03732 USD
2025-09-09 07:00:15,752 | INFO | initial extraction of page data done.
2025-09-09 07:00:23,688 | INFO | got response with OCR coordinates info from azure doc intelligence for page 10
2025-09-09 07:00:23,688 | INFO | started validating tables
2025-09-09 07:00:23,690 | INFO | -current table:
| RateCode   | Description   |   Rate | Salary   | Effective Dates          |
|:-----------|:--------------|-------:|:---------|:-------------------------|
| Base       | Base Rate     |  14.3  |          | 06/17/2019 to 12/31/2100 |
| Base       | Base Rate     |  13.9  |          | 06/17/2018 to 06/16/2019 |
| Base       | Base Rate     |  13.45 |          | 06/17/2017 to 06/16/2018 |
| Base       | Base Rate     |  13    |          | 09/04/2016 to 06/16/2017 |
| Base       | Base Rate     |  12    |          | 07/01/2016 to 09/03/2016 |
2025-09-09 07:00:23,690 | INFO | -validating table: Rate/Salary Information
2025-09-09 07:00:23,690 | INFO | --figuring out table emptiness...
2025-09-09 07:00:52,894 | INFO | llm gpt-5-mini api call took 29.202 seconds
2025-09-09 07:00:52,912 | INFO | total input tokens: 18053
2025-09-09 07:00:52,912 | INFO | input text tokens: 17122 # estimated
2025-09-09 07:00:52,912 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:00:52,912 | INFO | cost for input: $0.022566 USD
2025-09-09 07:00:52,912 | INFO | total output tokens: 3092
2025-09-09 07:00:52,912 | INFO | cost of output: $0.03092 USD
2025-09-09 07:00:52,913 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:02:02,755 | INFO | llm gpt-5-mini api call took 69.842 seconds
2025-09-09 07:02:02,758 | INFO | total input tokens: 2564
2025-09-09 07:02:02,758 | INFO | input text tokens: 2556 # estimated
2025-09-09 07:02:02,758 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:02:02,758 | INFO | cost for input: $0.003205 USD
2025-09-09 07:02:02,758 | INFO | total output tokens: 4288
2025-09-09 07:02:02,759 | INFO | cost of output: $0.04288 USD
2025-09-09 07:02:02,759 | INFO | --got table grid emptiness info:
|RateCode|Description|Rate|Salary|Effective Dates|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
2025-09-09 07:02:25,329 | INFO | llm gpt-5 api call took 22.569 seconds
2025-09-09 07:02:25,335 | INFO | total input tokens: 3518
2025-09-09 07:02:25,335 | INFO | input text tokens: 2880 # estimated
2025-09-09 07:02:25,336 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:02:25,336 | INFO | cost for input: $0.004398 USD
2025-09-09 07:02:25,336 | INFO | total output tokens: 552
2025-09-09 07:02:25,336 | INFO | cost of output: $0.00552 USD
2025-09-09 07:02:25,337 | INFO | done judging, ALL GOOD
2025-09-09 07:02:25,338 | INFO | -current table:
| Employee Tax (code description)   | Status   |   Add'l Amount | Effective Dates          | Default   |
|:----------------------------------|:---------|---------------:|:-------------------------|:----------|
| MED Medicare                      |          |              0 | 07/01/2016 to 12/31/2100 | Yes       |
| SS OASDI                          |          |              0 | 07/01/2016 to 12/31/2100 | Yes       |
| FITW Federal Income Tax           | S-2      |             20 | 01/01/2018 to 12/31/2100 | Yes       |
| MN Minnesota SITW                 | S-2      |              0 | 07/01/2016 to 12/31/2100 | Yes       |
2025-09-09 07:02:25,339 | INFO | -validating table: Tax Information (Employee)
2025-09-09 07:02:25,339 | INFO | --figuring out table emptiness...
2025-09-09 07:02:59,773 | INFO | llm gpt-5-mini api call took 34.432 seconds
2025-09-09 07:02:59,792 | INFO | total input tokens: 18033
2025-09-09 07:02:59,792 | INFO | input text tokens: 17102 # estimated
2025-09-09 07:02:59,792 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:02:59,792 | INFO | cost for input: $0.022541 USD
2025-09-09 07:02:59,792 | INFO | total output tokens: 3351
2025-09-09 07:02:59,792 | INFO | cost of output: $0.03351 USD
2025-09-09 07:02:59,793 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:03:53,063 | INFO | llm gpt-5-mini api call took 53.270 seconds
2025-09-09 07:03:53,066 | INFO | total input tokens: 2129
2025-09-09 07:03:53,066 | INFO | input text tokens: 2121 # estimated
2025-09-09 07:03:53,066 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:03:53,067 | INFO | cost for input: $0.002661 USD
2025-09-09 07:03:53,067 | INFO | total output tokens: 2710
2025-09-09 07:03:53,067 | INFO | cost of output: $0.0271 USD
2025-09-09 07:03:53,067 | INFO | --got table grid emptiness info:
|Employee Tax (code description)|Status|Add'l Amount|Effective Dates|Default|
|---:|:---:|:---:|:---:|:---:|
|X| |X|X|X|
|X| |X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
2025-09-09 07:04:15,244 | INFO | llm gpt-5 api call took 22.177 seconds
2025-09-09 07:04:15,249 | INFO | total input tokens: 3521
2025-09-09 07:04:15,250 | INFO | input text tokens: 2883 # estimated
2025-09-09 07:04:15,250 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:04:15,250 | INFO | cost for input: $0.001233 USD
2025-09-09 07:04:15,250 | INFO | total output tokens: 680
2025-09-09 07:04:15,250 | INFO | cost of output: $0.0068 USD
2025-09-09 07:04:15,251 | INFO | done judging, ALL GOOD
2025-09-09 07:04:15,252 | INFO | -current table:
| Employer Tax (code description)         | Effective Dates          | Default   |
|:----------------------------------------|:-------------------------|:----------|
| MED-R Medicare - Employer               | 07/01/2016 to 12/31/2100 |           |
| SS-R OASDI - Employer                   | 07/01/2016 to 12/31/2100 |           |
| FUTA Fed Unemployment                   | 07/01/2016 to 12/31/2100 |           |
| MNAST Minnesota Federal Loan Assessment | 07/01/2016 to 12/31/2100 |           |
| MNDW Workforce Enhancement Fee          | 07/01/2016 to 12/31/2100 |           |
| MNSUI Minnesota SUI                     | 07/01/2016 to 12/31/2100 |           |
2025-09-09 07:04:15,252 | INFO | -validating table: Tax Information (Employer)
2025-09-09 07:04:15,252 | INFO | --figuring out table emptiness...
2025-09-09 07:04:53,120 | INFO | llm gpt-5-mini api call took 37.866 seconds
2025-09-09 07:04:53,138 | INFO | total input tokens: 18047
2025-09-09 07:04:53,138 | INFO | input text tokens: 17116 # estimated
2025-09-09 07:04:53,138 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:04:53,139 | INFO | cost for input: $0.022559 USD
2025-09-09 07:04:53,139 | INFO | total output tokens: 2219
2025-09-09 07:04:53,139 | INFO | cost of output: $0.02219 USD
2025-09-09 07:04:53,139 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:06:03,158 | INFO | llm gpt-5-mini api call took 70.019 seconds
2025-09-09 07:06:03,161 | INFO | total input tokens: 1881
2025-09-09 07:06:03,161 | INFO | input text tokens: 1873 # estimated
2025-09-09 07:06:03,162 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:06:03,162 | INFO | cost for input: $0.002351 USD
2025-09-09 07:06:03,162 | INFO | total output tokens: 3581
2025-09-09 07:06:03,162 | INFO | cost of output: $0.03581 USD
2025-09-09 07:06:03,162 | INFO | --got table grid emptiness info:
|Employer Tax (code description)|Effective Dates|Default|
|---|---|---|
|X|X| |
|X|X| |
|X|X| |
|X|X| |
|X|X| |
|X|X| |
2025-09-09 07:06:31,725 | INFO | llm gpt-5 api call took 28.562 seconds
2025-09-09 07:06:31,730 | INFO | total input tokens: 3510
2025-09-09 07:06:31,731 | INFO | input text tokens: 2872 # estimated
2025-09-09 07:06:31,731 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:06:31,731 | INFO | cost for input: $0.004387 USD
2025-09-09 07:06:31,731 | INFO | total output tokens: 680
2025-09-09 07:06:31,731 | INFO | cost of output: $0.0068 USD
2025-09-09 07:06:31,732 | INFO | done judging, ALL GOOD
2025-09-09 07:06:31,733 | INFO | -current table:
| Code   | Deduction             |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-------|:----------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| FH125  | Health Insurance S125 |  87.87 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2019 to 12/31/2100 |
2025-09-09 07:06:31,733 | INFO | -validating table: Deduction Information
2025-09-09 07:06:31,733 | INFO | --figuring out table emptiness...
2025-09-09 07:07:00,953 | INFO | llm gpt-5-mini api call took 29.218 seconds
2025-09-09 07:07:00,971 | INFO | total input tokens: 18002
2025-09-09 07:07:00,971 | INFO | input text tokens: 17071 # estimated
2025-09-09 07:07:00,971 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:07:00,971 | INFO | cost for input: $0.022503 USD
2025-09-09 07:07:00,971 | INFO | total output tokens: 2349
2025-09-09 07:07:00,972 | INFO | cost of output: $0.02349 USD
2025-09-09 07:07:00,972 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:08:13,103 | INFO | llm gpt-5-mini api call took 72.131 seconds
2025-09-09 07:08:13,107 | INFO | total input tokens: 1988
2025-09-09 07:08:13,107 | INFO | input text tokens: 1980 # estimated
2025-09-09 07:08:13,107 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:08:13,107 | INFO | cost for input: $0.002485 USD
2025-09-09 07:08:13,107 | INFO | total output tokens: 4239
2025-09-09 07:08:13,108 | INFO | cost of output: $0.04239 USD
2025-09-09 07:08:13,108 | INFO | --got table grid emptiness info:
|Code|Deduction|Rate|CalcCode|Frequency|Goal/Paid|Min/Max/Annual Max|Arrears|Agency|Effective Dates|
|---|---|---|---|---|---|---|---|---|---|
|X|X|X| |X|X|X|X| |X|
2025-09-09 07:08:54,329 | INFO | llm gpt-5 api call took 41.221 seconds
2025-09-09 07:08:54,338 | INFO | total input tokens: 3482
2025-09-09 07:08:54,338 | INFO | input text tokens: 2844 # estimated
2025-09-09 07:08:54,338 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:08:54,338 | INFO | cost for input: $0.004352 USD
2025-09-09 07:08:54,338 | INFO | total output tokens: 999
2025-09-09 07:08:54,338 | INFO | cost of output: $0.00999 USD
2025-09-09 07:08:54,339 | INFO | done judging, ALL GOOD
2025-09-09 07:08:54,341 | INFO | -current table:
|   Sequence No. |   Transit No. |   Account No. | Checking?   | Account Name   | Amount Code   |   Amount | Prenote Date   | Effective Dates          | Exclude Special   |
|---------------:|--------------:|--------------:|:------------|:---------------|:--------------|---------:|:---------------|:-------------------------|:------------------|
|             99 |     091000019 |    9414336673 | Yes         | Laura Smith    | %             |      100 | 07/15/2016     | 07/15/2016 to 12/31/2100 | No                |
2025-09-09 07:08:54,341 | INFO | -validating table: Direct Deposit Information
2025-09-09 07:08:54,342 | INFO | --figuring out table emptiness...
2025-09-09 07:09:12,946 | INFO | llm gpt-5-mini api call took 18.602 seconds
2025-09-09 07:09:12,966 | INFO | total input tokens: 17995
2025-09-09 07:09:12,966 | INFO | input text tokens: 17064 # estimated
2025-09-09 07:09:12,966 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:09:12,967 | INFO | cost for input: $0.022494 USD
2025-09-09 07:09:12,967 | INFO | total output tokens: 2070
2025-09-09 07:09:12,967 | INFO | cost of output: $0.0207 USD
2025-09-09 07:09:12,967 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:10:20,542 | INFO | llm gpt-5-mini api call took 67.575 seconds
2025-09-09 07:10:20,549 | INFO | total input tokens: 1831
2025-09-09 07:10:20,549 | INFO | input text tokens: 1823 # estimated
2025-09-09 07:10:20,550 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:10:20,550 | INFO | cost for input: $0.002289 USD
2025-09-09 07:10:20,550 | INFO | total output tokens: 3544
2025-09-09 07:10:20,551 | INFO | cost of output: $0.03544 USD
2025-09-09 07:10:20,551 | INFO | --got table grid emptiness info:
|Sequence No.|Transit No.|Account No.|Checking?|Account Name|Amount Code|Amount|Prenote Date|Effective Dates|Exclude Special|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X|X|X|X|X|X|
2025-09-09 07:10:37,678 | INFO | llm gpt-5 api call took 17.125 seconds
2025-09-09 07:10:37,683 | INFO | total input tokens: 3484
2025-09-09 07:10:37,683 | INFO | input text tokens: 2846 # estimated
2025-09-09 07:10:37,683 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:10:37,684 | INFO | cost for input: $0.004355 USD
2025-09-09 07:10:37,684 | INFO | total output tokens: 424
2025-09-09 07:10:37,684 | INFO | cost of output: $0.00424 USD
2025-09-09 07:10:37,684 | INFO | done judging, ALL GOOD
2025-09-09 07:10:37,686 | INFO | -current table:
| ECode   | CalcCode   | Rate Code   |   Rate | Rate Per   |   Amount | Tabled?   |   Units | Frequency   | Goal/Paid/Goal Bal.   | Min/Max/Ann. Max   | Effective Dates          |
|:--------|:-----------|:------------|-------:|:-----------|---------:|:----------|--------:|:------------|:----------------------|:-------------------|:-------------------------|
| STD     |            |             |      0 |            |     4.85 | No        |       0 | B5          | 0.00/0.00/0.00        | 0.00/0.00/0.00     | 01/01/2018 to 12/31/2100 |
2025-09-09 07:10:37,686 | INFO | -validating table: Fringe Benefit Information
2025-09-09 07:10:37,686 | INFO | --figuring out table emptiness...
2025-09-09 07:11:33,796 | INFO | llm gpt-5-mini api call took 56.108 seconds
2025-09-09 07:11:33,814 | INFO | total input tokens: 18028
2025-09-09 07:11:33,814 | INFO | input text tokens: 17097 # estimated
2025-09-09 07:11:33,814 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:11:33,814 | INFO | cost for input: $0.022535 USD
2025-09-09 07:11:33,814 | INFO | total output tokens: 3624
2025-09-09 07:11:33,815 | INFO | cost of output: $0.03624 USD
2025-09-09 07:11:33,815 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:12:36,502 | INFO | llm gpt-5-mini api call took 62.687 seconds
2025-09-09 07:12:36,505 | INFO | total input tokens: 1809
2025-09-09 07:12:36,505 | INFO | input text tokens: 1801 # estimated
2025-09-09 07:12:36,505 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:12:36,505 | INFO | cost for input: $0.002261 USD
2025-09-09 07:12:36,506 | INFO | total output tokens: 4470
2025-09-09 07:12:36,506 | INFO | cost of output: $0.0447 USD
2025-09-09 07:12:36,506 | INFO | --got table grid emptiness info:
|ECode|CalcCode|Rate Code|Rate|Rate Per|Amount|Tabled?|Units|Frequency|Goal/Paid/Goal Bal.|Min/Max/Ann. Max|Effective Dates|
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|X| | |X| |X|X|X|X|X|X|X|
2025-09-09 07:12:58,841 | INFO | llm gpt-5 api call took 22.334 seconds
2025-09-09 07:12:58,846 | INFO | total input tokens: 3547
2025-09-09 07:12:58,846 | INFO | input text tokens: 2909 # estimated
2025-09-09 07:12:58,847 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:12:58,847 | INFO | cost for input: $0.001266 USD
2025-09-09 07:12:58,847 | INFO | total output tokens: 872
2025-09-09 07:12:58,847 | INFO | cost of output: $0.00872 USD
2025-09-09 07:12:58,847 | INFO | done judging, ALL GOOD
2025-09-09 07:12:58,849 | INFO | -current table:
| BCode    |   Rate |   Amount |   Hours | Max/Carryover Max   | Length of Service   | Hours: Used/Avail/Total/Prob   | Dollars: Used/Avail/Total/Prob   | Effective Dates          |
|:---------|-------:|---------:|--------:|:--------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| PER      |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 09/01/2016 to 12/31/2100 |
| SICK     |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 09/01/2016 to 12/31/2100 |
| VAC-NEX8 |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 09/01/2016 to 12/31/2100 |
| VAC/CO   |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 01/01/2018 to 12/31/2100 |
2025-09-09 07:12:58,850 | INFO | -validating table: Benefit Accrual Information
2025-09-09 07:12:58,850 | INFO | --figuring out table emptiness...
2025-09-09 07:13:39,593 | INFO | llm gpt-5-mini api call took 40.742 seconds
2025-09-09 07:13:39,616 | INFO | total input tokens: 18268
2025-09-09 07:13:39,616 | INFO | input text tokens: 17337 # estimated
2025-09-09 07:13:39,616 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:13:39,616 | INFO | cost for input: $0.003107 USD
2025-09-09 07:13:39,617 | INFO | total output tokens: 4451
2025-09-09 07:13:39,617 | INFO | cost of output: $0.04451 USD
2025-09-09 07:13:39,617 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:14:48,949 | INFO | llm gpt-5-mini api call took 69.332 seconds
2025-09-09 07:14:48,953 | INFO | total input tokens: 2962
2025-09-09 07:14:48,953 | INFO | input text tokens: 2954 # estimated
2025-09-09 07:14:48,953 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:14:48,954 | INFO | cost for input: $0.003703 USD
2025-09-09 07:14:48,954 | INFO | total output tokens: 4937
2025-09-09 07:14:48,954 | INFO | cost of output: $0.04937 USD
2025-09-09 07:14:48,954 | INFO | --got table grid emptiness info:
|BCode|Rate|Amount|Hours|Max/Carryover Max|Length of Service|Hours: Used/Avail/Total/Prob|Dollars: Used/Avail/Total/Prob|Effective Dates|
|---|---|---|---|---|---|---|---|---|
|X|X|X|X|X||X|X|X|
|X|X|X|X|X||X|X|X|
|X|X|X|X|X||X|X|X|
|X|X|X|X|X||X|X|X|
2025-09-09 07:15:56,860 | INFO | llm gpt-5 api call took 67.906 seconds
2025-09-09 07:15:56,866 | INFO | total input tokens: 3806
2025-09-09 07:15:56,866 | INFO | input text tokens: 3168 # estimated
2025-09-09 07:15:56,866 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:15:56,866 | INFO | cost for input: $0.004757 USD
2025-09-09 07:15:56,866 | INFO | total output tokens: 1000
2025-09-09 07:15:56,867 | INFO | cost of output: $0.01 USD
2025-09-09 07:15:56,867 | INFO | done judging, ALL GOOD
2025-09-09 07:15:56,868 | INFO | -current table:

2025-09-09 07:15:56,868 | INFO | -validating table: Review Information
2025-09-09 07:15:56,868 | INFO | -current table:

2025-09-09 07:15:56,869 | INFO | -validating table: Emergency Contact Information
2025-09-09 07:15:56,869 | INFO | started validating form fields
2025-09-09 07:15:56,869 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-09 07:15:56,869 | INFO | --current are:
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
2025-09-09 07:16:09,883 | INFO | llm gpt-5 api call took 13.006 seconds
2025-09-09 07:16:09,890 | INFO | total input tokens: 4684
2025-09-09 07:16:09,890 | INFO | input text tokens: 4046 # estimated
2025-09-09 07:16:09,890 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:16:09,890 | INFO | cost for input: $0.002687 USD
2025-09-09 07:16:09,891 | INFO | total output tokens: 512
2025-09-09 07:16:09,891 | INFO | cost of output: $0.00512 USD
2025-09-09 07:16:09,891 | INFO | done judging, ALL GOOD
2025-09-09 07:16:09,891 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-09 07:16:09,891 | INFO | --current are:
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
2025-09-09 07:16:43,783 | INFO | llm gpt-5 api call took 33.883 seconds
2025-09-09 07:16:43,790 | INFO | total input tokens: 4652
2025-09-09 07:16:43,790 | INFO | input text tokens: 4014 # estimated
2025-09-09 07:16:43,790 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:16:43,790 | INFO | cost for input: $0.005815 USD
2025-09-09 07:16:43,791 | INFO | total output tokens: 1154
2025-09-09 07:16:43,791 | INFO | cost of output: $0.01154 USD
2025-09-09 07:16:43,791 | INFO | done judging, ALL GOOD
2025-09-09 07:16:43,791 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-09 07:16:43,791 | INFO | --current are:
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
2025-09-09 07:17:29,233 | INFO | llm gpt-5 api call took 45.433 seconds
2025-09-09 07:17:29,241 | INFO | total input tokens: 4666
2025-09-09 07:17:29,241 | INFO | input text tokens: 4028 # estimated
2025-09-09 07:17:29,241 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:17:29,241 | INFO | cost for input: $0.005833 USD
2025-09-09 07:17:29,241 | INFO | total output tokens: 1025
2025-09-09 07:17:29,241 | INFO | cost of output: $0.01025 USD
2025-09-09 07:17:29,242 | INFO | done judging, ALL GOOD
2025-09-09 07:17:29,242 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-09 07:17:29,242 | INFO | --current are:
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
2025-09-09 07:18:14,286 | INFO | llm gpt-5 api call took 45.036 seconds
2025-09-09 07:18:14,293 | INFO | total input tokens: 4653
2025-09-09 07:18:14,293 | INFO | input text tokens: 4015 # estimated
2025-09-09 07:18:14,293 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:18:14,293 | INFO | cost for input: $0.005816 USD
2025-09-09 07:18:14,294 | INFO | total output tokens: 1092
2025-09-09 07:18:14,294 | INFO | cost of output: $0.01092 USD
2025-09-09 07:18:14,294 | INFO | done judging, ALL GOOD
2025-09-09 07:18:14,294 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-09 07:18:14,294 | INFO | --current are:
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
2025-09-09 07:18:33,933 | INFO | llm gpt-5 api call took 19.630 seconds
2025-09-09 07:18:33,944 | INFO | total input tokens: 4653
2025-09-09 07:18:33,945 | INFO | input text tokens: 4015 # estimated
2025-09-09 07:18:33,945 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:18:33,945 | INFO | cost for input: $0.005816 USD
2025-09-09 07:18:33,945 | INFO | total output tokens: 839
2025-09-09 07:18:33,945 | INFO | cost of output: $0.00839 USD
2025-09-09 07:18:33,946 | INFO | done judging, ALL GOOD
2025-09-09 07:18:33,946 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 07:18:33,947 | INFO | --current are:
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
2025-09-09 07:19:10,057 | INFO | llm gpt-5 api call took 36.099 seconds
2025-09-09 07:19:10,064 | INFO | total input tokens: 4642
2025-09-09 07:19:10,064 | INFO | input text tokens: 4004 # estimated
2025-09-09 07:19:10,064 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:19:10,064 | INFO | cost for input: $0.005803 USD
2025-09-09 07:19:10,065 | INFO | total output tokens: 1409
2025-09-09 07:19:10,065 | INFO | cost of output: $0.01409 USD
2025-09-09 07:19:10,065 | INFO | done judging, ALL GOOD
2025-09-09 07:19:10,065 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-09 07:19:10,066 | INFO | --current are:
Default Hours : 0.00
Locations : 606
Positions : 700
2025-09-09 07:19:30,075 | INFO | llm gpt-5 api call took 20.000 seconds
2025-09-09 07:19:30,082 | INFO | total input tokens: 4621
2025-09-09 07:19:30,082 | INFO | input text tokens: 3983 # estimated
2025-09-09 07:19:30,082 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:19:30,083 | INFO | cost for input: $0.005776 USD
2025-09-09 07:19:30,083 | INFO | total output tokens: 657
2025-09-09 07:19:30,083 | INFO | cost of output: $0.00657 USD
2025-09-09 07:19:30,083 | INFO | done judging, ALL GOOD

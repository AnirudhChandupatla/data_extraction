2025-09-09 05:44:52,221 | INFO | started initial extraction for page 3
2025-09-09 05:46:49,808 | INFO | llm gpt-5 api call took 117.300 seconds
2025-09-09 05:46:49,812 | INFO | total input tokens: 3005
2025-09-09 05:46:49,813 | INFO | input text tokens: 2367 # estimated
2025-09-09 05:46:49,813 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:46:49,813 | INFO | cost for input: $0.003756 USD
2025-09-09 05:46:49,813 | INFO | total output tokens: 3361
2025-09-09 05:46:49,813 | INFO | cost of output: $0.03361 USD
2025-09-09 05:46:49,814 | INFO | initial extraction of page data done.
2025-09-09 05:46:56,189 | INFO | got response with OCR coordinates info from azure doc intelligence for page 3
2025-09-09 05:46:56,190 | INFO | started validating tables
2025-09-09 05:46:56,191 | INFO | -current table:
| RateCode   | Description   |   Rate | Salary   | Effective Dates          |
|:-----------|:--------------|-------:|:---------|:-------------------------|
| Base       | Base Rate     |  17.83 |          | 02/04/2018 to 12/31/2100 |
| Base       | Base Rate     |  17.4  |          | 02/05/2017 to 02/03/2018 |
| Base       | Base Rate     |  16.9  |          | 05/15/2016 to 02/04/2017 |
| Base       | Base Rate     |  16.5  |          | 01/01/2015 to 05/14/2016 |
2025-09-09 05:46:56,192 | INFO | -validating table: Rate/Salary Information
2025-09-09 05:46:56,192 | INFO | --figuring out table emptiness...
2025-09-09 05:48:40,069 | WARNING | Transient error (status=429) attempt 1/6; sleeping 16.00s before retry.
2025-09-09 05:50:43,210 | INFO | llm gpt-5-mini api call took 107.140 seconds
2025-09-09 05:50:43,227 | INFO | total input tokens: 17731
2025-09-09 05:50:43,227 | INFO | input text tokens: 16800 # estimated
2025-09-09 05:50:43,228 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:50:43,228 | INFO | cost for input: $0.022164 USD
2025-09-09 05:50:43,228 | INFO | total output tokens: 3654
2025-09-09 05:50:43,228 | INFO | cost of output: $0.03654 USD
2025-09-09 05:50:43,228 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 05:51:34,514 | INFO | llm gpt-5-mini api call took 51.285 seconds
2025-09-09 05:51:34,517 | INFO | total input tokens: 2358
2025-09-09 05:51:34,517 | INFO | input text tokens: 2350 # estimated
2025-09-09 05:51:34,517 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 05:51:34,517 | INFO | cost for input: $0.002948 USD
2025-09-09 05:51:34,517 | INFO | total output tokens: 2891
2025-09-09 05:51:34,518 | INFO | cost of output: $0.02891 USD
2025-09-09 05:51:34,518 | INFO | --got table grid emptiness info:
|RateCode|Description|Rate|Salary|Effective Dates|
|---:|:---:|:---:|:---:|:---:|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
2025-09-09 05:52:00,070 | INFO | llm gpt-5 api call took 25.551 seconds
2025-09-09 05:52:00,075 | INFO | total input tokens: 3489
2025-09-09 05:52:00,075 | INFO | input text tokens: 2851 # estimated
2025-09-09 05:52:00,075 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:52:00,075 | INFO | cost for input: $0.004361 USD
2025-09-09 05:52:00,075 | INFO | total output tokens: 680
2025-09-09 05:52:00,076 | INFO | cost of output: $0.0068 USD
2025-09-09 05:52:00,076 | INFO | done judging, ALL GOOD
2025-09-09 05:52:00,077 | INFO | -current table:
| Employee Tax (code description)   | Status   |   Add'l Amount | Effective Dates          | Default   |
|:----------------------------------|:---------|---------------:|:-------------------------|:----------|
| MED Medicare                      |          |              0 | 01/01/2015 to 12/31/2100 | Yes       |
| SS OASDI                          |          |              0 | 01/01/2015 to 12/31/2100 | Yes       |
| FITW Federal Income Tax           | M-3      |              0 | 01/01/2015 to 12/31/2100 | Yes       |
| MN Minnesota SITW                 | M-3      |              0 | 01/01/2015 to 12/31/2100 | Yes       |
2025-09-09 05:52:00,077 | INFO | -validating table: Tax Information (Employee)
2025-09-09 05:52:00,078 | INFO | --figuring out table emptiness...
2025-09-09 05:53:43,462 | INFO | llm gpt-5-mini api call took 103.383 seconds
2025-09-09 05:53:43,480 | INFO | total input tokens: 17740
2025-09-09 05:53:43,480 | INFO | input text tokens: 16809 # estimated
2025-09-09 05:53:43,480 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:53:43,480 | INFO | cost for input: $0.022175 USD
2025-09-09 05:53:43,480 | INFO | total output tokens: 2332
2025-09-09 05:53:43,480 | INFO | cost of output: $0.02332 USD
2025-09-09 05:53:43,481 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 05:55:02,829 | INFO | llm gpt-5-mini api call took 79.348 seconds
2025-09-09 05:55:02,832 | INFO | total input tokens: 2134
2025-09-09 05:55:02,832 | INFO | input text tokens: 2126 # estimated
2025-09-09 05:55:02,832 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 05:55:02,833 | INFO | cost for input: $0.002668 USD
2025-09-09 05:55:02,833 | INFO | total output tokens: 4754
2025-09-09 05:55:02,833 | INFO | cost of output: $0.04754 USD
2025-09-09 05:55:02,833 | INFO | --got table grid emptiness info:
|Employee Tax (code description)|Status|Add'l Amount|Effective Dates|Default|
|---:|---:|---:|---:|---:|
|X| |X|X|X|
|X| |X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
2025-09-09 05:55:31,544 | INFO | llm gpt-5 api call took 28.711 seconds
2025-09-09 05:55:31,549 | INFO | total input tokens: 3506
2025-09-09 05:55:31,550 | INFO | input text tokens: 2868 # estimated
2025-09-09 05:55:31,550 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:55:31,550 | INFO | cost for input: $0.004383 USD
2025-09-09 05:55:31,550 | INFO | total output tokens: 936
2025-09-09 05:55:31,550 | INFO | cost of output: $0.00936 USD
2025-09-09 05:55:31,551 | INFO | done judging, ALL GOOD
2025-09-09 05:55:31,552 | INFO | -current table:
| Employer Tax (code description)         | Effective Dates          | Default   |
|:----------------------------------------|:-------------------------|:----------|
| MED-R Medicare - Employer               | 01/01/2015 to 12/31/2100 |           |
| SS-R OASDI - Employer                   | 01/01/2015 to 12/31/2100 |           |
| FUTA Fed Unemployment                   | 01/01/2015 to 12/31/2100 |           |
| MNAST Minnesota Federal Loan Assessment | 01/01/2015 to 12/31/2100 |           |
| MNDW Workforce Enhancement Fee          | 01/01/2015 to 12/31/2100 |           |
| MNSUI Minnesota SUI                     | 01/01/2015 to 12/31/2100 |           |
2025-09-09 05:55:31,552 | INFO | -validating table: Tax Information (Employer)
2025-09-09 05:55:31,552 | INFO | --figuring out table emptiness...
2025-09-09 05:55:55,066 | INFO | llm gpt-5-mini api call took 23.512 seconds
2025-09-09 05:55:55,084 | INFO | total input tokens: 17754
2025-09-09 05:55:55,084 | INFO | input text tokens: 16823 # estimated
2025-09-09 05:55:55,084 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:55:55,084 | INFO | cost for input: $0.022193 USD
2025-09-09 05:55:55,084 | INFO | total output tokens: 2380
2025-09-09 05:55:55,084 | INFO | cost of output: $0.0238 USD
2025-09-09 05:55:55,085 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 05:57:12,346 | INFO | llm gpt-5-mini api call took 77.261 seconds
2025-09-09 05:57:12,349 | INFO | total input tokens: 1786
2025-09-09 05:57:12,349 | INFO | input text tokens: 1778 # estimated
2025-09-09 05:57:12,349 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 05:57:12,349 | INFO | cost for input: $0.002233 USD
2025-09-09 05:57:12,349 | INFO | total output tokens: 4854
2025-09-09 05:57:12,349 | INFO | cost of output: $0.04854 USD
2025-09-09 05:57:12,350 | INFO | --got table grid emptiness info:
|Employer Tax (code description)|Effective Dates|Default|
|X|X| |
|X|X| |
|X|X| |
|X|X| |
|X|X| |
|X|X| |
2025-09-09 05:57:29,047 | INFO | llm gpt-5 api call took 16.696 seconds
2025-09-09 05:57:29,052 | INFO | total input tokens: 3492
2025-09-09 05:57:29,052 | INFO | input text tokens: 2854 # estimated
2025-09-09 05:57:29,052 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:57:29,052 | INFO | cost for input: $0.004365 USD
2025-09-09 05:57:29,053 | INFO | total output tokens: 488
2025-09-09 05:57:29,053 | INFO | cost of output: $0.00488 USD
2025-09-09 05:57:29,053 | INFO | done judging, ALL GOOD
2025-09-09 05:57:29,054 | INFO | -current table:
| Code   | Deduction         |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-------|:------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| 401KC  | 401K Contribution |      6 | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 04/08/2016 to 12/31/2100 |
2025-09-09 05:57:29,055 | INFO | -validating table: Deduction Information
2025-09-09 05:57:29,055 | INFO | --figuring out table emptiness...
2025-09-09 05:58:49,713 | INFO | llm gpt-5-mini api call took 80.657 seconds
2025-09-09 05:58:49,731 | INFO | total input tokens: 17709
2025-09-09 05:58:49,731 | INFO | input text tokens: 16778 # estimated
2025-09-09 05:58:49,731 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:58:49,731 | INFO | cost for input: $0.022136 USD
2025-09-09 05:58:49,731 | INFO | total output tokens: 1765
2025-09-09 05:58:49,731 | INFO | cost of output: $0.01765 USD
2025-09-09 05:58:49,732 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:00:11,402 | INFO | llm gpt-5-mini api call took 81.670 seconds
2025-09-09 06:00:11,405 | INFO | total input tokens: 1724
2025-09-09 06:00:11,405 | INFO | input text tokens: 1716 # estimated
2025-09-09 06:00:11,405 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:00:11,405 | INFO | cost for input: $0.002155 USD
2025-09-09 06:00:11,405 | INFO | total output tokens: 4943
2025-09-09 06:00:11,405 | INFO | cost of output: $0.04943 USD
2025-09-09 06:00:11,405 | INFO | --got table grid emptiness info:
|Code|Deduction|Rate|CalcCode|Frequency|Goal/Paid|Min/Max/Annual Max|Arrears|Agency|Effective Dates|
|---|---|---|---|---|---|---|---|---|---|
|X|X|X|X| |X|X|X| |X|
2025-09-09 06:00:31,713 | INFO | llm gpt-5 api call took 20.307 seconds
2025-09-09 06:00:31,718 | INFO | total input tokens: 3471
2025-09-09 06:00:31,718 | INFO | input text tokens: 2833 # estimated
2025-09-09 06:00:31,718 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:00:31,719 | INFO | cost for input: $0.004339 USD
2025-09-09 06:00:31,719 | INFO | total output tokens: 808
2025-09-09 06:00:31,719 | INFO | cost of output: $0.00808 USD
2025-09-09 06:00:31,719 | INFO | done judging, ALL GOOD
2025-09-09 06:00:31,720 | INFO | -current table:
|   Sequence No. |   Transit No. |   Account No. | Checking?   | Account Name   | Amount Code   |   Amount | Prenote Date   | Effective Dates          | Exclude Special   |
|---------------:|--------------:|--------------:|:------------|:---------------|:--------------|---------:|:---------------|:-------------------------|:------------------|
|             99 |     091000022 |    7301097572 | Yes         | Jefferey       | %             |      100 | 01/01/2015     | 01/01/2000 to 12/31/2100 | No                |
2025-09-09 06:00:31,721 | INFO | -validating table: Direct Deposit Information
2025-09-09 06:00:31,721 | INFO | --figuring out table emptiness...
2025-09-09 06:00:58,406 | INFO | llm gpt-5-mini api call took 26.683 seconds
2025-09-09 06:00:58,425 | INFO | total input tokens: 17703
2025-09-09 06:00:58,425 | INFO | input text tokens: 16772 # estimated
2025-09-09 06:00:58,425 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:00:58,425 | INFO | cost for input: $0.022129 USD
2025-09-09 06:00:58,426 | INFO | total output tokens: 1607
2025-09-09 06:00:58,426 | INFO | cost of output: $0.01607 USD
2025-09-09 06:00:58,426 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:01:25,916 | INFO | llm gpt-5-mini api call took 27.490 seconds
2025-09-09 06:01:25,918 | INFO | total input tokens: 1624
2025-09-09 06:01:25,918 | INFO | input text tokens: 1616 # estimated
2025-09-09 06:01:25,919 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:01:25,919 | INFO | cost for input: $0.00203 USD
2025-09-09 06:01:25,919 | INFO | total output tokens: 3342
2025-09-09 06:01:25,919 | INFO | cost of output: $0.03342 USD
2025-09-09 06:01:25,919 | INFO | --got table grid emptiness info:
|Sequence No.|Transit No.|Account No.|Checking?|Account Name|Amount Code|Amount|Prenote Date|Effective Dates|Exclude Special|
|---|---|---|---|---|---|---|---|---|---|
|X|X|X|X|X|X|X|X|X|X|
2025-09-09 06:01:40,578 | INFO | llm gpt-5 api call took 14.658 seconds
2025-09-09 06:01:40,583 | INFO | total input tokens: 3464
2025-09-09 06:01:40,583 | INFO | input text tokens: 2826 # estimated
2025-09-09 06:01:40,583 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:01:40,583 | INFO | cost for input: $0.00433 USD
2025-09-09 06:01:40,583 | INFO | total output tokens: 424
2025-09-09 06:01:40,583 | INFO | cost of output: $0.00424 USD
2025-09-09 06:01:40,584 | INFO | done judging, ALL GOOD
2025-09-09 06:01:40,585 | INFO | -current table:
| ECode   | CalcCode   | Rate Code   |   Rate | Rate Per   |   Amount | Tabled?   |   Units | Frequency   | Goal/Paid/Goal Bal.   | Min/Max/Ann. Max   | Effective Dates          |
|:--------|:-----------|:------------|-------:|:-----------|---------:|:----------|--------:|:------------|:----------------------|:-------------------|:-------------------------|
| STD     |            |             |      0 |            |     6.21 | No        |       0 | B5          | 0.00/0.00/0.00        | 0.00/0.00/0.00     | 01/01/2018 to 12/31/2100 |
2025-09-09 06:01:40,585 | INFO | -validating table: Fringe Benefit Information
2025-09-09 06:01:40,585 | INFO | --figuring out table emptiness...
2025-09-09 06:02:56,149 | WARNING | Transient error (status=429) attempt 1/6; sleeping 13.00s before retry.
2025-09-09 06:03:32,214 | INFO | llm gpt-5-mini api call took 23.064 seconds
2025-09-09 06:03:32,231 | INFO | total input tokens: 17735
2025-09-09 06:03:32,231 | INFO | input text tokens: 16804 # estimated
2025-09-09 06:03:32,231 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:03:32,231 | INFO | cost for input: $0.022169 USD
2025-09-09 06:03:32,232 | INFO | total output tokens: 2233
2025-09-09 06:03:32,232 | INFO | cost of output: $0.02233 USD
2025-09-09 06:03:32,232 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:04:49,931 | INFO | llm gpt-5-mini api call took 77.699 seconds
2025-09-09 06:04:49,934 | INFO | total input tokens: 1762
2025-09-09 06:04:49,934 | INFO | input text tokens: 1754 # estimated
2025-09-09 06:04:49,934 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:04:49,934 | INFO | cost for input: $0.002203 USD
2025-09-09 06:04:49,934 | INFO | total output tokens: 5766
2025-09-09 06:04:49,934 | INFO | cost of output: $0.05766 USD
2025-09-09 06:04:49,934 | INFO | --got table grid emptiness info:
|ECode|CalcCode|Rate Code|Rate|Rate Per|Amount|Tabled?|Units|Frequency|Goal/Paid/Goal Bal.|Min/Max/Ann. Max|Effective Dates|
|X| | |X| |X|X|X|X|X|X|X|
2025-09-09 06:05:08,690 | INFO | llm gpt-5 api call took 18.755 seconds
2025-09-09 06:05:08,695 | INFO | total input tokens: 3488
2025-09-09 06:05:08,696 | INFO | input text tokens: 2850 # estimated
2025-09-09 06:05:08,696 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:05:08,696 | INFO | cost for input: $0.00436 USD
2025-09-09 06:05:08,696 | INFO | total output tokens: 616
2025-09-09 06:05:08,696 | INFO | cost of output: $0.00616 USD
2025-09-09 06:05:08,697 | INFO | done judging, ALL GOOD
2025-09-09 06:05:08,698 | INFO | -current table:
| BCode    |   Rate |   Amount |   Hours | Max/Carryover Max   | Length of Service   | Hours: Used/Avail/Total/Prob   | Dollars: Used/Avail/Total/Prob   | Effective Dates          |
|:---------|-------:|---------:|--------:|:--------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| PER      |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 01/01/2016 to 12/31/2100 |
| SICK     |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 01/01/2016 to 12/31/2100 |
| VAC-NEX8 |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 01/01/2016 to 12/31/2100 |
| VAC/CO   |      0 |        0 |       0 | 0.00/0.00           |                     | 32.52/0.00/0.00/0.00           | 579.83/0.00/0.00/0.00            | 01/01/2018 to 06/30/2018 |
2025-09-09 06:05:08,699 | INFO | -validating table: Benefit Accrual Information
2025-09-09 06:05:08,699 | INFO | --figuring out table emptiness...
2025-09-09 06:05:45,959 | INFO | llm gpt-5-mini api call took 37.258 seconds
2025-09-09 06:05:45,977 | INFO | total input tokens: 17975
2025-09-09 06:05:45,977 | INFO | input text tokens: 17044 # estimated
2025-09-09 06:05:45,977 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:05:45,978 | INFO | cost for input: $0.022469 USD
2025-09-09 06:05:45,978 | INFO | total output tokens: 3830
2025-09-09 06:05:45,978 | INFO | cost of output: $0.0383 USD
2025-09-09 06:05:45,978 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:07:00,649 | INFO | llm gpt-5-mini api call took 74.671 seconds
2025-09-09 06:07:00,653 | INFO | total input tokens: 2917
2025-09-09 06:07:00,654 | INFO | input text tokens: 2909 # estimated
2025-09-09 06:07:00,654 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:07:00,654 | INFO | cost for input: $0.003646 USD
2025-09-09 06:07:00,654 | INFO | total output tokens: 6356
2025-09-09 06:07:00,654 | INFO | cost of output: $0.06356 USD
2025-09-09 06:07:00,654 | INFO | --got table grid emptiness info:
|BCode|Rate|Amount|Hours|Max/Carryover Max|Length of Service|Hours: Used/Avail/Total/Prob|Dollars: Used/Avail/Total/Prob|Effective Dates|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
|X| |X|X|X| |X|X|X|
|X| |X|X|X| |X|X|X|
2025-09-09 06:07:29,785 | INFO | llm gpt-5 api call took 29.131 seconds
2025-09-09 06:07:29,791 | INFO | total input tokens: 3806
2025-09-09 06:07:29,791 | INFO | input text tokens: 3168 # estimated
2025-09-09 06:07:29,791 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:07:29,791 | INFO | cost for input: $0.004757 USD
2025-09-09 06:07:29,791 | INFO | total output tokens: 1192
2025-09-09 06:07:29,791 | INFO | cost of output: $0.01192 USD
2025-09-09 06:07:29,792 | INFO | done judging, ALL GOOD
2025-09-09 06:07:29,793 | INFO | -current table:

2025-09-09 06:07:29,793 | INFO | -validating table: Review Information
2025-09-09 06:07:29,793 | INFO | -current table:

2025-09-09 06:07:29,793 | INFO | -validating table: Emergency Contact Information
2025-09-09 06:07:29,794 | INFO | started validating form fields
2025-09-09 06:07:29,794 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-09 06:07:29,794 | INFO | --current are:
Company Name : Velorynt Labs
Company Code : 37546
Period : 12/17/2024 to 12/26/2024
Employee Name : Jeffrey Bennett
Address line 1 : 3407 French River
City : Juliemouth
State : ND
Zip : 55428
Emp Id : 2796
SSN : 795-56-8275
2025-09-09 06:07:50,351 | INFO | llm gpt-5 api call took 20.548 seconds
2025-09-09 06:07:50,357 | INFO | total input tokens: 4645
2025-09-09 06:07:50,357 | INFO | input text tokens: 4007 # estimated
2025-09-09 06:07:50,357 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:07:50,357 | INFO | cost for input: $0.005806 USD
2025-09-09 06:07:50,358 | INFO | total output tokens: 704
2025-09-09 06:07:50,358 | INFO | cost of output: $0.00704 USD
2025-09-09 06:07:50,358 | INFO | done judging, ALL GOOD
2025-09-09 06:07:50,358 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-09 06:07:50,358 | INFO | --current are:
DOB (only date) : 12/08/1980
Gender : M
Marital Status : M
Status : T
Position : 
Title : 
Pay Group : 
Job Code : 
Emp Type : RFT
Statutory : 0.00
2025-09-09 06:08:08,606 | INFO | llm gpt-5 api call took 18.239 seconds
2025-09-09 06:08:08,612 | INFO | total input tokens: 4613
2025-09-09 06:08:08,613 | INFO | input text tokens: 3975 # estimated
2025-09-09 06:08:08,613 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:08:08,613 | INFO | cost for input: $0.005766 USD
2025-09-09 06:08:08,613 | INFO | total output tokens: 770
2025-09-09 06:08:08,613 | INFO | cost of output: $0.0077 USD
2025-09-09 06:08:08,614 | INFO | done judging, ALL GOOD
2025-09-09 06:08:08,614 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-09 06:08:08,614 | INFO | --current are:
Seasonal : 0.00
Domestic Emp : No
Probation : 0.00
Home # : 373-146-1203
Work # : 
Ext. : 
Email : aaronbyrd@exple.net
Mail Stop : 
Hire Date : 02/04/2012
Rehire Date : 
2025-09-09 06:08:37,798 | INFO | llm gpt-5 api call took 29.176 seconds
2025-09-09 06:08:37,805 | INFO | total input tokens: 4629
2025-09-09 06:08:37,805 | INFO | input text tokens: 3991 # estimated
2025-09-09 06:08:37,805 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:08:37,805 | INFO | cost for input: $0.005786 USD
2025-09-09 06:08:37,805 | INFO | total output tokens: 1025
2025-09-09 06:08:37,805 | INFO | cost of output: $0.01025 USD
2025-09-09 06:08:37,806 | INFO | done judging, ALL GOOD
2025-09-09 06:08:37,806 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-09 06:08:37,806 | INFO | --current are:
Term Date : 08/31/2018
Term Reason : 
Adj Sen Date : 
Pension : No
Visa Type : 
Exp : 
Citizen : 
I9 Reverify : 
I9 Verified : No
Deceased : No
2025-09-09 06:08:55,546 | INFO | llm gpt-5 api call took 17.730 seconds
2025-09-09 06:08:55,552 | INFO | total input tokens: 4612
2025-09-09 06:08:55,552 | INFO | input text tokens: 3974 # estimated
2025-09-09 06:08:55,553 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:08:55,553 | INFO | cost for input: $0.005765 USD
2025-09-09 06:08:55,553 | INFO | total output tokens: 836
2025-09-09 06:08:55,553 | INFO | cost of output: $0.00836 USD
2025-09-09 06:08:55,553 | INFO | done judging, ALL GOOD
2025-09-09 06:08:55,554 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-09 06:08:55,554 | INFO | --current are:
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
2025-09-09 06:09:14,786 | INFO | llm gpt-5 api call took 19.224 seconds
2025-09-09 06:09:14,793 | INFO | total input tokens: 4614
2025-09-09 06:09:14,793 | INFO | input text tokens: 3976 # estimated
2025-09-09 06:09:14,793 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:09:14,793 | INFO | cost for input: $0.005768 USD
2025-09-09 06:09:14,793 | INFO | total output tokens: 967
2025-09-09 06:09:14,793 | INFO | cost of output: $0.00967 USD
2025-09-09 06:09:14,794 | INFO | done judging, ALL GOOD
2025-09-09 06:09:14,794 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 06:09:14,794 | INFO | --current are:
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
2025-09-09 06:10:22,694 | INFO | llm gpt-5 api call took 67.892 seconds
2025-09-09 06:10:22,701 | INFO | total input tokens: 4607
2025-09-09 06:10:22,701 | INFO | input text tokens: 3969 # estimated
2025-09-09 06:10:22,701 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:10:22,701 | INFO | cost for input: $0.005759 USD
2025-09-09 06:10:22,701 | INFO | total output tokens: 2154
2025-09-09 06:10:22,702 | INFO | cost of output: $0.02154 USD
2025-09-09 06:10:22,702 | INFO | --found issues: [{'data_name': 'surname', 'status': 'wrong', 'feedback': 'Value captured as the field label; the field appears empty in the image.'}, {'data_name': 'AutoPay', 'status': 'wrong', 'feedback': "No value shown for the AutoPay field in the image; do not use 'No AutoPay Information' section as the value."}]
2025-09-09 06:10:29,237 | INFO | llm gpt-5-mini api call took 6.535 seconds
2025-09-09 06:10:29,241 | INFO | total input tokens: 2722
2025-09-09 06:10:29,241 | INFO | input text tokens: 1791 # estimated
2025-09-09 06:10:29,241 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:10:29,241 | INFO | cost for input: $0.003403 USD
2025-09-09 06:10:29,241 | INFO | total output tokens: 573
2025-09-09 06:10:29,241 | INFO | cost of output: $0.00573 USD
2025-09-09 06:10:29,242 | INFO | --corrected as:
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
2025-09-09 06:10:29,242 | INFO | -revalidating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 06:11:06,361 | INFO | llm gpt-5 api call took 37.118 seconds
2025-09-09 06:11:06,367 | INFO | total input tokens: 4603
2025-09-09 06:11:06,368 | INFO | input text tokens: 3965 # estimated
2025-09-09 06:11:06,368 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:11:06,368 | INFO | cost for input: $0.005754 USD
2025-09-09 06:11:06,368 | INFO | total output tokens: 1345
2025-09-09 06:11:06,368 | INFO | cost of output: $0.01345 USD
2025-09-09 06:11:06,369 | INFO | done judging, ALL GOOD
2025-09-09 06:11:06,369 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-09 06:11:06,369 | INFO | --current are:
Default Hours : 0.00
Locations : 605
Positions : 700
2025-09-09 06:11:29,488 | INFO | llm gpt-5 api call took 23.109 seconds
2025-09-09 06:11:29,494 | INFO | total input tokens: 4582
2025-09-09 06:11:29,495 | INFO | input text tokens: 3944 # estimated
2025-09-09 06:11:29,495 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:11:29,495 | INFO | cost for input: $0.00256 USD
2025-09-09 06:11:29,495 | INFO | total output tokens: 785
2025-09-09 06:11:29,495 | INFO | cost of output: $0.00785 USD
2025-09-09 06:11:29,496 | INFO | done judging, ALL GOOD

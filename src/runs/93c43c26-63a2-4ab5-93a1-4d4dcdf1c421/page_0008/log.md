2025-09-08 21:59:04,255 | INFO | started initial extraction for page 8
2025-09-08 22:00:34,365 | INFO | llm gpt-5 api call took 89.409 seconds
2025-09-08 22:00:35,056 | INFO | total input tokens: 3058
2025-09-08 22:00:35,057 | INFO | input text tokens: 2420 # estimated
2025-09-08 22:00:35,058 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:00:35,059 | INFO | cost for input: $0.003822 USD
2025-09-08 22:00:35,060 | INFO | total output tokens: 3477
2025-09-08 22:00:35,060 | INFO | cost of output: $0.03477 USD
2025-09-08 22:00:35,062 | INFO | initial extraction of page data done.
2025-09-08 22:00:44,046 | INFO | got response with OCR coordinates info from azure doc intelligence for page 8
2025-09-08 22:00:44,047 | INFO | started validating tables
2025-09-08 22:00:44,077 | INFO | -current table:
| RateCode   | Description   |   Rate | Salary   | Effective Dates          |
|:-----------|:--------------|-------:|:---------|:-------------------------|
| Base       | Base Rate     |  13.25 |          | 11/25/2018 to 12/31/2100 |
| Base       | Base Rate     |  13    |          | 08/07/2017 to 11/24/2018 |
| Base       | Base Rate     |  12    |          | 06/16/2017 to 08/06/2017 |
2025-09-08 22:00:44,077 | INFO | -validating table: Rate/Salary Information
2025-09-08 22:00:44,078 | INFO | --figuring out table emptiness...
2025-09-08 22:01:26,052 | INFO | llm gpt-5-mini api call took 41.972 seconds
2025-09-08 22:01:26,071 | INFO | total input tokens: 17874
2025-09-08 22:01:26,072 | INFO | input text tokens: 16943 # estimated
2025-09-08 22:01:26,073 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 22:01:26,074 | INFO | cost for input: $0.022343 USD
2025-09-08 22:01:26,075 | INFO | total output tokens: 4209
2025-09-08 22:01:26,076 | INFO | cost of output: $0.04209 USD
2025-09-08 22:01:26,076 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 22:02:31,499 | INFO | llm gpt-5-mini api call took 65.422 seconds
2025-09-08 22:02:31,503 | INFO | total input tokens: 2096
2025-09-08 22:02:31,503 | INFO | input text tokens: 2088 # estimated
2025-09-08 22:02:31,504 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 22:02:31,504 | INFO | cost for input: $0.00262 USD
2025-09-08 22:02:31,505 | INFO | total output tokens: 3710
2025-09-08 22:02:31,507 | INFO | cost of output: $0.0371 USD
2025-09-08 22:02:31,508 | INFO | --got table grid emptiness info:
|RateCode|Description|Rate|Salary|Effective Dates|
|---:|---:|---:|---:|---:|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
2025-09-08 22:02:57,624 | INFO | llm gpt-5 api call took 26.116 seconds
2025-09-08 22:02:57,630 | INFO | total input tokens: 3492
2025-09-08 22:02:57,631 | INFO | input text tokens: 2854 # estimated
2025-09-08 22:02:57,631 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:02:57,632 | INFO | cost for input: $0.004365 USD
2025-09-08 22:02:57,633 | INFO | total output tokens: 744
2025-09-08 22:02:57,634 | INFO | cost of output: $0.00744 USD
2025-09-08 22:02:57,635 | INFO | done judging, ALL GOOD
2025-09-08 22:02:57,637 | INFO | -current table:
| Employee Tax (code description)   | Status   |   Add'l Amount | Effective Dates          | Default   |
|:----------------------------------|:---------|---------------:|:-------------------------|:----------|
| MED Medicare                      |          |              0 | 06/16/2017 to 12/31/2100 | Yes       |
| SS OASDI                          |          |              0 | 06/16/2017 to 12/31/2100 | Yes       |
| FITW Federal Income Tax           | S-1      |              0 | 06/16/2017 to 12/31/2100 | Yes       |
| MN Minnesota SITW                 | S-1      |              0 | 06/16/2017 to 12/31/2100 | Yes       |
2025-09-08 22:02:57,637 | INFO | -validating table: Tax Information (Employee)
2025-09-08 22:02:57,638 | INFO | --figuring out table emptiness...
2025-09-08 22:03:21,845 | INFO | llm gpt-5-mini api call took 24.204 seconds
2025-09-08 22:03:21,864 | INFO | total input tokens: 17920
2025-09-08 22:03:21,865 | INFO | input text tokens: 16989 # estimated
2025-09-08 22:03:21,865 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 22:03:21,866 | INFO | cost for input: $0.0224 USD
2025-09-08 22:03:21,866 | INFO | total output tokens: 2813
2025-09-08 22:03:21,867 | INFO | cost of output: $0.02813 USD
2025-09-08 22:03:21,868 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 22:04:19,378 | INFO | llm gpt-5-mini api call took 57.510 seconds
2025-09-08 22:04:19,382 | INFO | total input tokens: 2310
2025-09-08 22:04:19,383 | INFO | input text tokens: 2302 # estimated
2025-09-08 22:04:19,384 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 22:04:19,385 | INFO | cost for input: $0.002887 USD
2025-09-08 22:04:19,386 | INFO | total output tokens: 2582
2025-09-08 22:04:19,387 | INFO | cost of output: $0.02582 USD
2025-09-08 22:04:19,388 | INFO | --got table grid emptiness info:
|Employee Tax (code description)|Status|Add'l Amount|Effective Dates|Default|
|---:|:---:|:---:|:---:|:---:|
|X| |X|X|X|
|X| |X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
2025-09-08 22:04:38,136 | INFO | llm gpt-5 api call took 18.746 seconds
2025-09-08 22:04:38,143 | INFO | total input tokens: 3563
2025-09-08 22:04:38,144 | INFO | input text tokens: 2925 # estimated
2025-09-08 22:04:38,144 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:04:38,145 | INFO | cost for input: $0.004454 USD
2025-09-08 22:04:38,146 | INFO | total output tokens: 808
2025-09-08 22:04:38,146 | INFO | cost of output: $0.00808 USD
2025-09-08 22:04:38,147 | INFO | done judging, ALL GOOD
2025-09-08 22:04:38,150 | INFO | -current table:
| Employer Tax (code description)         | Effective Dates          | Default   |
|:----------------------------------------|:-------------------------|:----------|
| MED-R Medicare - Employer               | 06/16/2017 to 12/31/2100 |           |
| SS-R OASDI - Employer                   | 06/16/2017 to 12/31/2100 |           |
| FUTA Fed Unemployment                   | 06/16/2017 to 12/31/2100 |           |
| MNAST Minnesota Federal Loan Assessment | 06/16/2017 to 12/31/2100 |           |
| MNDW Workforce Enhancement Fee          | 06/16/2017 to 12/31/2100 |           |
| MNSUI Minnesota SUI                     | 06/16/2017 to 12/31/2100 |           |
2025-09-08 22:04:38,150 | INFO | -validating table: Tax Information (Employer)
2025-09-08 22:04:38,151 | INFO | --figuring out table emptiness...
2025-09-08 22:05:37,067 | INFO | llm gpt-5-mini api call took 58.914 seconds
2025-09-08 22:05:37,086 | INFO | total input tokens: 17934
2025-09-08 22:05:37,087 | INFO | input text tokens: 17003 # estimated
2025-09-08 22:05:37,088 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 22:05:37,088 | INFO | cost for input: $0.022417 USD
2025-09-08 22:05:37,089 | INFO | total output tokens: 3834
2025-09-08 22:05:37,090 | INFO | cost of output: $0.03834 USD
2025-09-08 22:05:37,091 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 22:06:31,993 | INFO | llm gpt-5-mini api call took 54.901 seconds
2025-09-08 22:06:31,996 | INFO | total input tokens: 1719
2025-09-08 22:06:31,997 | INFO | input text tokens: 1711 # estimated
2025-09-08 22:06:31,998 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 22:06:31,999 | INFO | cost for input: $0.002149 USD
2025-09-08 22:06:31,999 | INFO | total output tokens: 3069
2025-09-08 22:06:32,000 | INFO | cost of output: $0.03069 USD
2025-09-08 22:06:32,000 | INFO | --got table grid emptiness info:
|Employer Tax (code description)|Effective Dates|Default|
|---|---|---|
|X|X| |
|X|X| |
|X|X| |
|X|X| |
|X|X| |
|X|X| |
2025-09-08 22:07:01,481 | INFO | llm gpt-5 api call took 29.480 seconds
2025-09-08 22:07:01,487 | INFO | total input tokens: 3552
2025-09-08 22:07:01,488 | INFO | input text tokens: 2914 # estimated
2025-09-08 22:07:01,488 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:07:01,489 | INFO | cost for input: $0.00444 USD
2025-09-08 22:07:01,490 | INFO | total output tokens: 936
2025-09-08 22:07:01,491 | INFO | cost of output: $0.00936 USD
2025-09-08 22:07:01,492 | INFO | done judging, ALL GOOD
2025-09-08 22:07:01,494 | INFO | -current table:
| Code   | Deduction             |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-------|:----------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| 401KC  | 401K Contribution     |    1   | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/08/2017 to 04/14/2019 |
| DNTL   | Dental Insurance S125 |   15.1 | B5         |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2017 to 04/14/2019 |
| FH125  | Health Insurance S125 |   78.9 | B5         |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2017 to 04/14/2019 |
2025-09-08 22:07:01,495 | INFO | -validating table: Deduction Information
2025-09-08 22:07:01,496 | INFO | --figuring out table emptiness...
2025-09-08 22:07:45,702 | INFO | llm gpt-5-mini api call took 44.203 seconds
2025-09-08 22:07:45,721 | INFO | total input tokens: 18028
2025-09-08 22:07:45,722 | INFO | input text tokens: 17097 # estimated
2025-09-08 22:07:45,722 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 22:07:45,723 | INFO | cost for input: $0.022535 USD
2025-09-08 22:07:45,724 | INFO | total output tokens: 3651
2025-09-08 22:07:45,724 | INFO | cost of output: $0.03651 USD
2025-09-08 22:07:45,725 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 22:08:53,353 | INFO | llm gpt-5-mini api call took 67.626 seconds
2025-09-08 22:08:53,357 | INFO | total input tokens: 3049
2025-09-08 22:08:53,358 | INFO | input text tokens: 3041 # estimated
2025-09-08 22:08:53,359 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 22:08:53,360 | INFO | cost for input: $0.003811 USD
2025-09-08 22:08:53,360 | INFO | total output tokens: 4783
2025-09-08 22:08:53,362 | INFO | cost of output: $0.04783 USD
2025-09-08 22:08:53,362 | INFO | --got table grid emptiness info:
|Code|Deduction|Rate|CalcCode|Frequency|Goal/Paid|Min/Max/Annual Max|Arrears|Agency|Effective Dates|
|---|---|---|---|---|---|---|---|---|---|
|X|X|X|X||X|X|X||X|
|X|X|X||X|X|X|X||X|
|X|X|X||X|X|X|X||X|
2025-09-08 22:10:07,865 | INFO | llm gpt-5 api call took 74.501 seconds
2025-09-08 22:10:07,871 | INFO | total input tokens: 3695
2025-09-08 22:10:07,872 | INFO | input text tokens: 3057 # estimated
2025-09-08 22:10:07,872 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:10:07,873 | INFO | cost for input: $0.004619 USD
2025-09-08 22:10:07,874 | INFO | total output tokens: 2703
2025-09-08 22:10:07,875 | INFO | cost of output: $0.02703 USD
2025-09-08 22:10:07,876 | INFO | --found issues: [{'row': '2,3', 'column': 'CalcCode', 'status': 'wrong', 'feedback': "Should be blank; 'B5' is positioned under Frequency in the image."}, {'row': '2,3', 'column': 'Frequency', 'status': 'wrong', 'feedback': "Value 'B5' is present in this column in the image but was left blank and placed under CalcCode."}]
2025-09-08 22:10:20,575 | INFO | llm gpt-5-mini api call took 12.698 seconds
2025-09-08 22:10:20,581 | INFO | total input tokens: 3059
2025-09-08 22:10:20,581 | INFO | input text tokens: 2128 # estimated
2025-09-08 22:10:20,582 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 22:10:20,584 | INFO | cost for input: $0.003824 USD
2025-09-08 22:10:20,585 | INFO | total output tokens: 1153
2025-09-08 22:10:20,585 | INFO | cost of output: $0.01153 USD
2025-09-08 22:10:20,588 | INFO | --corrected as:
| Code   | Deduction             |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-------|:----------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| 401KC  | 401K Contribution     |    1   | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/08/2017 to 04/14/2019 |
| DNTL   | Dental Insurance S125 |   15.1 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2017 to 04/14/2019 |
| FH125  | Health Insurance S125 |   78.9 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2017 to 04/14/2019 |
2025-09-08 22:10:20,589 | INFO | -revalidating table: Deduction Information
2025-09-08 22:11:01,184 | INFO | llm gpt-5 api call took 40.593 seconds
2025-09-08 22:11:01,191 | INFO | total input tokens: 3695
2025-09-08 22:11:01,192 | INFO | input text tokens: 3057 # estimated
2025-09-08 22:11:01,192 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:11:01,193 | INFO | cost for input: $0.004619 USD
2025-09-08 22:11:01,194 | INFO | total output tokens: 1000
2025-09-08 22:11:01,194 | INFO | cost of output: $0.01 USD
2025-09-08 22:11:01,195 | INFO | done judging, ALL GOOD
2025-09-08 22:11:01,197 | INFO | -current table:
|   Sequence No. |   Transit No. |   Account No. | Checking?   | Account Name   | Amount Code   |   Amount | Prenote Date   | Effective Dates          | Exclude Special   |
|---------------:|--------------:|--------------:|:------------|:---------------|:--------------|---------:|:---------------|:-------------------------|:------------------|
|             99 |     291070001 |    8224461774 | Yes         | Patricia, Paul | %             |      100 | 06/30/2017     | 06/30/2017 to 12/31/2100 | No                |
2025-09-08 22:11:01,198 | INFO | -validating table: Direct Deposit Information
2025-09-08 22:11:01,199 | INFO | --figuring out table emptiness...
2025-09-08 22:11:26,520 | INFO | llm gpt-5-mini api call took 25.318 seconds
2025-09-08 22:11:26,540 | INFO | total input tokens: 17882
2025-09-08 22:11:26,541 | INFO | input text tokens: 16951 # estimated
2025-09-08 22:11:26,541 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 22:11:26,542 | INFO | cost for input: $0.022353 USD
2025-09-08 22:11:26,543 | INFO | total output tokens: 1694
2025-09-08 22:11:26,544 | INFO | cost of output: $0.01694 USD
2025-09-08 22:11:26,546 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 22:12:41,364 | INFO | llm gpt-5-mini api call took 74.816 seconds
2025-09-08 22:12:41,367 | INFO | total input tokens: 1470
2025-09-08 22:12:41,368 | INFO | input text tokens: 1462 # estimated
2025-09-08 22:12:41,368 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 22:12:41,369 | INFO | cost for input: $0.001837 USD
2025-09-08 22:12:41,370 | INFO | total output tokens: 3352
2025-09-08 22:12:41,371 | INFO | cost of output: $0.03352 USD
2025-09-08 22:12:41,371 | INFO | --got table grid emptiness info:
|Sequence No.|Transit No.|Account No.|Checking?|Account Name|Amount Code|Amount|Prenote Date|Effective Dates|Exclude Special|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X|X|X|X|X|X|
2025-09-08 22:12:56,994 | INFO | llm gpt-5 api call took 15.622 seconds
2025-09-08 22:12:57,001 | INFO | total input tokens: 3526
2025-09-08 22:12:57,002 | INFO | input text tokens: 2888 # estimated
2025-09-08 22:12:57,005 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:12:57,006 | INFO | cost for input: $0.004407 USD
2025-09-08 22:12:57,007 | INFO | total output tokens: 488
2025-09-08 22:12:57,008 | INFO | cost of output: $0.00488 USD
2025-09-08 22:12:57,009 | INFO | done judging, ALL GOOD
2025-09-08 22:12:57,022 | INFO | -current table:

2025-09-08 22:12:57,023 | INFO | -validating table: Fringe Benefit Information
2025-09-08 22:12:57,025 | INFO | -current table:
| BCode    |   Rate |   Amount |   Hours | Max/Carryover Max   | Length of Service   | Hours: Used/Avail/Total/Prob   | Dollars: Used/Avail/Total/Prob   | Effective Dates          |
|:---------|-------:|---------:|--------:|:--------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| PER      |      0 |        0 |       0 | 0.00/0.00           |                     | 14.00/0.00/0.00/0.00           | 185.50/0.00/0.00/0.00            | 09/01/2017 to 04/13/2019 |
| SICK     |      0 |        0 |       0 | 0.00/0.00           |                     | 35.00/0.00/0.00/0.00           | 318.00/145.75/0.00/0.00          | 09/01/2017 to 04/13/2019 |
| VAC-NEX7 |      0 |        0 |       0 | 0.00/0.00           |                     | 18.83/0.00/0.00/0.00           | 0.00/249.50/0.00/0.00            | 10/05/2018 to 04/13/2019 |
| VAC-NEX8 |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 481.00/40.04/0.00/0.00           | 09/22/2017 to 10/05/2018 |
| VAC/CO   |      0 |        0 |       0 | 0.00/0.00           |                     | 0.96/0.00/0.00/0.00            | 0.00/12.72/0.00/0.00             | 01/01/2018 to 04/13/2019 |
2025-09-08 22:12:57,026 | INFO | -validating table: Benefit Accrual Information
2025-09-08 22:12:57,027 | INFO | --figuring out table emptiness...
2025-09-08 22:14:16,854 | INFO | llm gpt-5-mini api call took 79.825 seconds
2025-09-08 22:14:16,876 | INFO | total input tokens: 18237
2025-09-08 22:14:16,876 | INFO | input text tokens: 17306 # estimated
2025-09-08 22:14:16,877 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 22:14:16,878 | INFO | cost for input: $0.022796 USD
2025-09-08 22:14:16,879 | INFO | total output tokens: 6263
2025-09-08 22:14:16,879 | INFO | cost of output: $0.06263 USD
2025-09-08 22:14:16,881 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 22:15:04,944 | INFO | llm gpt-5-mini api call took 48.063 seconds
2025-09-08 22:15:04,949 | INFO | total input tokens: 3189
2025-09-08 22:15:04,950 | INFO | input text tokens: 3181 # estimated
2025-09-08 22:15:04,950 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 22:15:04,951 | INFO | cost for input: $0.003986 USD
2025-09-08 22:15:04,952 | INFO | total output tokens: 5475
2025-09-08 22:15:04,953 | INFO | cost of output: $0.05475 USD
2025-09-08 22:15:04,954 | INFO | --got table grid emptiness info:
|BCode|Rate|Amount|Hours|Max/Carryover Max|Length of Service|Hours: Used/Avail/Total/Prob|Dollars: Used/Avail/Total/Prob|Effective Dates|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X||X|X|X|
|X|X|X|X|X||X|X|X|
|X|X|X|X|X||X|X|X|
|X|X|X|X|X||X|X|X|
|X|X|X|X|X||X|X|X|
2025-09-08 22:15:33,013 | INFO | llm gpt-5 api call took 28.057 seconds
2025-09-08 22:15:33,021 | INFO | total input tokens: 3956
2025-09-08 22:15:33,022 | INFO | input text tokens: 3318 # estimated
2025-09-08 22:15:33,022 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:15:33,023 | INFO | cost for input: $0.004945 USD
2025-09-08 22:15:33,024 | INFO | total output tokens: 1064
2025-09-08 22:15:33,024 | INFO | cost of output: $0.01064 USD
2025-09-08 22:15:33,025 | INFO | done judging, ALL GOOD
2025-09-08 22:15:33,027 | INFO | -current table:

2025-09-08 22:15:33,028 | INFO | -validating table: Review Information
2025-09-08 22:15:33,030 | INFO | -current table:

2025-09-08 22:15:33,031 | INFO | -validating table: Emergency Contact Information
2025-09-08 22:15:33,032 | INFO | started validating form fields
2025-09-08 22:15:33,032 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-08 22:15:33,033 | INFO | --current are:
Company Name : Velorynt Labs
Company Code : 37546
Period : 12/17/2024 to 12/26/2024
Employee Name : Patricia Paul
Address line 1 : 515 Brittany Forks
City : Savannah
State : GA
Zip : 59966
Emp Id : 3602
SSN : 145-16-8120
2025-09-08 22:16:02,216 | INFO | llm gpt-5 api call took 29.173 seconds
2025-09-08 22:16:02,223 | INFO | total input tokens: 4714
2025-09-08 22:16:02,224 | INFO | input text tokens: 4076 # estimated
2025-09-08 22:16:02,224 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:16:02,225 | INFO | cost for input: $0.005893 USD
2025-09-08 22:16:02,226 | INFO | total output tokens: 704
2025-09-08 22:16:02,227 | INFO | cost of output: $0.00704 USD
2025-09-08 22:16:02,227 | INFO | done judging, ALL GOOD
2025-09-08 22:16:02,228 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-08 22:16:02,229 | INFO | --current are:
DOB (only date) : 11/26/1967
Gender : F
Marital Status : S
Status : T
Position : 
Title : 
Pay Group : 
Job Code : 
Emp Type : RPT
Statutory : 0.00
2025-09-08 22:16:19,545 | INFO | llm gpt-5 api call took 17.307 seconds
2025-09-08 22:16:19,553 | INFO | total input tokens: 4682
2025-09-08 22:16:19,554 | INFO | input text tokens: 4044 # estimated
2025-09-08 22:16:19,555 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:16:19,555 | INFO | cost for input: $0.002684 USD
2025-09-08 22:16:19,556 | INFO | total output tokens: 834
2025-09-08 22:16:19,557 | INFO | cost of output: $0.00834 USD
2025-09-08 22:16:19,558 | INFO | done judging, ALL GOOD
2025-09-08 22:16:19,559 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-08 22:16:19,560 | INFO | --current are:
Seasonal : 0.00
Domestic Emp : No
Probation : 0.00
Home # : 
Work # : 
Ext. : 
Email : Emailxhines@yahoo.com
Mail Stop : 
Hire Date : 06/07/2017
Rehire Date : 
2025-09-08 22:17:06,542 | INFO | llm gpt-5 api call took 46.973 seconds
2025-09-08 22:17:06,550 | INFO | total input tokens: 4689
2025-09-08 22:17:06,550 | INFO | input text tokens: 4051 # estimated
2025-09-08 22:17:06,551 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:17:06,551 | INFO | cost for input: $0.002693 USD
2025-09-08 22:17:06,552 | INFO | total output tokens: 1166
2025-09-08 22:17:06,553 | INFO | cost of output: $0.01166 USD
2025-09-08 22:17:06,554 | INFO | --found issues: [{'data_name': 'Email', 'status': 'wrong', 'feedback': 'Contains field label; value should be xhines@yahoo.com'}]
2025-09-08 22:17:13,903 | INFO | llm gpt-5-mini api call took 7.349 seconds
2025-09-08 22:17:13,908 | INFO | total input tokens: 2757
2025-09-08 22:17:13,909 | INFO | input text tokens: 1826 # estimated
2025-09-08 22:17:13,910 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 22:17:13,910 | INFO | cost for input: $0.003446 USD
2025-09-08 22:17:13,911 | INFO | total output tokens: 394
2025-09-08 22:17:13,912 | INFO | cost of output: $0.00394 USD
2025-09-08 22:17:13,913 | INFO | --corrected as:
Seasonal : 0.00
Domestic Emp : No
Probation : 0.00
Home # : 
Work # : 
Ext. : 
Email : xhines@yahoo.com
Mail Stop : 
Hire Date : 06/07/2017
Rehire Date : 
2025-09-08 22:17:13,914 | INFO | -revalidating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-08 22:17:46,043 | INFO | llm gpt-5 api call took 32.127 seconds
2025-09-08 22:17:46,051 | INFO | total input tokens: 4688
2025-09-08 22:17:46,052 | INFO | input text tokens: 4050 # estimated
2025-09-08 22:17:46,052 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:17:46,053 | INFO | cost for input: $0.000964 USD
2025-09-08 22:17:46,053 | INFO | total output tokens: 897
2025-09-08 22:17:46,054 | INFO | cost of output: $0.00897 USD
2025-09-08 22:17:46,055 | INFO | done judging, ALL GOOD
2025-09-08 22:17:46,055 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-08 22:17:46,056 | INFO | --current are:
Term Date : 12/21/2020
Term Reason : N/A
Adj Sen Date : 
Pension : No
Visa Type : 
Exp : 
Citizen : 
I9 Reverify : 
I9 Verified : Yes
Deceased : No
2025-09-08 22:18:20,676 | INFO | llm gpt-5 api call took 34.611 seconds
2025-09-08 22:18:20,684 | INFO | total input tokens: 4683
2025-09-08 22:18:20,685 | INFO | input text tokens: 4045 # estimated
2025-09-08 22:18:20,685 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:18:20,686 | INFO | cost for input: $0.005854 USD
2025-09-08 22:18:20,687 | INFO | total output tokens: 644
2025-09-08 22:18:20,687 | INFO | cost of output: $0.00644 USD
2025-09-08 22:18:20,688 | INFO | done judging, ALL GOOD
2025-09-08 22:18:20,688 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-08 22:18:20,689 | INFO | --current are:
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
2025-09-08 22:19:04,540 | INFO | llm gpt-5 api call took 43.843 seconds
2025-09-08 22:19:04,547 | INFO | total input tokens: 4683
2025-09-08 22:19:04,548 | INFO | input text tokens: 4045 # estimated
2025-09-08 22:19:04,549 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:19:04,549 | INFO | cost for input: $0.005854 USD
2025-09-08 22:19:04,550 | INFO | total output tokens: 903
2025-09-08 22:19:04,551 | INFO | cost of output: $0.00903 USD
2025-09-08 22:19:04,551 | INFO | done judging, ALL GOOD
2025-09-08 22:19:04,552 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-08 22:19:04,553 | INFO | --current are:
Veteran : 
Legal Rep : No
Nickname : 
surname : 
Prior Last : 
Disability : 
Smoker : No
AutoPay : No
Pay Frequency : B
OT Exempt : No
2025-09-08 22:20:23,575 | INFO | llm gpt-5 api call took 79.013 seconds
2025-09-08 22:20:23,583 | INFO | total input tokens: 4674
2025-09-08 22:20:23,584 | INFO | input text tokens: 4036 # estimated
2025-09-08 22:20:23,585 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:20:23,586 | INFO | cost for input: $0.000946 USD
2025-09-08 22:20:23,586 | INFO | total output tokens: 2136
2025-09-08 22:20:23,587 | INFO | cost of output: $0.02136 USD
2025-09-08 22:20:23,588 | INFO | --found issues: [{'data_name': 'AutoPay', 'status': 'wrong', 'feedback': "AutoPay appears as a header in Rate/Salary Information with no value shown; 'No' is not present."}]
2025-09-08 22:20:29,655 | INFO | llm gpt-5-mini api call took 6.066 seconds
2025-09-08 22:20:29,660 | INFO | total input tokens: 2753
2025-09-08 22:20:29,661 | INFO | input text tokens: 1822 # estimated
2025-09-08 22:20:29,662 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 22:20:29,662 | INFO | cost for input: $0.003441 USD
2025-09-08 22:20:29,663 | INFO | total output tokens: 381
2025-09-08 22:20:29,663 | INFO | cost of output: $0.00381 USD
2025-09-08 22:20:29,664 | INFO | --corrected as:
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
2025-09-08 22:20:29,665 | INFO | -revalidating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-08 22:21:13,559 | INFO | llm gpt-5 api call took 43.893 seconds
2025-09-08 22:21:13,567 | INFO | total input tokens: 4672
2025-09-08 22:21:13,568 | INFO | input text tokens: 4034 # estimated
2025-09-08 22:21:13,570 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:21:13,572 | INFO | cost for input: $0.00584 USD
2025-09-08 22:21:13,572 | INFO | total output tokens: 1665
2025-09-08 22:21:13,573 | INFO | cost of output: $0.01665 USD
2025-09-08 22:21:13,574 | INFO | done judging, ALL GOOD
2025-09-08 22:21:13,575 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-08 22:21:13,576 | INFO | --current are:
Default Hours : 0.00
Locations : 606
Positions : 700
2025-09-08 22:21:34,538 | INFO | llm gpt-5 api call took 20.950 seconds
2025-09-08 22:21:34,545 | INFO | total input tokens: 4651
2025-09-08 22:21:34,546 | INFO | input text tokens: 4013 # estimated
2025-09-08 22:21:34,546 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 22:21:34,547 | INFO | cost for input: $0.005814 USD
2025-09-08 22:21:34,548 | INFO | total output tokens: 721
2025-09-08 22:21:34,548 | INFO | cost of output: $0.00721 USD
2025-09-08 22:21:34,550 | INFO | done judging, ALL GOOD

2025-09-09 07:20:46,070 | INFO | started initial extraction for page 8
2025-09-09 07:22:17,482 | INFO | llm gpt-5 api call took 91.063 seconds
2025-09-09 07:22:18,214 | INFO | total input tokens: 3058
2025-09-09 07:22:18,216 | INFO | input text tokens: 2420 # estimated
2025-09-09 07:22:18,217 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:22:18,218 | INFO | cost for input: $0.003822 USD
2025-09-09 07:22:18,218 | INFO | total output tokens: 3351
2025-09-09 07:22:18,219 | INFO | cost of output: $0.03351 USD
2025-09-09 07:22:18,221 | INFO | initial extraction of page data done.
2025-09-09 07:22:26,209 | INFO | got response with OCR coordinates info from azure doc intelligence for page 8
2025-09-09 07:22:26,211 | INFO | started validating tables
2025-09-09 07:22:26,220 | INFO | -current table:
| RateCode   | Description   |   Rate | Salary   | Effective Dates          |
|:-----------|:--------------|-------:|:---------|:-------------------------|
| Base       | Base Rate     |  13.25 |          | 11/25/2018 to 12/31/2100 |
| Base       | Base Rate     |  13    |          | 08/07/2017 to 11/24/2018 |
| Base       | Base Rate     |  12    |          | 06/16/2017 to 08/06/2017 |
2025-09-09 07:22:26,221 | INFO | -validating table: Rate/Salary Information
2025-09-09 07:22:26,222 | INFO | --figuring out table emptiness...
2025-09-09 07:23:14,436 | INFO | llm gpt-5-mini api call took 48.211 seconds
2025-09-09 07:23:14,456 | INFO | total input tokens: 17874
2025-09-09 07:23:14,457 | INFO | input text tokens: 16943 # estimated
2025-09-09 07:23:14,458 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:23:14,458 | INFO | cost for input: $0.022343 USD
2025-09-09 07:23:14,459 | INFO | total output tokens: 4145
2025-09-09 07:23:14,460 | INFO | cost of output: $0.04145 USD
2025-09-09 07:23:14,461 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:24:02,174 | INFO | llm gpt-5-mini api call took 47.712 seconds
2025-09-09 07:24:02,178 | INFO | total input tokens: 2209
2025-09-09 07:24:02,179 | INFO | input text tokens: 2201 # estimated
2025-09-09 07:24:02,180 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:24:02,180 | INFO | cost for input: $0.002761 USD
2025-09-09 07:24:02,181 | INFO | total output tokens: 3577
2025-09-09 07:24:02,182 | INFO | cost of output: $0.03577 USD
2025-09-09 07:24:02,183 | INFO | --got table grid emptiness info:
|RateCode|Description|Rate|Salary|Effective Dates|
|---|---|---|---|---|
|X|X|X||X|
|X|X|X||X|
|X|X|X||X|
2025-09-09 07:24:19,391 | INFO | llm gpt-5 api call took 17.207 seconds
2025-09-09 07:24:19,397 | INFO | total input tokens: 3487
2025-09-09 07:24:19,398 | INFO | input text tokens: 2849 # estimated
2025-09-09 07:24:19,400 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:24:19,401 | INFO | cost for input: $0.004359 USD
2025-09-09 07:24:19,401 | INFO | total output tokens: 552
2025-09-09 07:24:19,402 | INFO | cost of output: $0.00552 USD
2025-09-09 07:24:19,404 | INFO | done judging, ALL GOOD
2025-09-09 07:24:19,407 | INFO | -current table:
| Employee Tax (code description)   | Status   |   Add'l Amount | Effective Dates          | Default   |
|:----------------------------------|:---------|---------------:|:-------------------------|:----------|
| MED Medicare                      |          |              0 | 06/16/2017 to 12/31/2100 | Yes       |
| SS OASDI                          |          |              0 | 06/16/2017 to 12/31/2100 | Yes       |
| FITW Federal Income Tax           | S-1      |              0 | 06/16/2017 to 12/31/2100 | Yes       |
| MN Minnesota SITW                 | S-1      |              0 | 06/16/2017 to 12/31/2100 | Yes       |
2025-09-09 07:24:19,408 | INFO | -validating table: Tax Information (Employee)
2025-09-09 07:24:19,409 | INFO | --figuring out table emptiness...
2025-09-09 07:25:08,523 | INFO | llm gpt-5-mini api call took 49.111 seconds
2025-09-09 07:25:08,542 | INFO | total input tokens: 17920
2025-09-09 07:25:08,543 | INFO | input text tokens: 16989 # estimated
2025-09-09 07:25:08,543 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:25:08,544 | INFO | cost for input: $0.0224 USD
2025-09-09 07:25:08,545 | INFO | total output tokens: 3441
2025-09-09 07:25:08,546 | INFO | cost of output: $0.03441 USD
2025-09-09 07:25:08,547 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:26:08,165 | INFO | llm gpt-5-mini api call took 59.617 seconds
2025-09-09 07:26:08,170 | INFO | total input tokens: 2859
2025-09-09 07:26:08,171 | INFO | input text tokens: 2851 # estimated
2025-09-09 07:26:08,172 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:26:08,174 | INFO | cost for input: $0.003574 USD
2025-09-09 07:26:08,175 | INFO | total output tokens: 4564
2025-09-09 07:26:08,176 | INFO | cost of output: $0.04564 USD
2025-09-09 07:26:08,177 | INFO | --got table grid emptiness info:
|Employee Tax (code description)|Status|Add'l Amount|Effective Dates|Default|
|---:|:---:|:---:|:---:|:---:|
|X||X|X|X|
|X||X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
2025-09-09 07:26:27,028 | INFO | llm gpt-5 api call took 18.850 seconds
2025-09-09 07:26:27,036 | INFO | total input tokens: 3561
2025-09-09 07:26:27,037 | INFO | input text tokens: 2923 # estimated
2025-09-09 07:26:27,038 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:26:27,040 | INFO | cost for input: $0.004451 USD
2025-09-09 07:26:27,040 | INFO | total output tokens: 552
2025-09-09 07:26:27,042 | INFO | cost of output: $0.00552 USD
2025-09-09 07:26:27,043 | INFO | done judging, ALL GOOD
2025-09-09 07:26:27,046 | INFO | -current table:
| Employer Tax (code description)         | Effective Dates          | Default   |
|:----------------------------------------|:-------------------------|:----------|
| MED-R Medicare - Employer               | 06/16/2017 to 12/31/2100 |           |
| SS-R OASDI - Employer                   | 06/16/2017 to 12/31/2100 |           |
| FUTA Fed Unemployment                   | 06/16/2017 to 12/31/2100 |           |
| MNAST Minnesota Federal Loan Assessment | 06/16/2017 to 12/31/2100 |           |
| MNDW Workforce Enhancement Fee          | 06/16/2017 to 12/31/2100 |           |
| MNSUI Minnesota SUI                     | 06/16/2017 to 12/31/2100 |           |
2025-09-09 07:26:27,048 | INFO | -validating table: Tax Information (Employer)
2025-09-09 07:26:27,049 | INFO | --figuring out table emptiness...
2025-09-09 07:27:10,579 | INFO | llm gpt-5-mini api call took 43.528 seconds
2025-09-09 07:27:10,597 | INFO | total input tokens: 17934
2025-09-09 07:27:10,599 | INFO | input text tokens: 17003 # estimated
2025-09-09 07:27:10,599 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:27:10,600 | INFO | cost for input: $0.022417 USD
2025-09-09 07:27:10,601 | INFO | total output tokens: 3770
2025-09-09 07:27:10,602 | INFO | cost of output: $0.0377 USD
2025-09-09 07:27:10,602 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:28:13,558 | INFO | llm gpt-5-mini api call took 62.954 seconds
2025-09-09 07:28:13,561 | INFO | total input tokens: 1832
2025-09-09 07:28:13,562 | INFO | input text tokens: 1824 # estimated
2025-09-09 07:28:13,563 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:28:13,564 | INFO | cost for input: $0.00229 USD
2025-09-09 07:28:13,565 | INFO | total output tokens: 3584
2025-09-09 07:28:13,565 | INFO | cost of output: $0.03584 USD
2025-09-09 07:28:13,566 | INFO | --got table grid emptiness info:
|Employer Tax (code description)|Effective Dates|Default|
|---:|---:|---:|
|X|X| |
|X|X| |
|X|X| |
|X|X| |
|X|X| |
|X|X| |
2025-09-09 07:28:34,072 | INFO | llm gpt-5 api call took 20.503 seconds
2025-09-09 07:28:34,078 | INFO | total input tokens: 3555
2025-09-09 07:28:34,079 | INFO | input text tokens: 2917 # estimated
2025-09-09 07:28:34,080 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:28:34,080 | INFO | cost for input: $0.004444 USD
2025-09-09 07:28:34,082 | INFO | total output tokens: 552
2025-09-09 07:28:34,083 | INFO | cost of output: $0.00552 USD
2025-09-09 07:28:34,084 | INFO | done judging, ALL GOOD
2025-09-09 07:28:34,087 | INFO | -current table:
| Code   | Deduction             |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-------|:----------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| 401KC  | 401K Contribution     |    1   | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/08/2017 to 04/14/2019 |
| DNTL   | Dental Insurance S125 |   15.1 | B5         |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2017 to 04/14/2019 |
| FH125  | Health Insurance S125 |   78.9 | B5         |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2017 to 04/14/2019 |
2025-09-09 07:28:34,088 | INFO | -validating table: Deduction Information
2025-09-09 07:28:34,088 | INFO | --figuring out table emptiness...
2025-09-09 07:29:10,466 | INFO | llm gpt-5-mini api call took 36.375 seconds
2025-09-09 07:29:10,484 | INFO | total input tokens: 18028
2025-09-09 07:29:10,485 | INFO | input text tokens: 17097 # estimated
2025-09-09 07:29:10,486 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:29:10,486 | INFO | cost for input: $0.022535 USD
2025-09-09 07:29:10,487 | INFO | total output tokens: 2883
2025-09-09 07:29:10,488 | INFO | cost of output: $0.02883 USD
2025-09-09 07:29:10,489 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:30:26,593 | INFO | llm gpt-5-mini api call took 76.103 seconds
2025-09-09 07:30:26,598 | INFO | total input tokens: 2586
2025-09-09 07:30:26,599 | INFO | input text tokens: 2578 # estimated
2025-09-09 07:30:26,601 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:30:26,602 | INFO | cost for input: $0.003233 USD
2025-09-09 07:30:26,602 | INFO | total output tokens: 5375
2025-09-09 07:30:26,603 | INFO | cost of output: $0.05375 USD
2025-09-09 07:30:26,604 | INFO | --got table grid emptiness info:
|Code|Deduction|Rate|CalcCode|Frequency|Goal/Paid|Min/Max/Annual Max|Arrears|Agency|Effective Dates|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X| |X|X|X| |X|
|X|X|X| |X|X|X|X| |X|
|X|X|X| |X|X|X|X| |X|
2025-09-09 07:31:28,298 | INFO | llm gpt-5 api call took 61.692 seconds
2025-09-09 07:31:28,304 | INFO | total input tokens: 3711
2025-09-09 07:31:28,305 | INFO | input text tokens: 3073 # estimated
2025-09-09 07:31:28,306 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:31:28,307 | INFO | cost for input: $0.004639 USD
2025-09-09 07:31:28,308 | INFO | total output tokens: 2323
2025-09-09 07:31:28,308 | INFO | cost of output: $0.02323 USD
2025-09-09 07:31:28,309 | INFO | --found issues: [{'row': 'multiple rows 2,3', 'column': 'multiple columns CalcCode, Frequency', 'status': 'wrong', 'feedback': "Column shift: per image layout, 'B5' is under Frequency and CalcCode is empty. Extractor put 'B5' in CalcCode and left Frequency blank."}]
2025-09-09 07:31:39,155 | INFO | llm gpt-5-mini api call took 10.844 seconds
2025-09-09 07:31:39,160 | INFO | total input tokens: 3045
2025-09-09 07:31:39,161 | INFO | input text tokens: 2114 # estimated
2025-09-09 07:31:39,162 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:31:39,162 | INFO | cost for input: $0.003806 USD
2025-09-09 07:31:39,163 | INFO | total output tokens: 1089
2025-09-09 07:31:39,164 | INFO | cost of output: $0.01089 USD
2025-09-09 07:31:39,166 | INFO | --corrected as:
| Code   | Deduction             |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-------|:----------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| 401KC  | 401K Contribution     |    1   | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/08/2017 to 04/14/2019 |
| DNTL   | Dental Insurance S125 |   15.1 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2017 to 04/14/2019 |
| FH125  | Health Insurance S125 |   78.9 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2017 to 04/14/2019 |
2025-09-09 07:31:39,167 | INFO | -revalidating table: Deduction Information
2025-09-09 07:32:02,756 | INFO | llm gpt-5 api call took 23.586 seconds
2025-09-09 07:32:02,762 | INFO | total input tokens: 3711
2025-09-09 07:32:02,763 | INFO | input text tokens: 3073 # estimated
2025-09-09 07:32:02,763 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:32:02,764 | INFO | cost for input: $0.001471 USD
2025-09-09 07:32:02,765 | INFO | total output tokens: 936
2025-09-09 07:32:02,766 | INFO | cost of output: $0.00936 USD
2025-09-09 07:32:02,767 | INFO | done judging, ALL GOOD
2025-09-09 07:32:02,769 | INFO | -current table:
|   Sequence No. |   Transit No. |   Account No. | Checking?   | Account Name   | Amount Code   |   Amount | Prenote Date   | Effective Dates          | Exclude Special   |
|---------------:|--------------:|--------------:|:------------|:---------------|:--------------|---------:|:---------------|:-------------------------|:------------------|
|             99 |     291070001 |    8224461774 | Yes         | Patricia, Paul | %             |      100 | 06/30/2017     | 06/30/2017 to 12/31/2100 | No                |
2025-09-09 07:32:02,770 | INFO | -validating table: Direct Deposit Information
2025-09-09 07:32:02,772 | INFO | --figuring out table emptiness...
2025-09-09 07:33:07,707 | INFO | llm gpt-5-mini api call took 64.933 seconds
2025-09-09 07:33:07,724 | INFO | total input tokens: 17882
2025-09-09 07:33:07,725 | INFO | input text tokens: 16951 # estimated
2025-09-09 07:33:07,726 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:33:07,727 | INFO | cost for input: $0.022353 USD
2025-09-09 07:33:07,728 | INFO | total output tokens: 2270
2025-09-09 07:33:07,729 | INFO | cost of output: $0.0227 USD
2025-09-09 07:33:07,729 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:34:05,262 | INFO | llm gpt-5-mini api call took 57.532 seconds
2025-09-09 07:34:05,265 | INFO | total input tokens: 1583
2025-09-09 07:34:05,266 | INFO | input text tokens: 1575 # estimated
2025-09-09 07:34:05,267 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:34:05,268 | INFO | cost for input: $0.001979 USD
2025-09-09 07:34:05,269 | INFO | total output tokens: 3544
2025-09-09 07:34:05,272 | INFO | cost of output: $0.03544 USD
2025-09-09 07:34:05,274 | INFO | --got table grid emptiness info:
|Sequence No.|Transit No.|Account No.|Checking?|Account Name|Amount Code|Amount|Prenote Date|Effective Dates|Exclude Special|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X|X|X|X|X|X|
2025-09-09 07:34:20,474 | INFO | llm gpt-5 api call took 15.199 seconds
2025-09-09 07:34:20,480 | INFO | total input tokens: 3526
2025-09-09 07:34:20,481 | INFO | input text tokens: 2888 # estimated
2025-09-09 07:34:20,482 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:34:20,483 | INFO | cost for input: $0.004407 USD
2025-09-09 07:34:20,484 | INFO | total output tokens: 552
2025-09-09 07:34:20,485 | INFO | cost of output: $0.00552 USD
2025-09-09 07:34:20,486 | INFO | done judging, ALL GOOD
2025-09-09 07:34:20,499 | INFO | -current table:

2025-09-09 07:34:20,500 | INFO | -validating table: Fringe Benefit Information
2025-09-09 07:34:20,502 | INFO | -current table:
| BCode    |   Rate |   Amount |   Hours | Max/Carryover Max   | Length of Service   | Hours: Used/Avail/Total/Prob   | Dollars: Used/Avail/Total/Prob   | Effective Dates          |
|:---------|-------:|---------:|--------:|:--------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| PER      |      0 |        0 |       0 | 0.00/0.00           |                     | 14.00/0.00/0.00/0.00           | 185.50/0.00/0.00/0.00            | 09/01/2017 to 04/13/2019 |
| SICK     |      0 |        0 |       0 | 0.00/0.00           |                     | 35.00/0.00/0.00/0.00           | 318.00/145.75/0.00/0.00          | 09/01/2017 to 04/13/2019 |
| VAC-NEX7 |      0 |        0 |       0 | 0.00/0.00           |                     | 18.83/0.00/0.00/0.00           | 0.00/249.50/0.00/0.00            | 10/05/2018 to 04/13/2019 |
| VAC-NEX8 |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 481.00/40.04/0.00/0.00           | 09/22/2017 to 10/05/2018 |
| VAC/CO   |      0 |        0 |       0 | 0.00/0.00           |                     | 0.96/0.00/0.00/0.00            | 0.00/12.72/0.00/0.00             | 01/01/2018 to 04/13/2019 |
2025-09-09 07:34:20,503 | INFO | -validating table: Benefit Accrual Information
2025-09-09 07:34:20,504 | INFO | --figuring out table emptiness...
2025-09-09 07:35:15,553 | INFO | llm gpt-5-mini api call took 55.047 seconds
2025-09-09 07:35:15,575 | INFO | total input tokens: 18237
2025-09-09 07:35:15,576 | INFO | input text tokens: 17306 # estimated
2025-09-09 07:35:15,577 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:35:15,578 | INFO | cost for input: $0.022796 USD
2025-09-09 07:35:15,579 | INFO | total output tokens: 4791
2025-09-09 07:35:15,580 | INFO | cost of output: $0.04791 USD
2025-09-09 07:35:15,580 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 07:36:34,990 | INFO | llm gpt-5-mini api call took 79.409 seconds
2025-09-09 07:36:34,997 | INFO | total input tokens: 3302
2025-09-09 07:36:34,998 | INFO | input text tokens: 3294 # estimated
2025-09-09 07:36:34,999 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 07:36:35,001 | INFO | cost for input: $0.004128 USD
2025-09-09 07:36:35,001 | INFO | total output tokens: 6312
2025-09-09 07:36:35,002 | INFO | cost of output: $0.06312 USD
2025-09-09 07:36:35,004 | INFO | --got table grid emptiness info:
|BCode|Rate|Amount|Hours|Max/Carryover Max|Length of Service|Hours: Used/Avail/Total/Prob|Dollars: Used/Avail/Total/Prob|Effective Dates|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
2025-09-09 07:37:12,231 | INFO | llm gpt-5 api call took 37.226 seconds
2025-09-09 07:37:12,238 | INFO | total input tokens: 3961
2025-09-09 07:37:12,239 | INFO | input text tokens: 3323 # estimated
2025-09-09 07:37:12,239 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:37:12,240 | INFO | cost for input: $0.004951 USD
2025-09-09 07:37:12,241 | INFO | total output tokens: 1192
2025-09-09 07:37:12,242 | INFO | cost of output: $0.01192 USD
2025-09-09 07:37:12,244 | INFO | done judging, ALL GOOD
2025-09-09 07:37:12,246 | INFO | -current table:

2025-09-09 07:37:12,247 | INFO | -validating table: Review Information
2025-09-09 07:37:12,249 | INFO | -current table:

2025-09-09 07:37:12,250 | INFO | -validating table: Emergency Contact Information
2025-09-09 07:37:12,250 | INFO | started validating form fields
2025-09-09 07:37:12,251 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-09 07:37:12,252 | INFO | --current are:
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
2025-09-09 07:37:24,714 | INFO | llm gpt-5 api call took 12.452 seconds
2025-09-09 07:37:24,722 | INFO | total input tokens: 4714
2025-09-09 07:37:24,723 | INFO | input text tokens: 4076 # estimated
2025-09-09 07:37:24,724 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:37:24,725 | INFO | cost for input: $0.005893 USD
2025-09-09 07:37:24,727 | INFO | total output tokens: 512
2025-09-09 07:37:24,728 | INFO | cost of output: $0.00512 USD
2025-09-09 07:37:24,729 | INFO | done judging, ALL GOOD
2025-09-09 07:37:24,730 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-09 07:37:24,731 | INFO | --current are:
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
2025-09-09 07:37:49,033 | INFO | llm gpt-5 api call took 24.293 seconds
2025-09-09 07:37:49,041 | INFO | total input tokens: 4682
2025-09-09 07:37:49,042 | INFO | input text tokens: 4044 # estimated
2025-09-09 07:37:49,043 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:37:49,044 | INFO | cost for input: $0.005853 USD
2025-09-09 07:37:49,045 | INFO | total output tokens: 770
2025-09-09 07:37:49,046 | INFO | cost of output: $0.0077 USD
2025-09-09 07:37:49,047 | INFO | done judging, ALL GOOD
2025-09-09 07:37:49,048 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-09 07:37:49,050 | INFO | --current are:
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
2025-09-09 07:38:16,334 | INFO | llm gpt-5 api call took 27.274 seconds
2025-09-09 07:38:16,342 | INFO | total input tokens: 4688
2025-09-09 07:38:16,343 | INFO | input text tokens: 4050 # estimated
2025-09-09 07:38:16,344 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:38:16,345 | INFO | cost for input: $0.000964 USD
2025-09-09 07:38:16,345 | INFO | total output tokens: 833
2025-09-09 07:38:16,346 | INFO | cost of output: $0.00833 USD
2025-09-09 07:38:16,347 | INFO | done judging, ALL GOOD
2025-09-09 07:38:16,348 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-09 07:38:16,348 | INFO | --current are:
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
2025-09-09 07:38:53,493 | INFO | llm gpt-5 api call took 37.136 seconds
2025-09-09 07:38:53,501 | INFO | total input tokens: 4683
2025-09-09 07:38:53,502 | INFO | input text tokens: 4045 # estimated
2025-09-09 07:38:53,503 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:38:53,504 | INFO | cost for input: $0.005854 USD
2025-09-09 07:38:53,504 | INFO | total output tokens: 964
2025-09-09 07:38:53,505 | INFO | cost of output: $0.00964 USD
2025-09-09 07:38:53,506 | INFO | done judging, ALL GOOD
2025-09-09 07:38:53,507 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-09 07:38:53,508 | INFO | --current are:
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
2025-09-09 07:39:17,649 | INFO | llm gpt-5 api call took 24.130 seconds
2025-09-09 07:39:17,656 | INFO | total input tokens: 4683
2025-09-09 07:39:17,657 | INFO | input text tokens: 4045 # estimated
2025-09-09 07:39:17,658 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:39:17,659 | INFO | cost for input: $0.002686 USD
2025-09-09 07:39:17,660 | INFO | total output tokens: 775
2025-09-09 07:39:17,661 | INFO | cost of output: $0.00775 USD
2025-09-09 07:39:17,662 | INFO | done judging, ALL GOOD
2025-09-09 07:39:17,663 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 07:39:17,664 | INFO | --current are:
Veteran : 
Legal Rep : No
Nickname : 
surname : 
Prior Last : 
Disability : 
Smoker : No
AutoPay : No AutoPay Information
Pay Frequency : B
OT Exempt : No
2025-09-09 07:40:06,121 | INFO | llm gpt-5 api call took 48.447 seconds
2025-09-09 07:40:06,129 | INFO | total input tokens: 4677
2025-09-09 07:40:06,130 | INFO | input text tokens: 4039 # estimated
2025-09-09 07:40:06,131 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:40:06,132 | INFO | cost for input: $0.00095 USD
2025-09-09 07:40:06,132 | INFO | total output tokens: 2134
2025-09-09 07:40:06,133 | INFO | cost of output: $0.02134 USD
2025-09-09 07:40:06,136 | INFO | --found issues: [{'data_name': 'AutoPay', 'status': 'wrong', 'feedback': "Value taken from the 'AutoPay Information' section; there is no form field. Should be empty."}]
2025-09-09 07:40:11,370 | INFO | llm gpt-5-mini api call took 5.233 seconds
2025-09-09 07:40:11,374 | INFO | total input tokens: 2754
2025-09-09 07:40:11,375 | INFO | input text tokens: 1823 # estimated
2025-09-09 07:40:11,376 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 07:40:11,377 | INFO | cost for input: $0.003442 USD
2025-09-09 07:40:11,378 | INFO | total output tokens: 317
2025-09-09 07:40:11,378 | INFO | cost of output: $0.00317 USD
2025-09-09 07:40:11,380 | INFO | --corrected as:
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
2025-09-09 07:40:11,380 | INFO | -revalidating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 07:41:03,641 | INFO | llm gpt-5 api call took 52.259 seconds
2025-09-09 07:41:03,648 | INFO | total input tokens: 4672
2025-09-09 07:41:03,649 | INFO | input text tokens: 4034 # estimated
2025-09-09 07:41:03,650 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:41:03,651 | INFO | cost for input: $0.00584 USD
2025-09-09 07:41:03,652 | INFO | total output tokens: 1473
2025-09-09 07:41:03,654 | INFO | cost of output: $0.01473 USD
2025-09-09 07:41:03,655 | INFO | done judging, ALL GOOD
2025-09-09 07:41:03,656 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-09 07:41:03,657 | INFO | --current are:
Default Hours : 0.00
Locations : 606
Positions : 700
2025-09-09 07:41:23,631 | INFO | llm gpt-5 api call took 19.965 seconds
2025-09-09 07:41:23,638 | INFO | total input tokens: 4651
2025-09-09 07:41:23,639 | INFO | input text tokens: 4013 # estimated
2025-09-09 07:41:23,640 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 07:41:23,641 | INFO | cost for input: $0.000918 USD
2025-09-09 07:41:23,643 | INFO | total output tokens: 913
2025-09-09 07:41:23,644 | INFO | cost of output: $0.00913 USD
2025-09-09 07:41:23,645 | INFO | done judging, ALL GOOD

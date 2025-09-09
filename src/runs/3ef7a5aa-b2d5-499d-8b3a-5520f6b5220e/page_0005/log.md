2025-09-09 06:04:56,501 | INFO | started initial extraction for page 5
2025-09-09 06:06:28,997 | INFO | llm gpt-5 api call took 92.238 seconds
2025-09-09 06:06:29,001 | INFO | total input tokens: 3043
2025-09-09 06:06:29,002 | INFO | input text tokens: 2405 # estimated
2025-09-09 06:06:29,002 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:06:29,002 | INFO | cost for input: $0.003804 USD
2025-09-09 06:06:29,002 | INFO | total output tokens: 3630
2025-09-09 06:06:29,002 | INFO | cost of output: $0.0363 USD
2025-09-09 06:06:29,003 | INFO | initial extraction of page data done.
2025-09-09 06:06:36,692 | INFO | got response with OCR coordinates info from azure doc intelligence for page 5
2025-09-09 06:06:36,692 | INFO | started validating tables
2025-09-09 06:06:36,695 | INFO | -current table:
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
2025-09-09 06:06:36,695 | INFO | -validating table: Rate/Salary Information
2025-09-09 06:06:36,695 | INFO | --figuring out table emptiness...
2025-09-09 06:17:35,165 | WARNING | Transient error (status=429) attempt 1/6; sleeping 31.00s before retry.
2025-09-09 06:20:53,101 | INFO | llm gpt-5-mini api call took 166.935 seconds
2025-09-09 06:20:53,119 | INFO | total input tokens: 18760
2025-09-09 06:20:53,119 | INFO | input text tokens: 17829 # estimated
2025-09-09 06:20:53,120 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:20:53,120 | INFO | cost for input: $0.02345 USD
2025-09-09 06:20:53,120 | INFO | total output tokens: 5727
2025-09-09 06:20:53,120 | INFO | cost of output: $0.05727 USD
2025-09-09 06:20:53,120 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:21:31,623 | INFO | llm gpt-5-mini api call took 38.503 seconds
2025-09-09 06:21:31,628 | INFO | total input tokens: 3727
2025-09-09 06:21:31,628 | INFO | input text tokens: 3719 # estimated
2025-09-09 06:21:31,628 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:21:31,629 | INFO | cost for input: $0.004659 USD
2025-09-09 06:21:31,629 | INFO | total output tokens: 3206
2025-09-09 06:21:31,629 | INFO | cost of output: $0.03206 USD
2025-09-09 06:21:31,629 | INFO | --got table grid emptiness info:
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
2025-09-09 06:22:05,385 | INFO | llm gpt-5 api call took 33.756 seconds
2025-09-09 06:22:05,391 | INFO | total input tokens: 3807
2025-09-09 06:22:05,391 | INFO | input text tokens: 3169 # estimated
2025-09-09 06:22:05,391 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:22:05,391 | INFO | cost for input: $0.004759 USD
2025-09-09 06:22:05,391 | INFO | total output tokens: 1192
2025-09-09 06:22:05,392 | INFO | cost of output: $0.01192 USD
2025-09-09 06:22:05,392 | INFO | done judging, ALL GOOD
2025-09-09 06:22:05,393 | INFO | -current table:
| Employee Tax (code description)   | Status   |   Add'l Amount | Effective Dates          | Default   |
|:----------------------------------|:---------|---------------:|:-------------------------|:----------|
| MED Medicare                      |          |              0 | 01/15/2016 to 12/31/2100 | Yes       |
| SS OASDI                          |          |              0 | 01/15/2016 to 12/31/2100 | Yes       |
| FITW Federal Income Tax           | M-1      |             20 | 01/04/2016 to 12/31/2100 | Yes       |
| MN Minnesota SITW                 | M-1      |              0 | 01/04/2016 to 12/31/2100 | Yes       |
2025-09-09 06:22:05,393 | INFO | -validating table: Tax Information (Employee)
2025-09-09 06:22:05,394 | INFO | --figuring out table emptiness...
2025-09-09 06:23:57,986 | WARNING | Transient error (status=429) attempt 1/6; sleeping 15.00s before retry.
2025-09-09 06:25:30,839 | WARNING | Transient error (status=429) attempt 2/6; sleeping 52.00s before retry.
2025-09-09 06:28:13,515 | WARNING | Transient error (status=429) attempt 3/6; sleeping 15.00s before retry.
2025-09-09 06:29:06,328 | INFO | llm gpt-5-mini api call took 37.812 seconds
2025-09-09 06:29:06,346 | INFO | total input tokens: 18548
2025-09-09 06:29:06,346 | INFO | input text tokens: 17617 # estimated
2025-09-09 06:29:06,346 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:29:06,346 | INFO | cost for input: $0.002881 USD
2025-09-09 06:29:06,346 | INFO | total output tokens: 3802
2025-09-09 06:29:06,346 | INFO | cost of output: $0.03802 USD
2025-09-09 06:29:06,347 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:30:13,773 | INFO | llm gpt-5-mini api call took 67.426 seconds
2025-09-09 06:30:13,778 | INFO | total input tokens: 3221
2025-09-09 06:30:13,778 | INFO | input text tokens: 3213 # estimated
2025-09-09 06:30:13,778 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:30:13,779 | INFO | cost for input: $0.004026 USD
2025-09-09 06:30:13,779 | INFO | total output tokens: 4894
2025-09-09 06:30:13,779 | INFO | cost of output: $0.04894 USD
2025-09-09 06:30:13,779 | INFO | --got table grid emptiness info:
|Employee Tax (code description)|Status|Add'l Amount|Effective Dates|Default|
|---:|---:|---:|---:|---:|
|X| |X|X|X|
|X| |X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
| | | | | |
| | | | | |
2025-09-09 06:30:50,698 | INFO | llm gpt-5 api call took 36.918 seconds
2025-09-09 06:30:50,704 | INFO | total input tokens: 3556
2025-09-09 06:30:50,704 | INFO | input text tokens: 2918 # estimated
2025-09-09 06:30:50,704 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:30:50,705 | INFO | cost for input: $0.004445 USD
2025-09-09 06:30:50,705 | INFO | total output tokens: 552
2025-09-09 06:30:50,705 | INFO | cost of output: $0.00552 USD
2025-09-09 06:30:50,705 | INFO | done judging, ALL GOOD
2025-09-09 06:30:50,706 | INFO | -current table:
| Employer Tax (code description)         | Effective Dates          | Default   |
|:----------------------------------------|:-------------------------|:----------|
| MED-R Medicare - Employer               | 01/15/2016 to 12/31/2100 |           |
| SS-R OASDI - Employer                   | 01/15/2016 to 12/31/2100 |           |
| FUTA Fed Unemployment                   | 01/15/2016 to 12/31/2100 |           |
| MNAST Minnesota Federal Loan Assessment | 01/15/2016 to 12/31/2100 |           |
| MNDW Workforce Enhancement Fee          | 01/15/2016 to 12/31/2100 |           |
| MNSUI Minnesota SUI                     | 01/15/2016 to 12/31/2100 |           |
2025-09-09 06:30:50,707 | INFO | -validating table: Tax Information (Employer)
2025-09-09 06:30:50,707 | INFO | --figuring out table emptiness...
2025-09-09 06:31:12,231 | INFO | llm gpt-5-mini api call took 21.522 seconds
2025-09-09 06:31:12,249 | INFO | total input tokens: 18562
2025-09-09 06:31:12,249 | INFO | input text tokens: 17631 # estimated
2025-09-09 06:31:12,249 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:31:12,250 | INFO | cost for input: $0.023203 USD
2025-09-09 06:31:12,250 | INFO | total output tokens: 2733
2025-09-09 06:31:12,250 | INFO | cost of output: $0.02733 USD
2025-09-09 06:31:12,250 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:32:26,414 | INFO | llm gpt-5-mini api call took 74.163 seconds
2025-09-09 06:32:26,416 | INFO | total input tokens: 1884
2025-09-09 06:32:26,416 | INFO | input text tokens: 1876 # estimated
2025-09-09 06:32:26,417 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:32:26,417 | INFO | cost for input: $0.002355 USD
2025-09-09 06:32:26,417 | INFO | total output tokens: 4151
2025-09-09 06:32:26,417 | INFO | cost of output: $0.04151 USD
2025-09-09 06:32:26,417 | INFO | --got table grid emptiness info:
|Employer Tax (code description)|Effective Dates|Default|
|---|---|---|
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
2025-09-09 06:32:41,283 | INFO | llm gpt-5 api call took 14.866 seconds
2025-09-09 06:32:41,289 | INFO | total input tokens: 3531
2025-09-09 06:32:41,289 | INFO | input text tokens: 2893 # estimated
2025-09-09 06:32:41,289 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:32:41,289 | INFO | cost for input: $0.004414 USD
2025-09-09 06:32:41,289 | INFO | total output tokens: 552
2025-09-09 06:32:41,289 | INFO | cost of output: $0.00552 USD
2025-09-09 06:32:41,290 | INFO | done judging, ALL GOOD
2025-09-09 06:32:41,292 | INFO | -current table:
| Code       | Deduction             |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-----------|:----------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| 401KC      | 401K Contribution     |   6    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 04/01/2016 to 12/31/2100 |
| 401kUM     | 401kUnmatch           |  14    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 08/01/2022 to 12/31/2100 |
| 401kUnmatc | 401K Unmatch          |  12    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 03/31/2019 to 08/01/2022 |
| DNTL       | Dental Insurance S125 |  18.32 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2019 to 12/31/2100 |
| FH125      | Health Insurance S125 | 158.14 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2019 to 12/31/2100 |
2025-09-09 06:32:41,292 | INFO | -validating table: Deduction Information
2025-09-09 06:32:41,292 | INFO | --figuring out table emptiness...
2025-09-09 06:34:01,331 | WARNING | Transient error (status=429) attempt 1/6; sleeping 58.00s before retry.
2025-09-09 06:37:40,532 | INFO | llm gpt-5-mini api call took 161.200 seconds
2025-09-09 06:37:40,551 | INFO | total input tokens: 18800
2025-09-09 06:37:40,551 | INFO | input text tokens: 17869 # estimated
2025-09-09 06:37:40,551 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:37:40,552 | INFO | cost for input: $0.0235 USD
2025-09-09 06:37:40,552 | INFO | total output tokens: 4360
2025-09-09 06:37:40,552 | INFO | cost of output: $0.0436 USD
2025-09-09 06:37:40,552 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:39:08,901 | INFO | llm gpt-5-mini api call took 88.349 seconds
2025-09-09 06:39:08,905 | INFO | total input tokens: 3359
2025-09-09 06:39:08,905 | INFO | input text tokens: 3351 # estimated
2025-09-09 06:39:08,905 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:39:08,906 | INFO | cost for input: $0.004199 USD
2025-09-09 06:39:08,906 | INFO | total output tokens: 5614
2025-09-09 06:39:08,906 | INFO | cost of output: $0.05614 USD
2025-09-09 06:39:08,906 | INFO | --got table grid emptiness info:
|Code|Deduction|Rate|CalcCode|Frequency|Goal/Paid|Min/Max/Annual Max|Arrears|Agency|Effective Dates|
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|X|X|X|X| |X|X|X| |X|
|X|X|X|X| |X|X|X| |X|
|X|X|X|X| |X|X|X| |X|
|X|X|X| |X|X|X|X| |X|
|X|X|X| |X|X|X|X| |X|
2025-09-09 06:39:58,424 | INFO | llm gpt-5 api call took 49.517 seconds
2025-09-09 06:39:58,429 | INFO | total input tokens: 3887
2025-09-09 06:39:58,430 | INFO | input text tokens: 3249 # estimated
2025-09-09 06:39:58,430 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:39:58,430 | INFO | cost for input: $0.004859 USD
2025-09-09 06:39:58,430 | INFO | total output tokens: 1512
2025-09-09 06:39:58,430 | INFO | cost of output: $0.01512 USD
2025-09-09 06:39:58,431 | INFO | done judging, ALL GOOD
2025-09-09 06:39:58,432 | INFO | -current table:
|   Sequence No. |   Transit No. |   Account No. | Checking?   | Account Name    | Amount Code   |   Amount | Prenote Date   | Effective Dates          | Exclude Special   |
|---------------:|--------------:|--------------:|:------------|:----------------|:--------------|---------:|:---------------|:-------------------------|:------------------|
|             99 |     296076262 |    2743046665 | Yes         | Jocelyn, Taylor | %             |      100 | 02/12/2016     | 02/12/2016 to 12/31/2100 | No                |
2025-09-09 06:39:58,432 | INFO | -validating table: Direct Deposit Information
2025-09-09 06:39:58,432 | INFO | --figuring out table emptiness...
2025-09-09 06:42:00,107 | INFO | llm gpt-5-mini api call took 121.673 seconds
2025-09-09 06:42:00,125 | INFO | total input tokens: 18511
2025-09-09 06:42:00,125 | INFO | input text tokens: 17580 # estimated
2025-09-09 06:42:00,125 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:42:00,125 | INFO | cost for input: $0.023139 USD
2025-09-09 06:42:00,125 | INFO | total output tokens: 2334
2025-09-09 06:42:00,125 | INFO | cost of output: $0.02334 USD
2025-09-09 06:42:00,126 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:43:12,255 | INFO | llm gpt-5-mini api call took 72.129 seconds
2025-09-09 06:43:12,258 | INFO | total input tokens: 1583
2025-09-09 06:43:12,258 | INFO | input text tokens: 1575 # estimated
2025-09-09 06:43:12,258 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:43:12,258 | INFO | cost for input: $0.001979 USD
2025-09-09 06:43:12,258 | INFO | total output tokens: 3736
2025-09-09 06:43:12,258 | INFO | cost of output: $0.03736 USD
2025-09-09 06:43:12,258 | INFO | --got table grid emptiness info:
|Sequence No.|Transit No.|Account No.|Checking?|Account Name|Amount Code|Amount|Prenote Date|Effective Dates|Exclude Special|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X|X|X|X|X|X|
2025-09-09 06:43:29,390 | INFO | llm gpt-5 api call took 17.131 seconds
2025-09-09 06:43:29,396 | INFO | total input tokens: 3512
2025-09-09 06:43:29,396 | INFO | input text tokens: 2874 # estimated
2025-09-09 06:43:29,396 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:43:29,396 | INFO | cost for input: $0.00439 USD
2025-09-09 06:43:29,397 | INFO | total output tokens: 424
2025-09-09 06:43:29,397 | INFO | cost of output: $0.00424 USD
2025-09-09 06:43:29,397 | INFO | done judging, ALL GOOD
2025-09-09 06:43:29,399 | INFO | -current table:
| ECode   | CalcCode   | Rate Code   |   Rate | Rate Per   |   Amount | Tabled?   |   Units | Frequency   | Goal/Paid/Goal Bal.   | Min/Max/Ann. Max   | Effective Dates          |
|:--------|:-----------|:------------|-------:|:-----------|---------:|:----------|--------:|:------------|:----------------------|:-------------------|:-------------------------|
| STD     |            |             |      0 |            |    11.07 | No        |       0 | ML          | 0.00/0.00/0.00        | 0.00/0.00/0.00     | 03/17/2019 to 12/31/2100 |
2025-09-09 06:43:29,399 | INFO | -validating table: Fringe Benefit Information
2025-09-09 06:43:29,399 | INFO | --figuring out table emptiness...
2025-09-09 06:44:02,308 | INFO | llm gpt-5-mini api call took 32.908 seconds
2025-09-09 06:44:02,327 | INFO | total input tokens: 18542
2025-09-09 06:44:02,327 | INFO | input text tokens: 17611 # estimated
2025-09-09 06:44:02,327 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:44:02,327 | INFO | cost for input: $0.023178 USD
2025-09-09 06:44:02,327 | INFO | total output tokens: 1885
2025-09-09 06:44:02,327 | INFO | cost of output: $0.01885 USD
2025-09-09 06:44:02,328 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:45:31,928 | INFO | llm gpt-5-mini api call took 89.600 seconds
2025-09-09 06:45:31,930 | INFO | total input tokens: 1670
2025-09-09 06:45:31,931 | INFO | input text tokens: 1662 # estimated
2025-09-09 06:45:31,931 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:45:31,931 | INFO | cost for input: $0.002087 USD
2025-09-09 06:45:31,931 | INFO | total output tokens: 4959
2025-09-09 06:45:31,931 | INFO | cost of output: $0.04959 USD
2025-09-09 06:45:31,932 | INFO | --got table grid emptiness info:
|ECode|CalcCode|Rate Code|Rate|Rate Per|Amount|Tabled?|Units|Frequency|Goal/Paid/Goal Bal.|Min/Max/Ann. Max|Effective Dates|
|---|---|---|---|---|---|---|---|---|---|---|---|
|X| | |X| |X|X|X|X|X|X|X|
2025-09-09 06:46:16,672 | INFO | llm gpt-5 api call took 44.740 seconds
2025-09-09 06:46:16,678 | INFO | total input tokens: 3550
2025-09-09 06:46:16,678 | INFO | input text tokens: 2912 # estimated
2025-09-09 06:46:16,679 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:46:16,679 | INFO | cost for input: $0.004437 USD
2025-09-09 06:46:16,679 | INFO | total output tokens: 872
2025-09-09 06:46:16,679 | INFO | cost of output: $0.00872 USD
2025-09-09 06:46:16,680 | INFO | done judging, ALL GOOD
2025-09-09 06:46:16,681 | INFO | -current table:

2025-09-09 06:46:16,681 | INFO | -validating table: Benefit Accrual Information
2025-09-09 06:46:16,682 | INFO | -current table:

2025-09-09 06:46:16,682 | INFO | -validating table: Review Information
2025-09-09 06:46:16,683 | INFO | -current table:

2025-09-09 06:46:16,683 | INFO | -validating table: Emergency Contact Information
2025-09-09 06:46:16,683 | INFO | started validating form fields
2025-09-09 06:46:16,683 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-09 06:46:16,684 | INFO | --current are:
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
2025-09-09 06:46:43,953 | INFO | llm gpt-5 api call took 27.261 seconds
2025-09-09 06:46:43,961 | INFO | total input tokens: 4786
2025-09-09 06:46:43,962 | INFO | input text tokens: 4148 # estimated
2025-09-09 06:46:43,962 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:46:43,962 | INFO | cost for input: $0.005982 USD
2025-09-09 06:46:43,962 | INFO | total output tokens: 704
2025-09-09 06:46:43,963 | INFO | cost of output: $0.00704 USD
2025-09-09 06:46:43,963 | INFO | done judging, ALL GOOD
2025-09-09 06:46:43,963 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-09 06:46:43,963 | INFO | --current are:
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
2025-09-09 06:47:20,189 | INFO | llm gpt-5 api call took 36.216 seconds
2025-09-09 06:47:20,195 | INFO | total input tokens: 4749
2025-09-09 06:47:20,196 | INFO | input text tokens: 4111 # estimated
2025-09-09 06:47:20,196 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:47:20,196 | INFO | cost for input: $0.005936 USD
2025-09-09 06:47:20,196 | INFO | total output tokens: 1154
2025-09-09 06:47:20,196 | INFO | cost of output: $0.01154 USD
2025-09-09 06:47:20,197 | INFO | done judging, ALL GOOD
2025-09-09 06:47:20,197 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-09 06:47:20,197 | INFO | --current are:
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
2025-09-09 06:48:07,605 | INFO | llm gpt-5 api call took 47.399 seconds
2025-09-09 06:48:07,611 | INFO | total input tokens: 4750
2025-09-09 06:48:07,612 | INFO | input text tokens: 4112 # estimated
2025-09-09 06:48:07,612 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:48:07,612 | INFO | cost for input: $0.005938 USD
2025-09-09 06:48:07,612 | INFO | total output tokens: 833
2025-09-09 06:48:07,612 | INFO | cost of output: $0.00833 USD
2025-09-09 06:48:07,613 | INFO | done judging, ALL GOOD
2025-09-09 06:48:07,613 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-09 06:48:07,613 | INFO | --current are:
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
2025-09-09 06:48:34,150 | INFO | llm gpt-5 api call took 26.529 seconds
2025-09-09 06:48:34,157 | INFO | total input tokens: 4949
2025-09-09 06:48:34,157 | INFO | input text tokens: 4103 # estimated
2025-09-09 06:48:34,158 | INFO | input image tokens: 846 # estimated (input - text)
2025-09-09 06:48:34,158 | INFO | cost for input: $0.006186 USD
2025-09-09 06:48:34,158 | INFO | total output tokens: 245
2025-09-09 06:48:34,158 | INFO | cost of output: $0.00245 USD
2025-09-09 06:48:34,158 | INFO | done judging, ALL GOOD
2025-09-09 06:48:34,158 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-09 06:48:34,159 | INFO | --current are:
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
2025-09-09 06:49:16,110 | INFO | llm gpt-5 api call took 41.943 seconds
2025-09-09 06:49:16,116 | INFO | total input tokens: 4750
2025-09-09 06:49:16,117 | INFO | input text tokens: 4112 # estimated
2025-09-09 06:49:16,117 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:49:16,117 | INFO | cost for input: $0.002769 USD
2025-09-09 06:49:16,117 | INFO | total output tokens: 903
2025-09-09 06:49:16,117 | INFO | cost of output: $0.00903 USD
2025-09-09 06:49:16,118 | INFO | done judging, ALL GOOD
2025-09-09 06:49:16,118 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 06:49:16,118 | INFO | --current are:
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
2025-09-09 06:50:12,053 | INFO | llm gpt-5 api call took 55.927 seconds
2025-09-09 06:50:12,060 | INFO | total input tokens: 4739
2025-09-09 06:50:12,060 | INFO | input text tokens: 4101 # estimated
2025-09-09 06:50:12,061 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:50:12,061 | INFO | cost for input: $0.005924 USD
2025-09-09 06:50:12,061 | INFO | total output tokens: 1473
2025-09-09 06:50:12,061 | INFO | cost of output: $0.01473 USD
2025-09-09 06:50:12,062 | INFO | done judging, ALL GOOD
2025-09-09 06:50:12,062 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-09 06:50:12,062 | INFO | --current are:
Default Hours : 0.00
Locations : 606
Positions : 700
2025-09-09 06:50:55,722 | INFO | llm gpt-5 api call took 43.651 seconds
2025-09-09 06:50:55,729 | INFO | total input tokens: 4718
2025-09-09 06:50:55,729 | INFO | input text tokens: 4080 # estimated
2025-09-09 06:50:55,729 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:50:55,729 | INFO | cost for input: $0.005897 USD
2025-09-09 06:50:55,729 | INFO | total output tokens: 721
2025-09-09 06:50:55,730 | INFO | cost of output: $0.00721 USD
2025-09-09 06:50:55,730 | INFO | done judging, ALL GOOD

2025-09-09 06:20:50,284 | INFO | started initial extraction for page 7
2025-09-09 06:21:40,105 | INFO | llm gpt-5 api call took 49.554 seconds
2025-09-09 06:21:40,109 | INFO | total input tokens: 2535
2025-09-09 06:21:40,109 | INFO | input text tokens: 1897 # estimated
2025-09-09 06:21:40,110 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:21:40,110 | INFO | cost for input: $0.003169 USD
2025-09-09 06:21:40,110 | INFO | total output tokens: 2612
2025-09-09 06:21:40,110 | INFO | cost of output: $0.02612 USD
2025-09-09 06:21:40,111 | INFO | initial extraction of page data done.
2025-09-09 06:21:46,398 | INFO | got response with OCR coordinates info from azure doc intelligence for page 7
2025-09-09 06:21:46,398 | INFO | started validating tables
2025-09-09 06:21:46,400 | INFO | -current table:
| RateCode   | Description   |   Rate | Salary   | Effective Dates          |
|:-----------|:--------------|-------:|:---------|:-------------------------|
| Base       | Base Rate     |     18 |          | 08/04/2023 to 12/31/2100 |
2025-09-09 06:21:46,400 | INFO | -validating table: Rate/Salary Information
2025-09-09 06:21:46,400 | INFO | --figuring out table emptiness...
2025-09-09 06:22:03,659 | INFO | llm gpt-5-mini api call took 17.257 seconds
2025-09-09 06:22:03,673 | INFO | total input tokens: 13962
2025-09-09 06:22:03,673 | INFO | input text tokens: 13031 # estimated
2025-09-09 06:22:03,674 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:22:03,674 | INFO | cost for input: $0.017452 USD
2025-09-09 06:22:03,674 | INFO | total output tokens: 1765
2025-09-09 06:22:03,674 | INFO | cost of output: $0.01765 USD
2025-09-09 06:22:03,674 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:22:34,915 | INFO | llm gpt-5-mini api call took 31.240 seconds
2025-09-09 06:22:34,917 | INFO | total input tokens: 1621
2025-09-09 06:22:34,918 | INFO | input text tokens: 1613 # estimated
2025-09-09 06:22:34,918 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:22:34,918 | INFO | cost for input: $0.002026 USD
2025-09-09 06:22:34,918 | INFO | total output tokens: 4316
2025-09-09 06:22:34,918 | INFO | cost of output: $0.04316 USD
2025-09-09 06:22:34,918 | INFO | --got table grid emptiness info:
|RateCode|Description|Rate|Salary|Effective Dates|
|X|X|X||X|
2025-09-09 06:22:52,537 | INFO | llm gpt-5 api call took 17.618 seconds
2025-09-09 06:22:52,541 | INFO | total input tokens: 2871
2025-09-09 06:22:52,542 | INFO | input text tokens: 2233 # estimated
2025-09-09 06:22:52,542 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:22:52,542 | INFO | cost for input: $0.003589 USD
2025-09-09 06:22:52,542 | INFO | total output tokens: 680
2025-09-09 06:22:52,542 | INFO | cost of output: $0.0068 USD
2025-09-09 06:22:52,542 | INFO | done judging, ALL GOOD
2025-09-09 06:22:52,544 | INFO | -current table:
| Employee Tax (code description)   | Status   |   Add'l Amount | Effective Dates          | Default   |
|:----------------------------------|:---------|---------------:|:-------------------------|:----------|
| MED Medicare                      |          |              0 | 08/04/2023 to12/31/2100  | Yes       |
| SS OASDI                          |          |              0 | 08/04/2023 to 12/31/2100 | Yes       |
| FITW Federal Income Tax           | S-0      |              0 | 08/04/2023 to 12/31/2100 | Yes       |
| MN Minnesota SITW                 | S-1      |              0 | 07/31/2023 to 12/31/2100 | Yes       |
2025-09-09 06:22:52,544 | INFO | -validating table: Tax Information (Employee)
2025-09-09 06:22:52,544 | INFO | --figuring out table emptiness...
2025-09-09 06:23:11,876 | INFO | llm gpt-5-mini api call took 19.330 seconds
2025-09-09 06:23:11,890 | INFO | total input tokens: 14072
2025-09-09 06:23:11,890 | INFO | input text tokens: 13141 # estimated
2025-09-09 06:23:11,890 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:23:11,890 | INFO | cost for input: $0.01759 USD
2025-09-09 06:23:11,891 | INFO | total output tokens: 2396
2025-09-09 06:23:11,891 | INFO | cost of output: $0.02396 USD
2025-09-09 06:23:11,891 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:23:40,300 | INFO | llm gpt-5-mini api call took 28.409 seconds
2025-09-09 06:23:40,303 | INFO | total input tokens: 2134
2025-09-09 06:23:40,303 | INFO | input text tokens: 2126 # estimated
2025-09-09 06:23:40,304 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:23:40,304 | INFO | cost for input: $0.002668 USD
2025-09-09 06:23:40,304 | INFO | total output tokens: 3663
2025-09-09 06:23:40,304 | INFO | cost of output: $0.03663 USD
2025-09-09 06:23:40,304 | INFO | --got table grid emptiness info:
|Employee Tax (code description)|Status|Add'l Amount|Effective Dates|Default|
|---|---|---|---|---|
|X|X|X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
|X|X|X|X|X|
2025-09-09 06:23:58,015 | INFO | llm gpt-5 api call took 17.710 seconds
2025-09-09 06:23:58,020 | INFO | total input tokens: 3033
2025-09-09 06:23:58,020 | INFO | input text tokens: 2395 # estimated
2025-09-09 06:23:58,020 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:23:58,020 | INFO | cost for input: $0.003791 USD
2025-09-09 06:23:58,020 | INFO | total output tokens: 680
2025-09-09 06:23:58,021 | INFO | cost of output: $0.0068 USD
2025-09-09 06:23:58,021 | INFO | done judging, ALL GOOD
2025-09-09 06:23:58,022 | INFO | -current table:
| Employer Tax (code description)         | Effective Dates          | Default   |
|:----------------------------------------|:-------------------------|:----------|
| MED-R Medicare - Employer               | 08/04/2023 to 12/31/2100 |           |
| SS-R OASDI - Employer                   | 08/04/2023 to 12/31/2100 |           |
| FUTA Fed Unemployment                   | 08/04/2023 to 12/31/2100 |           |
| MNAST Minnesota Federal Loan Assessment | 08/04/2023 to 12/31/2100 |           |
| MNDW Workforce Enhancement Fee          | 08/04/2023 to 12/31/2100 |           |
| MNSUI Minnesota SUI                     | 08/04/2023 to 12/31/2100 |           |
2025-09-09 06:23:58,023 | INFO | -validating table: Tax Information (Employer)
2025-09-09 06:23:58,023 | INFO | --figuring out table emptiness...
2025-09-09 06:24:26,172 | INFO | llm gpt-5-mini api call took 28.147 seconds
2025-09-09 06:24:26,187 | INFO | total input tokens: 14086
2025-09-09 06:24:26,187 | INFO | input text tokens: 13155 # estimated
2025-09-09 06:24:26,188 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:24:26,188 | INFO | cost for input: $0.017608 USD
2025-09-09 06:24:26,188 | INFO | total output tokens: 3346
2025-09-09 06:24:26,188 | INFO | cost of output: $0.03346 USD
2025-09-09 06:24:26,188 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:24:47,851 | INFO | llm gpt-5-mini api call took 21.662 seconds
2025-09-09 06:24:47,854 | INFO | total input tokens: 1792
2025-09-09 06:24:47,854 | INFO | input text tokens: 1784 # estimated
2025-09-09 06:24:47,854 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:24:47,855 | INFO | cost for input: $0.00224 USD
2025-09-09 06:24:47,855 | INFO | total output tokens: 3001
2025-09-09 06:24:47,855 | INFO | cost of output: $0.03001 USD
2025-09-09 06:24:47,855 | INFO | --got table grid emptiness info:
|Employer Tax (code description)|Effective Dates|Default|
|---|---:|---:|
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
|X|X||
2025-09-09 06:25:04,731 | INFO | llm gpt-5 api call took 16.876 seconds
2025-09-09 06:25:04,737 | INFO | total input tokens: 3025
2025-09-09 06:25:04,737 | INFO | input text tokens: 2387 # estimated
2025-09-09 06:25:04,738 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:25:04,738 | INFO | cost for input: $0.003781 USD
2025-09-09 06:25:04,738 | INFO | total output tokens: 616
2025-09-09 06:25:04,738 | INFO | cost of output: $0.00616 USD
2025-09-09 06:25:04,738 | INFO | done judging, ALL GOOD
2025-09-09 06:25:04,740 | INFO | -current table:

2025-09-09 06:25:04,740 | INFO | -validating table: Deduction Information
2025-09-09 06:25:04,741 | INFO | -current table:
|   Sequence No. |   Transit No. |   Account No. | Checking?   | Account Name   | Amount Code   |   Amount | Prenote Date   | Effective Dates          | Exclude Special   |
|---------------:|--------------:|--------------:|:------------|:---------------|:--------------|---------:|:---------------|:-------------------------|:------------------|
|             99 |     296076301 |    5589890010 | Yes         | Joel Dorsey    | %             |      100 | 07/31/2023     | 07/31/2023 to 12/31/2100 | No                |
2025-09-09 06:25:04,742 | INFO | -validating table: Direct Deposit Information
2025-09-09 06:25:04,742 | INFO | --figuring out table emptiness...
2025-09-09 06:25:21,987 | INFO | llm gpt-5-mini api call took 17.244 seconds
2025-09-09 06:25:22,001 | INFO | total input tokens: 14036
2025-09-09 06:25:22,002 | INFO | input text tokens: 13105 # estimated
2025-09-09 06:25:22,002 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:25:22,002 | INFO | cost for input: $0.017545 USD
2025-09-09 06:25:22,002 | INFO | total output tokens: 1694
2025-09-09 06:25:22,002 | INFO | cost of output: $0.01694 USD
2025-09-09 06:25:22,002 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:25:50,889 | INFO | llm gpt-5-mini api call took 28.886 seconds
2025-09-09 06:25:50,891 | INFO | total input tokens: 1583
2025-09-09 06:25:50,891 | INFO | input text tokens: 1575 # estimated
2025-09-09 06:25:50,891 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:25:50,891 | INFO | cost for input: $0.001979 USD
2025-09-09 06:25:50,892 | INFO | total output tokens: 3160
2025-09-09 06:25:50,892 | INFO | cost of output: $0.0316 USD
2025-09-09 06:25:50,892 | INFO | --got table grid emptiness info:
|Sequence No.|Transit No.|Account No.|Checking?|Account Name|Amount Code|Amount|Prenote Date|Effective Dates|Exclude Special|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X|X|X|X|X|X|
2025-09-09 06:26:04,785 | INFO | llm gpt-5 api call took 13.893 seconds
2025-09-09 06:26:04,790 | INFO | total input tokens: 3005
2025-09-09 06:26:04,790 | INFO | input text tokens: 2367 # estimated
2025-09-09 06:26:04,790 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:26:04,790 | INFO | cost for input: $0.003756 USD
2025-09-09 06:26:04,790 | INFO | total output tokens: 424
2025-09-09 06:26:04,791 | INFO | cost of output: $0.00424 USD
2025-09-09 06:26:04,791 | INFO | done judging, ALL GOOD
2025-09-09 06:26:04,792 | INFO | -current table:

2025-09-09 06:26:04,792 | INFO | -validating table: Fringe Benefit Information
2025-09-09 06:26:04,793 | INFO | -current table:
| BCode   |   Rate |   Amount |   Hours | Max/Carryover Max   | Length of Service   | Hours: Used/Avail/Total/Prob   | Dollars: Used/Avail/Total/Prob   | Effective Dates          |
|:--------|-------:|---------:|--------:|:--------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| PTO1    |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/13.86           | 0.00/0.00/0.00/249.48            | 07/27/2023 to 12/31/2100 |
2025-09-09 06:26:04,793 | INFO | -validating table: Benefit Accrual Information
2025-09-09 06:26:04,793 | INFO | --figuring out table emptiness...
2025-09-09 06:26:29,848 | INFO | llm gpt-5-mini api call took 25.053 seconds
2025-09-09 06:26:29,865 | INFO | total input tokens: 14063
2025-09-09 06:26:29,865 | INFO | input text tokens: 13132 # estimated
2025-09-09 06:26:29,865 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:26:29,865 | INFO | cost for input: $0.017579 USD
2025-09-09 06:26:29,865 | INFO | total output tokens: 2687
2025-09-09 06:26:29,865 | INFO | cost of output: $0.02687 USD
2025-09-09 06:26:29,866 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:26:56,757 | INFO | llm gpt-5-mini api call took 26.891 seconds
2025-09-09 06:26:56,760 | INFO | total input tokens: 1646
2025-09-09 06:26:56,760 | INFO | input text tokens: 1638 # estimated
2025-09-09 06:26:56,760 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:26:56,760 | INFO | cost for input: $0.002057 USD
2025-09-09 06:26:56,760 | INFO | total output tokens: 4183
2025-09-09 06:26:56,760 | INFO | cost of output: $0.04183 USD
2025-09-09 06:26:56,760 | INFO | --got table grid emptiness info:
|BCode|Rate|Amount|Hours|Max/Carryover Max|Length of Service|Hours: Used/Avail/Total/Prob|Dollars: Used/Avail/Total/Prob|Effective Dates|
|---|---|---|---|---|---|---|---|---|
|X|X|X|X|X| |X|X|X|
2025-09-09 06:27:08,537 | INFO | llm gpt-5 api call took 11.776 seconds
2025-09-09 06:27:08,542 | INFO | total input tokens: 3031
2025-09-09 06:27:08,542 | INFO | input text tokens: 2393 # estimated
2025-09-09 06:27:08,542 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:27:08,542 | INFO | cost for input: $0.003789 USD
2025-09-09 06:27:08,542 | INFO | total output tokens: 488
2025-09-09 06:27:08,542 | INFO | cost of output: $0.00488 USD
2025-09-09 06:27:08,543 | INFO | done judging, ALL GOOD
2025-09-09 06:27:08,543 | INFO | -current table:

2025-09-09 06:27:08,544 | INFO | -validating table: Review Information
2025-09-09 06:27:08,545 | INFO | -current table:
| Name           | Relationship   | Home Phone   | Work Phone   | Address   | City   | State   | Zip   | Country   |
|:---------------|:---------------|:-------------|:-------------|:----------|:-------|:--------|:------|:----------|
| Michel Richard |                | 667-577-7708 |              |           |        |         |       |           |
2025-09-09 06:27:08,545 | INFO | -validating table: Emergency Contact Information
2025-09-09 06:27:08,545 | INFO | --figuring out table emptiness...
2025-09-09 06:27:27,016 | INFO | llm gpt-5-mini api call took 18.470 seconds
2025-09-09 06:27:27,030 | INFO | total input tokens: 13980
2025-09-09 06:27:27,030 | INFO | input text tokens: 13049 # estimated
2025-09-09 06:27:27,030 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:27:27,031 | INFO | cost for input: $0.017475 USD
2025-09-09 06:27:27,031 | INFO | total output tokens: 1681
2025-09-09 06:27:27,031 | INFO | cost of output: $0.01681 USD
2025-09-09 06:27:27,031 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:27:51,498 | INFO | llm gpt-5-mini api call took 24.466 seconds
2025-09-09 06:27:51,500 | INFO | total input tokens: 1296
2025-09-09 06:27:51,500 | INFO | input text tokens: 1288 # estimated
2025-09-09 06:27:51,500 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:27:51,500 | INFO | cost for input: $0.00162 USD
2025-09-09 06:27:51,501 | INFO | total output tokens: 3111
2025-09-09 06:27:51,501 | INFO | cost of output: $0.03111 USD
2025-09-09 06:27:51,501 | INFO | --got table grid emptiness info:
|Name|Relationship|Home Phone|Work Phone|Address|City|State|Zip|Country|
|X| |X| | | | | | |
2025-09-09 06:28:06,908 | INFO | llm gpt-5 api call took 15.407 seconds
2025-09-09 06:28:06,913 | INFO | total input tokens: 2900
2025-09-09 06:28:06,913 | INFO | input text tokens: 2262 # estimated
2025-09-09 06:28:06,913 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:28:06,913 | INFO | cost for input: $0.003625 USD
2025-09-09 06:28:06,913 | INFO | total output tokens: 424
2025-09-09 06:28:06,913 | INFO | cost of output: $0.00424 USD
2025-09-09 06:28:06,914 | INFO | done judging, ALL GOOD
2025-09-09 06:28:06,914 | INFO | started validating form fields
2025-09-09 06:28:06,914 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-09 06:28:06,914 | INFO | --current are:
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
2025-09-09 06:28:35,335 | INFO | llm gpt-5 api call took 28.413 seconds
2025-09-09 06:28:35,340 | INFO | total input tokens: 3606
2025-09-09 06:28:35,340 | INFO | input text tokens: 2968 # estimated
2025-09-09 06:28:35,340 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:28:35,341 | INFO | cost for input: $0.004508 USD
2025-09-09 06:28:35,341 | INFO | total output tokens: 1024
2025-09-09 06:28:35,341 | INFO | cost of output: $0.01024 USD
2025-09-09 06:28:35,341 | INFO | done judging, ALL GOOD
2025-09-09 06:28:35,341 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-09 06:28:35,342 | INFO | --current are:
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
2025-09-09 06:29:04,341 | INFO | llm gpt-5 api call took 28.992 seconds
2025-09-09 06:29:04,346 | INFO | total input tokens: 3570
2025-09-09 06:29:04,347 | INFO | input text tokens: 2932 # estimated
2025-09-09 06:29:04,347 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:29:04,347 | INFO | cost for input: $0.004463 USD
2025-09-09 06:29:04,347 | INFO | total output tokens: 962
2025-09-09 06:29:04,347 | INFO | cost of output: $0.00962 USD
2025-09-09 06:29:04,348 | INFO | done judging, ALL GOOD
2025-09-09 06:29:04,348 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-09 06:29:04,348 | INFO | --current are:
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
2025-09-09 06:29:26,486 | INFO | llm gpt-5 api call took 22.131 seconds
2025-09-09 06:29:26,491 | INFO | total input tokens: 3577
2025-09-09 06:29:26,492 | INFO | input text tokens: 2939 # estimated
2025-09-09 06:29:26,492 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:29:26,492 | INFO | cost for input: $0.004471 USD
2025-09-09 06:29:26,492 | INFO | total output tokens: 1025
2025-09-09 06:29:26,492 | INFO | cost of output: $0.01025 USD
2025-09-09 06:29:26,492 | INFO | done judging, ALL GOOD
2025-09-09 06:29:26,493 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-09 06:29:26,493 | INFO | --current are:
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
2025-09-09 06:29:51,267 | INFO | llm gpt-5 api call took 24.768 seconds
2025-09-09 06:29:51,273 | INFO | total input tokens: 3573
2025-09-09 06:29:51,273 | INFO | input text tokens: 2935 # estimated
2025-09-09 06:29:51,273 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:29:51,273 | INFO | cost for input: $0.000866 USD
2025-09-09 06:29:51,274 | INFO | total output tokens: 964
2025-09-09 06:29:51,274 | INFO | cost of output: $0.00964 USD
2025-09-09 06:29:51,274 | INFO | done judging, ALL GOOD
2025-09-09 06:29:51,274 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-09 06:29:51,274 | INFO | --current are:
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
2025-09-09 06:30:13,461 | INFO | llm gpt-5 api call took 22.180 seconds
2025-09-09 06:30:13,467 | INFO | total input tokens: 3573
2025-09-09 06:30:13,467 | INFO | input text tokens: 2935 # estimated
2025-09-09 06:30:13,467 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:30:13,467 | INFO | cost for input: $0.004466 USD
2025-09-09 06:30:13,467 | INFO | total output tokens: 839
2025-09-09 06:30:13,467 | INFO | cost of output: $0.00839 USD
2025-09-09 06:30:13,468 | INFO | done judging, ALL GOOD
2025-09-09 06:30:13,468 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 06:30:13,468 | INFO | --current are:
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
2025-09-09 06:31:22,554 | INFO | llm gpt-5 api call took 69.080 seconds
2025-09-09 06:31:22,560 | INFO | total input tokens: 3562
2025-09-09 06:31:22,560 | INFO | input text tokens: 2924 # estimated
2025-09-09 06:31:22,560 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:31:22,560 | INFO | cost for input: $0.004452 USD
2025-09-09 06:31:22,560 | INFO | total output tokens: 2369
2025-09-09 06:31:22,560 | INFO | cost of output: $0.02369 USD
2025-09-09 06:31:22,561 | INFO | done judging, ALL GOOD
2025-09-09 06:31:22,561 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-09 06:31:22,561 | INFO | --current are:
Default Hours : 0.00
Locations : 606
Positions : 700
2025-09-09 06:31:32,250 | INFO | llm gpt-5 api call took 9.681 seconds
2025-09-09 06:31:32,255 | INFO | total input tokens: 3541
2025-09-09 06:31:32,255 | INFO | input text tokens: 2903 # estimated
2025-09-09 06:31:32,255 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:31:32,256 | INFO | cost for input: $0.000826 USD
2025-09-09 06:31:32,256 | INFO | total output tokens: 337
2025-09-09 06:31:32,256 | INFO | cost of output: $0.00337 USD
2025-09-09 06:31:32,256 | INFO | done judging, ALL GOOD

2025-09-08 20:23:39,983 | INFO | started initial extraction for page 4
2025-09-08 20:24:11,857 | INFO | llm gpt-5 api call took 31.518 seconds
2025-09-08 20:24:11,860 | INFO | total input tokens: 1661
2025-09-08 20:24:11,860 | INFO | input text tokens: 1023 # estimated
2025-09-08 20:24:11,860 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:24:11,860 | INFO | cost for input: $0.002076 USD
2025-09-08 20:24:11,860 | INFO | total output tokens: 906
2025-09-08 20:24:11,861 | INFO | cost of output: $0.00906 USD
2025-09-08 20:24:11,861 | INFO | initial extraction of page data done.
2025-09-08 20:24:18,630 | INFO | got response with OCR coordinates info from azure doc intelligence for page 4
2025-09-08 20:24:18,630 | INFO | started validating tables
2025-09-08 20:24:18,632 | INFO | -current table:

2025-09-08 20:24:18,632 | INFO | -validating table: Rate/Salary Information
2025-09-08 20:24:18,633 | INFO | -current table:

2025-09-08 20:24:18,633 | INFO | -validating table: Tax Information (Employee)
2025-09-08 20:24:18,633 | INFO | -current table:

2025-09-08 20:24:18,633 | INFO | -validating table: Tax Information (Employer)
2025-09-08 20:24:18,634 | INFO | -current table:

2025-09-08 20:24:18,635 | INFO | -validating table: Deduction Information
2025-09-08 20:24:18,635 | INFO | -current table:

2025-09-08 20:24:18,635 | INFO | -validating table: Direct Deposit Information
2025-09-08 20:24:18,636 | INFO | -current table:

2025-09-08 20:24:18,636 | INFO | -validating table: Fringe Benefit Information
2025-09-08 20:24:18,637 | INFO | -current table:

2025-09-08 20:24:18,637 | INFO | -validating table: Benefit Accrual Information
2025-09-08 20:24:18,638 | INFO | -current table:
| Date       | Reviewer   | Rating   |   Raise Amount |   New Pay Amnt | New Pay Per   | New Position   | Effective Date   | Next Review   |
|:-----------|:-----------|:---------|---------------:|---------------:|:--------------|:---------------|:-----------------|:--------------|
| 02/04/2018 |            |          |              0 |          17.83 |               |                | 02/04/2018       | 01/01/1900    |
2025-09-08 20:24:18,639 | INFO | -validating table: Review Information
2025-09-08 20:24:18,639 | INFO | --figuring out table emptiness...
2025-09-08 20:25:15,240 | INFO | llm gpt-5-mini api call took 56.600 seconds
2025-09-08 20:25:15,251 | INFO | total input tokens: 3694
2025-09-08 20:25:15,252 | INFO | input text tokens: 2763 # estimated
2025-09-08 20:25:15,252 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:25:15,252 | INFO | cost for input: $0.004618 USD
2025-09-08 20:25:15,252 | INFO | total output tokens: 1453
2025-09-08 20:25:15,252 | INFO | cost of output: $0.01453 USD
2025-09-08 20:25:15,252 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:25:37,467 | INFO | llm gpt-5-mini api call took 22.215 seconds
2025-09-08 20:25:37,474 | INFO | total input tokens: 1352
2025-09-08 20:25:37,474 | INFO | input text tokens: 1344 # estimated
2025-09-08 20:25:37,474 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:25:37,474 | INFO | cost for input: $0.00169 USD
2025-09-08 20:25:37,474 | INFO | total output tokens: 2481
2025-09-08 20:25:37,475 | INFO | cost of output: $0.02481 USD
2025-09-08 20:25:37,475 | INFO | --got table grid emptiness info:
|Date|Reviewer|Rating|Raise Amount|New Pay Amnt|New Pay Per|New Position|Effective Date|Next Review|
|X| | |X|X| | |X|X|
2025-09-08 20:25:54,072 | INFO | llm gpt-5 api call took 16.597 seconds
2025-09-08 20:25:54,081 | INFO | total input tokens: 2061
2025-09-08 20:25:54,081 | INFO | input text tokens: 1423 # estimated
2025-09-08 20:25:54,082 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:25:54,082 | INFO | cost for input: $0.002576 USD
2025-09-08 20:25:54,082 | INFO | total output tokens: 424
2025-09-08 20:25:54,082 | INFO | cost of output: $0.00424 USD
2025-09-08 20:25:54,083 | INFO | done judging, ALL GOOD
2025-09-08 20:25:54,084 | INFO | -current table:
| Name         | Relationship   | Home Phone   | Work Phone   | Address   | City   | State   | Zip   | Country   |
|:-------------|:---------------|:-------------|:-------------|:----------|:-------|:--------|:------|:----------|
| Terri Rivers | Spouse         | 119-586-5181 |              |           |        |         |       |           |
2025-09-08 20:25:54,084 | INFO | -validating table: Emergency Contact Information
2025-09-08 20:25:54,084 | INFO | --figuring out table emptiness...
2025-09-08 20:26:05,292 | INFO | llm gpt-5-mini api call took 11.207 seconds
2025-09-08 20:26:05,301 | INFO | total input tokens: 3672
2025-09-08 20:26:05,301 | INFO | input text tokens: 2741 # estimated
2025-09-08 20:26:05,301 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:26:05,302 | INFO | cost for input: $0.00459 USD
2025-09-08 20:26:05,302 | INFO | total output tokens: 1030
2025-09-08 20:26:05,302 | INFO | cost of output: $0.0103 USD
2025-09-08 20:26:05,302 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:26:25,753 | INFO | llm gpt-5-mini api call took 20.450 seconds
2025-09-08 20:26:25,757 | INFO | total input tokens: 1236
2025-09-08 20:26:25,757 | INFO | input text tokens: 1228 # estimated
2025-09-08 20:26:25,757 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:26:25,757 | INFO | cost for input: $0.001545 USD
2025-09-08 20:26:25,758 | INFO | total output tokens: 2358
2025-09-08 20:26:25,758 | INFO | cost of output: $0.02358 USD
2025-09-08 20:26:25,758 | INFO | --got table grid emptiness info:
|Name|Relationship|Home Phone|Work Phone|Address|City|State|Zip|Country|
|---|---|---|---|---|---|---|---|---|
|X|X|X|||||||
2025-09-08 20:26:38,553 | INFO | llm gpt-5 api call took 12.794 seconds
2025-09-08 20:26:38,564 | INFO | total input tokens: 2044
2025-09-08 20:26:38,564 | INFO | input text tokens: 1406 # estimated
2025-09-08 20:26:38,565 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:26:38,565 | INFO | cost for input: $0.002555 USD
2025-09-08 20:26:38,565 | INFO | total output tokens: 296
2025-09-08 20:26:38,565 | INFO | cost of output: $0.00296 USD
2025-09-08 20:26:38,565 | INFO | done judging, ALL GOOD
2025-09-08 20:26:38,565 | INFO | started validating form fields
2025-09-08 20:26:38,566 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-08 20:26:38,566 | INFO | --current are:
Company Name : Velorynt Labs
Company Code : 37546
Period : 12/17/2024 to 12/26/2024
Employee Name : 
Address line 1 : 
City : 
State : 
Zip : 
Emp Id : 
SSN : 
2025-09-08 20:27:34,317 | INFO | llm gpt-5 api call took 55.743 seconds
2025-09-08 20:27:34,325 | INFO | total input tokens: 2098
2025-09-08 20:27:34,326 | INFO | input text tokens: 1460 # estimated
2025-09-08 20:27:34,326 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:27:34,326 | INFO | cost for input: $0.002622 USD
2025-09-08 20:27:34,326 | INFO | total output tokens: 896
2025-09-08 20:27:34,327 | INFO | cost of output: $0.00896 USD
2025-09-08 20:27:34,327 | INFO | done judging, ALL GOOD
2025-09-08 20:27:34,327 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-08 20:27:34,327 | INFO | --current are:
DOB (only date) : 
Gender : 
Marital Status : 
Status : 
Position : 
Title : 
Pay Group : 
Job Code : 
Emp Type : 
Statutory : 
2025-09-08 20:28:12,094 | INFO | llm gpt-5 api call took 37.762 seconds
2025-09-08 20:28:12,099 | INFO | total input tokens: 2077
2025-09-08 20:28:12,099 | INFO | input text tokens: 1439 # estimated
2025-09-08 20:28:12,100 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:28:12,100 | INFO | cost for input: $0.002596 USD
2025-09-08 20:28:12,100 | INFO | total output tokens: 706
2025-09-08 20:28:12,100 | INFO | cost of output: $0.00706 USD
2025-09-08 20:28:12,101 | INFO | done judging, ALL GOOD
2025-09-08 20:28:12,101 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-08 20:28:12,101 | INFO | --current are:
Seasonal : 
Domestic Emp : 
Probation : 
Home # : 
Work # : 
Ext. : 
Email : 
Mail Stop : 
Hire Date : 
Rehire Date : 
2025-09-08 20:28:33,786 | INFO | llm gpt-5 api call took 21.678 seconds
2025-09-08 20:28:33,792 | INFO | total input tokens: 2077
2025-09-08 20:28:33,792 | INFO | input text tokens: 1439 # estimated
2025-09-08 20:28:33,793 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:28:33,793 | INFO | cost for input: $0.002596 USD
2025-09-08 20:28:33,793 | INFO | total output tokens: 641
2025-09-08 20:28:33,794 | INFO | cost of output: $0.00641 USD
2025-09-08 20:28:33,794 | INFO | done judging, ALL GOOD
2025-09-08 20:28:33,794 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-08 20:28:33,794 | INFO | --current are:
Term Date : 
Term Reason : 
Adj Sen Date : 
Pension : 
Visa Type : 
Exp : 
Citizen : 
I9 Reverify : 
I9 Verified : 
Deceased : 
2025-09-08 20:29:17,189 | INFO | llm gpt-5 api call took 43.390 seconds
2025-09-08 20:29:17,195 | INFO | total input tokens: 2079
2025-09-08 20:29:17,195 | INFO | input text tokens: 1441 # estimated
2025-09-08 20:29:17,195 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:29:17,196 | INFO | cost for input: $0.000727 USD
2025-09-08 20:29:17,196 | INFO | total output tokens: 708
2025-09-08 20:29:17,196 | INFO | cost of output: $0.00708 USD
2025-09-08 20:29:17,196 | INFO | done judging, ALL GOOD
2025-09-08 20:29:17,197 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-08 20:29:17,197 | INFO | --current are:
Tax Form : 
WCC : 
EEOC : 
Supervisor ID : 
Name (supervisor name) : 
Def Comp : 
Union : 
Union Date : 
Collect Dues : 
Paid Init. Fees : 
2025-09-08 20:29:44,977 | INFO | llm gpt-5 api call took 27.776 seconds
2025-09-08 20:29:44,987 | INFO | total input tokens: 2082
2025-09-08 20:29:44,987 | INFO | input text tokens: 1444 # estimated
2025-09-08 20:29:44,988 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:29:44,988 | INFO | cost for input: $0.000731 USD
2025-09-08 20:29:44,988 | INFO | total output tokens: 583
2025-09-08 20:29:44,988 | INFO | cost of output: $0.00583 USD
2025-09-08 20:29:44,989 | INFO | done judging, ALL GOOD
2025-09-08 20:29:44,989 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-08 20:29:44,989 | INFO | --current are:
Veteran : 
Legal Rep : 
Nickname : 
surname : 
Prior Last : 
Disability : 
Smoker : 
AutoPay : 
Pay Frequency : 
OT Exempt : 
2025-09-08 20:30:18,258 | INFO | llm gpt-5 api call took 33.262 seconds
2025-09-08 20:30:18,264 | INFO | total input tokens: 2076
2025-09-08 20:30:18,264 | INFO | input text tokens: 1438 # estimated
2025-09-08 20:30:18,264 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:30:18,264 | INFO | cost for input: $0.002595 USD
2025-09-08 20:30:18,265 | INFO | total output tokens: 577
2025-09-08 20:30:18,265 | INFO | cost of output: $0.00577 USD
2025-09-08 20:30:18,265 | INFO | done judging, ALL GOOD
2025-09-08 20:30:18,265 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-08 20:30:18,266 | INFO | --current are:
Default Hours : 
Locations : 
Positions : 
2025-09-08 20:30:43,466 | INFO | llm gpt-5 api call took 25.193 seconds
2025-09-08 20:30:43,471 | INFO | total input tokens: 2054
2025-09-08 20:30:43,471 | INFO | input text tokens: 1416 # estimated
2025-09-08 20:30:43,471 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:30:43,471 | INFO | cost for input: $0.002567 USD
2025-09-08 20:30:43,471 | INFO | total output tokens: 849
2025-09-08 20:30:43,472 | INFO | cost of output: $0.00849 USD
2025-09-08 20:30:43,472 | INFO | done judging, ALL GOOD

2025-09-08 21:04:02,816 | INFO | started initial extraction for page 9
2025-09-08 21:04:33,200 | INFO | llm gpt-5 api call took 30.086 seconds
2025-09-08 21:04:33,203 | INFO | total input tokens: 1673
2025-09-08 21:04:33,203 | INFO | input text tokens: 1035 # estimated
2025-09-08 21:04:33,203 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:04:33,203 | INFO | cost for input: $0.002091 USD
2025-09-08 21:04:33,204 | INFO | total output tokens: 1100
2025-09-08 21:04:33,204 | INFO | cost of output: $0.011 USD
2025-09-08 21:04:33,204 | INFO | initial extraction of page data done.
2025-09-08 21:04:42,129 | INFO | got response with OCR coordinates info from azure doc intelligence for page 9
2025-09-08 21:04:42,129 | INFO | started validating tables
2025-09-08 21:04:42,142 | INFO | -current table:

2025-09-08 21:04:42,142 | INFO | -validating table: Rate/Salary Information
2025-09-08 21:04:42,143 | INFO | -current table:

2025-09-08 21:04:42,143 | INFO | -validating table: Tax Information (Employee)
2025-09-08 21:04:42,144 | INFO | -current table:

2025-09-08 21:04:42,144 | INFO | -validating table: Tax Information (Employer)
2025-09-08 21:04:42,144 | INFO | -current table:

2025-09-08 21:04:42,145 | INFO | -validating table: Deduction Information
2025-09-08 21:04:42,145 | INFO | -current table:

2025-09-08 21:04:42,145 | INFO | -validating table: Direct Deposit Information
2025-09-08 21:04:42,146 | INFO | -current table:

2025-09-08 21:04:42,146 | INFO | -validating table: Fringe Benefit Information
2025-09-08 21:04:42,146 | INFO | -current table:

2025-09-08 21:04:42,147 | INFO | -validating table: Benefit Accrual Information
2025-09-08 21:04:42,148 | INFO | -current table:
| Date       | Reviewer   |   Rating |   Raise Amount |   New Pay Amnt | New Pay Per   | New Position   | Effective Date   | Next Review   |
|:-----------|:-----------|---------:|---------------:|---------------:|:--------------|:---------------|:-----------------|:--------------|
| 08/21/2017 |            |        1 |              1 |             13 |               |                | 08/07/2017       | 01/01/1900    |
2025-09-08 21:04:42,148 | INFO | -validating table: Review Information
2025-09-08 21:04:42,148 | INFO | --figuring out table emptiness...
2025-09-08 21:04:57,922 | INFO | llm gpt-5-mini api call took 15.774 seconds
2025-09-08 21:04:57,926 | INFO | total input tokens: 3846
2025-09-08 21:04:57,926 | INFO | input text tokens: 2915 # estimated
2025-09-08 21:04:57,926 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 21:04:57,927 | INFO | cost for input: $0.004808 USD
2025-09-08 21:04:57,927 | INFO | total output tokens: 1383
2025-09-08 21:04:57,927 | INFO | cost of output: $0.01383 USD
2025-09-08 21:04:57,927 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 21:05:22,887 | INFO | llm gpt-5-mini api call took 24.960 seconds
2025-09-08 21:05:22,890 | INFO | total input tokens: 1346
2025-09-08 21:05:22,890 | INFO | input text tokens: 1338 # estimated
2025-09-08 21:05:22,890 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 21:05:22,890 | INFO | cost for input: $0.001682 USD
2025-09-08 21:05:22,890 | INFO | total output tokens: 2289
2025-09-08 21:05:22,890 | INFO | cost of output: $0.02289 USD
2025-09-08 21:05:22,890 | INFO | --got table grid emptiness info:
|Date|Reviewer|Rating|Raise Amount|New Pay Amnt|New Pay Per|New Position|Effective Date|Next Review|
|X| | |X|X| | |X|X|
2025-09-08 21:05:49,524 | INFO | llm gpt-5 api call took 26.633 seconds
2025-09-08 21:05:49,527 | INFO | total input tokens: 2073
2025-09-08 21:05:49,527 | INFO | input text tokens: 1435 # estimated
2025-09-08 21:05:49,527 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:05:49,527 | INFO | cost for input: $0.002591 USD
2025-09-08 21:05:49,528 | INFO | total output tokens: 754
2025-09-08 21:05:49,528 | INFO | cost of output: $0.00754 USD
2025-09-08 21:05:49,528 | INFO | --found issues: [{'row': 1, 'column': 'Rating', 'status': 'wrong', 'feedback': 'Should be blank; no rating present in the source row.'}]
2025-09-08 21:06:59,238 | INFO | llm gpt-5-mini api call took 69.710 seconds
2025-09-08 21:06:59,241 | INFO | total input tokens: 1453
2025-09-08 21:06:59,242 | INFO | input text tokens: 522 # estimated
2025-09-08 21:06:59,242 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 21:06:59,242 | INFO | cost for input: $0.001816 USD
2025-09-08 21:06:59,242 | INFO | total output tokens: 527
2025-09-08 21:06:59,242 | INFO | cost of output: $0.00527 USD
2025-09-08 21:06:59,244 | INFO | --corrected as:
| Date       | Reviewer   | Rating   |   Raise Amount |   New Pay Amnt | New Pay Per   | New Position   | Effective Date   | Next Review   |
|:-----------|:-----------|:---------|---------------:|---------------:|:--------------|:---------------|:-----------------|:--------------|
| 08/21/2017 |            |          |              1 |             13 |               |                | 08/07/2017       | 01/01/1900    |
2025-09-08 21:06:59,244 | INFO | -revalidating table: Review Information
2025-09-08 21:07:21,355 | INFO | llm gpt-5 api call took 22.110 seconds
2025-09-08 21:07:21,358 | INFO | total input tokens: 2071
2025-09-08 21:07:21,358 | INFO | input text tokens: 1433 # estimated
2025-09-08 21:07:21,358 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:07:21,358 | INFO | cost for input: $0.002589 USD
2025-09-08 21:07:21,359 | INFO | total output tokens: 488
2025-09-08 21:07:21,359 | INFO | cost of output: $0.00488 USD
2025-09-08 21:07:21,359 | INFO | done judging, ALL GOOD
2025-09-08 21:07:21,360 | INFO | -current table:
| Name          | Relationship   | Home Phone   | Work Phone   | Address   | City   | State   | Zip   | Country   |
|:--------------|:---------------|:-------------|:-------------|:----------|:-------|:--------|:------|:----------|
| Daniel Carter | Son            | 509-308-5675 |              |           |        |         |       |           |
| Joshua Powell | Daughter       | 931-098-1556 |              |           |        |         |       |           |
2025-09-08 21:07:21,361 | INFO | -validating table: Emergency Contact Information
2025-09-08 21:07:21,361 | INFO | --figuring out table emptiness...
2025-09-08 21:07:34,932 | INFO | llm gpt-5-mini api call took 13.570 seconds
2025-09-08 21:07:34,936 | INFO | total input tokens: 3849
2025-09-08 21:07:34,936 | INFO | input text tokens: 2918 # estimated
2025-09-08 21:07:34,936 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 21:07:34,936 | INFO | cost for input: $0.004811 USD
2025-09-08 21:07:34,937 | INFO | total output tokens: 1250
2025-09-08 21:07:34,937 | INFO | cost of output: $0.0125 USD
2025-09-08 21:07:34,937 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 21:07:44,850 | INFO | llm gpt-5-mini api call took 9.913 seconds
2025-09-08 21:07:44,852 | INFO | total input tokens: 1520
2025-09-08 21:07:44,852 | INFO | input text tokens: 1512 # estimated
2025-09-08 21:07:44,853 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 21:07:44,853 | INFO | cost for input: $0.0019 USD
2025-09-08 21:07:44,853 | INFO | total output tokens: 1032
2025-09-08 21:07:44,853 | INFO | cost of output: $0.01032 USD
2025-09-08 21:07:44,854 | INFO | --got table grid emptiness info:
|Name|Relationship|Home Phone|Work Phone|Address|City|State|Zip|Country|
|---|---|---|---|---|---|---|---|---|
|X|X|X| | | | | | |
|X|X|X| | | | | | |
2025-09-08 21:07:58,372 | INFO | llm gpt-5 api call took 13.518 seconds
2025-09-08 21:07:58,376 | INFO | total input tokens: 2099
2025-09-08 21:07:58,376 | INFO | input text tokens: 1461 # estimated
2025-09-08 21:07:58,376 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:07:58,376 | INFO | cost for input: $0.00104 USD
2025-09-08 21:07:58,376 | INFO | total output tokens: 360
2025-09-08 21:07:58,377 | INFO | cost of output: $0.0036 USD
2025-09-08 21:07:58,377 | INFO | done judging, ALL GOOD
2025-09-08 21:07:58,377 | INFO | started validating form fields
2025-09-08 21:07:58,378 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-08 21:07:58,378 | INFO | --current are:
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
2025-09-08 21:08:27,896 | INFO | llm gpt-5 api call took 29.513 seconds
2025-09-08 21:08:27,899 | INFO | total input tokens: 2133
2025-09-08 21:08:27,899 | INFO | input text tokens: 1495 # estimated
2025-09-08 21:08:27,900 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:08:27,900 | INFO | cost for input: $0.002666 USD
2025-09-08 21:08:27,900 | INFO | total output tokens: 896
2025-09-08 21:08:27,900 | INFO | cost of output: $0.00896 USD
2025-09-08 21:08:27,901 | INFO | done judging, ALL GOOD
2025-09-08 21:08:27,901 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-08 21:08:27,901 | INFO | --current are:
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
2025-09-08 21:08:52,022 | INFO | llm gpt-5 api call took 24.116 seconds
2025-09-08 21:08:52,026 | INFO | total input tokens: 2112
2025-09-08 21:08:52,026 | INFO | input text tokens: 1474 # estimated
2025-09-08 21:08:52,026 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:08:52,026 | INFO | cost for input: $0.00264 USD
2025-09-08 21:08:52,026 | INFO | total output tokens: 834
2025-09-08 21:08:52,027 | INFO | cost of output: $0.00834 USD
2025-09-08 21:08:52,027 | INFO | done judging, ALL GOOD
2025-09-08 21:08:52,027 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-08 21:08:52,027 | INFO | --current are:
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
2025-09-08 21:09:20,201 | INFO | llm gpt-5 api call took 28.170 seconds
2025-09-08 21:09:20,204 | INFO | total input tokens: 2112
2025-09-08 21:09:20,204 | INFO | input text tokens: 1474 # estimated
2025-09-08 21:09:20,204 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:09:20,204 | INFO | cost for input: $0.00264 USD
2025-09-08 21:09:20,205 | INFO | total output tokens: 833
2025-09-08 21:09:20,205 | INFO | cost of output: $0.00833 USD
2025-09-08 21:09:20,205 | INFO | done judging, ALL GOOD
2025-09-08 21:09:20,205 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-08 21:09:20,205 | INFO | --current are:
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
2025-09-08 21:09:41,412 | INFO | llm gpt-5 api call took 21.202 seconds
2025-09-08 21:09:41,415 | INFO | total input tokens: 2114
2025-09-08 21:09:41,416 | INFO | input text tokens: 1476 # estimated
2025-09-08 21:09:41,416 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:09:41,416 | INFO | cost for input: $0.002642 USD
2025-09-08 21:09:41,416 | INFO | total output tokens: 644
2025-09-08 21:09:41,416 | INFO | cost of output: $0.00644 USD
2025-09-08 21:09:41,417 | INFO | done judging, ALL GOOD
2025-09-08 21:09:41,417 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-08 21:09:41,417 | INFO | --current are:
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
2025-09-08 21:10:00,103 | INFO | llm gpt-5 api call took 18.681 seconds
2025-09-08 21:10:00,106 | INFO | total input tokens: 2117
2025-09-08 21:10:00,106 | INFO | input text tokens: 1479 # estimated
2025-09-08 21:10:00,106 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:10:00,106 | INFO | cost for input: $0.002646 USD
2025-09-08 21:10:00,106 | INFO | total output tokens: 775
2025-09-08 21:10:00,107 | INFO | cost of output: $0.00775 USD
2025-09-08 21:10:00,107 | INFO | done judging, ALL GOOD
2025-09-08 21:10:00,107 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-08 21:10:00,107 | INFO | --current are:
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
2025-09-08 21:10:22,619 | INFO | llm gpt-5 api call took 22.508 seconds
2025-09-08 21:10:22,622 | INFO | total input tokens: 2111
2025-09-08 21:10:22,623 | INFO | input text tokens: 1473 # estimated
2025-09-08 21:10:22,623 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:10:22,623 | INFO | cost for input: $0.000623 USD
2025-09-08 21:10:22,623 | INFO | total output tokens: 577
2025-09-08 21:10:22,623 | INFO | cost of output: $0.00577 USD
2025-09-08 21:10:22,623 | INFO | done judging, ALL GOOD
2025-09-08 21:10:22,624 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-08 21:10:22,624 | INFO | --current are:
Default Hours : 
Locations : 
Positions : 
2025-09-08 21:10:38,781 | INFO | llm gpt-5 api call took 16.153 seconds
2025-09-08 21:10:38,785 | INFO | total input tokens: 2089
2025-09-08 21:10:38,785 | INFO | input text tokens: 1451 # estimated
2025-09-08 21:10:38,785 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:10:38,785 | INFO | cost for input: $0.002611 USD
2025-09-08 21:10:38,785 | INFO | total output tokens: 593
2025-09-08 21:10:38,785 | INFO | cost of output: $0.00593 USD
2025-09-08 21:10:38,785 | INFO | done judging, ALL GOOD

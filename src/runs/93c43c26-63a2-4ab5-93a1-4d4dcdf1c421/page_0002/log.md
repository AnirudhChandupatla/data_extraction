2025-09-08 20:05:29,665 | INFO | started initial extraction for page 2
2025-09-08 20:06:06,633 | INFO | llm gpt-5 api call took 36.515 seconds
2025-09-08 20:06:07,198 | INFO | total input tokens: 1635
2025-09-08 20:06:07,199 | INFO | input text tokens: 997 # estimated
2025-09-08 20:06:07,199 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:06:07,199 | INFO | cost for input: $0.002044 USD
2025-09-08 20:06:07,199 | INFO | total output tokens: 969
2025-09-08 20:06:07,200 | INFO | cost of output: $0.00969 USD
2025-09-08 20:06:07,201 | INFO | initial extraction of page data done.
2025-09-08 20:06:12,508 | INFO | got response with OCR coordinates info from azure doc intelligence for page 2
2025-09-08 20:06:12,509 | INFO | started validating tables
2025-09-08 20:06:12,522 | INFO | -current table:

2025-09-08 20:06:12,522 | INFO | -validating table: Rate/Salary Information
2025-09-08 20:06:12,523 | INFO | -current table:

2025-09-08 20:06:12,523 | INFO | -validating table: Tax Information (Employee)
2025-09-08 20:06:12,524 | INFO | -current table:

2025-09-08 20:06:12,525 | INFO | -validating table: Tax Information (Employer)
2025-09-08 20:06:12,525 | INFO | -current table:

2025-09-08 20:06:12,526 | INFO | -validating table: Deduction Information
2025-09-08 20:06:12,526 | INFO | -current table:

2025-09-08 20:06:12,527 | INFO | -validating table: Direct Deposit Information
2025-09-08 20:06:12,527 | INFO | -current table:

2025-09-08 20:06:12,527 | INFO | -validating table: Fringe Benefit Information
2025-09-08 20:06:12,528 | INFO | -current table:

2025-09-08 20:06:12,528 | INFO | -validating table: Benefit Accrual Information
2025-09-08 20:06:12,529 | INFO | -current table:

2025-09-08 20:06:12,529 | INFO | -validating table: Review Information
2025-09-08 20:06:12,530 | INFO | -current table:
| Name          | Relationship   | Home Phone   | Work Phone   | Address           | City         | State   |   Zip | Country   |
|:--------------|:---------------|:-------------|:-------------|:------------------|:-------------|:--------|------:|:----------|
| Alexa Taylor  | Partner        | 276-237-7575 |              | 992 Maria Plain   | Jamesborough | PR      | 52030 |           |
| Nicole Miller | Brother        | 149-629-1234 |              | 2737 Sexton Glens | Thomasport   | PR      | 55119 |           |
2025-09-08 20:06:12,536 | INFO | -validating table: Emergency Contact Information
2025-09-08 20:06:12,537 | INFO | --figuring out table emptiness...
2025-09-08 20:06:49,312 | INFO | llm gpt-5-mini api call took 36.775 seconds
2025-09-08 20:06:49,318 | INFO | total input tokens: 3519
2025-09-08 20:06:49,318 | INFO | input text tokens: 2588 # estimated
2025-09-08 20:06:49,318 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:06:49,318 | INFO | cost for input: $0.004399 USD
2025-09-08 20:06:49,318 | INFO | total output tokens: 3271
2025-09-08 20:06:49,319 | INFO | cost of output: $0.03271 USD
2025-09-08 20:06:49,319 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:07:08,390 | INFO | llm gpt-5-mini api call took 19.071 seconds
2025-09-08 20:07:08,393 | INFO | total input tokens: 1749
2025-09-08 20:07:08,394 | INFO | input text tokens: 1741 # estimated
2025-09-08 20:07:08,394 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:07:08,394 | INFO | cost for input: $0.002186 USD
2025-09-08 20:07:08,394 | INFO | total output tokens: 2252
2025-09-08 20:07:08,394 | INFO | cost of output: $0.02252 USD
2025-09-08 20:07:08,394 | INFO | --got table grid emptiness info:
|Name|Relationship|Home Phone|Work Phone|Address|City|State|Zip|Country|
|---|---|---|---|---|---|---|---|---|
|X|X|X||X|X|X|X||
|X|X|X||X|X|X|X||
2025-09-08 20:07:36,972 | INFO | llm gpt-5 api call took 28.578 seconds
2025-09-08 20:07:36,975 | INFO | total input tokens: 2086
2025-09-08 20:07:36,976 | INFO | input text tokens: 1448 # estimated
2025-09-08 20:07:36,976 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:07:36,976 | INFO | cost for input: $0.002608 USD
2025-09-08 20:07:36,976 | INFO | total output tokens: 808
2025-09-08 20:07:36,976 | INFO | cost of output: $0.00808 USD
2025-09-08 20:07:36,976 | INFO | done judging, ALL GOOD
2025-09-08 20:07:36,976 | INFO | started validating form fields
2025-09-08 20:07:36,977 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-08 20:07:36,977 | INFO | --current are:
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
2025-09-08 20:08:04,658 | INFO | llm gpt-5 api call took 27.677 seconds
2025-09-08 20:08:04,661 | INFO | total input tokens: 2012
2025-09-08 20:08:04,661 | INFO | input text tokens: 1374 # estimated
2025-09-08 20:08:04,661 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:08:04,662 | INFO | cost for input: $0.002515 USD
2025-09-08 20:08:04,662 | INFO | total output tokens: 896
2025-09-08 20:08:04,662 | INFO | cost of output: $0.00896 USD
2025-09-08 20:08:04,662 | INFO | done judging, ALL GOOD
2025-09-08 20:08:04,662 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-08 20:08:04,662 | INFO | --current are:
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
2025-09-08 20:08:31,421 | INFO | llm gpt-5 api call took 26.755 seconds
2025-09-08 20:08:31,424 | INFO | total input tokens: 1991
2025-09-08 20:08:31,424 | INFO | input text tokens: 1353 # estimated
2025-09-08 20:08:31,425 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:08:31,425 | INFO | cost for input: $0.002489 USD
2025-09-08 20:08:31,425 | INFO | total output tokens: 514
2025-09-08 20:08:31,425 | INFO | cost of output: $0.00514 USD
2025-09-08 20:08:31,426 | INFO | done judging, ALL GOOD
2025-09-08 20:08:31,426 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-08 20:08:31,426 | INFO | --current are:
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
2025-09-08 20:09:10,576 | INFO | llm gpt-5 api call took 39.146 seconds
2025-09-08 20:09:10,580 | INFO | total input tokens: 1991
2025-09-08 20:09:10,580 | INFO | input text tokens: 1353 # estimated
2025-09-08 20:09:10,580 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:09:10,580 | INFO | cost for input: $0.002489 USD
2025-09-08 20:09:10,580 | INFO | total output tokens: 769
2025-09-08 20:09:10,581 | INFO | cost of output: $0.00769 USD
2025-09-08 20:09:10,581 | INFO | done judging, ALL GOOD
2025-09-08 20:09:10,581 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-08 20:09:10,581 | INFO | --current are:
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
2025-09-08 20:09:28,007 | INFO | llm gpt-5 api call took 17.422 seconds
2025-09-08 20:09:28,010 | INFO | total input tokens: 1993
2025-09-08 20:09:28,010 | INFO | input text tokens: 1355 # estimated
2025-09-08 20:09:28,011 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:09:28,011 | INFO | cost for input: $0.002491 USD
2025-09-08 20:09:28,011 | INFO | total output tokens: 708
2025-09-08 20:09:28,011 | INFO | cost of output: $0.00708 USD
2025-09-08 20:09:28,011 | INFO | done judging, ALL GOOD
2025-09-08 20:09:28,011 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-08 20:09:28,012 | INFO | --current are:
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
2025-09-08 20:09:51,032 | INFO | llm gpt-5 api call took 23.017 seconds
2025-09-08 20:09:51,035 | INFO | total input tokens: 1996
2025-09-08 20:09:51,035 | INFO | input text tokens: 1358 # estimated
2025-09-08 20:09:51,035 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:09:51,035 | INFO | cost for input: $0.002495 USD
2025-09-08 20:09:51,036 | INFO | total output tokens: 647
2025-09-08 20:09:51,036 | INFO | cost of output: $0.00647 USD
2025-09-08 20:09:51,036 | INFO | done judging, ALL GOOD
2025-09-08 20:09:51,036 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-08 20:09:51,036 | INFO | --current are:
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
2025-09-08 20:10:15,830 | INFO | llm gpt-5 api call took 24.790 seconds
2025-09-08 20:10:15,833 | INFO | total input tokens: 1990
2025-09-08 20:10:15,833 | INFO | input text tokens: 1352 # estimated
2025-09-08 20:10:15,834 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:10:15,834 | INFO | cost for input: $0.002488 USD
2025-09-08 20:10:15,834 | INFO | total output tokens: 641
2025-09-08 20:10:15,834 | INFO | cost of output: $0.00641 USD
2025-09-08 20:10:15,835 | INFO | done judging, ALL GOOD
2025-09-08 20:10:15,835 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-08 20:10:15,835 | INFO | --current are:
Default Hours : 
Locations : 
Positions : 
2025-09-08 20:10:40,756 | INFO | llm gpt-5 api call took 24.917 seconds
2025-09-08 20:10:40,759 | INFO | total input tokens: 1968
2025-09-08 20:10:40,759 | INFO | input text tokens: 1330 # estimated
2025-09-08 20:10:40,759 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:10:40,760 | INFO | cost for input: $0.00246 USD
2025-09-08 20:10:40,760 | INFO | total output tokens: 657
2025-09-08 20:10:40,760 | INFO | cost of output: $0.00657 USD
2025-09-08 20:10:40,760 | INFO | done judging, ALL GOOD

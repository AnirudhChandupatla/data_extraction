2025-09-09 05:40:33,311 | INFO | started initial extraction for page 2
2025-09-09 05:41:21,291 | INFO | llm gpt-5 api call took 47.575 seconds
2025-09-09 05:41:21,996 | INFO | total input tokens: 1635
2025-09-09 05:41:21,996 | INFO | input text tokens: 997 # estimated
2025-09-09 05:41:21,997 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:41:21,997 | INFO | cost for input: $0.002044 USD
2025-09-09 05:41:21,997 | INFO | total output tokens: 905
2025-09-09 05:41:21,997 | INFO | cost of output: $0.00905 USD
2025-09-09 05:41:21,998 | INFO | initial extraction of page data done.
2025-09-09 05:41:27,490 | INFO | got response with OCR coordinates info from azure doc intelligence for page 2
2025-09-09 05:41:27,490 | INFO | started validating tables
2025-09-09 05:41:27,569 | INFO | -current table:

2025-09-09 05:41:27,569 | INFO | -validating table: Rate/Salary Information
2025-09-09 05:41:27,570 | INFO | -current table:

2025-09-09 05:41:27,571 | INFO | -validating table: Tax Information (Employee)
2025-09-09 05:41:27,571 | INFO | -current table:

2025-09-09 05:41:27,571 | INFO | -validating table: Tax Information (Employer)
2025-09-09 05:41:27,572 | INFO | -current table:

2025-09-09 05:41:27,572 | INFO | -validating table: Deduction Information
2025-09-09 05:41:27,573 | INFO | -current table:

2025-09-09 05:41:27,573 | INFO | -validating table: Direct Deposit Information
2025-09-09 05:41:27,574 | INFO | -current table:

2025-09-09 05:41:27,574 | INFO | -validating table: Fringe Benefit Information
2025-09-09 05:41:27,574 | INFO | -current table:

2025-09-09 05:41:27,574 | INFO | -validating table: Benefit Accrual Information
2025-09-09 05:41:27,575 | INFO | -current table:

2025-09-09 05:41:27,575 | INFO | -validating table: Review Information
2025-09-09 05:41:27,593 | INFO | -current table:
| Name          | Relationship   | Home Phone   | Work Phone   | Address           | City         | State   |   Zip | Country   |
|:--------------|:---------------|:-------------|:-------------|:------------------|:-------------|:--------|------:|:----------|
| Alexa Taylor  | Partner        | 276-237-7575 |              | 992 Maria Plain   | Jamesborough | PR      | 52030 |           |
| Nicole Miller | Brother        | 149-629-1234 |              | 2737 Sexton Glens | Thomasport   | PR      | 55119 |           |
2025-09-09 05:41:27,594 | INFO | -validating table: Emergency Contact Information
2025-09-09 05:41:27,594 | INFO | --figuring out table emptiness...
2025-09-09 05:41:45,184 | INFO | llm gpt-5-mini api call took 17.590 seconds
2025-09-09 05:41:45,189 | INFO | total input tokens: 3519
2025-09-09 05:41:45,189 | INFO | input text tokens: 2588 # estimated
2025-09-09 05:41:45,189 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:41:45,189 | INFO | cost for input: $0.004399 USD
2025-09-09 05:41:45,189 | INFO | total output tokens: 2029
2025-09-09 05:41:45,189 | INFO | cost of output: $0.02029 USD
2025-09-09 05:41:45,190 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 05:42:11,169 | INFO | llm gpt-5-mini api call took 25.979 seconds
2025-09-09 05:42:11,174 | INFO | total input tokens: 2092
2025-09-09 05:42:11,174 | INFO | input text tokens: 2084 # estimated
2025-09-09 05:42:11,174 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 05:42:11,174 | INFO | cost for input: $0.002615 USD
2025-09-09 05:42:11,175 | INFO | total output tokens: 3468
2025-09-09 05:42:11,175 | INFO | cost of output: $0.03468 USD
2025-09-09 05:42:11,175 | INFO | --got table grid emptiness info:
|Name|Relationship|Home Phone|Work Phone|Address|City|State|Zip|Country|
|---|---|---|---|---|---|---|---|---|
|X|X|X||X|X|X|X||
|X|X|X||X|X|X|X||
2025-09-09 05:42:28,456 | INFO | llm gpt-5 api call took 17.281 seconds
2025-09-09 05:42:28,460 | INFO | total input tokens: 2086
2025-09-09 05:42:28,460 | INFO | input text tokens: 1448 # estimated
2025-09-09 05:42:28,460 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:42:28,460 | INFO | cost for input: $0.002608 USD
2025-09-09 05:42:28,460 | INFO | total output tokens: 680
2025-09-09 05:42:28,460 | INFO | cost of output: $0.0068 USD
2025-09-09 05:42:28,461 | INFO | done judging, ALL GOOD
2025-09-09 05:42:28,461 | INFO | started validating form fields
2025-09-09 05:42:28,461 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-09 05:42:28,461 | INFO | --current are:
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
2025-09-09 05:42:40,430 | INFO | llm gpt-5 api call took 11.965 seconds
2025-09-09 05:42:40,433 | INFO | total input tokens: 2012
2025-09-09 05:42:40,433 | INFO | input text tokens: 1374 # estimated
2025-09-09 05:42:40,434 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:42:40,434 | INFO | cost for input: $0.002515 USD
2025-09-09 05:42:40,434 | INFO | total output tokens: 576
2025-09-09 05:42:40,434 | INFO | cost of output: $0.00576 USD
2025-09-09 05:42:40,434 | INFO | done judging, ALL GOOD
2025-09-09 05:42:40,434 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-09 05:42:40,435 | INFO | --current are:
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
2025-09-09 05:42:57,709 | INFO | llm gpt-5 api call took 17.271 seconds
2025-09-09 05:42:57,712 | INFO | total input tokens: 1991
2025-09-09 05:42:57,713 | INFO | input text tokens: 1353 # estimated
2025-09-09 05:42:57,713 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:42:57,713 | INFO | cost for input: $0.002489 USD
2025-09-09 05:42:57,713 | INFO | total output tokens: 642
2025-09-09 05:42:57,713 | INFO | cost of output: $0.00642 USD
2025-09-09 05:42:57,714 | INFO | done judging, ALL GOOD
2025-09-09 05:42:57,714 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-09 05:42:57,714 | INFO | --current are:
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
2025-09-09 05:43:23,333 | INFO | llm gpt-5 api call took 25.615 seconds
2025-09-09 05:43:23,336 | INFO | total input tokens: 1991
2025-09-09 05:43:23,337 | INFO | input text tokens: 1353 # estimated
2025-09-09 05:43:23,337 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:43:23,337 | INFO | cost for input: $0.002489 USD
2025-09-09 05:43:23,337 | INFO | total output tokens: 705
2025-09-09 05:43:23,337 | INFO | cost of output: $0.00705 USD
2025-09-09 05:43:23,338 | INFO | done judging, ALL GOOD
2025-09-09 05:43:23,338 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-09 05:43:23,338 | INFO | --current are:
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
2025-09-09 05:43:38,441 | INFO | llm gpt-5 api call took 15.099 seconds
2025-09-09 05:43:38,445 | INFO | total input tokens: 1993
2025-09-09 05:43:38,445 | INFO | input text tokens: 1355 # estimated
2025-09-09 05:43:38,445 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:43:38,445 | INFO | cost for input: $0.002491 USD
2025-09-09 05:43:38,445 | INFO | total output tokens: 580
2025-09-09 05:43:38,445 | INFO | cost of output: $0.0058 USD
2025-09-09 05:43:38,446 | INFO | done judging, ALL GOOD
2025-09-09 05:43:38,446 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-09 05:43:38,446 | INFO | --current are:
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
2025-09-09 05:44:10,556 | INFO | llm gpt-5 api call took 32.106 seconds
2025-09-09 05:44:10,559 | INFO | total input tokens: 1996
2025-09-09 05:44:10,560 | INFO | input text tokens: 1358 # estimated
2025-09-09 05:44:10,560 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:44:10,560 | INFO | cost for input: $0.002495 USD
2025-09-09 05:44:10,560 | INFO | total output tokens: 1031
2025-09-09 05:44:10,561 | INFO | cost of output: $0.01031 USD
2025-09-09 05:44:10,561 | INFO | done judging, ALL GOOD
2025-09-09 05:44:10,561 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 05:44:10,561 | INFO | --current are:
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
2025-09-09 05:44:28,300 | INFO | llm gpt-5 api call took 17.735 seconds
2025-09-09 05:44:28,303 | INFO | total input tokens: 1990
2025-09-09 05:44:28,303 | INFO | input text tokens: 1352 # estimated
2025-09-09 05:44:28,303 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:44:28,303 | INFO | cost for input: $0.002488 USD
2025-09-09 05:44:28,304 | INFO | total output tokens: 513
2025-09-09 05:44:28,304 | INFO | cost of output: $0.00513 USD
2025-09-09 05:44:28,304 | INFO | done judging, ALL GOOD
2025-09-09 05:44:28,304 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-09 05:44:28,305 | INFO | --current are:
Default Hours : 
Locations : 
Positions : 
2025-09-09 05:44:52,140 | INFO | llm gpt-5 api call took 23.832 seconds
2025-09-09 05:44:52,143 | INFO | total input tokens: 1968
2025-09-09 05:44:52,144 | INFO | input text tokens: 1330 # estimated
2025-09-09 05:44:52,144 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:44:52,144 | INFO | cost for input: $0.00246 USD
2025-09-09 05:44:52,144 | INFO | total output tokens: 1169
2025-09-09 05:44:52,144 | INFO | cost of output: $0.01169 USD
2025-09-09 05:44:52,144 | INFO | done judging, ALL GOOD

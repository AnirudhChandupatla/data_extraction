2025-09-09 05:59:03,093 | INFO | started initial extraction for page 4
2025-09-09 05:59:29,507 | INFO | llm gpt-5 api call took 26.098 seconds
2025-09-09 05:59:29,509 | INFO | total input tokens: 1661
2025-09-09 05:59:29,510 | INFO | input text tokens: 1023 # estimated
2025-09-09 05:59:29,510 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 05:59:29,510 | INFO | cost for input: $0.002076 USD
2025-09-09 05:59:29,510 | INFO | total output tokens: 906
2025-09-09 05:59:29,510 | INFO | cost of output: $0.00906 USD
2025-09-09 05:59:29,511 | INFO | initial extraction of page data done.
2025-09-09 05:59:35,008 | INFO | got response with OCR coordinates info from azure doc intelligence for page 4
2025-09-09 05:59:35,008 | INFO | started validating tables
2025-09-09 05:59:35,010 | INFO | -current table:

2025-09-09 05:59:35,010 | INFO | -validating table: Rate/Salary Information
2025-09-09 05:59:35,010 | INFO | -current table:

2025-09-09 05:59:35,011 | INFO | -validating table: Tax Information (Employee)
2025-09-09 05:59:35,012 | INFO | -current table:

2025-09-09 05:59:35,012 | INFO | -validating table: Tax Information (Employer)
2025-09-09 05:59:35,013 | INFO | -current table:

2025-09-09 05:59:35,013 | INFO | -validating table: Deduction Information
2025-09-09 05:59:35,014 | INFO | -current table:

2025-09-09 05:59:35,014 | INFO | -validating table: Direct Deposit Information
2025-09-09 05:59:35,014 | INFO | -current table:

2025-09-09 05:59:35,014 | INFO | -validating table: Fringe Benefit Information
2025-09-09 05:59:35,015 | INFO | -current table:

2025-09-09 05:59:35,015 | INFO | -validating table: Benefit Accrual Information
2025-09-09 05:59:35,016 | INFO | -current table:
| Date       | Reviewer   | Rating   |   Raise Amount |   New Pay Amnt | New Pay Per   | New Position   | Effective Dates   | Next Review   |
|:-----------|:-----------|:---------|---------------:|---------------:|:--------------|:---------------|:------------------|:--------------|
| 02/04/2018 |            |          |              0 |          17.83 |               |                | 02/04/2018        | 01/01/1900    |
2025-09-09 05:59:35,016 | INFO | -validating table: Review Information
2025-09-09 05:59:35,016 | INFO | --figuring out table emptiness...
2025-09-09 05:59:49,139 | INFO | llm gpt-5-mini api call took 14.122 seconds
2025-09-09 05:59:49,142 | INFO | total input tokens: 3695
2025-09-09 05:59:49,143 | INFO | input text tokens: 2764 # estimated
2025-09-09 05:59:49,143 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 05:59:49,143 | INFO | cost for input: $0.004619 USD
2025-09-09 05:59:49,143 | INFO | total output tokens: 1197
2025-09-09 05:59:49,143 | INFO | cost of output: $0.01197 USD
2025-09-09 05:59:49,143 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:00:17,434 | INFO | llm gpt-5-mini api call took 28.291 seconds
2025-09-09 06:00:17,437 | INFO | total input tokens: 1465
2025-09-09 06:00:17,437 | INFO | input text tokens: 1457 # estimated
2025-09-09 06:00:17,437 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:00:17,437 | INFO | cost for input: $0.001831 USD
2025-09-09 06:00:17,437 | INFO | total output tokens: 3565
2025-09-09 06:00:17,438 | INFO | cost of output: $0.03565 USD
2025-09-09 06:00:17,438 | INFO | --got table grid emptiness info:
|Date|Reviewer|Rating|Raise Amount|New Pay Amnt|New Pay Per|New Position|Effective Date|Next Review|
|X|||X|X|||X|X|
2025-09-09 06:00:41,346 | INFO | llm gpt-5 api call took 23.908 seconds
2025-09-09 06:00:41,348 | INFO | total input tokens: 2058
2025-09-09 06:00:41,349 | INFO | input text tokens: 1420 # estimated
2025-09-09 06:00:41,349 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:00:41,349 | INFO | cost for input: $0.002573 USD
2025-09-09 06:00:41,349 | INFO | total output tokens: 1533
2025-09-09 06:00:41,349 | INFO | cost of output: $0.01533 USD
2025-09-09 06:00:41,349 | INFO | --found issues: [{'row': 'all rows', 'column': 'Effective Date', 'status': 'wrong', 'feedback': "Header extracted as 'Effective Dates'; should be 'Effective Date' per schema. Cell value is correct."}]
2025-09-09 06:01:53,397 | INFO | llm gpt-5-mini api call took 72.047 seconds
2025-09-09 06:01:53,399 | INFO | total input tokens: 1452
2025-09-09 06:01:53,399 | INFO | input text tokens: 521 # estimated
2025-09-09 06:01:53,399 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:01:53,399 | INFO | cost for input: $0.001815 USD
2025-09-09 06:01:53,400 | INFO | total output tokens: 721
2025-09-09 06:01:53,400 | INFO | cost of output: $0.00721 USD
2025-09-09 06:01:53,401 | INFO | --corrected as:
| Date       | Reviewer   | Rating   |   Raise Amount |   New Pay Amnt | New Pay Per   | New Position   | Effective Date   | Next Review   |
|:-----------|:-----------|:---------|---------------:|---------------:|:--------------|:---------------|:-----------------|:--------------|
| 02/04/2018 |            |          |              0 |          17.83 |               |                | 02/04/2018       | 01/01/1900    |
2025-09-09 06:01:53,401 | INFO | -revalidating table: Review Information
2025-09-09 06:02:07,798 | INFO | llm gpt-5 api call took 14.396 seconds
2025-09-09 06:02:07,801 | INFO | total input tokens: 2057
2025-09-09 06:02:07,801 | INFO | input text tokens: 1419 # estimated
2025-09-09 06:02:07,801 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:02:07,801 | INFO | cost for input: $0.002571 USD
2025-09-09 06:02:07,802 | INFO | total output tokens: 488
2025-09-09 06:02:07,802 | INFO | cost of output: $0.00488 USD
2025-09-09 06:02:07,802 | INFO | done judging, ALL GOOD
2025-09-09 06:02:07,803 | INFO | -current table:
| Name         | Relationship   | Home Phone   | Work Phone   | Address   | City   | State   | Zip   | Country   |
|:-------------|:---------------|:-------------|:-------------|:----------|:-------|:--------|:------|:----------|
| Terri Rivers | Spouse         | 119-586-5181 |              |           |        |         |       |           |
2025-09-09 06:02:07,803 | INFO | -validating table: Emergency Contact Information
2025-09-09 06:02:07,803 | INFO | --figuring out table emptiness...
2025-09-09 06:02:20,159 | INFO | llm gpt-5-mini api call took 12.355 seconds
2025-09-09 06:02:20,163 | INFO | total input tokens: 3672
2025-09-09 06:02:20,163 | INFO | input text tokens: 2741 # estimated
2025-09-09 06:02:20,163 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 06:02:20,163 | INFO | cost for input: $0.00459 USD
2025-09-09 06:02:20,164 | INFO | total output tokens: 1606
2025-09-09 06:02:20,164 | INFO | cost of output: $0.01606 USD
2025-09-09 06:02:20,164 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 06:02:41,244 | INFO | llm gpt-5-mini api call took 21.080 seconds
2025-09-09 06:02:41,247 | INFO | total input tokens: 1349
2025-09-09 06:02:41,247 | INFO | input text tokens: 1341 # estimated
2025-09-09 06:02:41,247 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 06:02:41,247 | INFO | cost for input: $0.001686 USD
2025-09-09 06:02:41,247 | INFO | total output tokens: 3235
2025-09-09 06:02:41,247 | INFO | cost of output: $0.03235 USD
2025-09-09 06:02:41,248 | INFO | --got table grid emptiness info:
|Name|Relationship|Home Phone|Work Phone|Address|City|State|Zip|Country|
|X|X|X|||||||
2025-09-09 06:02:56,867 | INFO | llm gpt-5 api call took 15.619 seconds
2025-09-09 06:02:56,870 | INFO | total input tokens: 2025
2025-09-09 06:02:56,870 | INFO | input text tokens: 1387 # estimated
2025-09-09 06:02:56,870 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:02:56,870 | INFO | cost for input: $0.002531 USD
2025-09-09 06:02:56,870 | INFO | total output tokens: 488
2025-09-09 06:02:56,870 | INFO | cost of output: $0.00488 USD
2025-09-09 06:02:56,871 | INFO | done judging, ALL GOOD
2025-09-09 06:02:56,871 | INFO | started validating form fields
2025-09-09 06:02:56,871 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-09 06:02:56,871 | INFO | --current are:
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
2025-09-09 06:03:14,136 | INFO | llm gpt-5 api call took 17.260 seconds
2025-09-09 06:03:14,139 | INFO | total input tokens: 2098
2025-09-09 06:03:14,139 | INFO | input text tokens: 1460 # estimated
2025-09-09 06:03:14,139 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:03:14,139 | INFO | cost for input: $0.002622 USD
2025-09-09 06:03:14,139 | INFO | total output tokens: 704
2025-09-09 06:03:14,140 | INFO | cost of output: $0.00704 USD
2025-09-09 06:03:14,140 | INFO | done judging, ALL GOOD
2025-09-09 06:03:14,140 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-09 06:03:14,140 | INFO | --current are:
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
2025-09-09 06:03:27,922 | INFO | llm gpt-5 api call took 13.778 seconds
2025-09-09 06:03:27,925 | INFO | total input tokens: 2077
2025-09-09 06:03:27,925 | INFO | input text tokens: 1439 # estimated
2025-09-09 06:03:27,925 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:03:27,926 | INFO | cost for input: $0.002596 USD
2025-09-09 06:03:27,926 | INFO | total output tokens: 514
2025-09-09 06:03:27,926 | INFO | cost of output: $0.00514 USD
2025-09-09 06:03:27,926 | INFO | done judging, ALL GOOD
2025-09-09 06:03:27,926 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-09 06:03:27,926 | INFO | --current are:
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
2025-09-09 06:03:44,608 | INFO | llm gpt-5 api call took 16.678 seconds
2025-09-09 06:03:44,611 | INFO | total input tokens: 2077
2025-09-09 06:03:44,611 | INFO | input text tokens: 1439 # estimated
2025-09-09 06:03:44,612 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:03:44,612 | INFO | cost for input: $0.002596 USD
2025-09-09 06:03:44,612 | INFO | total output tokens: 833
2025-09-09 06:03:44,612 | INFO | cost of output: $0.00833 USD
2025-09-09 06:03:44,612 | INFO | done judging, ALL GOOD
2025-09-09 06:03:44,612 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-09 06:03:44,612 | INFO | --current are:
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
2025-09-09 06:04:03,505 | INFO | llm gpt-5 api call took 18.888 seconds
2025-09-09 06:04:03,508 | INFO | total input tokens: 2079
2025-09-09 06:04:03,508 | INFO | input text tokens: 1441 # estimated
2025-09-09 06:04:03,509 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:04:03,509 | INFO | cost for input: $0.002599 USD
2025-09-09 06:04:03,509 | INFO | total output tokens: 644
2025-09-09 06:04:03,509 | INFO | cost of output: $0.00644 USD
2025-09-09 06:04:03,509 | INFO | done judging, ALL GOOD
2025-09-09 06:04:03,509 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-09 06:04:03,509 | INFO | --current are:
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
2025-09-09 06:04:20,820 | INFO | llm gpt-5 api call took 17.307 seconds
2025-09-09 06:04:20,823 | INFO | total input tokens: 2082
2025-09-09 06:04:20,824 | INFO | input text tokens: 1444 # estimated
2025-09-09 06:04:20,824 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:04:20,824 | INFO | cost for input: $0.002603 USD
2025-09-09 06:04:20,824 | INFO | total output tokens: 583
2025-09-09 06:04:20,824 | INFO | cost of output: $0.00583 USD
2025-09-09 06:04:20,824 | INFO | done judging, ALL GOOD
2025-09-09 06:04:20,824 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 06:04:20,825 | INFO | --current are:
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
2025-09-09 06:04:35,209 | INFO | llm gpt-5 api call took 14.380 seconds
2025-09-09 06:04:35,212 | INFO | total input tokens: 2076
2025-09-09 06:04:35,212 | INFO | input text tokens: 1438 # estimated
2025-09-09 06:04:35,212 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:04:35,212 | INFO | cost for input: $0.002595 USD
2025-09-09 06:04:35,212 | INFO | total output tokens: 513
2025-09-09 06:04:35,212 | INFO | cost of output: $0.00513 USD
2025-09-09 06:04:35,213 | INFO | done judging, ALL GOOD
2025-09-09 06:04:35,213 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-09 06:04:35,213 | INFO | --current are:
Default Hours : 
Locations : 
Positions : 
2025-09-09 06:04:56,481 | INFO | llm gpt-5 api call took 21.264 seconds
2025-09-09 06:04:56,484 | INFO | total input tokens: 2054
2025-09-09 06:04:56,484 | INFO | input text tokens: 1416 # estimated
2025-09-09 06:04:56,484 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 06:04:56,484 | INFO | cost for input: $0.002567 USD
2025-09-09 06:04:56,485 | INFO | total output tokens: 657
2025-09-09 06:04:56,485 | INFO | cost of output: $0.00657 USD
2025-09-09 06:04:56,485 | INFO | done judging, ALL GOOD

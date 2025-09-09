2025-09-09 08:05:02,733 | INFO | started initial extraction for page 9
2025-09-09 08:05:22,969 | INFO | llm gpt-5 api call took 19.948 seconds
2025-09-09 08:05:22,973 | INFO | total input tokens: 1673
2025-09-09 08:05:22,973 | INFO | input text tokens: 1035 # estimated
2025-09-09 08:05:22,975 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 08:05:22,976 | INFO | cost for input: $0.002091 USD
2025-09-09 08:05:22,977 | INFO | total output tokens: 904
2025-09-09 08:05:22,978 | INFO | cost of output: $0.00904 USD
2025-09-09 08:05:22,979 | INFO | initial extraction of page data done.
2025-09-09 08:05:28,600 | INFO | got response with OCR coordinates info from azure doc intelligence for page 9
2025-09-09 08:05:28,601 | INFO | started validating tables
2025-09-09 08:05:28,604 | INFO | -current table:

2025-09-09 08:05:28,604 | INFO | -validating table: Rate/Salary Information
2025-09-09 08:05:28,606 | INFO | -current table:

2025-09-09 08:05:28,607 | INFO | -validating table: Tax Information (Employee)
2025-09-09 08:05:28,608 | INFO | -current table:

2025-09-09 08:05:28,609 | INFO | -validating table: Tax Information (Employer)
2025-09-09 08:05:28,611 | INFO | -current table:

2025-09-09 08:05:28,612 | INFO | -validating table: Deduction Information
2025-09-09 08:05:28,614 | INFO | -current table:

2025-09-09 08:05:28,615 | INFO | -validating table: Direct Deposit Information
2025-09-09 08:05:28,617 | INFO | -current table:

2025-09-09 08:05:28,617 | INFO | -validating table: Fringe Benefit Information
2025-09-09 08:05:28,619 | INFO | -current table:

2025-09-09 08:05:28,621 | INFO | -validating table: Benefit Accrual Information
2025-09-09 08:05:28,625 | INFO | -current table:
| Date       | Reviewer   |   Rating | Raise Amount   |   New Pay Amnt | New Pay Per   | New Position   | Effective Date   | Next Review   |
|:-----------|:-----------|---------:|:---------------|---------------:|:--------------|:---------------|:-----------------|:--------------|
| 08/21/2017 |            |        1 |                |             13 |               |                | 08/07/2017       | 01/01/1900    |
2025-09-09 08:05:28,626 | INFO | -validating table: Review Information
2025-09-09 08:05:28,627 | INFO | --figuring out table emptiness...
2025-09-09 08:05:43,602 | INFO | llm gpt-5-mini api call took 14.974 seconds
2025-09-09 08:05:43,607 | INFO | total input tokens: 3844
2025-09-09 08:05:43,608 | INFO | input text tokens: 2913 # estimated
2025-09-09 08:05:43,609 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 08:05:43,610 | INFO | cost for input: $0.004805 USD
2025-09-09 08:05:43,611 | INFO | total output tokens: 1575
2025-09-09 08:05:43,612 | INFO | cost of output: $0.01575 USD
2025-09-09 08:05:43,612 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 08:06:09,858 | INFO | llm gpt-5-mini api call took 26.245 seconds
2025-09-09 08:06:09,862 | INFO | total input tokens: 1459
2025-09-09 08:06:09,863 | INFO | input text tokens: 1451 # estimated
2025-09-09 08:06:09,864 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 08:06:09,865 | INFO | cost for input: $0.001824 USD
2025-09-09 08:06:09,866 | INFO | total output tokens: 3885
2025-09-09 08:06:09,867 | INFO | cost of output: $0.03885 USD
2025-09-09 08:06:09,868 | INFO | --got table grid emptiness info:
|Date|Reviewer|Rating|Raise Amount|New Pay Amnt|New Pay Per|New Position|Effective Date|Next Review|
|X|||X|X|||X|X|
2025-09-09 08:06:35,028 | INFO | llm gpt-5 api call took 25.159 seconds
2025-09-09 08:06:35,033 | INFO | total input tokens: 2087
2025-09-09 08:06:35,034 | INFO | input text tokens: 1449 # estimated
2025-09-09 08:06:35,035 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 08:06:35,036 | INFO | cost for input: $0.000881 USD
2025-09-09 08:06:35,037 | INFO | total output tokens: 1060
2025-09-09 08:06:35,037 | INFO | cost of output: $0.0106 USD
2025-09-09 08:06:35,038 | INFO | --found issues: [{'row': 1, 'column': 'Rating', 'status': 'wrong', 'feedback': 'Should be blank; value 1.00 belongs to Raise Amount.'}, {'row': 1, 'column': 'Raise Amount', 'status': 'wrong', 'feedback': 'Should be 1.00; extractor left it blank and placed it under Rating.'}]
2025-09-09 08:06:41,810 | INFO | llm gpt-5-mini api call took 6.770 seconds
2025-09-09 08:06:41,813 | INFO | total input tokens: 1485
2025-09-09 08:06:41,814 | INFO | input text tokens: 554 # estimated
2025-09-09 08:06:41,815 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 08:06:41,816 | INFO | cost for input: $0.001856 USD
2025-09-09 08:06:41,817 | INFO | total output tokens: 657
2025-09-09 08:06:41,818 | INFO | cost of output: $0.00657 USD
2025-09-09 08:06:41,820 | INFO | --corrected as:
| Date       | Reviewer   | Rating   |   Raise Amount |   New Pay Amnt | New Pay Per   | New Position   | Effective Date   | Next Review   |
|:-----------|:-----------|:---------|---------------:|---------------:|:--------------|:---------------|:-----------------|:--------------|
| 08/21/2017 |            |          |              1 |             13 |               |                | 08/07/2017       | 01/01/1900    |
2025-09-09 08:06:41,821 | INFO | -revalidating table: Review Information
2025-09-09 08:06:57,930 | INFO | llm gpt-5 api call took 16.106 seconds
2025-09-09 08:06:57,934 | INFO | total input tokens: 2087
2025-09-09 08:06:57,935 | INFO | input text tokens: 1449 # estimated
2025-09-09 08:06:57,936 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 08:06:57,937 | INFO | cost for input: $0.002609 USD
2025-09-09 08:06:57,938 | INFO | total output tokens: 680
2025-09-09 08:06:57,939 | INFO | cost of output: $0.0068 USD
2025-09-09 08:06:57,940 | INFO | done judging, ALL GOOD
2025-09-09 08:06:57,942 | INFO | -current table:
| Name          | Relationship   | Home Phone   | Work Phone   | Address   | City   | State   | Zip   | Country   |
|:--------------|:---------------|:-------------|:-------------|:----------|:-------|:--------|:------|:----------|
| Daniel Carter | Son            | 509-308-5675 |              |           |        |         |       |           |
| Joshua Powell | Daughter       | 931-098-1556 |              |           |        |         |       |           |
2025-09-09 08:06:57,943 | INFO | -validating table: Emergency Contact Information
2025-09-09 08:06:57,944 | INFO | --figuring out table emptiness...
2025-09-09 08:07:07,966 | INFO | llm gpt-5-mini api call took 10.021 seconds
2025-09-09 08:07:07,971 | INFO | total input tokens: 3849
2025-09-09 08:07:07,972 | INFO | input text tokens: 2918 # estimated
2025-09-09 08:07:07,973 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-09 08:07:07,974 | INFO | cost for input: $0.004811 USD
2025-09-09 08:07:07,975 | INFO | total output tokens: 1164
2025-09-09 08:07:07,976 | INFO | cost of output: $0.01164 USD
2025-09-09 08:07:07,977 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-09 08:07:31,062 | INFO | llm gpt-5-mini api call took 23.083 seconds
2025-09-09 08:07:31,066 | INFO | total input tokens: 1483
2025-09-09 08:07:31,067 | INFO | input text tokens: 1475 # estimated
2025-09-09 08:07:31,068 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-09 08:07:31,068 | INFO | cost for input: $0.001854 USD
2025-09-09 08:07:31,069 | INFO | total output tokens: 3400
2025-09-09 08:07:31,070 | INFO | cost of output: $0.034 USD
2025-09-09 08:07:31,071 | INFO | --got table grid emptiness info:
|Name|Relationship|Home Phone|Work Phone|Address|City|State|Zip|Country|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|||||||
|X|X|X|||||||
2025-09-09 08:07:50,288 | INFO | llm gpt-5 api call took 19.217 seconds
2025-09-09 08:07:50,292 | INFO | total input tokens: 2119
2025-09-09 08:07:50,293 | INFO | input text tokens: 1481 # estimated
2025-09-09 08:07:50,293 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 08:07:50,294 | INFO | cost for input: $0.002649 USD
2025-09-09 08:07:50,295 | INFO | total output tokens: 488
2025-09-09 08:07:50,297 | INFO | cost of output: $0.00488 USD
2025-09-09 08:07:50,298 | INFO | done judging, ALL GOOD
2025-09-09 08:07:50,299 | INFO | started validating form fields
2025-09-09 08:07:50,300 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-09 08:07:50,301 | INFO | --current are:
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
2025-09-09 08:08:02,283 | INFO | llm gpt-5 api call took 11.976 seconds
2025-09-09 08:08:02,287 | INFO | total input tokens: 2133
2025-09-09 08:08:02,288 | INFO | input text tokens: 1495 # estimated
2025-09-09 08:08:02,289 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 08:08:02,291 | INFO | cost for input: $0.002666 USD
2025-09-09 08:08:02,292 | INFO | total output tokens: 768
2025-09-09 08:08:02,292 | INFO | cost of output: $0.00768 USD
2025-09-09 08:08:02,294 | INFO | done judging, ALL GOOD
2025-09-09 08:08:02,295 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-09 08:08:02,296 | INFO | --current are:
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
2025-09-09 08:08:20,291 | INFO | llm gpt-5 api call took 17.988 seconds
2025-09-09 08:08:20,295 | INFO | total input tokens: 2112
2025-09-09 08:08:20,297 | INFO | input text tokens: 1474 # estimated
2025-09-09 08:08:20,297 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 08:08:20,298 | INFO | cost for input: $0.00264 USD
2025-09-09 08:08:20,299 | INFO | total output tokens: 706
2025-09-09 08:08:20,300 | INFO | cost of output: $0.00706 USD
2025-09-09 08:08:20,301 | INFO | done judging, ALL GOOD
2025-09-09 08:08:20,302 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-09 08:08:20,303 | INFO | --current are:
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
2025-09-09 08:08:31,915 | INFO | llm gpt-5 api call took 11.606 seconds
2025-09-09 08:08:31,920 | INFO | total input tokens: 2112
2025-09-09 08:08:31,921 | INFO | input text tokens: 1474 # estimated
2025-09-09 08:08:31,922 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 08:08:31,923 | INFO | cost for input: $0.00264 USD
2025-09-09 08:08:31,924 | INFO | total output tokens: 513
2025-09-09 08:08:31,924 | INFO | cost of output: $0.00513 USD
2025-09-09 08:08:31,925 | INFO | done judging, ALL GOOD
2025-09-09 08:08:31,926 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-09 08:08:31,927 | INFO | --current are:
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
2025-09-09 08:08:45,542 | INFO | llm gpt-5 api call took 13.609 seconds
2025-09-09 08:08:45,547 | INFO | total input tokens: 2114
2025-09-09 08:08:45,547 | INFO | input text tokens: 1476 # estimated
2025-09-09 08:08:45,548 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 08:08:45,549 | INFO | cost for input: $0.002642 USD
2025-09-09 08:08:45,550 | INFO | total output tokens: 516
2025-09-09 08:08:45,551 | INFO | cost of output: $0.00516 USD
2025-09-09 08:08:45,552 | INFO | done judging, ALL GOOD
2025-09-09 08:08:45,553 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-09 08:08:45,553 | INFO | --current are:
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
2025-09-09 08:09:04,584 | INFO | llm gpt-5 api call took 19.023 seconds
2025-09-09 08:09:04,588 | INFO | total input tokens: 2117
2025-09-09 08:09:04,589 | INFO | input text tokens: 1479 # estimated
2025-09-09 08:09:04,590 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 08:09:04,591 | INFO | cost for input: $0.002646 USD
2025-09-09 08:09:04,591 | INFO | total output tokens: 583
2025-09-09 08:09:04,592 | INFO | cost of output: $0.00583 USD
2025-09-09 08:09:04,593 | INFO | done judging, ALL GOOD
2025-09-09 08:09:04,595 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-09 08:09:04,596 | INFO | --current are:
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
2025-09-09 08:09:22,373 | INFO | llm gpt-5 api call took 17.772 seconds
2025-09-09 08:09:22,377 | INFO | total input tokens: 2111
2025-09-09 08:09:22,378 | INFO | input text tokens: 1473 # estimated
2025-09-09 08:09:22,379 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 08:09:22,380 | INFO | cost for input: $0.002639 USD
2025-09-09 08:09:22,380 | INFO | total output tokens: 641
2025-09-09 08:09:22,381 | INFO | cost of output: $0.00641 USD
2025-09-09 08:09:22,382 | INFO | done judging, ALL GOOD
2025-09-09 08:09:22,383 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-09 08:09:22,384 | INFO | --current are:
Default Hours : 
Locations : 
Positions : 
2025-09-09 08:09:37,643 | INFO | llm gpt-5 api call took 15.252 seconds
2025-09-09 08:09:37,648 | INFO | total input tokens: 2089
2025-09-09 08:09:37,648 | INFO | input text tokens: 1451 # estimated
2025-09-09 08:09:37,649 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-09 08:09:37,650 | INFO | cost for input: $0.002611 USD
2025-09-09 08:09:37,650 | INFO | total output tokens: 721
2025-09-09 08:09:37,652 | INFO | cost of output: $0.00721 USD
2025-09-09 08:09:37,653 | INFO | done judging, ALL GOOD

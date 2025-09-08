2025-09-08 20:47:44,581 | INFO | started initial extraction for page 6
2025-09-08 20:49:21,160 | INFO | llm gpt-5 api call took 96.200 seconds
2025-09-08 20:49:21,181 | INFO | total input tokens: 2405
2025-09-08 20:49:21,181 | INFO | input text tokens: 1767 # estimated
2025-09-08 20:49:21,182 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:49:21,182 | INFO | cost for input: $0.003006 USD
2025-09-08 20:49:21,182 | INFO | total output tokens: 2877
2025-09-08 20:49:21,182 | INFO | cost of output: $0.02877 USD
2025-09-08 20:49:21,183 | INFO | initial extraction of page data done.
2025-09-08 20:49:27,649 | INFO | got response with OCR coordinates info from azure doc intelligence for page 6
2025-09-08 20:49:27,649 | INFO | started validating tables
2025-09-08 20:49:27,653 | INFO | -current table:

2025-09-08 20:49:27,654 | INFO | -validating table: Rate/Salary Information
2025-09-08 20:49:27,654 | INFO | -current table:

2025-09-08 20:49:27,655 | INFO | -validating table: Tax Information (Employee)
2025-09-08 20:49:27,655 | INFO | -current table:

2025-09-08 20:49:27,655 | INFO | -validating table: Tax Information (Employer)
2025-09-08 20:49:27,656 | INFO | -current table:

2025-09-08 20:49:27,656 | INFO | -validating table: Deduction Information
2025-09-08 20:49:27,657 | INFO | -current table:

2025-09-08 20:49:27,657 | INFO | -validating table: Direct Deposit Information
2025-09-08 20:49:27,658 | INFO | -current table:

2025-09-08 20:49:27,658 | INFO | -validating table: Fringe Benefit Information
2025-09-08 20:49:27,662 | INFO | -current table:
| BCode    |   Rate |   Amount |   Hours | Max/Carryover Max   | Length of Service   | Hours: Used/Avail/Total/Prob   | Dollars: Used/Avail/Total/Prob   | Effective Dates          |
|:---------|-------:|---------:|--------:|:--------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| ESST     |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/-1.30/0.00/0.00             | 01/01/2024 to 01/01/2024 |
| PER      |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 01/01/2016 to 12/31/2020 |
| PTO1     |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 01/01/2021 to 01/01/2021 |
| PTO2     |      0 |        0 |       0 | 0.00/0.00           |                     | 130.00/64.61/0.00/0.00         | 2723.50/1353.58/0.00/0.00        | 01/01/2021 to 12/31/2100 |
| SICK     |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 04/22/2016 to 12/31/2020 |
| VAC-NEX7 |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 08/06/2017 to 12/31/2020 |
| VAC-NEX8 |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 107.20/553.15/0.00/0.00          | 04/22/2016 to 08/05/2017 |
| VAC/CO   |      0 |        0 |       0 | 0.00/0.00           |                     | 0.00/0.00/0.00/0.00            | 0.00/0.00/0.00/0.00              | 01/01/2018 to 12/31/2020 |
2025-09-08 20:49:27,662 | INFO | -validating table: Benefit Accrual Information
2025-09-08 20:49:27,662 | INFO | --figuring out table emptiness...
2025-09-08 20:50:15,285 | INFO | llm gpt-5-mini api call took 47.622 seconds
2025-09-08 20:50:15,301 | INFO | total input tokens: 8979
2025-09-08 20:50:15,301 | INFO | input text tokens: 8048 # estimated
2025-09-08 20:50:15,302 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:50:15,302 | INFO | cost for input: $0.011224 USD
2025-09-08 20:50:15,302 | INFO | total output tokens: 5871
2025-09-08 20:50:15,302 | INFO | cost of output: $0.05871 USD
2025-09-08 20:50:15,302 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:51:21,135 | INFO | llm gpt-5-mini api call took 65.832 seconds
2025-09-08 20:51:21,141 | INFO | total input tokens: 4014
2025-09-08 20:51:21,141 | INFO | input text tokens: 4006 # estimated
2025-09-08 20:51:21,142 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:51:21,142 | INFO | cost for input: $0.005018 USD
2025-09-08 20:51:21,142 | INFO | total output tokens: 6046
2025-09-08 20:51:21,142 | INFO | cost of output: $0.06046 USD
2025-09-08 20:51:21,142 | INFO | --got table grid emptiness info:
|BCode|Rate|Amount|Hours|Max/Carryover Max|Length of Service|Hours: Used/Avail/Total/Prob|Dollars: Used/Avail/Total/Prob|Effective Dates|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
|X|X|X|X|X| |X|X|X|
2025-09-08 20:52:05,024 | INFO | llm gpt-5 api call took 43.882 seconds
2025-09-08 20:52:05,030 | INFO | total input tokens: 3607
2025-09-08 20:52:05,031 | INFO | input text tokens: 2969 # estimated
2025-09-08 20:52:05,031 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:52:05,031 | INFO | cost for input: $0.004509 USD
2025-09-08 20:52:05,031 | INFO | total output tokens: 1576
2025-09-08 20:52:05,031 | INFO | cost of output: $0.01576 USD
2025-09-08 20:52:05,032 | INFO | done judging, ALL GOOD
2025-09-08 20:52:05,033 | INFO | -current table:
| Date       | Reviewer     |   Rating | Raise Amount   |   New Pay Amnt | New Pay Per   | New Position   | Effective Date   | Next Review   |
|:-----------|:-------------|---------:|:---------------|---------------:|:--------------|:---------------|:-----------------|:--------------|
| 01/04/2018 |              |        0 |                |          13.75 |               |                | 01/04/2018       | 01/01/1900    |
| 04/04/2016 | Ronell Raney |        1 |                |          13    |               |                | 04/04/2016       | 01/04/2017    |
2025-09-08 20:52:05,033 | INFO | -validating table: Review Information
2025-09-08 20:52:05,034 | INFO | --figuring out table emptiness...
2025-09-08 20:54:35,305 | INFO | llm gpt-5-mini api call took 150.271 seconds
2025-09-08 20:54:35,314 | INFO | total input tokens: 8397
2025-09-08 20:54:35,314 | INFO | input text tokens: 7466 # estimated
2025-09-08 20:54:35,315 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:54:35,315 | INFO | cost for input: $0.010496 USD
2025-09-08 20:54:35,315 | INFO | total output tokens: 3227
2025-09-08 20:54:35,315 | INFO | cost of output: $0.03227 USD
2025-09-08 20:54:35,315 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:55:06,677 | INFO | llm gpt-5-mini api call took 31.360 seconds
2025-09-08 20:55:06,680 | INFO | total input tokens: 1654
2025-09-08 20:55:06,680 | INFO | input text tokens: 1646 # estimated
2025-09-08 20:55:06,681 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:55:06,681 | INFO | cost for input: $0.002067 USD
2025-09-08 20:55:06,681 | INFO | total output tokens: 3045
2025-09-08 20:55:06,681 | INFO | cost of output: $0.03045 USD
2025-09-08 20:55:06,681 | INFO | --got table grid emptiness info:
|Date|Reviewer|Rating|Raise Amount|New Pay Amnt|New Pay Per|New Position|Effective Date|Next Review|
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|X| | |X|X| | |X|X|
|X|X| |X|X| | |X|X|
2025-09-08 20:56:15,589 | INFO | llm gpt-5 api call took 68.907 seconds
2025-09-08 20:56:15,593 | INFO | total input tokens: 2904
2025-09-08 20:56:15,594 | INFO | input text tokens: 2266 # estimated
2025-09-08 20:56:15,594 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:56:15,594 | INFO | cost for input: $0.00363 USD
2025-09-08 20:56:15,594 | INFO | total output tokens: 2694
2025-09-08 20:56:15,594 | INFO | cost of output: $0.02694 USD
2025-09-08 20:56:15,594 | INFO | --found issues: [{'row': 1, 'column': 'Rating', 'status': 'wrong', 'feedback': 'Column should be empty per layout; extractor placed 0.'}, {'row': 1, 'column': 'Raise Amount', 'status': 'wrong', 'feedback': 'A value is present in this column per layout (0.00 per text), but extractor left it blank.'}, {'row': 2, 'column': 'Rating', 'status': 'wrong', 'feedback': 'Column should be empty per layout; extractor placed 1.'}, {'row': 2, 'column': 'Raise Amount', 'status': 'wrong', 'feedback': 'A value is present in this column per layout (1.00 per text), but extractor left it blank.'}]
2025-09-08 20:56:24,600 | INFO | llm gpt-5-mini api call took 9.005 seconds
2025-09-08 20:56:24,603 | INFO | total input tokens: 2332
2025-09-08 20:56:24,603 | INFO | input text tokens: 1401 # estimated
2025-09-08 20:56:24,603 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:56:24,604 | INFO | cost for input: $0.002915 USD
2025-09-08 20:56:24,604 | INFO | total output tokens: 675
2025-09-08 20:56:24,604 | INFO | cost of output: $0.00675 USD
2025-09-08 20:56:24,605 | INFO | --corrected as:
| Date       | Reviewer     | Rating   |   Raise Amount |   New Pay Amnt | New Pay Per   | New Position   | Effective Date   | Next Review   |
|:-----------|:-------------|:---------|---------------:|---------------:|:--------------|:---------------|:-----------------|:--------------|
| 01/04/2018 |              |          |              0 |          13.75 |               |                | 01/04/2018       | 01/01/1900    |
| 04/04/2016 | Ronell Raney |          |              1 |          13    |               |                | 04/04/2016       | 01/04/2017    |
2025-09-08 20:56:24,606 | INFO | -revalidating table: Review Information
2025-09-08 20:57:22,428 | INFO | llm gpt-5 api call took 57.822 seconds
2025-09-08 20:57:22,433 | INFO | total input tokens: 2904
2025-09-08 20:57:22,433 | INFO | input text tokens: 2266 # estimated
2025-09-08 20:57:22,433 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:57:22,433 | INFO | cost for input: $0.00363 USD
2025-09-08 20:57:22,434 | INFO | total output tokens: 2024
2025-09-08 20:57:22,434 | INFO | cost of output: $0.02024 USD
2025-09-08 20:57:22,434 | INFO | done judging, ALL GOOD
2025-09-08 20:57:22,435 | INFO | -current table:
| Name          | Relationship   | Home Phone   | Work Phone   | Address        | City       | State   |   Zip | Country   |
|:--------------|:---------------|:-------------|:-------------|:---------------|:-----------|:--------|------:|:----------|
| Emily Sanchez | Spouse         | 872-015-4314 |              | USNV Hernandez | Maplesyrup | AE      | 60890 |           |
2025-09-08 20:57:22,435 | INFO | -validating table: Emergency Contact Information
2025-09-08 20:57:22,436 | INFO | --figuring out table emptiness...
2025-09-08 20:57:48,609 | INFO | llm gpt-5-mini api call took 26.173 seconds
2025-09-08 20:57:48,618 | INFO | total input tokens: 8335
2025-09-08 20:57:48,618 | INFO | input text tokens: 7404 # estimated
2025-09-08 20:57:48,619 | INFO | input image tokens: 931 # estimated (input - text)
2025-09-08 20:57:48,619 | INFO | cost for input: $0.010419 USD
2025-09-08 20:57:48,619 | INFO | total output tokens: 1252
2025-09-08 20:57:48,619 | INFO | cost of output: $0.01252 USD
2025-09-08 20:57:48,619 | INFO | --got table related OCR content from Azure Doc Intelligence
2025-09-08 20:58:16,577 | INFO | llm gpt-5-mini api call took 27.957 seconds
2025-09-08 20:58:16,582 | INFO | total input tokens: 1458
2025-09-08 20:58:16,582 | INFO | input text tokens: 1450 # estimated
2025-09-08 20:58:16,582 | INFO | input image tokens: 8 # estimated (input - text)
2025-09-08 20:58:16,583 | INFO | cost for input: $0.001822 USD
2025-09-08 20:58:16,583 | INFO | total output tokens: 2602
2025-09-08 20:58:16,583 | INFO | cost of output: $0.02602 USD
2025-09-08 20:58:16,583 | INFO | --got table grid emptiness info:
|Name|Relationship|Home Phone|Work Phone|Address|City|State|Zip|Country|
|X|X|X||X|X|X|X||
2025-09-08 20:58:34,697 | INFO | llm gpt-5 api call took 18.113 seconds
2025-09-08 20:58:34,701 | INFO | total input tokens: 2783
2025-09-08 20:58:34,701 | INFO | input text tokens: 2145 # estimated
2025-09-08 20:58:34,701 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:58:34,701 | INFO | cost for input: $0.003479 USD
2025-09-08 20:58:34,701 | INFO | total output tokens: 488
2025-09-08 20:58:34,702 | INFO | cost of output: $0.00488 USD
2025-09-08 20:58:34,702 | INFO | done judging, ALL GOOD
2025-09-08 20:58:34,702 | INFO | started validating form fields
2025-09-08 20:58:34,702 | INFO | -validating form fields: ['Company Name', 'Company Code', 'Period', 'Employee Name', 'Address line 1', 'City', 'State', 'Zip', 'Emp Id', 'SSN']
2025-09-08 20:58:34,702 | INFO | --current are:
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
2025-09-08 20:58:55,208 | INFO | llm gpt-5 api call took 20.500 seconds
2025-09-08 20:58:55,213 | INFO | total input tokens: 3628
2025-09-08 20:58:55,213 | INFO | input text tokens: 2990 # estimated
2025-09-08 20:58:55,214 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:58:55,214 | INFO | cost for input: $0.004535 USD
2025-09-08 20:58:55,214 | INFO | total output tokens: 768
2025-09-08 20:58:55,214 | INFO | cost of output: $0.00768 USD
2025-09-08 20:58:55,214 | INFO | done judging, ALL GOOD
2025-09-08 20:58:55,214 | INFO | -validating form fields: ['DOB (only date)', 'Gender', 'Marital Status', 'Status', 'Position', 'Title', 'Pay Group', 'Job Code', 'Emp Type', 'Statutory']
2025-09-08 20:58:55,215 | INFO | --current are:
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
2025-09-08 20:59:22,121 | INFO | llm gpt-5 api call took 26.900 seconds
2025-09-08 20:59:22,125 | INFO | total input tokens: 4268
2025-09-08 20:59:22,126 | INFO | input text tokens: 2969 # estimated
2025-09-08 20:59:22,126 | INFO | input image tokens: 1299 # estimated (input - text)
2025-09-08 20:59:22,126 | INFO | cost for input: $0.005335 USD
2025-09-08 20:59:22,126 | INFO | total output tokens: 216
2025-09-08 20:59:22,126 | INFO | cost of output: $0.00216 USD
2025-09-08 20:59:22,138 | INFO | done judging, ALL GOOD
2025-09-08 20:59:22,138 | INFO | -validating form fields: ['Seasonal', 'Domestic Emp', 'Probation', 'Home #', 'Work #', 'Ext.', 'Email', 'Mail Stop', 'Hire Date', 'Rehire Date']
2025-09-08 20:59:22,138 | INFO | --current are:
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
2025-09-08 20:59:50,183 | INFO | llm gpt-5 api call took 28.038 seconds
2025-09-08 20:59:50,189 | INFO | total input tokens: 3607
2025-09-08 20:59:50,189 | INFO | input text tokens: 2969 # estimated
2025-09-08 20:59:50,189 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 20:59:50,189 | INFO | cost for input: $0.004509 USD
2025-09-08 20:59:50,189 | INFO | total output tokens: 769
2025-09-08 20:59:50,189 | INFO | cost of output: $0.00769 USD
2025-09-08 20:59:50,190 | INFO | done judging, ALL GOOD
2025-09-08 20:59:50,190 | INFO | -validating form fields: ['Term Date', 'Term Reason', 'Adj Sen Date', 'Pension', 'Visa Type', 'Exp', 'Citizen', 'I9 Reverify', 'I9 Verified', 'Deceased']
2025-09-08 20:59:50,190 | INFO | --current are:
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
2025-09-08 21:00:21,969 | INFO | llm gpt-5 api call took 31.773 seconds
2025-09-08 21:00:21,974 | INFO | total input tokens: 3609
2025-09-08 21:00:21,974 | INFO | input text tokens: 2971 # estimated
2025-09-08 21:00:21,975 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:00:21,975 | INFO | cost for input: $0.004511 USD
2025-09-08 21:00:21,975 | INFO | total output tokens: 1028
2025-09-08 21:00:21,975 | INFO | cost of output: $0.01028 USD
2025-09-08 21:00:21,976 | INFO | done judging, ALL GOOD
2025-09-08 21:00:21,976 | INFO | -validating form fields: ['Tax Form', 'WCC', 'EEOC', 'Supervisor ID', 'Name (supervisor name)', 'Def Comp', 'Union', 'Union Date', 'Collect Dues', 'Paid Init. Fees']
2025-09-08 21:00:21,976 | INFO | --current are:
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
2025-09-08 21:00:44,142 | INFO | llm gpt-5 api call took 22.159 seconds
2025-09-08 21:00:44,147 | INFO | total input tokens: 3612
2025-09-08 21:00:44,147 | INFO | input text tokens: 2974 # estimated
2025-09-08 21:00:44,147 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:00:44,147 | INFO | cost for input: $0.004515 USD
2025-09-08 21:00:44,147 | INFO | total output tokens: 647
2025-09-08 21:00:44,148 | INFO | cost of output: $0.00647 USD
2025-09-08 21:00:44,148 | INFO | done judging, ALL GOOD
2025-09-08 21:00:44,148 | INFO | -validating form fields: ['Veteran', 'Legal Rep', 'Nickname', 'surname', 'Prior Last', 'Disability', 'Smoker', 'AutoPay', 'Pay Frequency', 'OT Exempt']
2025-09-08 21:00:44,148 | INFO | --current are:
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
2025-09-08 21:01:00,496 | INFO | llm gpt-5 api call took 16.341 seconds
2025-09-08 21:01:00,501 | INFO | total input tokens: 3606
2025-09-08 21:01:00,501 | INFO | input text tokens: 2968 # estimated
2025-09-08 21:01:00,501 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:01:00,501 | INFO | cost for input: $0.000907 USD
2025-09-08 21:01:00,501 | INFO | total output tokens: 513
2025-09-08 21:01:00,502 | INFO | cost of output: $0.00513 USD
2025-09-08 21:01:00,502 | INFO | done judging, ALL GOOD
2025-09-08 21:01:00,502 | INFO | -validating form fields: ['Default Hours', 'Locations', 'Positions']
2025-09-08 21:01:00,502 | INFO | --current are:
Default Hours : 
Locations : 
Positions : 
2025-09-08 21:01:27,255 | INFO | llm gpt-5 api call took 26.746 seconds
2025-09-08 21:01:27,260 | INFO | total input tokens: 3584
2025-09-08 21:01:27,261 | INFO | input text tokens: 2946 # estimated
2025-09-08 21:01:27,261 | INFO | input image tokens: 638 # estimated (input - text)
2025-09-08 21:01:27,261 | INFO | cost for input: $0.00448 USD
2025-09-08 21:01:27,261 | INFO | total output tokens: 721
2025-09-08 21:01:27,261 | INFO | cost of output: $0.00721 USD
2025-09-08 21:01:27,262 | INFO | done judging, ALL GOOD

2025-09-06 17:03:04,092 | INFO | started initial extraction for page 5
2025-09-06 17:03:52,653 | INFO | initial extraction of page data done.
2025-09-06 17:03:59,873 | INFO | got markdown response from azure doc intelligence for page 5
2025-09-06 17:03:59,874 | INFO | started validating tables
2025-09-06 17:03:59,875 | INFO | -validating table: Rate/Salary Information
2025-09-06 17:03:59,876 | INFO | --figuring out table emptiness...
2025-09-06 17:04:18,867 | INFO | --got table grid emptiness info:
| RateCode | Description | Rate | Salary | Effective Dates |
| --- | --- | --- | --- | --- |
| X | X | X |  | X |
| X | X | X |  | X |
| X | X | X |  | X |
| X | X | X |  | X |
| X | X | X |  | X |
| X | X | X |  | X |
| X | X | X |  | X |
| X | X | X |  | X |
| X | X | X |  | X |
| X | X | X |  | X |
| X | X | X |  | X |
2025-09-06 17:04:37,018 | INFO | done judging, ALL GOOD
2025-09-06 17:04:37,019 | INFO | -validating table: Employee Tax Information
2025-09-06 17:04:37,020 | INFO | --figuring out table emptiness...
2025-09-06 17:04:46,701 | INFO | --got table grid emptiness info:
| Employee Tax Code | Employee Tax Description | Status | Add'l Amount | Effective Dates | Default |
| --- | --- | --- | --- | --- | --- |
| X | X |  | X | X | X |
| X | X |  | X | X | X |
| X | X | X | X | X | X |
| X | X | X | X | X | X |
2025-09-06 17:04:57,057 | INFO | done judging, ALL GOOD
2025-09-06 17:04:57,058 | INFO | -validating table: Employer Tax Information
2025-09-06 17:04:57,059 | INFO | --figuring out table emptiness...
2025-09-06 17:05:17,085 | INFO | --got table grid emptiness info:
| Employer Tax Code | Employer Tax Description | Effective Dates | Default |
| --- | --- | --- | --- |
| X | X | X |  |
| X | X | X |  |
| X | X | X |  |
| X | X | X |  |
| X | X | X |  |
| X | X | X |  |
2025-09-06 17:05:28,038 | INFO | done judging, ALL GOOD
2025-09-06 17:05:28,039 | INFO | -validating table: Deduction Information
2025-09-06 17:05:28,040 | INFO | --figuring out table emptiness...
2025-09-06 17:05:41,972 | INFO | --got table grid emptiness info:
| Code | Deduction | Rate | CalcCode | Frequency | Goal/Paid | Min/Max/Annual Max | Arrears | Agency | Effective Dates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X | X | X | X |  | X | X | X |  | X |
| X | X | X | X |  | X | X | X |  | X |
| X | X | X | X |  | X | X | X |  | X |
| X | X | X |  | X | X | X | X |  | X |
| X | X | X |  | X | X | X | X |  | X |
2025-09-06 17:06:06,930 | INFO | --found issues: [{'row': 4, 'column': 'multiple columns CalcCode, Frequency', 'status': 'wrong', 'feedback': "Value 'B5' is placed under CalcCode; it should be in Frequency, and CalcCode should be blank."}, {'row': 5, 'column': 'multiple columns CalcCode, Frequency', 'status': 'wrong', 'feedback': "Value 'B5' is placed under CalcCode; it should be in Frequency, and CalcCode should be blank."}]
2025-09-06 17:06:18,517 | INFO | --previous was:
| Code       | Deduction             |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-----------|:----------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| 401KC      | 401K Contribution     |   6    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 04/01/2016 to 12/31/2100 |
| 401kUM     | 401kUnmatch           |  14    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 08/01/2022 to 12/31/2100 |
| 401kUnmatc | 401K Unmatch          |  12    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 03/31/2019 to 08/01/2022 |
| DNTL       | Dental Insurance S125 |  18.32 | B5         |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2019 to 12/31/2100 |
| FH125      | Health Insurance S125 | 158.14 | B5         |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2019 to 12/31/2100 |
2025-09-06 17:06:18,520 | INFO | --corrected as:
| Code       | Deduction             |   Rate | CalcCode   | Frequency   | Goal/Paid   | Min/Max/Annual Max   |   Arrears | Agency   | Effective Dates          |
|:-----------|:----------------------|-------:|:-----------|:------------|:------------|:---------------------|----------:|:---------|:-------------------------|
| 401KC      | 401K Contribution     |   6    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 04/01/2016 to 12/31/2100 |
| 401kUM     | 401kUnmatch           |  14    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 08/01/2022 to 12/31/2100 |
| 401kUnmatc | 401K Unmatch          |  12    | %401K      |             | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 03/31/2019 to 08/01/2022 |
| DNTL       | Dental Insurance S125 |  18.32 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2019 to 12/31/2100 |
| FH125      | Health Insurance S125 | 158.14 |            | B5          | 0.00/0.00   | 0.00/0.00/0.00       |         0 |          | 09/01/2019 to 12/31/2100 |
2025-09-06 17:06:18,521 | INFO | -revalidating table: Deduction Information
2025-09-06 17:06:43,399 | INFO | done judging, ALL GOOD
2025-09-06 17:06:43,400 | INFO | -validating table: Direct Deposit Information
2025-09-06 17:06:43,401 | INFO | --figuring out table emptiness...
2025-09-06 17:06:51,899 | INFO | --got table grid emptiness info:
| Sequence No. | Transit No. | Account No. | Checking? | Account Name | Amount Code | Amount | Prenote Date | Effective Dates | Exclude Special |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X | X | X | X | X | X | X | X | X | X |
2025-09-06 17:07:02,680 | INFO | done judging, ALL GOOD
2025-09-06 17:07:02,681 | INFO | -validating table: Fringe Benefit Information
2025-09-06 17:07:02,681 | INFO | --figuring out table emptiness...
2025-09-06 17:07:15,610 | INFO | --got table grid emptiness info:
| ECode | CalcCode | Rate Code | Rate | Rate Per | Amount | Tabled? | Units | Frequency | Goal/Paid/Goal Bal. | Min/Max/Ann. Max | Effective Dates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X |  |  | X |  | X | X | X | X | X | X | X |
2025-09-06 17:07:47,308 | INFO | --found issues: [{'row': 1, 'column': 'Rate Code, Rate Per, Amount', 'status': 'wrong', 'feedback': 'Rate Code should be blank; Rate Per blank; Amount is 11.07. Extractor placed 0 under Rate Code, 11.07 under Rate Per, and left Amount empty.'}]
2025-09-06 17:07:54,708 | INFO | --previous was:
| ECode   | CalcCode   |   Rate Code |   Rate |   Rate Per | Amount   | Tabled?   |   Units | Frequency   | Goal/Paid/Goal Bal.   | Min/Max/Ann. Max   | Effective Dates          |
|:--------|:-----------|------------:|-------:|-----------:|:---------|:----------|--------:|:------------|:----------------------|:-------------------|:-------------------------|
| STD     |            |           0 |      0 |      11.07 |          | No        |       0 | ML          | 0.00/0.00/0.00        | 0.00/0.00/0.00     | 03/17/2019 to 12/31/2100 |
2025-09-06 17:07:54,710 | INFO | --corrected as:
| ECode   | CalcCode   | Rate Code   |   Rate | Rate Per   |   Amount | Tabled?   |   Units | Frequency   | Goal/Paid/Goal Bal.   | Min/Max/Ann. Max   | Effective Dates          |
|:--------|:-----------|:------------|-------:|:-----------|---------:|:----------|--------:|:------------|:----------------------|:-------------------|:-------------------------|
| STD     |            |             |      0 |            |    11.07 | No        |       0 | ML          | 0.00/0.00/0.00        | 0.00/0.00/0.00     | 03/17/2019 to 12/31/2100 |
2025-09-06 17:07:54,711 | INFO | -revalidating table: Fringe Benefit Information
2025-09-06 17:08:11,046 | INFO | done judging, ALL GOOD
2025-09-06 17:08:11,046 | INFO | -validating table: Benefit Accrual Information
2025-09-06 17:08:11,047 | INFO | -validating table: Review Information
2025-09-06 17:08:11,047 | INFO | -validating table: Emergency Contact Information

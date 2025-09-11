millenium_profile_schema = \
{
 'Form_fields': [
  'Company Name',
  'Company Code',  
  'Period',
  'Employee Name',
  'Address line 1',  
  'City',
  'State',
  'Zip',
  'Emp Id',
  'SSN',
  'DOB (only date)',
  'Gender',
  'Marital Status',
  'Status',
  'Position',
  'Title',
  'Pay Group',
  'Job Code',
  'Emp Type',
  'Statutory',
  'Seasonal',
  'Domestic Emp',
  'Probation',
  'Home #',
  'Work #',
  'Ext.',
  'Email',
  'Mail Stop',
  'Hire Date',
  'Rehire Date',
  'Term Date',
  'Term Reason',    
  'Adj Sen Date',
  'Pension',
  'Visa Type',
  'Exp',
  'Citizen',
  'I9 Reverify',
  'I9 Verified',
  'Deceased',
  'Tax Form',
  'WCC',
  'EEOC',
  'Supervisor ID',
  'Name (supervisor name)',
  'Def Comp',
  'Union',
  'Union Date',
  'Collect Dues',
  'Paid Init. Fees',
  'Veteran',
  'Legal Rep',
  'Nickname',
  'surname',  
  'Prior Last',
  'Disability',
  'Smoker',
  'AutoPay',
  'Pay Frequency',
  'OT Exempt',
  'Default Hours',
  'Locations',
  'Positions'],
 'Tables': {
  'Rate/Salary Information': [
   'RateCode',
   'Description',
   'Rate',
   'Salary',  
   'Effective Dates'],
  'Tax Information (Employee)': [
   'Employee Tax (code description)',
   'Status',
   "Add'l Amount",
   'Effective Dates',
   'Default'],
  'Tax Information (Employer)': [
   'Employer Tax (code description)',
   'Effective Dates',
   'Default'],
  'Deduction Information': [
   'Code',
   'Deduction',
   'Rate',
   'CalcCode',
   'Frequency',
   'Goal/Paid',
   'Min/Max/Annual Max',
   'Arrears',
   'Agency',   
   'Effective Dates'],
  'Direct Deposit Information': [
   'Sequence No.',
   'Transit No.',
   'Account No.',
   'Checking?',  
   'Account Name',
   'Amount Code', 
   'Amount',
   'Prenote Date',
   'Effective Dates',
   'Exclude Special'],
  'Fringe Benefit Information': ['ECode',
   'CalcCode',
   'Rate Code',
   'Rate',
   'Rate Per',
   'Amount',
   'Tabled?',
   'Units', 
   'Frequency',
   'Goal/Paid/Goal Bal.',
   'Min/Max/Ann. Max',
   'Effective Dates'],
  'Benefit Accrual Information': [
   'BCode',
   'Rate',
   'Amount',
   'Hours',
   'Max/Carryover Max',
   'Length of Service',
   'Hours: Used/Avail/Total/Prob',
   'Dollars: Used/Avail/Total/Prob',   
   'Effective Dates'],
  'Review Information':[ 
   'Date',
   'Reviewer',
   'Rating',
   'Raise Amount',
   'New Pay Amnt',
   'New Pay Per',
   'New Position',
   'Effective Date',
   'Next Review'
  ],
  'Emergency Contact Information': [
   'Name',
   'Relationship',
   'Home Phone',
   'Work Phone',
   'Address', 
   'City',
   'State',
   'Zip',
   'Country']
  }
}

paychex_profile_schema = {
  "Form_fields": [
    "Name (Preferred Name)",
    "Employee ID / Clock ID",
    "Address Line 1",
    "Address Line 2",
    "City, State Zip",
    "Country",
    "Work Phone",
    "Extension",
    "Home Phone",
    "Cell Phone",
    "Social Security Number",
    "Birth Date",
    "Work E-mail",
    "Personal E-mail",
    "Work State",
    "Officer Type",
    "Class Code",
    "Waive Code"
  ],
  "Tables": {
    "Employment": [
      "Hire Date",
      "Type",
      "Status",
      "As Of",
      "Reason",
      "Statutory Employee",
      "Eligible For Retirement Plan",
      "Organization",
      "Location",
      "Position"
    ],
    "Tax Withholdings (Federal Taxes)": [
      "Name",
      "Taxability",
      "Residency",
      "Filing Status",
      "Allowances (coma separated values possible)",
      "Additional / Override Amount",
      "% of Time Worked (State)",
      "% of Earnings Taxed (Local)"
    ],
    "Tax Withholdings (State Taxes)": [
      "Name",
      "Taxability",
      "Residency",
      "Filing Status",
      "Allowances (coma separated values possible)",
      "Additional / Override Amount",
      "% of Time Worked (State)",
      "% of Earnings Taxed (Local)"
    ],
    "Compensation": [
      "Rate / Salary",
      "Description",
      "Hours",
      "Frequency",
      "Overtime Hours",
      "Overtime Factor",
      "Exempt"
    ],
    "Direct Deposit": [
      "Used For",
      "Routing & Transit Number",
      "Bank Name",
      "Account Number",
      "Account Type",
      "Calculation Method",
      "Amount or %"
    ],
    "Earnings & Deductions": [
      "(E or D) Name",
      "Calculation Type (for each cell - capture all text along this column until next Name row)",
      "Amount",
      "Frequency",
      "Effect on Pay",
      "Check Limit",
      "Bank Account"
    ]
  }
}
human_reviewed_schema = paychex_profile_schema
# Prompts for various agents
extractor = {
    'user_prompt': f"""Extract data from this document using the following schema:
    
## Schema:
{human_reviewed_schema}

Instructions:
- First locate the form field or table in image to get its position and layout.
- Secondly it can happen that some text is partially visible or hidden or overlapped in image, for that parse the text from FULL_RAW_TEXT.
- Extract all form field values and table data as specified in the schema.
- In brackets beside field/column name there could be some hints or guidelines, follow them.

Respond only in JSON format with extracted data (no prose or explanations):
{{
 "Form_fields": {{
   "field1": "value1",
   "field2": "value2"
 }},
 "Tables": {{
   "table1": [
     {{"column1": "value", "column2": "value"}},
     {{"column1": "value", "column2": "value"}}
   ],
   "table2": [...]
 }}
}}""",
    'system_prompt': "You are a Document data extraction expert",
    'model': "gpt-5",
    'reasoning_effort': 'low'
}

judge = {
    'user_prompt': f'## Schema:\n{human_reviewed_schema}' + \
'''

## GRID_INFO:

The extractor said that DATA_PART DATA_NAME is/are: 
DATA_VALUE

validate above data against the ground truth image and text. finally tell me if correct or not.

Instructions and guidelines to follow during validation:
DATA_PART_INSTRUCTIONS

if a element is correct then return empty "feedback".

Respond only in below format (no prose or explanations):
OUTPUT_FORMAT
''',
    'system_prompt': "You are a strict data validation expert",
    'model': "gpt-5",
    'reasoning_effort': 'medium',
    'form_field_output_format': '''[
    {
     "data_name": <key name>,
     "status": correct | wrong, 
     "feedback": <observation>
    },
    ...
]''',
    'form_field_instructions': '''- A form field value should never be present in schema['Form_fields'] i.e list of form field names.
- Do not use FULL_RAW_TEXT to decide whether a form field value is empty or not.
- Locate form field first in image, then decide if its empty or not and finally parse FULL_RAW_TEXT only to get its value.
- If extractor listed a form field as X then you must also look for exact matching field name in image or FULL_RAW_TEXT.
- If form fields are not visible in image or FULL_RAW_TEXT and extractor said they are empty then that is correct.
- When a form field name and a table name are semantically close as in schema, carefully distinguish between both of them.
- If a form field name and a table column name are same or semantically close do not pick field value from that table.''',
    'table_output_format': '''[
    {
    "row": specific row_number | all rows | multiple rows a,b,c | range of rows x-y
    "column": specific columne_name | all columns | multiple columns column1, column2 | range of columns column1-column5,
    "status": correct | wrong,
    "feedback": <observation>
    },
    ...
]''',
    'table_instructions':'''- Ground the image, locate the concerned table.
- There could be hidden or overlapping text in image so do not extract any text from grounded image
- Only infer positional and layout related information of table and its cells from grounded image.
- For actual text parse FULL_RAW_TEXT but prioritize positional and layout info from grounded image.
- Strictly follow the column headers mentioned in schema for the concerned table.
- Compare the table grid of the extractor with that in image cell by cell, and check extractor's table for:
  - if any row(s) or column(s) shifting happened.
  - if any cells or rows or columns are missing.
  - if a cell value is wrong placed in another cell.
  - judge numeric equality, not formatting: always parse values as numbers and treat them as equal if numerically identical (e.g., 0 vs 0.0, 1 vs 1.0)
- Check if any form field values are wrongs placed in table or not.
- Unless column header names doesn't match the column header names in schema (ignoring the ones in brackets), never change column header names in feedback.
- Hints or guidelines for a specific column will be in brackets beside table column name in schema. preserve them while giving feedback. it helps while judging.'''
}

extractor_with_feedback = {
    'user_prompt': '''
You previously extracted DATA_PART DATA_NAME as 
DATA_VALUE

but the Judge validated and gave below feedback:
FEEDBACK

- recheck your extraction based on feedback and correct your mistake.
- do not modify any other values which the Judge did not report.
- if any form field key or table not present in image just leave its value blank in output.
- for tables never change column header names while correction.

Respond only in below format (no prose or explanations):
OUTPUT_FORMAT
''',
    'system_prompt': "You are a Document data extraction expert who focuses on feedback and improves the extraction based on it.",
    'model': "gpt-5-mini",
    'reasoning_effort': 'medium',
    'form_field_output_format': "{ 'field_name1':'field_value1', 'field_name2':'field_value2' }",
    'table_output_format': '''[
  {"column1": "value", "column2": "value"},
  {"column1": "value", "column2": "value"}
]'''
}

# use this prompt when dealing with simple and clear tables, since in that case Azure doc intelligence can extract the table well
table_grid_emptiness = {
    'system_prompt': "You are a specialized agent for Table Grid and Cell Emptiness detection",
    'model': 'gpt-5',
    'reasoning_effort': 'low',
    'user_prompt': '''
Table Name: "TABLE_NAME"
Table Column Header: TABLE_COLUMNS

Task:
- Given a document image and its corresponding markdown OCR text, identify the specified table, reconstruct its grid (rows, columns), and determine which cells are empty vs. non-empty.
- Strictly follow Table Column Header.
- Mark non empty cells with 'X' and leave empty cells blank.
- Do not extract any info from table and populate it in the output.
- If the requested table data is not present then return empty string.

Pitfalls to look out for:
- For each cell first look at image, (reading order left to right and top to bottom) 
- - if a cell is overflowing into its adjacent cell in image or its corresponding cell text in the markdown seems to have more than one cell contents mark both of those adjacent cells as 'X'

- if some columns or cells values appear be merged in markdown then in that case fall back to image .

Response format (no prose or explanations): 
if table data present: Markdown table with requested table column header and each cells is either filled with 'X' or is blank.
else: return ''
'''
}

# use this prompt when dealing with complex tables where Azure doc intelligence fails to extract the table directly in markdown format and can't even get the table grid right with empty vs non-empty cells
OCR_content_filter = {
    'system_prompt': "You are a specialized agent for filtering OCR content elements related to a specific table",
    'model': 'gpt-5-mini',
    'reasoning_effort': 'medium',
    'user_prompt': '''
Table Name: TABLE_NAME
Table Content:
TABLE_CONTENT

but not sure if its correct or not
I've attached the OCR content of this page with name OCR_COORDINATES.

Task: 
- filter line elements in OCR content that are related to the concerned table (table name if present + table column header + data rows).

Resonse format (no prose or explanations): return only the filtered table related elements including content and polygon fields as is.
'''
}

coordinate_based_empty_cell_finder = {
    'system_prompt': "You are a specialized agent for finding empty vs non-empty cells in a table based on OCR coordinates",
    'model': 'gpt-5-mini',
    'reasoning_effort': 'medium',
    'user_prompt': '''
OCR Content related to table with bounding box co-ordinates:
OCR_CONTENT

- 'polygon' contains co-ordinates of four corners, [x1,y1, x2,y2, x3,y3, x4,y4]
- x is horizontal axis and y is vertical axis
- x1,y1 is top-left, x2,y2 is top-right, x3,y3 is bottom-right, x4,y4 is bottom-left corners

Table Name: TABLE_NAME
Column header: COLUMN_HEADERS

Task: now based on co-ordinates find what all cells are empty, mark the non empty cells with X and leave empty ones blank

Steps to follow:
- if a user provided column name have multiple words and those are present in OCR content as separate word contents group them 
- when grouped as instructed in step 1 pick x1,y1, x4,y4 of first/left most word and x2,y2, x3,y3 of last/right most word to make a single column element polygon
- repeat above 2 steps for all column headers to get their polygons
- for tabular data elements with near y co-ordinates fall in same line (tolerance 0.002)
- in a row/line a cell's x co-ordinates (x1,x2 or x3,x4) must overlap beyond a certain threshold with any one of column's x co-ordinates (x1,x2 or x3,x4) for it to be non empty else its empty

example 1:
|x1<----column---->x2|
|x1<----cell---->x2|
or
|x1<----column---->x2|
--|x1<-cell->x2|------
if cell x1 >= column x1 and cell x2 <= column x2 (with tolerence for small misalignment like 0.002)
then this column cell is non empty

response:
|column|
|   X  |

example 2:
|x1<----column---->x2| 
-----------------------|x1<----cell---->x2|  
or
|x1<----column---->x2| 
--------------------|x1<----cell---->x2|  
if (cell x1 < column x1 and cell x2 > column x2) or (cell x1 > column x1 and cell x2 < column x2) (with tolerence for small misalignment like 0.002)
then this column cell is empty, even if cell overlaps but its very small overlap with column

response:
|column|
|      |

example 3:
|x1<----column1---->x2| |x1<----column2---->x2|
|x1<----cell---->x2|-----|x1<----cell---->x2|
-------------------------|x1<----cell---->x2|
|x1<------------------cell--------------->x2|
one cell is spanning two columns significantly, so both columns are non empty, happens when cell text is overflowing into adjacent cell

response:
|column1|column2|
|   X   |   X   |
|       |   X   |
|   X   |   X   |

Response format (no prose or explanations): respond only in markdown table with COLUMN_HEADERS as column header and each cell is either filled with X or is blank.
'''
}

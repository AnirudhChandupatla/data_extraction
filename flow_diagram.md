flowchart TD
  subgraph P[Process one page]
    direction TB
    E2[Initial extraction via AzureResponsesClient using extractor prompts]

    E2 --> F{Check If processing Form fields or Tables?}

    %% Form fields branch
    F -->|Form_fields| FF1[Chunk fields size 10]
    FF1 --> FF2[Judge validate form fields using 
    schema + full text + image]
    FF2 --> FF3{Issues?}
    FF3 -->|Yes| FF4[Extractor_with_feedback correct subset]
    FF4 --> FF2
    FF3 -->|No| FF5[Update Form_fields]

    %% Tables branch
    F -->|Tables| T1[Get OCR Coordinate info from AzureDocIntelligence]
    T1 --> T2[Iterate tables]
    T2 --> T3{Table empty?}
    T3 -->|Yes| T2
    T3 -->|No| T4[Convert table to markdown string]
    T4 --> T5[Filter OCR coordinates of concerned table]
    T5 --> T6[Calculate what are all the empty cells in concerned table grid]
    T6 --> T7[Judge: validates table using 
    schema + extracted table + empty cell info + image ]
    T7 --> T8{Issues?}
    T8 -->|Yes| T9[Extractor_with_feedback correct table as per feedback provided by the Judge]
    T9 --> T7
    T8 -->|No| T10[Update Tables]

    FF5 --> E5[Finally save into corrected_extraction.json]
    T10 --> E5
    E5 --> E6[Stop]
  end

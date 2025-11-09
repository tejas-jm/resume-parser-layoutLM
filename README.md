# Resume Parser Pipeline (LayoutLMv3)

## Overview
This project implements a layout-aware resume parsing pipeline built on **LayoutLMv3** (without fine-tuning).  
It supports multiple input file types—**DOCX**, **DOC**, and **PDF** (including scanned resumes)—and outputs a structured JSON containing contact details, education, work experience, skills, and other relevant sections.

The current version includes:
1. Ingestion and layout extraction  
2. Multi-column layout handling  
3. LayoutLMv3 inference  
4. Post-processing and heuristic structuring  

A future enhancement (Step 5) will introduce **Small Language Model (SLM)**–based JSON refinement and schema validation.

---

## Features
- Works with DOCX, DOC, and PDF (both text and scanned)  
- Extracts text, bounding boxes, and page-level metadata  
- Detects and handles multi-column resume layouts  
- Uses LayoutLMv3 for layout-aware text understanding  
- Converts model output into structured, interpretable JSON  
- Modular and extendable architecture for future improvements  

---

## Architecture

```
File (DOC / DOCX / PDF)
       ↓
Ingestion & OCR
       ↓
Layout Normalization (Column Detection)
       ↓
LayoutLMv3 Inference
       ↓
Heuristic Section Extraction
       ↓
Structured Resume JSON
```

---

## Installation

```bash
git clone https://github.com/your-username/studious-funicular.git
cd studious-funicular
pip install -r requirements.txt
```

### Required Libraries
- `transformers`
- `torch`
- `pdfplumber`
- `python-docx`
- `docx2txt`
- `easyocr` or `pytesseract`
- `Pillow`

---

## Usage

```python
from pipeline import parse_resume

result = parse_resume("Sample_Resume.pdf")
print(result)
```

### Example Output

```json
{
  "contact": {
    "email": "johndoe@example.com",
    "phone": "+1-555-234-9876"
  },
  "education": [
    {
      "institution": "Greenfield University",
      "degree": "Bachelor of Computer Science",
      "start_date": "2017",
      "end_date": "2021"
    }
  ],
  "work_experience": [
    {
      "company": "TechNova Solutions",
      "position": "Software Engineer",
      "description": [
        "Developed web APIs using Python and Flask",
        "Implemented CI/CD pipelines and automated test cases"
      ]
    },
    {
      "company": "ByteWorks Ltd.",
      "position": "Intern",
      "description": [
        "Assisted in frontend development using ReactJS",
        "Performed data preprocessing for internal analytics tools"
      ]
    }
  ],
  "skills": ["Python", "React", "SQL", "Data Analysis", "Machine Learning"],
  "languages": ["English", "Spanish"]
}
```

---

## Module Overview

### 1. `ingestion.py`
- Detects file type (DOCX/DOC/PDF)  
- Extracts text, bounding boxes, and layout metadata  
- Performs OCR for scanned PDFs  
- Normalizes coordinates and removes headers/footers  

### 2. `layout_utils.py`
- Detects multiple columns per page  
- Assigns column IDs and sorts tokens by `(page, column, y, x)`  

### 3. `inference.py`
- Runs pretrained LayoutLMv3 using Hugging Face Transformers  
- Processes text and bounding boxes (and optional page images)  
- Generates embeddings or token-level labels  

### 4. `postprocess.py`
- Groups tokens into lines and sections  
- Identifies resume headings like “SKILLS,” “EDUCATION,” “EXPERIENCE,” etc.  
- Extracts entities, normalizes dates, and constructs structured JSON  

---

## Planned Step 5: SLM-Based Refinement

The next phase will integrate a **Small Language Model (SLM)** post-processor to:
- Clean and re-nest flattened JSON structures  
- Enforce schema validation  
- Remove unsupported or hallucinated fields  

This refinement layer will ensure that all outputs strictly follow a unified schema and are ready for downstream applications.

---

## Limitations
- LayoutLMv3 is used in zero-shot mode (no fine-tuning).  
- OCR quality impacts accuracy for scanned documents.  
- Highly irregular or decorative layouts may require further visual segmentation logic.

---

## Future Work
- Fine-tune LayoutLMv3 on annotated resume datasets.  
- Integrate `layoutparser` for more accurate region detection.  
- Add SLM-based refinement for structured JSON validation.  
- Introduce confidence scoring for extracted fields.

---

## License
This project is released under the **MIT License**.
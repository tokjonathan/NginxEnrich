# ❇️ Nginx Log Parser & Enricher

## Overview
This project is a tool that parses **Nginx access logs**, enriches them with information extracted from the **User-Agent string**, and exports the results as a structured **JSON file**.

Developed as part of a **Product Engineering assessment**, this solution demonstrates:
- Regex-based log parsing
- Data transformation and enrichment
- JSON transformation
- Clean python standard pep8 style using linters Black and Flake8

---

## Features
- Parse Nginx access logs (Combined Log Format)
- Enrich User-Agent strings (Browser, OS, Device)
- Output timestamped structured JSON
---

## Project Structure
- `nginx_enrich/`
  - `.github/`
    - `workflows/`
      - `super-linter.yml` 
  - `.dockerignore` — flake8 docker ignore file, prevent docker issues on github actions
  - `.flake8`  — flake8 configuration for super-linter
  - `.gitignore`
  - `requirements.txt`
  - `access.log` — sample Nginx access log for testing
  - `enriched_output_<DateTime>.JSON` — sample output JSON file
  - `enrich.py` — helper functions for user-agent enriching
  - `parse.py` — helper functions for log parsing 
  - `transform.py` — helper function for writing logs to JSON
  - `main.py` — Project Entry Point

---
## Setup
Setting up on <ins>Linux / MacOS</ins>
```
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Setting up on <ins>Windows</ins>
```
# Create virtual environment
python -m venv venv
venv\Scripts\Activate

pip install -r requirements.txt
```
---

### Running the project

> ✏️ Edit **main.py** <ins>filepath</ins> variable to pass access logs 
> into script 

> ✏️ Edit **main.py** <ins>output_path</ins> variable to set output file 
> destination.

```
# Run script
python main.py
```

---
<ins>**Methodology & Assumptions**</ins> <br><br>

When approaching this Nginx Log Parsing and Enrichment ool, I decided to develop it in a
modular way, with distinctive helper functions separated into
respective libraries based on it's intended utilities. This is to allow easier extension and 
future management of the code.

The management of the repository is done using Dependabot to ensure dependencies are
secure and up to date. Automated Python linters Black and flake8 is used to help standardize formatting in accordance
to PEP8 standards. All in which is set up in Github Actions to automatically occur when new code is pushed
to the repository.

For the purpose of this assessment, the usability features are kept to a minimum, there is no UI or CLI functionalities 
added. It is assumed this tool will be used as a script or as an extension to a broader project integration.

---

### Find me at :
<div id="badges">
  <a href="https://www.linkedin.com/in/jonathantok">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
</div>

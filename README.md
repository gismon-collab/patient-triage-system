🏥 Patient Triage System (Educational Project)

📌 Project Overview

The Patient Triage System is a Python-based application that simulates how hospitals prioritize patients based on symptoms and vital signs such as:



\- Age

\- Pain level (0–10)

\- Body temperature (°C)

\- Pulse rate

\- Symptoms

\- Shortness of breath



The system assigns patients into four categories:

\- 🔴 IMMEDIATE

\- 🟡 URGENT

\- 🟢 NORMAL

\- 🟢 NON-URGENT



\---



🧠 Features



\- ✔ Object-Oriented Design (OOP)

\- ✔ Rule-based triage engine

\- ✔ Input validation system

\- ✔ Retry system for invalid inputs

\- ✔ Unit testing with pytest

\- ✔ Code coverage support

\- ✔ Modular architecture (src/tests separation)



\---------------------------------------------------



📂 Project Structure





patient-triage-system/

│

├── src/

│ ├── main.py

│ ├── patient.py

│ ├── triage\_engine.py

│ ├── triage\_category.py

│ ├── validator.py

│

├── tests/

│ ├── test\_patient.py

│ ├── test\_triage\_engine.py

│

├── requirements.txt

└── README.md   

\---------------------------------------------------



PROJECT MANAGEMENT(History)

📌 Step 1: To start Git

&#x20;      git init



📌 Step 2: To add files

&#x09;git add .



📌 Step 3: first commit



&#x09;git commit -m "Initial project setup"



📌 Step 4: code add

&#x09;git commit -m "Added triage engine logic"





📌 Step 5: adding test

&#x09;git commit -m "Added unit tests using pytest"



📌 Step 6: improvements

&#x09;git commit -m "Improved validation and risk system"



\----------------------------------------------------

⚙️ How to Install



&#x20;  1. Create virtual environment

&#x20;      	bash

python -m venv .venv



&#x20;2. Activate environment

&#x09;.venv\\Scripts\\activate



3\. Install dependencies

&#x09;pip install pytest coverage



▶️ How to Run Project

&#x09;python -m src.main

🧪 How to Run Tests

&#x20;   	python -m pytest

🧪 output

&#x09;5 passed

🧾Example Input

&#x09;Patient name: John

&#x09;Age: 25

&#x09;Symptoms: Fever

&#x09;Pain level (0-10): 6

&#x09;Temperature (°C): 38.5

&#x09;Pulse rate: 90

&#x09;Shortness of breath: no

📤 Example Output

&#x09;Triage Category: URGENT

&#x09;Risk Level: 🟡 YELLOW - MEDIUM RISK

\-------------------------------------------------



🏗 Architecture



The system is divided into modules:



&#x09;main.py → Handles user input

&#x09;patient.py → Stores patient data

&#x09;triage\_engine.py → Decision-making logic

&#x09;validator.py → Input validation

&#x09;triage\_category.py → Enum categories





🧪 Testing Strategy



&#x09;Unit testing using pytest

&#x09;Covers triage decision logic

&#x09;Ensures correct classification of patients

&#x09;Current coverage: \~88%



⚙️ Design Approach



&#x09;Rule-based scoring system

&#x09;Priority order:

&#x09;IMMEDIATE

&#x09;URGENT

&#x09;NORMAL

&#x09;NON-URGENT

&#x09;Emergency conditions checked first














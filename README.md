# Elyx Health Hackathon: Personalized Health Planning Simulation

## Overview

This project is a modular health simulation framework built for hackathon demonstration.  
It models a patient journey with automated chat scenarios, health metrics, diagnostic tests, personalized plans, interventions, and a multidisciplinary care team. All workflow stages generate validated data and export results for analytics, visualization, or prototype integration.

---

## Features

- Dataclass-based models for clear, structured data.
- Static and dynamic conversation simulators reflecting real-world medical and concierge interactions.
- Automated weekly health metric generation (e.g., exercise, symptoms).
- Sample diagnostic test results.
- Validation functions for every core entity.
- Data export in both CSV and JSON formats.
- Easy to modify for other scenarios, data types, or team roles.

---



## How It Works

1. **Define the member and care team** in `chat_simulator.py`.
2. **Create personalized plans and interventions** using scenario functions.
3. **Generate weekly health metrics** and diagnostic test simulation.
4. **Simulate conversations** (static and dynamic) between member and team based on status and events.
5. **Validate all generated data.**
6. **Export everything to CSV/JSON** for analytics.
7. **Console displays** a readable chat transcript.

---

## Installation

1. **Clone the repo:**
    ```
    git clone https://github.com/YOUR_USER/elyx-health-hackathon.git
    cd elyx-health-hackathon
    ```

2. **Create the data directory (if missing):**
    ```
    mkdir -p data
    ```

3. **(Optional) Use a virtual environment:**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **No external dependencies needed (Python 3.7+).**

---

## Quickstart

1. **Run the chat simulator:**
    ```
    python src/chat_simulator.py
    ```
2. **View chat logs in console and exported data in the `/data` folder.**

---

## Modules

- **models.py:** Member, TeamMember, Plan, Intervention, DiagnosticTest, Conversation, Metric (dataclasses).
- **scenario_simulator.py:** Chat scenario generators, data creators.
- **model_validation_demo.py:** Data validation utilities.
- **data_io.py:** Export data to CSV and JSON.
- **chat_simulator.py:** Main orchestrator, handling setup, validation, export, and logging.

---

## Data Export

Your `/data` folder will contain:
- conversations.csv / conversations.json
- diagnostics.csv / diagnostics.json
- plans.csv / plans.json
- interventions.csv / interventions.json
- metrics.csv / metrics.json

---

## Customization

- Change member, team, or scenario logic in `chat_simulator.py` and `scenario_simulator.py`.
- Add new metrics, tests, or conversation types easily.
- Integrate outputs with any data analytics tool, dashboard, or patient portal.

---

## Contributors

- Avi Gupta  
- Eklavya Joshi

---




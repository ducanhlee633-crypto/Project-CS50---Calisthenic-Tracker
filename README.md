# Smart Athlete Performance Engine

#### Description:
The **Smart Athlete Performance Engine** is a command-line interface (CLI) application designed for athletes and fitness enthusiasts (specifically those practicing weightlifting or Calisthenics) to log, track, and analyze their physical performance over time. 

Unlike generic to-do apps, this program applies real-world fitness science—specifically **Epley's Formula**—to calculate an athlete's estimated **1 Rep Max (1RM)** and total workout volume. It processes raw inputs, parses them using regular expressions, maps them to Python objects, and stores them permanently in a CSV database.

---

## Key Features
1. **Interactive CLI Menu**: A user-friendly, loop-based menu that allows seamless navigation between logging, viewing history, and viewing analytics.
2. **Robust Input Parsing (RegEx)**: Users can quickly log workouts using standard fitness shorthand (e.g., `dips [4x12r @ 15kg]`). The program utilizes Regular Expressions to validate and extract variables (Exercise Name, Sets, Reps, and Weight) dynamically.
3. **Smart Data Cleaning**: Handles real-world user inconsistencies (such as entering weight as "15", "15kg", or "15 Kg") by stripping non-numeric noise before processing calculations.
4. **Beautiful Tabular Visualization**: Integrates the `tabulate` library to format raw database logs into aligned, elegant tables directly inside the terminal.
5. **Scientifically Backed Analytics**: Calculates 1RM dynamically. If an athlete queries an exercise in the Analytics menu, the program isolates their history, calculates progress, and displays their current strength ceiling.

---

## File Structure

*   `project.py`: The main entry point of the application containing the core execution loop, menu handling, and helper functions for parsing and calculations.
*   `test_project.py`: The test suite utilizing `pytest` to thoroughly test the parsing, validation, and calculations, ensuring the application handles edge cases and invalid inputs gracefully.
*   `database.csv`: The persistent flat-file database storing workout history (Date, Name, Sets, Reps, Weight).
*   `requirements.txt`: Lists third-party dependencies required for the project (such as `tabulate` and `pytest`).

---

## Design Decisions

### Why CSV instead of a complex SQL database?
For a lightweight CLI utility, a local CSV file is highly portable, easy to back up, and doesn't require the user to configure database servers (like PostgreSQL) or install heavy engines. It satisfies the CS50P standard while keeping the data easily editable in spreadsheet software like Excel.

### Separation of Concerns for Testing
To make the application fully testable with `pytest` (without halting execution during automated tests), all core parsing, validation, and mathematical calculations are isolated into pure functions outside of the `main()` input loop:
*   `clean_weight(weight_str)`: Resolves formatting discrepancies (e.g., "12 Kg" -> `12.0`).
*   `calculate_one_rep_max(reps, weight)`: Handles Epley's algorithm mathematically while handling the edge case of 1 rep (where 1RM equals the weight itself).
*   `validate_date(date_str)`: Leverages regex to strictly enforce the ISO standard `YYYY-MM-DD` format.

---

## How to Install and Run

1. **Install Dependencies**:
   Ensure you have Python installed, then run the following command to install required packages:
   ```bash
   pip install -r requirements.txt
2. **Run the Application**
    Launch the engine by running:
   ```bash
   python project.py 
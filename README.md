# In-Memory Transactional Database

## Setup (Optional, if cloning from GitHub)

If you are running this project by cloning a GitHub repository:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/JagerRager/ec.git
   ```
2. Ensure you have Python 3.7 or higher installed.  
   You can verify your Python version with:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

No additional libraries or environment setup are needed — this project runs with standard Python only.

---

## How to Run

If you already have the `inmemory_db.py` file (or after cloning):

1. Open a terminal in the project directory.

2. Run the following command:
   ```bash
   python inmemory_db.py
   ```
   (Use `python3 inmemory_db.py` if your system uses `python3`.)

3. Alternatively, you can open the file in an IDE like **Visual Studio Code** or **PyCharm** and click **Run**.

---

## What Happens When You Run It

- The program automatically executes a series of labeled tests (`Test 1`, `Test 2`, ..., `Big Test`).
- Each test prints both the expected and actual outcomes for easy validation.
- No manual input is required.

---

## Suggestions for Improving the Assignment Instructions

To make this assignment stronger if made official, a few improvements could help:
- **Clarify Expected Behaviors**: Make it clearer that `get()` during a transaction should prioritize temporary transaction values before falling back to committed values.
- **Extended Testing Requirements**: Encourage or require writing organized unit tests (e.g., using Python’s `unittest` or `pytest` frameworks) instead of only using print statements.
- **Implement Transaction Isolation Levels**: As an optional advanced challenge, require supporting different transaction isolation levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable), allowing students to simulate how real-world databases manage concurrency and consistency.
- **Grading Automation**: Provide a grader script or rubric with specific input/output expectations so graders can verify correctness automatically.


---

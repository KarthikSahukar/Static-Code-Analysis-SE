# Static-Code-Analysis-SE


### Table

| Issue | Type | Line(s) | Description | Fix Approach |
| --- | --- | --- | --- | --- |
| Use of `eval` | Security | 59 | [cite_start]**Bandit** and **Pylint** both flagged the use of `eval()` as a major security risk[cite: 3, 6]. | Replaced the `eval()` call with a standard `print()` function to eliminate the vulnerability. |
| Dangerous default value | Bug | 8 | [cite_start]**Pylint** warned that using `logs=[]` as a default argument is dangerous because the same list is shared across all calls to the function[cite: 1]. | Changed the function signature to use `logs=None` and then initialized a new list `logs = []` inside the function if it was `None`. |
| Bare 'except' | Bug | 19 | [cite_start]**Flake8** and **Pylint** reported that using a bare `except:` is bad practice because it hides all errors, not just the expected ones[cite: 1, 101]. | Replaced the generic `except:` with the specific `except KeyError:` to only catch errors where a dictionary key is not found. |
| Type error in `addItem` | Bug (Runtime) | 12, 52 | The program crashed with a `TypeError` because it tried to add a number and a string. This was not caught by static analysis tools. | Added input validation using `isinstance()` at the beginning of the `add_item` function to ensure `item` is a string and `qty` is an integer before proceeding. |
| Unsafe file handling | Bug / Quality | 37, 43 | [cite_start]**Pylint** warned that opening files without using a `with` statement (`R1732`) or specifying an `encoding` (`W1514`) could lead to resource leaks and errors[cite: 9]. | Refactored the `load_data` and `save_data` functions to use a `with open(...)` block and specified `encoding="utf-8"` for safe and reliable file operations. |

---

### Reflection Question Answers

Here are the answers to the reflection questions, based on the work you've done.

#### Which issues were the easiest to fix, and which were the hardest? Why?

* **Easiest:** The `eval()` security risk was the easiest. Both Bandit and Pylint pointed to the exact line, and the fix was a simple replacement of one function with another.
* **Hardest:** The `TypeError` in `addItem` was the hardest because it was a **runtime bug**, meaning none of the static analysis tools detected it. I had to run the program, see it crash, understand the traceback, and then add input validation logic to make the function more robust.

#### Did the static analysis tools report any false positives? If so, describe one example.

Yes, Pylint's warning about function names (`C0103: Function name "addItem" doesn't conform to snake_case naming style`) could be considered a **false positive**. While `add_item` is the standard Python style (PEP 8), using `addItem` (camelCase) doesn't break the code or cause a bug. It's a stylistic preference, so flagging it as an "error" is very strict, and in some development teams, it might be ignored.

#### How would you integrate static analysis tools into your actual software development workflow?

I would integrate these tools at two key points in the development process:
1.  **Local Development:** I would configure my code editor (like VS Code) to run Flake8 and Pylint automatically every time I save a file. This provides instant feedback. I would also use a "pre-commit hook" to run all three tools before I'm allowed to commit my code to version control.
2.  **Continuous Integration (CI):** I would set up a CI pipeline (like GitHub Actions) to automatically run Pylint, Bandit, and Flake8 on the code every time a team member pushes changes. This acts as a quality gate to ensure that insecure or buggy code doesn't get merged into the main project.

#### What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The improvements were significant across the board:
* **Robustness:** The code is much more robust. By adding input validation and fixing the unsafe file handling with `with open`, the program no longer crashes on bad data or if a file is missing.
* **Security:** The code is more secure. Removing the `eval()` function closed a major vulnerability.
* **Readability & Maintainability:** The code is far more professional and easier to maintain. Changing function names to `snake_case`, adding docstrings, and fixing all the formatting issues makes it much easier for another developer to understand and contribute to the project.The final Pylint score increase from `4.80/10` to over `9.22/10` is a clear metric of this improvement.

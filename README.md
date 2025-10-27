# Static-Code-Analysis-SE

Here is the updated table.

This version replaces the "Unused import" issue with the more critical "Type error" fix for the `addItem` function.

| Issue | Type | Line(s) | Description | Fix Approach |
| --- | --- | --- | --- | --- |
| Use of `eval` | Security | 59 | [cite_start]**Bandit** reported `[B307:blacklist] Use of possibly insecure function`[cite: 3]. This is a medium-severity security risk. | Replace the `eval("print('eval used')")` call with a simple `print('eval used')` command. |
| Dangerous default value | Bug | 8 | [cite_start]**Pylint** reported `W0102: Dangerous default value [] as argument`[cite: 94]. This means the `logs` list is shared across all calls, which is a bug. | Change the default value `logs=[]` to `logs=None`. Inside the function, add a check: `if logs is None: logs = []`. |
| Bare 'except' | Bug | 19 | [cite_start]**Flake8** reported `E722 do not use bare 'except'` [cite: 4] [cite_start]and Pylint reported `W0702: No exception type(s) specified`[cite: 94]. This catches *all* errors, hiding bugs. | Replace `except:` with the specific error we expect, which is `except KeyError:`. |
| Type error in `addItem` | Bug | 52 | The call `addItem(123, "ten")` causes a `TypeError` when line 12 tries to add an integer (`0`) and a string (`"ten"`). | Add input validation to the `addItem` function using `isinstance()` to check that `item` is a string and `qty` is an integer before running the addition. |
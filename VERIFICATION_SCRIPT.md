## `VERIFICATION_SCRIPT`

The requirements for the `VERIFICATION_SCRIPT` are 
- output is binary: `exit(0)`, `exit(1)` for successful and unsucessful result respectively.
- running of the verification script should not take more than 1 minute.

### How to define an execution graph

```python
# 1 → 2
# ↓ ↙
# 3    

from validator import Validator

@Validator.step(1)
def do_thing1() -> tuple[bool, str]:
    return True, "All good"

@Validator.step(2, depends_on=[1])
def do_thing_dependant_on_1() -> tuple[bool, str]:
    return False, "Something Happened"

@Validator.step(3, depends_on=[1, 2])
def do_thing_3() -> tuple[bool, str]:
    return True, "All Good"
```

### Create submission checker

- Add a submission directory under the `submission` directory named after the `SUBMISSION` ID.
- Add a `check.py` under this directory
- Create execution graph

```sh
.
└── src
    ├── __init__.py
    ├── __pycache__
    ├── base.py
    ├── toolX/
    │   ├── checker.py 
    │   └── resources.py 
    └── submissions/
        └── 123456/
            └── check.py
``` 


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
    # ...Checking Logic...
    return True, "All good with thing 1"

@Validator.step(2, depends_on=[1])
def do_thing_dependant_on_1() -> tuple[bool, str]:
    # ...Checking Logic...
    return False, "Something Happened, I was expecting X"

@Validator.step(3, depends_on=[1, 2])
def do_thing_3() -> tuple[bool, str]:
    # ...Checking Logic...
    return True, "All good with thing 3"
```

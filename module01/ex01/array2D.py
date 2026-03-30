import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list) \
         or not isinstance(start, int) \
         or not isinstance(end, int):
            raise AssertionError("Input must be a list and two integers")
        if not (len(item) == len(family) for item in family):
            raise AssertionError("Input list with different sizes")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end].shape}")
        return np.array(family)[start:end].tolist()
    except AssertionError as e:
        print("Assertion Error: ", e)
        

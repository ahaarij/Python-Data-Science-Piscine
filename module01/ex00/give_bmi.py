

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    try:
        assert isinstance(height, list) and isinstance(weight, list), \
            "Height and Weight must be lists"
        assert len(height) == len(weight), \
            "Height and Weight lists must be of same length"

        bmi_values = []
        for h, w in zip(height, weight):
            assert isinstance(h, (int, float)) and \
                isinstance(w, (int, float)), \
                "Height and Weight must be either integers or floats"
            assert h > 0 and w > 0, \
                "Height and Weight must be of positive values"
            bmi = w / (h ** 2)  # double star is exponential operator
            bmi_values.append(bmi)

        return bmi_values
    except AssertionError as e:
        print("Assertion Error: ", e)
    except Exception as e:
        print("Exception: ", e)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        assert isinstance(bmi, list), "BMI must be list"
        assert isinstance(limit, int), "Limit must be an integer"
        limits = []
        for b in bmi:
            assert isinstance(b, (int, float)), \
                "BMI must be an integer or a float"
            limits.append(b > limit)
        return limits
    except AssertionError as e:
        print("Assertion Error: ", e)
    except Exception as e:
        print("Exception: ", e)

import pandas as pd

def load(path:str) -> pd.DataFrame:
    try:
        assert isinstance(path, str), "The path must be a string"
        assert path.endswith(".csv"), "The file is not a CSV"

        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)

        return data
    
    except AssertionError as e:
        print("Assertion Error:", e)
        return None
    except Exception as e:
        print("Exception:", e)
        return None
    
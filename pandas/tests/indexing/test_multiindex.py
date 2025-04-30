import pytest

def test_multiindex_difference_with_pyarrow():
    import pandas as pd
    pa = pytest.importorskip("pyarrow")

    df = pd.DataFrame([
        (1, "1900-01-01", "a"),
        (2, "1900-01-01", "b")
    ], columns=["id", "date", "val"]).astype({
        "id": "int64[pyarrow]",
        "date": "timestamp[ns][pyarrow]",
        "val": "string[pyarrow]",
    })

    df = df.set_index(["id", "date"])
    idx_val = df.index[0]
    
    result = df.index.difference([idx_val])
    expected = df.index[[1]]  # the second row should remain
    tm.assert_index_equal(result, expected)

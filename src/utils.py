import pandas as pd


def get_clean_df(file):
    df = pd.read_csv(file, sep="\t", skiprows=[0, 1, 2, 3], header=None, index_col=0)
    df = df.iloc[:, [1]]
    df.index.name = "microbe"
    df.columns = ["abundance"]
    df = df.T

    keep = list(filter((lambda x: "s__" in x and "t__" not in x), df.columns))
    reduced = df[keep]

    new_names = [col.split("|")[-1] for col in keep]
    renamed = reduced.copy()
    renamed.columns = new_names
    return renamed

import pandas as pd
from GMHI import GMHI_model
import numpy as np
import os


def get_score(df):
    df = df.reset_index(drop=True)
    df = df.rename_axis(None, axis=1)

    clf = GMHI_model()
    names = list(clf.features)

    set_diff = set(names) - set(df.columns)

    blank = pd.DataFrame(np.zeros((1, len(set_diff))), columns=set_diff)
    concat = pd.concat([blank, df], axis=1)
    reindexed = concat[names]
    scaled = reindexed / reindexed.sum().sum()
    gmhi_score = clf.decision_function(scaled)
    return gmhi_score[0]

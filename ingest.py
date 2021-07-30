import pandas as pd
from elasticsearch import Elasticsearch
import eland as ed
import numpy as np

def ingest():
    es = Elasticsearch(
        ["https://74e30042023542b39d86b6b3a4ba3d2d.europe-west1.gcp.cloud.es.io:9243"],
        api_key=("Q5QkZ3oBHh9R-qNypNBq", "DcA0TvujSKa6nhVLHsVJmw")
    )
    df = pd.DataFrame(np.random.normal(size=[100, 3]), columns=["x", "y", "z"])
    ed.pandas_to_eland(df,es, "uzleuven_mir_demo_2021_06-02")



if __name__ == "__main__":
    ingest()
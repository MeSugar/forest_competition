import click

from typing import Any
from typing import List

from joblib import dump
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA
from boruta import BorutaPy
from sklearn.ensemble import RandomForestClassifier

def build_pipeline(
    use_pca : bool,
    use_boruta : bool,
    columns_to_transorm : List,
    clf : Any
) -> Pipeline:
    steps = []
    steps.append(("scaler", StandardScaler(), columns_to_transorm))
    if use_pca:
        steps.append(("pca", PCA(n_components=0.95), columns_to_transorm))
    preprocessor = ColumnTransformer(
    steps,
    remainder="passthrough"
    )
    pipeline = make_pipeline(preprocessor)
    if use_boruta:
        rfc = RandomForestClassifier(n_estimators=1000, n_jobs=-1, random_state=42)
        pipeline.steps.append(
            (
                "boruta",
                BorutaPy(
                    rfc, n_estimators='auto',
                    verbose=2, random_state=1
                ),
            )
        )
    pipeline.steps.append(clf)
    return pipeline

import numpy as np
import xgboost as xgb
from hyperopt import hp
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

from config import random_seed
from utils.python_utils import quniform_int

steps = [
    ('pca', PCA(n_components=40, random_state=random_seed)),
    ('xgb', xgb.XGBClassifier(n_estimators=6700, max_depth=11, min_child_weight=9, subsample=0.900152352061, gamma=0.188234394605, colsample_bytree=0.8, learning_rate=0.00540318190441, silent=True, nthread=1, seed=random_seed))
]

model = Pipeline(steps=steps)

params_space = {
    'pca__n_components': quniform_int('n_components', 10, 75, 1),
    'xgb__max_depth': quniform_int('max_depth', 10, 30, 1),
    'xgb__min_child_weight': hp.quniform('min_child_weight', 1, 20, 1),
    'xgb__subsample': hp.uniform('subsample', 0.8, 1),
    'xgb__n_estimators': quniform_int('n_estimators', 1000, 10000, 50),
    'xgb__learning_rate': hp.loguniform('learning_rate', np.log(0.0001), np.log(0.5)) - 0.0001,
    'xgb__gamma': hp.loguniform('gamma', np.log(0.0001), np.log(5)) - 0.0001,
    'xgb__colsample_bytree': hp.quniform('colsample_bytree', 0.5, 1, 0.05)
}


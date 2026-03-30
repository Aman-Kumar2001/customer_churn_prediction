# Building Pipelines
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder

def preprocess_data(num_cols, ord_cat, nom_cat):

    num_pipe = Pipeline(steps = [("num_impute", SimpleImputer(strategy='mean')),
                                ("num_scaling", StandardScaler())])

    ord_cat_pipe = Pipeline(steps = [("ord_impute", SimpleImputer(strategy='most_frequent')),
                                    ("ord_encode", OrdinalEncoder())])

    nom_cat_pipe = Pipeline(steps = [("nom_impute", SimpleImputer(strategy='most_frequent')),
                                    ("nom_encode", OneHotEncoder(handle_unknown='ignore', sparse_output=False, drop='first'))])

    preprocessing = ColumnTransformer(transformers=[('num_trf', num_pipe, num_cols),
                                                    ('ord_trf',ord_cat_pipe, ord_cat),
                                                    ('nom_trf', nom_cat_pipe, nom_cat)],
                                                    remainder='passthrough')
    
    return preprocessing


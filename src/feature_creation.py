from sklearn.preprocessing import LabelEncoder

def new_features(df, y):
    df["AverageCharges"] = df["TotalCharges"]/(df["tenure"]+1)
    df["ServiceSupport"] = (df[["OnlineSecurity", "TechSupport", "DeviceProtection","OnlineBackup"]] == 'Yes').sum(axis=1)
    df["StreamService"] = (df[["StreamingTV", "StreamingMovies"]] == 'Yes').sum(axis=1)


    df['trusted'] = ((df["Contract"] == 'One year') | (df["Contract"] == 'Two year')).astype(int) + ((df["PaymentMethod"] == 'Credit card (automatic)') | (df["PaymentMethod"] == 'Bank transfer (automatic)')).astype(int)

    le = LabelEncoder()
    y = le.fit_transform(y)
    return df , y
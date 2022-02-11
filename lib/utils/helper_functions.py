import pandas as pd
from sklearn.model_selection import train_test_split

def custom_train_test_split(df, index = None, cv = 10):

    if cv == 1:
        X_train, y_train = df.loc[:, df.columns != 'Politikbereich'], df.loc[:,df.columns == 'Politikbereich']
        X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.1, random_state=42, stratify=y_train)
        return X_train, X_test, y_train, y_test

    X_test_dfs = []
    y_test_dfs = []

    # Get minority classes: classes that have less than cv=10 examples
    tmp_df = df.groupby(["Politikbereich"]).count().sort_values(by="Zweck", ascending = False).reset_index()
    minority_classes = tmp_df[tmp_df["Zweck"] < cv]["Politikbereich"].values

    # Split dataset into 10 equally distributed chunks

    # For classes that have more than cv=10 examples, 10 splits are going to be made
    tmp_df = df[~df["Politikbereich"].isin(minority_classes)]
    total_count = tmp_df.value_counts().sum()
    X_train, y_train = tmp_df.loc[:, tmp_df.columns != 'Politikbereich'], tmp_df.loc[:,tmp_df.columns == 'Politikbereich']
    for _ in range(cv-1):
        X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=int(total_count/cv), random_state=42, stratify=y_train)
        # print(f'{i}:\
        # {y_train[y_train["Politikbereich"] == "Umwelt"].value_counts().sum()}\
        # {y_test[y_test["Politikbereich"] == "Umwelt"].value_counts().sum()}\
        # {y_train[y_train["Politikbereich"] == "Verkehr"].value_counts().sum()}\
        # {y_test[y_test["Politikbereich"] == "Verkehr"].value_counts().sum()}')
        X_test_dfs.append(X_test)
        y_test_dfs.append(y_test)
    X_test_dfs.append(X_train)
    y_test_dfs.append(y_train)

    # Create and fill X_train_dfs and y_train_dfs
    X_train_dfs = [pd.concat(X_test_dfs[:i] + X_test_dfs[i+1:], ignore_index=True) for i in range(10)]
    y_train_dfs = [pd.concat(y_test_dfs[:i] + y_test_dfs[i+1:], ignore_index=True) for i in range(10)]

    # For classes that have less than cv=10 examples, 2 splits will be done
    # The first 5 chunks will be concatenates the first split, 
    # and the second 5 chunks the second split.
    tmp_df = df[df["Politikbereich"].isin(minority_classes)]
    total_count = tmp_df.value_counts().sum()
    X_train, y_train = tmp_df.loc[:, tmp_df.columns != 'Politikbereich'], tmp_df.loc[:,tmp_df.columns == 'Politikbereich']
    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.5, random_state=42, stratify=y_train)
    for i in range(cv):
        if i < 5:
            X_test_dfs[i] = pd.concat([X_test_dfs[i],X_train], ignore_index=True)
            y_test_dfs[i] = pd.concat([y_test_dfs[i],y_train], ignore_index=True)
            X_train_dfs[i] = pd.concat([X_train_dfs[i],X_test], ignore_index=True)
            y_train_dfs[i] = pd.concat([y_train_dfs[i],y_test], ignore_index=True)
        else:
            X_test_dfs[i] = pd.concat([X_test_dfs[i],X_test], ignore_index=True)
            y_test_dfs[i] = pd.concat([y_test_dfs[i],y_test], ignore_index=True)
            X_train_dfs[i] = pd.concat([X_train_dfs[i],X_train], ignore_index=True)
            y_train_dfs[i] = pd.concat([y_train_dfs[i],y_train], ignore_index=True)

    if index is not None:
        return X_train_dfs[index], X_test_dfs[index], y_train_dfs[index], y_test_dfs[index]
    else:
        return X_train_dfs, X_test_dfs, y_train_dfs, y_test_dfs
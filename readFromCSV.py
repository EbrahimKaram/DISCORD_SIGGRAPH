import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("..\s2020_sessions_Test.csv")
    print(df.head(5))
    print(df.columns)
    # We need to look at session Title and event type
    df["Reduced_sessionTitle"]=df['Session Title'].str.strip().str[:20]

    # TODO: get all categories and print them
    # There are 23 categories
    df["Reduced_sessionTitle"].unique()
    


    

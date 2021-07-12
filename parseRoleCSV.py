import pandas as pd


if __name__ == '__main__':
    print("Hello World")
    # TODO: parse the CSV file
    # Send message in welcome channel
    # Create roles
    df=pd.read_csv("..\Channels, Categories, and Roles - Roles.csv")

    for column in df.columns:
        print("\n")
        print(column)
        df_temp=df[column]
        for i in range(len(df_temp)) :
            if not  pd.isnull(df_temp.iloc[i]):
                print(df_temp.iloc[i].split(':')[:2])


def run(path) :     
    # import modules here 
    import pandas as pd 

    # logic 
    df = pd.read_csv("dataset.csv")

    df["attendance_date"] = pd.to_datetime(df["attendance_date"])
    
    # return your output
    return df
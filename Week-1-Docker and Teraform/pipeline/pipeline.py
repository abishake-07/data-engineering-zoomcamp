import sys
import pandas as pd
print('Arguements:',sys.argv)

month  = int(sys.argv[1])


df = pd.DataFrame({"Month":[month],"Sales":[1000]})
print(df.head())


df.to_parquet(f'output_{month}.parquet')
print("Hello Pipeline ,month = {month}")

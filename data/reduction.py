import sys
import pandas as pd

# expects stdin=filename when program is called
# takes the file and only keeps data in 10 minute increments
# saves into a file appended with 'reduced'

filename = sys.argv[1]
df=pd.read_csv(filename)
df['minute']=df.time.apply(lambda x: x[14:16]).astype(int).apply(lambda x: x%10)
df[df.minute==0].to_csv(filename[:-4]+'reduced.csv')

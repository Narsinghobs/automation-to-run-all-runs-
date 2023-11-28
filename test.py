import datetime
from datetime import date
import os
import pandas as pd

l=os.listdir()

data1 = {'Test Type': [], 
        'Run Name': [],'Date':date.today(),'Running':[],'Issues':[]} 

for i in l:
    if(i!='test.py'):
        
        t=f"QA-{i[:-3]}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        data1['Test Type'].append(i[:-3])
        data1['Run Name'].append(t)
        
        dt=date.today()
        
        print(i)
        
        try:
             exec(open(i).read().replace("put_run_name",t))
             data1['Running'].append('Running')
             data1['Issues'].append('')
        except Exception as e:
            print(e)
            data1['Running'].append('Not Running')
            data1['Issues'].append(e)
       
        
       
   
o=pd.DataFrame(data1,columns=['Test Type','Run Name','Date','Running','Issues']) 

print(o)
o.to_excel("runs.xlsx")



       
       
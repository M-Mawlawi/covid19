import requests,json
import pandas as pd

class getdata():
    def get():
        remote_url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
        local_file = 'data.csv'
        jsondata = 'data.json'
        data = requests.get(remote_url)
        dataset = {}

        with open(local_file, 'wb') as file:
            file.write(data.content)

        df = pd.read_csv(local_file)
        df = df.reset_index()
        df = df.rename(columns={"Name":"Region","index":"Name","Deaths - newly reported in last 24 hours":"Flag","Deaths - newly reported in last 7 days per 100000 population":"Deaths - newly reported in last 24 hours","Deaths - newly reported in last 7 days":"Deaths - newly reported in last 7 days per 100000 population","Deaths - cumulative total per 100000 population":"Deaths - newly reported in last 7 days","Deaths - cumulative total":"Deaths - cumulative total per 100000 population","Cases - newly reported in last 24 hours":"Deaths - cumulative total","Cases - newly reported in last 7 days per 100000 population":"Cases - newly reported in last 24 hours","Cases - newly reported in last 7 days":"Cases - newly reported in last 7 days per 100000 population","Cases - cumulative total per 100000 population":"Cases - newly reported in last 7 days","Cases - cumulative total":"Cases - cumulative total per 100000 population","WHO Region":"Cases - cumulative total"})
        df.at[0,'Region'] = 'Global'
        df.at[34,'Name'] = "Palestine, State of"

        js = df.to_json(orient= 'records')
        with open(jsondata,'w') as file:
            js = json.loads(js)
            file.write(json.dumps(js,indent=4))


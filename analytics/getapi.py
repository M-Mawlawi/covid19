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
        df = df.rename(columns={"Name":"Region","index":"Name","Deaths - newly reported in last 24 hours":"Flag","Deaths - newly reported in last 7 days per 100000 population":"Deaths_newly_reported_in_last_24_hours","Deaths - newly reported in last 7 days":"Deaths_newly_reported_in_last_7_days_per_100000_population","Deaths - cumulative total per 100000 population":"Deaths_newly_reported_in_last_7_days","Deaths - cumulative total":"Deaths_cumulative_total_per_100000_population","Cases - newly reported in last 24 hours":"Deaths_cumulative_total","Cases - newly reported in last 7 days per 100000 population":"Cases_newly_reported_in_last_24_hours","Cases - newly reported in last 7 days":"Cases_newly_reported_in_last_7_days_per_100000_population","Cases - cumulative total per 100000 population":"Cases_newly_reported_in_last_7_days","Cases - cumulative total":"Cases_cumulative_total_per_100000_population","WHO Region":"Cases_cumulative_total"})
        df.at[0,'Region'] = 'Global'
        df.at[34,'Name'] = "Palestine, State of"

        js = df.to_json(orient= 'records')
        with open(jsondata,'w') as file:
            js = json.loads(js)
            file.write(json.dumps(js,indent=4))


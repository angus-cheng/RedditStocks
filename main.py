import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

plt.close('all')

base_url = 'https://cloud.iexapis.com/stable'
sandbox_url = 'https://sandbox.iexapis.com/stable'

token = os.environ.get('IEX_TOKEN')
params = {'token' : token}

tokenSandbox = os.environ.get('IEX_SANDBOX_TOKEN')
paramsSandbox = {'token' : tokenSandbox}

def historicalData(_symbol, _range=None, _date=None):
    # endpoint = f'{base_url}/stock/{_symbol}/chart'
    endpoint = f'{sandbox_url}/stock/{_symbol}/chart'
    if _range:
        endpoint += f'/{_range}'
    elif _date:
        endpoint += f'/date/{_date}'

    paramsSandbox.update(chartCloseOnly = 'true', chartSimplify = 'true')

    # resp = requests.get(endpoint, params=params)
    resp = requests.get(endpoint, params=paramsSandbox)
    resp.raise_for_status()
    
    return pd.DataFrame(resp.json())

def plotData(data):
    plt.figure()
    data.plot(x='date', y='close')
    plt.show()
    return

def main():
    appl_6m_df = historicalData('AAPL', '6m')
    print(appl_6m_df.head())
    print()
    plotData(appl_6m_df)

if __name__ == "__main__":
    main()
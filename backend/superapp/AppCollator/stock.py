import requests,json
from django.http import HttpResponse,JsonResponse
def stocklist():
    stocks_symbol=['IBM','MSFT']
    latest_records={}
    for stock in stocks_symbol:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock}&interval=5min&apikey="
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get('Information') != "Intraday (5min) open, high, low, close prices and volume":
                    data = {"AAPL": {"1. open": "233.4400", "2. high": "233.5000", "3. low": "233.4400", "4. close": "233.4900", "5. volume": "22"},
                            "MSFT": {"1. open": "345.5500", "2. high": "346.0000", "3. low": "345.5500", "4. close": "345.9000", "5. volume": "15"},
                            "GOOG": {"1. open": "2875.0000", "2. high": "2900.0000", "3. low": "2860.0000", "4. close": "2880.0000", "5. volume": "30"},
                            "TSLA": {"1. open": "715.5000", "2. high": "720.0000", "3. low": "710.0000", "4. close": "718.0000", "5. volume": "50"},
                            "AMZN": {"1. open": "3450.0000", "2. high": "3475.0000", "3. low": "3440.0000", "4. close": "3460.0000", "5. volume": "20"},
                            "NFLX": {"1. open": "650.0000", "2. high": "655.0000", "3. low": "645.0000", "4. close": "652.0000", "5. volume": "18"},
}               
                    return JsonResponse({'data':data})
                else:
                    timeseries=(data['Time Series (5min)'])
                    latest_timestamp= max(timeseries.keys())
                    latest_records[stock] = {"timestamp": latest_timestamp,"data": timeseries[latest_timestamp]
                    }
                    return JsonResponse({'data':latest_records})
            else:
                return JsonResponse({'status': 'error', 'message': 'Failed to fetch data.'}, status=response.status_code)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

import requests

def fetch_data(url, timeout=10):
    try:
        response = requests.get(url,timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error occurred: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    else:
        print("Data fetched successfully!")
        print(f"Response content: {response.text[0:200]}")
    finally:
        print("Execution of the network request is complete.")

print("*"*55)
fetch_data("https://realpython.com/python-calendar-module/")
print("*"*55)
fetch_data("https://realpython.com/python-calendar-module/1")
print("*"*55)
fetch_data("https://ajay.url")
print("*"*55)
fetch_data("ajay.url")
print("*"*55)
fetch_data("https://realpython.com/python-calendar-module/", 0.00001)
print("*"*55)

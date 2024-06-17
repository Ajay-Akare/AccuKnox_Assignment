import requests


def check_application_status(url):
    response = requests.get(url, timeout=5)

    # Check the status code
    if response.status_code == 200:
        print(f"The application at {url} is UP. Status code: {response.status_code}")
    elif response.status_code == 404:
        print(f"Not found. Status code: {response.status_code}")
    elif response.status_code == 500:
        print(f"Internal server error. Status code: {response.status_code}")
    elif response.status_code == 503:
        print(f"Service is not available. Status code: {response.status_code}")
    elif response.status_code == 504:
        print(f"Gateway time out. Status code: {response.status_code}")
    else:
        print(f"The application at {url} is DOWN")


if __name__ == "__main__":
    check_application_status('http://google.com/')

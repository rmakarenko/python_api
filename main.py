# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

def test_get_locations_for_us_90210_check_status_code_equals_200():

    response = requests.get("http://api.zippopotam.us/us/90210")
    print('response in function 1 is', response)
    print("status code in test 1 is", response.status_code)
    assert response.status_code == 200

def test_get_locations_for_us_90210_check_content_type_equals_json():
    response = requests.get("http://api.zippopotam.us/us/90210")
    print('response in function 2 is', response)
    print('response in function 2 is', response.headers['Content-Type'])
    print('response in function 2 is', response.headers)

    response_body = response.json()
    print(response_body)


    assert response.headers['Content-Type'] == "application/json"


test_get_locations_for_us_90210_check_status_code_equals_200()
test_get_locations_for_us_90210_check_content_type_equals_json()



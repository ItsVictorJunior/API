import requests
import pytest

my_new_post_header = {
    'Ocp-Apim-Subscription-Key': '0fff331c6b1e4655ac4cedcd6345bb4c',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

head = {
    'Ocp-Apim-Subscription-Key': '0fff331c6b1e4655ac4cedcd6345bb4c',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

def test_check_status_Code():
    response = requests.get(
        "https://apis.qa.alaskaair.com/flightOps/orm/tailassignmentmetrics/api/v1/TailAssignmentMetrics/tailassign?fileName=TailAssign_AS_ACC90084B5DE4AD48265C44449BCEE9A_20230713T091804Z",
        headers=head)
    assert response.status_code == 200


def test_check_content_type_equals_json():
    response = requests.get(
        "https://apis.qa.alaskaair.com/flightOps/orm/tailassignmentmetrics/api/v1/TailAssignmentMetrics/tailassign?fileName=TailAssign_AS_ACC90084B5DE4AD48265C44449BCEE9A_20230713T091804Z",
        headers=head)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_check_field_exist_in_json_body():
    response = requests.get(
        "https://apis.qa.alaskaair.com/flightOps/orm/tailassignmentmetrics/api/v1/TailAssignmentMetrics/tailassign?fileName=TailAssign_AS_ACC90084B5DE4AD48265C44449BCEE9A_20230713T091804Z",
        headers=head)
    response_body = response.json()
    assert "name" in response_body


def test_check_variable_equals_results_in_json_body():
    response = requests.get(
        "https://apis.qa.alaskaair.com/flightOps/orm/tailassignmentmetrics/api/v1/TailAssignmentMetrics/tailassign?fileName=TailAssign_AS_ACC90084B5DE4AD48265C44449BCEE9A_20230713T091804Z",
        headers=head)
    response_body = response.json()
    assert response_body["name"] == "TailAssign_AS_ACC90084B5DE4AD48265C44449BCEE9A_20230713T091804Z"


def test_check_deep_variable_equals_result():
    response = requests.get(
        "https://apis.qa.alaskaair.com/flightOps/orm/tailassignmentmetrics/api/v1/TailAssignmentMetrics/tailassign?fileName=TailAssign_AS_ACC90084B5DE4AD48265C44449BCEE9A_20230713T091804Z",
        headers=head)
    response_body = response.json()
    assert response_body["dataPoints"][0]["operation"] == "Process"


def test_get_all_counts_in_json_body():
    response = requests.get(
        "https://apis.qa.alaskaair.com/flightOps/orm/tailassignmentmetrics/api/v1/TailAssignmentMetrics/tailassign?fileName=TailAssign_AS_ACC90084B5DE4AD48265C44449BCEE9A_20230713T091804Z",
        headers=head)
    response_body = response.json()
    assert len(response_body["dataPoints"]) == 245
    # assert len(response_body) == 2


#Status Code Error 500
# def test_check_post_works():
#     my_new_post = {
#         "orchestratorCorrelationID": "286295fe-9eda-4e2e-9a60-a7c5807c29ff",
#         "operatingAirlineCode": "AS",
#         "requestedBy": "jjs-POSTMAN",
#         "ssimDate": "2023-08-14"
#     }
#     response = requests.post("https://orchestrator-qa-func-westus2.azurewebsites.net/api/OrchestratorFunction",
#                              json=my_new_post, headers=my_new_post_header)
#     assert response.status_code == 201


test_data_users = [
    ("", "SubFleetDefaultRule match on N615AS/ANC"),
    ("", "SubFleetDefaultRule match on N921AK/PDX")
    # (3, "c")
]


@pytest.mark.parametrize("userid, expected_name", test_data_users)
def test_get_data_for_user_check_name(userid, expected_name):
    response = requests.get(f"https://apis.qa.alaskaair.com/flightOps/orm/tailassignmentmetrics/api/v1/TailAssignmentMetrics/tailassign?fileName=TailAssign_AS_ACC90084B5DE4AD48265C44449BCEE9A_20230713T091804Z{userid}",headers=head)
    response_body = response.json()
    assert response_body['dataPoints'][5]['message'] == expected_name


# req = requests.get(
#     "https://apis.qa.alaskaair.com/flightOps/orm/tailassignmentmetrics/api/v1/TailAssignmentMetrics/tailassign?fileName=TailAssign_AS_ACC90084B5DE4AD48265C44449BCEE9A_20230713T091804Z",
#     headers=head)
# response2 = req.json()
# print(response2)

from utils.api_client import client

def get_root():
    response = client.make_request(handle="/", method="GET")
    return response

def create_case(json={}):
    response = client.make_request(handle="/testcases", method="POST", json=json)
    return response

def get_allcases():    
    response = client.make_request(handle=f"/testcases", method="GET")
    return response


def get_case(id_case):    
    response = client.make_request(handle=f"/testcases/{str(id_case)}", method="GET")
    return response

def delete_case(id_case):    
    response = client.make_request(handle=f"/testcases/1", method="DELETE")
    return response
#{str(id_case)}

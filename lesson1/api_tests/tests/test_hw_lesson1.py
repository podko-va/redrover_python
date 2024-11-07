from case.pom.case import create_case, get_allcases, get_case, delete_case, get_root
from case.models.case import Case
from case.data.case import create_case_dict
import json
import pytest
import random


# @pytest.fixture(scope="module")
# def case_id():
#     response = create_case(Case(**create_case_dict).model_dump())
#     response.status_code_should_be_eq(200)
#     return response.value_with_key("id")

#@pytest.mark.only

def test_get_read_root():
    response = get_root()
    response.status_code_should_be_eq(200)
    response.json_should_be_eq({"Hello": "World"})
    

def test_create_case():
    response = create_case(Case(**create_case_dict).model_dump())
    response.status_code_should_be_eq(200)
    response.json_should_be_eq(Case(**create_case_dict).model_dump())
    response.schema_should_be_eq(Case(**create_case_dict).model_json_schema())    
 
@pytest.mark.only    
def test_negative_case():
    response = create_case({})
    print(response)
    response.status_code_should_be_eq(422)


def test_get_id_case(case_id):
    response = get_case(case_id)
    response.status_code_should_be_eq(200)
    response.schema_should_be_eq(Case(**create_case_dict).model_json_schema())
    
    
def test_cases_exists():
    response = get_allcases()
    response.status_code_should_be_eq(200)


def test_delete_id_case(case_id):
    response = delete_case(case_id)
    response.status_code_should_be_eq(200)
    res ={
        "detail": "Test case deleted."
        }
    response.json_should_be_eq(res)
    


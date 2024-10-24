import pytest
from case.pom.case import create_case
from case.models.case import Case
from case.data.case import create_case_dict

@pytest.fixture(scope="module")
def case_id():
    response = create_case(Case(**create_case_dict).model_dump())
    response.status_code_should_be_eq(200)
    return response.value_with_key("id")
from function import number_to_month, validate_number
import pytest

# ใช้คำสั่ง pytest -m code หากใช้ @pytest.mark.code  
@pytest.mark.code  
def test_january_1():
    input = 1
    expected_result = "january"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code  
def test_february_2():
    input = 2
    expected_result = "february"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code  
def test_march_3():
    input = 3
    expected_result = "march"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code  
def test_april_4():
    input = 4
    expected_result = "april"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code  
def test_may_5():
    input = 5
    expected_result = "may"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code  
def test_june_6():
    input = 6
    expected_result = "june"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code  
def test_july_7():
    input = 7
    expected_result = "july"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code  
def test_august_8():
    input = 8
    expected_result = "august"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code  
def test_september_9():
    input = 9
    expected_result = "september"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code  
def test_october_10():
    input = 10
    expected_result = "october"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code  
def test_november_11():
    input = 11
    expected_result = "november"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code  
def test_march_12():
    input = 12
    expected_result = "december"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


# ใช้คำสั่ง pytest -m validate หากใช้ @pytest.mark.validate 
@pytest.mark.validate  
def test_out_of_range_input_0():
    input = 0
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_out_of_range_input_13():
    input = 13
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result
 
@pytest.mark.validate  
def test_out_of_range_input_minus10():
    input = -10
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_out_of_range_input_22():
    input = 22
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_input_integer_input_1_1():
    input = 1.1
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_out_of_range_input_13_1():
    input = 13.1
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_input_integer_input_a():
    input = "a"
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_input_integer_input_sharp():
    input = "#"
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_1_input_1():
    input = 1
    expected_result = 1
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_12_input_12():
    input = 12
    expected_result = 12
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_out_of_range_input_0_5():
    input = 0.5
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_out_of_range_input_minus_1_5():
    input = -1.5
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_input_integer_input_1_5():
    input = 1.5
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

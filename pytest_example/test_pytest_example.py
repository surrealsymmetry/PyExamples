import pytest
from pytest_example import first_target_element_index

@pytest.fixture
def targets():
	return [3, 4, 5, 7, 2, 23]

def test_targets_twenty_three(targets):
	assert first_target_element_index(targets, [71, 6, -50, 0, 23, -2]) == 4

def test_fails_if_non_int_encountered(targets):
	with pytest.raises(TypeError):
		first_target_element_index(targets, [9, 8, 22, "cat", 7])

def test_passes_if_non_int_not_encountered(targets):
	assert first_target_element_index(targets, [9, 8, 2, "cat", 7]) == 2


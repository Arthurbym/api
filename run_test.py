import pytest
from common.path_data import test_suit_path, allure_data_path

if __name__ == '__main__':
    pytest.main([test_suit_path, '--alluredir', '%s' % allure_data_path, '--clean-alluredir'])

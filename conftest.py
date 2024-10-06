import os
import pytest
import random
from utils.common_utils import get_random_string
from pages.login_page import LoginPage
from utils.logger.logger import Logger

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
    **browser_context_args,
    "record_video_size":{
        "width": 1080,
        "height": 1920
    }
}

@pytest.fixture(scope="session")
def logger():
    return Logger()

@pytest.fixture(autouse=True)
def login_to_app(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(os.getenv('USERNAME'), os.getenv('PASSWORD'))
    login_page.dashboard_link.wait_for()


@pytest.fixture(scope="function")
def test_data():
    random_string = get_random_string(6)
    d = dict()
    d['user_role'] = random.choice(['Admin', 'ESS'])
    d['employee_name'] = "Carolin Frank Jenkins"
    d['status'] = random.choice([True, False])
    d['username'] = 'name_'+random_string
    d['password'] = "pass_"+random_string
    return d
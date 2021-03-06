import os

import pytest
import sys

from tests.test_cache import cache
from tests.test_chrome_driver import delete_cache
from webdriver_manager.driver import EdgeDriver
from webdriver_manager.microsoft import EdgeDriverManager
from selenium import webdriver


@pytest.mark.skipif(sys.platform != 'win32',
                    reason="run only on windows")
def test_edge_manager_with_selenium():
    delete_cache()
    driver_path = EdgeDriverManager().install()
    dr = webdriver.Edge(driver_path)
    dr.quit()


@pytest.mark.skipif(sys.platform != 'win32',
                    reason="run only on windows")
def test_edge_manager_with_selenium_cache():
    driver_path = EdgeDriverManager().install()
    dr = webdriver.Edge(driver_path)
    dr.quit()


def test_can_download_edge_driver_binary():
    edge_driver = EdgeDriver("latest", "win")
    edge_driver_bin = cache.download_binary(edge_driver)
    assert edge_driver_bin.name == u'MicrosoftWebDriver'
    assert os.path.exists(edge_driver_bin.path)


def test_can_user_cached_edge_driver_binary():
    delete_cache()
    edge_driver = EdgeDriver("latest", "win")
    cache.download_binary(edge_driver)
    edge_driver_bin = cache.download_binary(edge_driver)
    assert edge_driver_bin.name == u'MicrosoftWebDriver'
    assert os.path.exists(edge_driver_bin.path)

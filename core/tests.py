from playwright.sync_api import Page, expect
import pytest
import re


@pytest.mark.playwright()
def test_can_load_example_page(selenium, live_server):
    selenium.get("https://playwright.dev/")

    assert "Playwright" in selenium.title


@pytest.mark.playwright()
def test_change_a_quanity_and_submit():
    pass

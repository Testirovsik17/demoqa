from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_text_element(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    demo_qa_page.btn_elements.click()
    assert elements_page.center_text.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()

    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()

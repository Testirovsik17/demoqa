from pages.demoqa import DemoQa
from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.btns_sub_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    demo_qa_page = DemoQa(browser)
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    modal_dialogs_page.refresh()
    modal_dialogs_page.icon_main_page.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()

    assert modal_dialogs_page.get_url() == demo_qa_page.get_url()
    assert modal_dialogs_page.get_title() == demo_qa_page.get_title()

    browser.set_window_size(1000, 1000)

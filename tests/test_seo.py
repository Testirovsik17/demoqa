from pages.demoqa import DemoQa

def test_check_tittle_demo(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert browser.title == 'DEMOQA'
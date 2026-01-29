

def test_google__title(page):
    page.goto("www.google.com")
    assert "Google" in page.title()

page.get_by_role("button", name="Log in").click()
print(test_google__title(page))
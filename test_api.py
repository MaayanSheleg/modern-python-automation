import pytest
from playwright.sync_api import Playwright
from api_objects import PostsAPI


def test_get_single_post(playwright: Playwright):
    """
    Test to verify a specific post returns 200 and has a title.
    """
    # 1. Create the API Request Context (Isolated network state)
    api_context = playwright.request.new_context()

    # 2. Initialize our API Object with the context
    posts_api = PostsAPI(api_context)

    # 3. specific Test Steps
    post_id = 1
    response = posts_api.get_post_by_id(post_id)

    # 4. Validations
    # Check Status Code
    assert response.ok, f"API Request failed: {response.status}"
    assert response.status == 200

    # Check Response Body
    data = response.json()

    # Ensure 'title' exists and is not empty
    assert "title" in data, "Response JSON is missing the 'title' field"
    assert data["title"] is not None, "Title field is None"
    assert len(data["title"]) > 0, "Title string is empty"

    # 5. Cleanup (Good practice, though Playwright closes contexts automatically on exit)
    api_context.dispose()

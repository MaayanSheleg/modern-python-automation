from playwright.sync_api import APIRequestContext, APIResponse

class PostsAPI:
    """
    Object Model for the JSONPlaceholder Posts API.
    This encapsulates the endpoint logic, separating it from the test validation.
    """
    def __init__(self, request_context: APIRequestContext):
        self.request = request_context
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_post_by_id(self, post_id: int) -> APIResponse:
        """
        Fetches a single post by its ID.
        """
        # We perform the GET request and return the raw response object
        # so the test can validate status codes and headers.
        response = self.request.get(f"{self.base_url}/posts/{post_id}")
        return response
class RequestInfoMiddleware:
    def _init_(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        # Access the request URL
        request_url = request.get_full_path()

        # Access the user agent
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown User Agent')

        # You can store or log the information as needed
        # For simplicity, we are just printing it here
        print(f"Request URL: {request_url}")
        print(f"User Agent: {user_agent}")

        # Continue with the request processing
        return self.get_response(request)
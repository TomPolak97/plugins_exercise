"""
This class include all the relevant exception the system should handle.
"""


class RequestFailedException(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(f"Request failed. The error status is: {status_code}")
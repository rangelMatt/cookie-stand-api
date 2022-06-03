import fire
import requests

# NOTE: Adjust these settings as needed
API_HOST = "http://localhost:8000"
RESOURCE_URI = "cookie_stands"
USERNAME = "admin"
PASSWORD = "admin"


class ApiTester:
    """CLI for testing API
    Server must be running.
    WARNING: Database queries are performed on supplied database.
        So be extra careful and/or use a test database.
    """

    def __init__(self, host=API_HOST):
        self.host = host

    def fetch_tokens(self):
        """Fetches access and refresh JWT tokens from api

        Returns:
            tuple: access,refresh
        """

        token_url = f"{self.host}/api/token/"

        response = requests.post(
            token_url, json={"username": USERNAME, "password": PASSWORD}
        )

        data = response.json()

        tokens = data["access"], data["refresh"]

        return tokens

    def get_all(self):
        """get list of all resources from api
        Usage: python api_tester.py get_all

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json() or 'No resources'

    def get_one(self, id):
        """get 1 resource by id from api

        Usage:
        python api_tester.py get_one 1

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    # TODO adjust parameter names to match API
    def create(self, location=None, owner=None, description=None, hourly_sales=0, minimum_customers_per_hour=0, maximum_customers_per_hour=0, average_cookies_per_sale=0):
        """creates a resource in api

        Usage:
        python api_tester.py create /
            --name=required --description=optional --owner=optional

        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        data = {
            "location": location,
            "description": description,
            "purchaser": purchaser,
        }

        response = requests.post(url, json=data, headers=headers)

        return response.json()

    def update(self, id, location=None, owner=None, description=None, hourly_sales=0, minimum_customers_per_hour=0, maximum_customers_per_hour=0, average_cookies_per_sale=0):
        """updates a resource in api

        Usage:
        python api_tester.py update 1 /
            --name=optional --description=optional --owner=optional

        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        original = self.get_one(id)

        data = {
            "location": location or original["location"],
            "owner": owner or original["owner"],
            "description": description or original["description"],
            "hourly_sales": hourly_sales or original["hourly_sales"],
            "minimum_customers_per_hour": minimum_customers_per_hour or original["minimum_customers_per_hour"],
            "maximum_customers_per_hour": maximum_customers_per_hour or original["maximum_customers_per_hour"],
            "maximum_customers_per_hour": maximum_customers_per_hour or original["maximum_customers_per_hour"],
        }

        response = requests.put(url, json=data, headers=headers)

        return response.text

    def delete(self, id):
        """deletes a resource in api

        Usage:
        python api_tester.py delete 1

        Returns: Empty string if no error
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.delete(url, headers=headers)

        return response.text


if __name__ == "__main__":
    fire.Fire(ApiTester)

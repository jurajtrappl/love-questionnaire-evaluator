from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


class GoogleFormsService:
    """
    Represents a wrapper around the Google Forms API.
    """

    def __init__(self, key_file_location, scopes):
        self.__key_file_location = key_file_location
        self.__scopes = scopes

    def get_service(self):
        """
        Get a service that communicates to a Google Forms API.

        Returns:
            A service that is connected to the Forms API.
        """

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.__key_file_location, scopes=self.__scopes)

        service = discovery.build("forms", "v1", credentials=credentials)

        return service

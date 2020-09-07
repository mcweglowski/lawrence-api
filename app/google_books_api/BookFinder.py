import requests


class BookFinder:

    def __init__(self, google_books_uri):
        self.__uri = google_books_uri
        self.__title = None
        self.__author = None
        self.__isbn = None

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_status_code(self):
        return self.__response.status_code

    def get_json(self):
        return self.__response.text

    def find_a_book(self):
        condition = self.__build_condition()

        if condition is None:
            return

        payload = {"q": condition}

        self.__response = self.__execute_request(payload)

        return self.__response.status_code

    def __build_condition(self):
        condition = None
        condition = self.__query_add_condition(condition,
                                               "intitle",
                                               self.__title)
        condition = self.__query_add_condition(condition,
                                               "inauthor",
                                               self.__author)
        condition = self.__query_add_condition(condition,
                                               "isbn",
                                               self.__isbn)
        return condition

    def __query_add_condition(self, condition, search_criterium, value):
        if not value:
            return condition
        if not condition:
            return f"{search_criterium}:{value}"
        return condition + f"+{search_criterium}:{value}"

    def __execute_request(self, payload):
        return requests.get(self.__uri, payload)

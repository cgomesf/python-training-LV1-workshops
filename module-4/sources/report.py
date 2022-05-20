class Page:
    def __init__(self, text):
        self.text = text


class ValidExtensions:
    @staticmethod
    def is_pdf():
        return ".pdf"

    @staticmethod
    def is_txt():
        return ".txt"


class Report:
    NUMBER_OF_PAGES = 0

    @classmethod
    def number_of_pages(cls):
        return cls.NUMBER_OF_PAGES

    @staticmethod
    def with_valid_extension(name_with_extension: str):
        is_valid = None
        if ValidExtensions.is_pdf() in name_with_extension:
            is_valid = "pdf"
        elif ValidExtensions.is_txt() in name_with_extension:
            is_valid = "txt"
        return is_valid

    def __init__(self, filename: str):
        self.filename = filename
        self.pages = []

    def add_page(self, page_text):
        self.pages.append(Page(page_text))
        Report.NUMBER_OF_PAGES += 1


def main():
    page_1 = Page("First page")
    page_2 = Page("Second page")
    page_3 = Page("Third page")
    assert Report.with_valid_extension("test.invalid") is None
    assert Report.with_valid_extension("test.pdf") is not None
    assert Report.with_valid_extension("test.txt") is not None

    report = Report("valid_document.pdf")
    assert report.number_of_pages() == 0

    report.add_page(page_1)
    report.add_page(page_2)
    report.add_page(page_3)

    assert report.number_of_pages() == 3
    for page in report.pages:
      assert isinstance(page, Page)

    print("OK !")


if __name__ == "__main__":
    main()

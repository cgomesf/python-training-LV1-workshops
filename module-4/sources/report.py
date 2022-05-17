class Page:
    def __init__(self, text):
        self.text = text


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

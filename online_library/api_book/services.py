from PyPDF2 import PdfReader


def read_pdf(book_path: str, current_page: int) -> dict:
    reader = PdfReader(book_path)
    number_of_pages = reader.getNumPages()
    page_end = current_page + 10 if number_of_pages - 10 > current_page else number_of_pages
    pages = reader.pages[current_page:page_end]
    return {
        "current_page": current_page,
        "num_of_pages": number_of_pages,
        "page_end": page_end,
        "pages": pages
    }


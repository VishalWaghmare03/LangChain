# # from langchain_docling import DoclingLoader

FILE_PATH = "/home/vishal/Documents/Documents/Non-Heading Document/Agreement for Sale.docx"

# # loader = DoclingLoader(file_path=FILE_PATH)

# # docs = loader.load()

# # for d in docs[:3]:
# #     print(f"- {d.page_content=}")

# from docling.document_converter import DocumentConverter

# converter = DocumentConverter()
# result = converter.convert(FILE_PATH)

# markdown_text = result.document.export_to_dict()
# print(markdown_text)


from langchain_docling import DoclingLoader
from langchain_docling.loader import ExportType

# Replace with your document's file path or URL
# FILE_PATH = "path/to/your/document.docx"

loader = DoclingLoader(
    file_path=FILE_PATH,
    export_type=ExportType.MARKDOWN  # Preserves numbering in markdown format
)

docs = loader.load()


for doc in docs:
    print(doc.page_content)

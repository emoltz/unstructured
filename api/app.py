from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from unstructured.documents.elements import Element
from unstructured.partition.pdf import partition_pdf


class PDFPartitionRequest(BaseModel):
    pdf_data: bytes
    filename: Optional[str] = None
    metadata: Optional[dict] = None


app = FastAPI()


@app.get("/")
def test_api():
    return {"Hello": "World"}


@app.get("/test/")
def test_unstructured():
    filepath = "/app/example-docs/pdf/layout-parser-paper-fast.pdf"
    elements: list[Element] = partition_pdf(filepath)
    return {"data1": elements}


@app.post("/partition/pdf/")
def partition_pdf_api(pdf_req: PDFPartitionRequest):
    pdf_data: bytes = pdf_req.pdf_data
    elements: list[Element] = partition_pdf(pdf_data)
    return {"elements": elements}

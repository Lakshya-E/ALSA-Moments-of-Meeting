import whisper
from PyPDF2 import PdfReader


def get_text(audios):
    result = None
    model = whisper.load_model("medium.en")
    for audio in audios:
        result = model.transcribe(audio, fp16=False)

    return result["text"]


def get_pdf(pdfs):
    text = ""
    for pdf in pdfs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()

    return text


if __name__ == "__main__":
    get_pdf("pdf_file.pdf")
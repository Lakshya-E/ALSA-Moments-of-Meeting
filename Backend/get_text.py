import whisper
# from PyPDF2 import PdfReader


def get_text(audio):
    """This function takes audio and converts it into text and return the
    generated text"""
    model = whisper.load_model("medium.en")
    result = model.transcribe(audio, fp16=False)

    return result["text"]


# def get_pdf(pdfs):
#     text = ""
#     for pdf in pdfs:
#         pdf_reader = PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#
#     return text
#
#
# if __name__ == "__main__":
#     get_pdf("pdf_file.pdf")

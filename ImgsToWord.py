from ImgsToWordApp import ImgsToWordApp

if __name__ == "__main__":
    app = ImgsToWordApp(dir_path=".", doc_name="imgs.docx")
    app.convert()

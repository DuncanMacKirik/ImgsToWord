import argparse

from ImgsToWordApp import ImgsToWordApp


class ImgsToWordAppCLI(ImgsToWordApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_cli_params()
    
    def set_cli_params(self):
        parser = argparse.ArgumentParser(description="A tool to insert image thumbnails in a new Word document")
        parser.add_argument("-f", "--filename", help="result file name", default="imgs.docx")
        parser.add_argument("--height_h", help="height (in pixels) for horizontal image thumbnails", type=int, default=120)
        parser.add_argument("--height_v", help="height (in pixels) for vertical image thumbnails", type=int, default=160)
        parser.add_argument("-s", "--split", help="split horizontal and vertical thumbnail sections by inserting a page break", action="store_true")
        parser.add_argument("dir", help="directory with image files", nargs='?', default=".")
        args = parser.parse_args()
        self.info_func(args)
        args_map = {"dir": "dir_path", "f": "doc_name", "filename": "doc_name", "height_h": "imgh_h", "height_v": "imgh_v",
            "s": "split", "split": "split"}
        args_val = dict()
        for arg_name in args_map:
            if arg_name in args:
                args_val[args_map[arg_name]] = getattr(args, arg_name)
        self.info_func(args_val)
        self.set_params(**args_val)

    def run(self):
        self.convert()


if __name__ == "__main__":
    app = ImgsToWordAppCLI()
    app.run()

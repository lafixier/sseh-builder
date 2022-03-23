import os
import sys


def main():
    builder = Builder()
    # 引数が足りない場合にヘルプを表示
    if len(sys.argv) != 3:
        print(builder.help)
        return
    builder.build(sys.argv[1], sys.argv[2])


class Builder:
    def __init__(self) -> None:
        self.help = """Commands:\n\tbuild {src_file_path} {dest_file_path}\tBuild the source file and write the result into the dest file."""
        self._src_file_path = ""
        self._dest_file_path = ""
        self._src = ""

    def _error(self, message: str) -> None:
        print(f"ERROR: {message}")

    def _read_src_file(self) -> None:
        with open(self._src_file_path, encoding="utf-8") as f:
            self._src = f.read()

    def build(self, src_file_path: str, dest_file_path: str) -> None:
        self._src_file_path = src_file_path
        self._dest_file_path = dest_file_path
        if not os.path.exists(self._src_file_path):
            self._error(
                f"The source file '{self._src_file_path}' does not exists.")
            return
        self._read_src_file()


if __name__ == "__main__":
    main()

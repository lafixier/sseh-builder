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

    def build(self, src_file_path: str, dest_file_path: str) -> None:
        self._src_file_path = src_file_path
        self._dest_file_path = dest_file_path


if __name__ == "__main__":
    main()

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
        self._lines = []
        self._built_lines = []
        self._build_status = {"mode": "", "is_active": False}

    def _error(self, message: str) -> None:
        print(f"ERROR: {message}")

    def _read_src_file(self) -> None:
        with open(self._src_file_path, encoding="utf-8") as f:
            self._src = f.read()

    def _build_src(self) -> None:
        self._lines = self._src.split("\n")
        for line in self._lines:
            line_stripped = line.strip()
            command_line = line_stripped.lstrip(
                "<!--").rstrip("-->").lstrip("//").strip()
            if line_stripped.startswith("<!--") or line.startswith("//"):
                if command_line.startswith("$build"):
                    args = command_line.lstrip("$build").lstrip().split()
                    if len(args) != 2 or (args[0] != "develop" and args[0] != "production") and (args[1] != "begin" or args[1] != "end"):
                        self._error(
                            f"Line `{line}` is invalid.\nUsage:\n\t$build [develop/production] [begin/end]")
                    else:
                        self._build_status["mode"] = args[0]
                        if args[1] == "begin":
                            self._build_status["is_active"] = True
                        else:
                            self._build_status["is_active"] = False
                        continue
            if self._build_status["is_active"]:
                if self._build_status["mode"] == "production":
                    line_tmp = line_stripped.lstrip(
                        "<!--").rstrip("-->").strip().lstrip("//")
                    for char in line:
                        if char == " ":
                            line_tmp = " " + line_tmp
                        else:
                            break
                    self._built_lines.append(line_tmp)
                elif self._build_status["mode"] == "develop":
                    continue
            else:
                self._built_lines.append(line)

    def build(self, src_file_path: str, dest_file_path: str) -> None:
        self._src_file_path = src_file_path
        self._dest_file_path = dest_file_path
        if not os.path.exists(self._src_file_path):
            self._error(
                f"The source file '{self._src_file_path}' does not exists.")
            return
        self._read_src_file()
        self._build_src()


if __name__ == "__main__":
    main()

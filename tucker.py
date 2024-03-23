import argparse


class Tucker:
    def __init__(self, zip_path: str, jpg_path: str, output_path: str) -> None:
        self.zip_file_path = zip_path
        self.jpg_file_path = jpg_path
        self.output_file_path = output_path

    def open_zip(self) -> bytes:
        with open(self.zip_file_path, 'rb') as zip_obj:
            return zip_obj.read()

    def open_jpg(self) -> bytes:
        with open(self.jpg_file_path, 'rb') as jpg_obj:
            return jpg_obj.read()

    def combine(self) -> None:
        zip_file_data = self.open_zip()
        jpg_file_data = self.open_jpg()

        combined_file = jpg_file_data + zip_file_data

        with open(self.output_file_path, 'wb') as output_obj:
            output_obj.write(combined_file)

        print("[+] Data combined!")


def main() -> None:
    parser = argparse.ArgumentParser(description="Hide a zip file at the end of a jpg.")
    parser.add_argument('--jpg', required=True, dest="jpg_file_path")
    parser.add_argument('--zip', required=True, dest="zip_file_path")
    parser.add_argument('--output', required=True, dest="output_file_path")
    args = parser.parse_args()

    tucker = Tucker(args.zip_file_path, args.jpg_file_path, args.output_file_path)

    tucker.combine()


if __name__ == "__main__":
    main()

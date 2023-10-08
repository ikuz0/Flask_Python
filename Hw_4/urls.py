import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-url")
    return parser


urls = [
    "https://gas-kvas.com/uploads/posts/2023-02/1675489758_gas-kvas-com-p-izobrazheniya-i-kartinki-na-fonovii-risuno-41.jpg",
    "https://w.forfun.com/fetch/b7/b7bb4d30d03d45eb1cbbcf56cfdb72fb.jpeg",
    "https://klike.net/uploads/posts/2023-02/1675342516_3-46.jpg",
    "https://ink-project.ru/sites/1-ink-project/photoalbums/18157.jpg",
]

if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    urls.append(namespace.url)
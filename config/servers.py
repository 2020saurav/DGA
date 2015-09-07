from src.util.server import Server

servers = [
    Server('01', '127.0.0.1', 2020, "master", True),
    Server('02', '127.0.0.1', 2021, "slave", True),
    Server('03', '127.0.0.1', 2022, "slave", False),
    Server('04', '127.0.0.1', 2023, "slave", False)
]

from src.util.server import Server

servers = [
    Server('master', '127.0.0.1', 2020, "master", True),
    Server('s1', '127.0.0.1', 2021, "slave", True),
    Server('s2', '127.0.0.1', 2022, "slave", False),
    Server('s3', '127.0.0.1', 2023, "slave", False),
    Server('s4', '127.0.0.1', 2024, "slave", False)
]

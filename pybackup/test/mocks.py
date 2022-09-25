path_structure = {
    "/": ["test1/", "test2", "log.txt"],
    "/test1/": ["game.pdf", "game.exe"],
    "/test2/": ["logs/", "img.png", "player.asdf"],
    "/test2/logs/": ["make.txt", "make.py"],
}


def listDirMock(path: str):
    path_structure.get(path, [])

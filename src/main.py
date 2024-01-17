import queue

from src.FileWalker import DirWalker, MdParser

mdQueue = queue.Queue()

if __name__ == "__main__":
    dirWalker = DirWalker('./ru', mdQueue)
    dirWalker.run()

    parser = MdParser(mdQueue)
    parser.run()

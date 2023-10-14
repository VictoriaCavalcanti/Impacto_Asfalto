import sys
import os

# Obtenha o caminho absoluto do diretório em que este script está localizado.
current_path = os.path.abspath(os.path.dirname(__file__))
src_path = os.path.join(current_path, "src")

# Adicione o diretório atual ao sys.path se ainda não estiver lá.
if src_path not in sys.path:
    sys.path.append(src_path)

from src.app import Scrappy

if (__name__ == '__main__'):
  scrappy = Scrappy(None, False, True)
  scrappy.run()

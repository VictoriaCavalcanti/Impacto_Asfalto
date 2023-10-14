import sys
import os

# Obtenha o caminho absoluto do diretório em que este script está localizado.
diretorio_atual = os.path.abspath(os.path.dirname(__file__))
src_path = os.path.join(diretorio_atual, "src")

# Adicione o diretório atual ao sys.path se ainda não estiver lá.
if src_path not in sys.path:
    sys.path.append(src_path)

from src.app import Scrappy

if (__name__ == '__main__'):
  scrappy = Scrappy(None, False, True)
  scrappy.run()

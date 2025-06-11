import subprocess
import os
import sys

class Cripto:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.executable_path = os.path.join(base_path, "motor_cripto")
        if sys.platform == "win32":
            self.executable_path += ".exe"

        if not os.path.exists(self.executable_path):
            raise FileNotFoundError(f"Executável não encontrado em: {self.executable_path}")

    def _run_engine(self, action, key, text):
        try:
            result = subprocess.run(
                [self.executable_path, action, key, text],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Erro ao executar o motor de criptografia: {e}"
        except Exception as e:
            return f"Ocorreu um erro inesperado: {e}"

    def encrypt(self, text, key):
        if not key or not text:
            raise ValueError("Texto e chave não podem ser vazios.")
        return self._run_engine("encrypt", key, text)

    def decrypt(self, encrypted_text, key):
        if not key or not encrypted_text:
            raise ValueError("Texto cifrado e chave não podem ser vazios.")
        return self._run_engine("decrypt", key, encrypted_text)
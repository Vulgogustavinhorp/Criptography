# 🚀 Projeto de Criptografia Híbrida: Python + C++

Olá, rede!

Gostaria de compartilhar um projeto que desenvolvi para explorar a sinergia entre Python e C++, demonstrando como utilizar a força de cada linguagem para criar uma solução de automação eficiente e de alta performance.

### O Conceito

Este projeto é um sistema de criptografia simples que utiliza uma arquitetura híbrida:

* **Python (O Orquestrador Inteligente):** Atua como a interface amigável (front-end). É responsável por gerenciar a interação com o usuário, validar os dados de entrada e orquestrar o fluxo de trabalho. Sua simplicidade e legibilidade o tornam perfeito para essa tarefa.

* **C++ (O Motor de Alta Performance):** Atua como o núcleo de processamento (back-end). A lógica de criptografia, que pode ser computacionalmente intensiva, é implementada em C++ para garantir a máxima velocidade e eficiência. O programa C++ é compilado em um executável e chamado pelo script Python.

Essa abordagem combina "o melhor dos dois mundos": a agilidade e facilidade de desenvolvimento do Python com a performance bruta do C++.

### Arquitetura do Projeto

1.  **Interface em Python:** Um script `cripto.py` oferece funções simples de `encrypt()` e `decrypt()`.
2.  **Comunicação:** O Python utiliza o módulo `subprocess` para executar o programa C++ compilado, passando a ação (criptografar/descriptografar), a chave e o texto como argumentos de linha de comando.
3.  **Processamento em C++:** O executável `motor_cripto` recebe os argumentos, realiza a operação de criptografia (usando uma cifra de XOR como prova de conceito) e imprime o resultado na saída padrão.
4.  **Retorno:** O Python captura a saída do programa C++ e a retorna ao usuário final.

### Como Executar

1.  **Pré-requisitos:**
    * Um compilador C++ (como o g++ via MSYS2 no Windows).
    * Python 3.x.

2.  **Compilação:**
    * Compile o motor de criptografia:
        ```sh
        g++ -o motor_cripto motor_cripto.cpp
        ```

3.  **Execução:**
    * Execute o script de exemplo para ver a mágica acontecer:
        ```sh
        python exemplo_uso.py
        ```

Este projeto foi um exercício fascinante sobre interoperabilidade de linguagens e design de software, mostrando que é possível construir sistemas robustos e eficientes escolhendo a ferramenta certa para cada tarefa.

Sinta-se à vontade para conectar e discutir mais sobre tecnologia, programação e o futuro da IA!

#Python #Cpp #Cplusplus #DesenvolvimentoDeSoftware #Programação #EngenhariaDeSoftware #Criptografia #Automação
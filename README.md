# [Match-IBM] Projeto Final

## Índice

- [Sobre](#sobre)
- [Projeto Escolhido](#projeto-escolhido)
- [Descrição](#descrição)
- [Etapas/Fluxo do app (Requisitos Mínimos do Projeto)](#etapasfluxo-do-app-requisitos-mínimos-do-projeto)
- [Ambientes de Desenvolvimento e Homologação](#ambientes-de-desenvolvimento-e-homologação)
- [Como executar o projeto](#como-executar-o-projeto)
- [Autores](#autores)
- [Licença](#licença)

## Sobre

Este repositório contém o projeto final da formação **[Match!](https://match.mastertech.com.br/)**, oferecido pela **IBM** em parceria com a **Mastertech**.

O projeto consiste em uma aplicação Web (front e back-end), desenvolvido com o framework Flask, que calcula quanto tempo levará para atingir uma meta financeira com base em uma economia mensal definida.

## Projeto Escolhido

- [x] Projeto 6: Calculadora de Meta Financeira com Economia Mensal

## Descrição

- Desenvolvimento de aplicação Web com back-end em Python;
- Aplicação deve calcular **quanto tempo** levará para atingir a "**meta financeira**" com base em
  uma **economia mensal** definida. - A meta financeira pode ser, por exemplo uma economia para uma viagem, compra importante ou qualquer objetivo financeiro.

## Etapas/Fluxo do app (Requisitos Mínimos do Projeto)

1. Definição da Meta Financeira;
   - Usuário inserire valor da meta financeira que deseja atingir.
2. Definição da Economia Mensal;
   - Usuário fornecer valor que podem economizar mensalmente para alcançar sua meta.
3. Cálculo do Tempo Necessário;
   - A aplicação deve calcular o número de meses necessários para atingir a meta financeira com base na economia mensal e no valor da meta.
4. Apresentação dos Resultados.
   - A aplicação exibirá o tempo estimado para atingir a meta financeira com base nas informações fornecidas pelo usuário.

## Ambientes de Desenvolvimento e Homologação

- Desenvolvido e testado com Python 3.11.5 no Windows 11;
- Deploy no Vercel com Python 3.9 (Linux);

## Como executar o projeto

- Recomendo instalar o [chocolatey](https://chocolatey.org/install);
- Python (versão >=3.9 & <4) é necessário, dado os requisitos do projeto: `choco install python --version=3.11.5`;
- `make` é opcional, mas facilita a execução do projeto: `choco install make`;
- Instale as dependências do projeto: `make install`;
- Execute o projeto: `make run`;

Caso não queira instalar o `make`, execute os comandos do arquivo `Makefile` manualmente.

- `pip install poetry`;
- `poetry install`;
- `poetry run python api/index.py`;

## Autores

- [@ArielMAJ](https://ariel.artadevs.tech/): ariel.maj@hotmail.com

## Licença

Este projeto está licenciado sob a licença [MIT](https://choosealicense.com/licenses/mit/) - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

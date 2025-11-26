# Linguagem Formal: Covogal

Projeto desenvolvido para a disciplina de Teoria da Computação. Este projeto implementa um Autômato Finito Determinístico (AFD) para reconhecer a linguagem regular **Covogal**.

## 📋 Regras da Linguagem
O alfabeto é **Σ = {A, E, H, N}**.
A regra fundamental é:
> Toda vogal (**A**, **E**) deve ser imediatamente seguida por uma consoante (**H**, **N**).

## 🚀 Como Rodar
Certifique-se de ter o Python 3 instalado.

```bash
python3 main.py
```

## 🛠️ Estrutura do Autômato

Estados: q0 (Seguro), q1 (Inseguro), q_erro (Morto)

Estado Inicial: q0

Estados Finais: {q0}

# 🧪 Testes Unitários da Calculadora

Este projeto adiciona testes automatizados para uma calculadora escrita em Python. 

Utilizamos dois frameworks:

- [`unittest`](https://docs.python.org/3/library/unittest.html): Módulo de testes padrão da linguagem.
- [`pytest`](https://docs.pytest.org/en/stable/): Framework moderno e mais produtivo para testes em Python.

---

## ✅ Funcionalidades testadas

- Adição
- Subtração
- Multiplicação
- Divisão
- Potência
- Raiz quadrada
- Porcentagem
- Erros esperados (ex: divisão por zero, raiz de número negativo)

---

## 🗂️ Estrutura do Projeto

```bash
.
├── calculadora.py                    # Código principal da calculadora
├── requirements.txt                 # Dependências do projeto (opcional)
├── test_calculadora_unittest.py    # Testes usando unittest
├── test_calculadora_pytest.py      # Testes usando pytest
└── __pycache__/                    # Cache interno do Python
```

---

## ▶️ Executando os testes

### Com `unittest` (built-in no Python)

```bash
python3 -m unittest test_calculadora_unittest.py
```

### Com `pytest` (instale com `pip install pytest`)

```bash
pytest test_calculadora_pytest.py
```

---

## 📌 Observações

* Os testes cobrem **apenas as funções puras** da calculadora.
* Entradas e saídas via `input()` e `print()` **não são testadas** diretamente aqui.
* Para testar a interface interativa (CLI), seria necessário usar `unittest.mock` ou `pytest-mock`.

---

## 💡 Recomendação

Use `pytest` sempre que possível — ele é mais simples, mais poderoso, e fornece mensagens de erro mais legíveis.

---


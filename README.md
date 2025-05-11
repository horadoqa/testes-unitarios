# 🧪 Testes Unitários em Desenvolvimento de Software

## 📖 O que são Testes Unitários?

**Testes unitários** são métodos automatizados usados para validar se pequenas partes do seu código (as “unidades”) estão funcionando corretamente. Normalmente, uma unidade é uma função ou método individual.

Eles ajudam a garantir que o comportamento de cada parte do sistema esteja de acordo com o esperado — mesmo após mudanças no código.

<div align="center">
    <img src="./images/unitarios.jfif">
</div>

---

## 🎯 Objetivos dos Testes Unitários

* **Verificar a lógica de cada função de forma isolada.**
* **Detectar erros rapidamente durante o desenvolvimento.**
* **Evitar regressões (quebras acidentais) em versões futuras.**
* **Servir como documentação viva sobre o comportamento do código.**

---

## 🛠️ Quando e onde usar?

Você deve escrever testes unitários para qualquer função ou método que contenha lógica de negócio importante ou que possa apresentar variações de comportamento, por exemplo:

* Operações matemáticas
* Validações de entrada
* Processamento de dados
* Cálculos de regras de negócio

---

## ⚙️ Ferramentas Comuns por Linguagem

| Linguagem  | Ferramenta(s) Popular(es) |
| ---------- | ------------------------- |
| Python     | `unittest`, `pytest`      |
| JavaScript | `Jest`, `Mocha`, `Chai`   |
| Java       | `JUnit`, `Mockito`        |
| C# / .NET  | `xUnit`, `NUnit`          |
| Go         | `testing` (nativo)        |

---

## ✅ Características de um bom teste unitário

* **Rápido:** deve rodar em milissegundos.
* **Isolado:** não depende de outras funções ou do ambiente externo (como rede ou banco de dados).
* **Repetível:** deve produzir o mesmo resultado sempre.
* **Clareza:** fácil de entender e de saber o que está sendo testado.

---

## 🧪 Estrutura de um Teste Unitário (Exemplo em Pseudocódigo)

```pseudocode
função soma(a, b) => a + b

// Teste
entrada: soma(2, 3)
esperado: 5
verificar: resultado == 5
```

---

## 🧹 Boas práticas

* Use nomes descritivos para os testes (ex: `deveRetornarErroQuandoDivisaoPorZero`)
* Evite testes duplicados.
* Foque em **um único comportamento por teste**.
* Mantenha os testes sempre atualizados junto com o código.

---

## 🔍 Diferença entre tipos de testes

| Tipo de Teste        | O que cobre?                   | Exemplo                                   |
| -------------------- | ------------------------------ | ----------------------------------------- |
| **Unitário**         | Funções ou métodos isolados    | `soma(2, 3) === 5`                        |
| **Integração**       | Módulos que interagem entre si | Serviço de login usando banco de dados    |
| **End-to-End (E2E)** | Fluxos completos de usuário    | Testar um cadastro completo via navegador |

---

## 🚀 Por que testar?

* Reduz bugs em produção
* Aumenta a confiança na refatoração
* Facilita a manutenção
* Permite desenvolvimento orientado a testes (TDD)

---

## 📚 Leitura complementar

* [Guia do Jest (JS)](https://jestjs.io/pt-BR/docs/getting-started)
* [Documentação do Pytest (Python)](https://docs.pytest.org/en/stable/)
* [Livro: Test-Driven Development - Kent Beck](https://www.goodreads.com/book/show/387190.Test_Driven_Development)

---

## 🧩 Exemplos Práticos

- Python com Pytest e Unitest
- Javascript com Jest



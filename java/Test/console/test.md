# Executando testes no projeto

Neste guia, você aprenderá a executar testes usando a biblioteca **JUnit** em um projeto Java organizado.

---

## 1. Organização do projeto

É importante que o código esteja organizado em módulos (classes separadas), pois isso melhora a organização, reutilização e manutenção do código — uma boa prática essencial em programação orientada a objetos, especialmente em Java.

### Estrutura de arquivos exemplo:

Suponha que você tenha o seguinte conteúdo na pasta `ModulosIMC`:

```bash
.
├── console
│   ├── CalculaIMC.java
│   ├── IMCCalculadora.java
│   ├── Pessoa.java
│   └── test.md
├── images
│   └── test-junit.png
├── lib
│   └── junit-platform-console-standalone-1.13.1.jar
├── out
│   └── Test
│       ├── console
│       │   ├── CalculaIMC.class
│       │   ├── IMCCalculadora.class
│       │   └── Pessoa.class
│       └── test
│           └── CalculaIMCTest.class
├── run-tests.sh
└── test
    └── CalculaIMCTest.java

8 directories, 12 files
```

### Principais arquivos/classes

1. **Classe `Pessoa`**
   Responsável por armazenar os dados do usuário.

2. **Classe `IMCCalculadora`**
   Responsável por calcular o IMC e classificar o resultado.

3. **Classe `CalculaIMC` (classe principal)**
   Responsável por executar o programa.

4. **Classe `CalculaIMCTest`**
   Contém os testes unitários para as funcionalidades do projeto.

---

## 2. Preparação do ambiente

Se você ainda não tem, baixe o JUnit 5 (arquivo `junit-platform-console-standalone-x.y.z.jar`) do site oficial:

[https://search.maven.org/artifact/org.junit.platform/junit-platform-console-standalone](https://search.maven.org/artifact/org.junit.platform/junit-platform-console-standalone)

Link direto para a versão usada neste projeto:

```
https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.13.1/junit-platform-console-standalone-1.13.1.jar
```

Coloque o `.jar` dentro da pasta `lib` do seu projeto.

---

## 3. Compilar os arquivos

Abra o terminal na pasta que contém a pasta `ModulosIMC` e execute:

### Compilar os arquivos de produção (console):

```bash
javac -d Test/out -cp Test/lib/junit-platform-console-standalone-1.13.1.jar Test/console/*.java
```

### Compilar os arquivos de teste:

```bash
javac -d Test/out -cp "Test/lib/junit-platform-console-standalone-1.13.1.jar:Test/out" Test/test/*.java
```

---

## 4. Executar os testes

Após compilar, execute os testes com o comando:

```bash
java -jar Test/lib/junit-platform-console-standalone-1.13.1.jar execute --class-path Test/out --scan-class-path
```

---

## 5. Saída esperada

Você deverá ver algo parecido com:

```bash
💚 Thanks for using JUnit! Support its development at https://junit.org/sponsoring

╷
├─ JUnit Platform Suite ✔
├─ JUnit Jupiter ✔
│  └─ CalculaIMCTest ✔
│     ├─ testCalculoIMC() ✔
│     ├─ testClassificacaoAbaixoPeso() ✔
│     ├─ testClassificacaoSobrepeso() ✔
│     ├─ testClassificacaoObesidade() ✔
│     └─ testClassificacaoPesoNormal() ✔
└─ JUnit Vintage ✔

Test run finished after 84 ms
[         4 containers found      ]
[         0 containers skipped    ]
[         4 containers started    ]
[         0 containers aborted    ]
[         4 containers successful ]
[         0 containers failed     ]
[         5 tests found           ]
[         0 tests skipped         ]
[         5 tests started         ]
[         0 tests aborted         ]
[         5 tests successful      ]
[         0 tests failed          ]
```

---

## 6. Configuração do VSCode para reconhecer o JUnit

Para que o VSCode reconheça o JUnit no editor (autocomplete, verificação de erros etc.), adicione no arquivo `.vscode/settings.json` do seu projeto a referência ao JAR do JUnit:

```json
{
  "java.project.referencedLibraries": [
    "projetos/ModulosIMC/gson/lib/gson-2.10.1.jar",
    "projetos/ModulosIMC/Test/lib/junit-platform-console-standalone-1.13.1.jar"
  ]
}
```

**Atenção:** Ajuste os caminhos conforme a estrutura e o local do seu projeto.

---

### 7. Reinicie o VSCode

Após salvar as alterações no `settings.json`, reinicie o VSCode ou use o comando da paleta:

```
Ctrl+Shift+P → Reload Window
```

Isso fará o VSCode recarregar o projeto e reconhecer as bibliotecas corretamente.

Bons testes !!!

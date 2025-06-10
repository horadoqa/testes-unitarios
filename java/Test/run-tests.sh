#!/bin/bash
echo "Compilando..."
javac -cp lib/junit-platform-console-standalone-1.13.1.jar Test/console/*.java

echo "Executando testes..."
java -jar lib/junit-platform-console-standalone-1.13.1.jar \
  --class-path Test \
  --scan-class-path


# chmod +x run-tests.sh
# ./run-tests.sh
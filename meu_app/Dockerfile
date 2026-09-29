# Imagem base: sistema operacional Ubuntu
FROM ubuntu:24.04

# Metadados da imagem
LABEL maintainer="Luiz Filipe <lfsjs@cesar.school>"

# Evita perguntas interativas do apt durante o build
ENV DEBIAN_FRONTEND=noninteractive

# Instala o Python e limpa o cache do apt na mesma camada (imagem menor)
RUN apt-get update && apt-get install -y --no-install-recommends python3 \
    && rm -rf /var/lib/apt/lists/*

# Pasta de trabalho dentro do container
WORKDIR /app

# Copia o codigo para dentro da imagem
COPY app.py .

# Comando executado quando o container sobe
CMD ["python3", "app.py"]

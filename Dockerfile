# Use uma imagem base do Python
FROM python:3.11-slim

# Defina variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    VENV_PATH="/opt/venv"

# Instale pacotes necessários
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*  # Limpa o cache do apt para reduzir o tamanho da imagem

# Criar o ambiente virtual **como root** e definir as permissões
RUN python -m venv ${VENV_PATH} && chown -R 1001:1001 ${VENV_PATH}

# Criar um usuário não-root
RUN useradd -ms /bin/bash -u 1001 appuser

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos da aplicação e garantir que o usuário appuser tenha acesso
COPY --chown=appuser:appuser . /app

# Mudar para o usuário não-root
USER appuser

# Instalar dependências dentro do venv
RUN ${VENV_PATH}/bin/pip install --no-cache-dir --upgrade pip && \
    ${VENV_PATH}/bin/pip install --no-cache-dir -r requirements.txt

# Definir o comando de execução
#CMD ["/opt/venv/bin/python", "app.py"]
CMD ["sh", "-c", "python app.py && tail -f /dev/null"]

FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .

# Install lightweight packages first
RUN pip install --no-cache-dir streamlit python-dotenv requests beautifulsoup4 PyPDF2 python-docx

# Install medium-weight packages
RUN pip install --no-cache-dir pandas openai langchain langchain-community

# Install heavy packages one by one to avoid timeouts
RUN pip install --no-cache-dir spacy
RUN pip install --no-cache-dir faiss-cpu
RUN pip install --no-cache-dir crewai

# Download spaCy model after spacy installation
RUN python -m spacy download en_core_web_sm

COPY . .

EXPOSE 8501

HEALTHCHECK --interval=60s --timeout=30s --start-period=60s --retries=2 \
    CMD curl --fail http://localhost:8501/_stcore/health || exit 1

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
FROM python:3.10
WORKDIR /code
ENV PORT 8000
EXPOSE 8000
# Install dependencies and clean up in one layer
RUN apt-get update && \
   apt-get install -y --no-install-recommends \
       libmagic1 \
       libgl1-mesa-glx \
       libreoffice \
       cmake \
       poppler-utils \
       tesseract-ocr && \
   apt-get clean && \
   rm -rf /var/lib/apt/lists/*
# Set LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
# Copy requirements file and install Python dependencies
COPY requirements.txt constraints.txt /code/
# --no-cache-dir --upgrade 

RUN pip install --upgrade pip
RUN pip install -U langchain-community
RUN pip install -r requirements.txt -c constraints.txt


RUN pip install --upgrade protobuf && \
    cp /usr/local/lib/python3.10/site-packages/google/protobuf/runtime_version.py /tmp/

RUN pip install protobuf==3.20.3 --force-reinstall && \
    cp /tmp/runtime_version.py /usr/local/lib/python3.10/site-packages/google/protobuf/

# Copy application code
COPY . /code
# Set command
CMD ["uvicorn", "score:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

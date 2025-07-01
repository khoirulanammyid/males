FROM python:3.9-slim

# Tetapkan direktori kerja di dalam kontainer
WORKDIR /app

# Salin file requirements dan install dependensi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin sisa kode aplikasi ke direktori kerja
COPY . .

# Ekspos port yang digunakan oleh Flask di dalam kontainer
EXPOSE 5000

# Perintah untuk menjalankan aplikasi saat kontainer dimulai
CMD ["flask", "run", "--host=0.0.0.0"]
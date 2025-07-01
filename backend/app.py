# backend/app.py
import os
import io
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS

# Inisialisasi aplikasi Flask
app = Flask(__name__)
# Mengaktifkan Cross-Origin Resource Sharing (CORS) agar frontend bisa berkomunikasi dengan backend
CORS(app)

@app.route('/create-file', methods=['POST'])
def create_corrupt_file():
    """
    Endpoint untuk membuat file dengan data acak (corrupt).
    Menerima nama, format, dan ukuran dari request JSON.
    Mengembalikan file sebagai attachment untuk diunduh.
    """
    try:
        # Mendapatkan data JSON dari request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        name = data.get('name')
        fmt = data.get('format')
        size_str = data.get('size')

        # Validasi input
        if not all([name, fmt, size_str]):
            return jsonify({"error": "Missing required fields: name, format, size"}), 400
        
        if not name.strip() or not fmt.strip():
            return jsonify({"error": "Name and format cannot be empty"}), 400

        # Konversi ukuran ke integer dan validasi
        try:
            size = int(size_str)
            if size <= 0 or size > 500 * 1024 * 1024: # Batas ukuran 500 MB
                 return jsonify({"error": "Size must be a positive number and not exceed 500MB"}), 400
        except (ValueError, TypeError):
            return jsonify({"error": "Size must be a valid integer"}), 400

        # Membuat data biner acak
        random_data = os.urandom(size)

        # Membuat file di memori menggunakan io.BytesIO
        buffer = io.BytesIO(random_data)
        buffer.seek(0) # Pindahkan kursor ke awal buffer

        # Nama file yang akan diunduh
        download_name = f"{name}.{fmt}"

        # Mengirim file sebagai respons yang dapat diunduh
        return send_file(
            buffer,
            as_attachment=True,
            download_name=download_name,
            mimetype='application/octet-stream' # Tipe MIME umum untuk data biner
        )

    except Exception as e:
        # Menangani error tak terduga
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == '__main__':
    # Menjalankan aplikasi pada host 0.0.0.0 agar dapat diakses dari luar kontainer
    app.run(host='0.0.0.0', port=5000, debug=True)

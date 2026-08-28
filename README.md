# Corrupt File Generator

**males** is a simple tool for generating corrupt (dummy) files with a user-specified
name, format, and size. It fills files with random data and, where the format is known,
prepends the correct magic bytes so the file is recognized by tools such as `file`.

## Features

- **Customizable:** Create files with a specified name, format, and size.
- **Format signatures:** Known formats are stamped with their correct magic bytes
  (`mp4`, `mkv`, `mp3`, `wav`, `jpg`/`jpeg`, `png`, `gif`, `webp`, `pdf`, `zip`,
  `docx`, `xlsx`, `rar`, `7z`).
- **Multi-interface:** Available as Bash, Python, and Rust command-line tools, plus a
  web application.
- **Cross-platform (Rust):** Uses a self-contained xorshift pseudo-random generator
  instead of `/dev/urandom`, so it builds and runs on Linux, macOS, and Windows.

## Implementations

| Interface | Language | Location |
|-----------|----------|----------|
| CLI | Rust | `males-rust/` |
| CLI | Python | `males.py` |
| CLI | Bash | `males.sh` |
| Web app | Flask + HTML/JS | `backend/`, `frontend/`, `docker-compose.yml` |

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jonyxz/males.git
   cd males
   ```

2. **(Rust) Install Rust** by following the instructions at <https://rustup.rs>.

3. **(Python) Install Python** (e.g., on Arch Linux):

   ```bash
   sudo pacman -S python
   ```

## Usage

### Rust (Recommended)

Build and run:

```bash
cd males-rust
cargo run --release
```

The program prompts for a file name, a format, and a size:

```text
Nama file (tanpa ekstensi): dummy
Format (mp4, mkv, mp3, wav, jpg, jpeg, png, gif, webp, pdf, zip, docx, xlsx, rar, 7z): pdf
Ukuran (contoh: 5M, 10K, 100): 5M
```

- **Format:** any of the supported extensions listed in the prompt. Unknown extensions
  still produce a file, just without magic bytes.
- **Size:** accepts plain bytes (`100`) or suffixes in multiples of 1024 — `K`
  (KiB), `M` (MiB), `G` (GiB).

### Python

```bash
python males.py
```

### Bash

```bash
chmod +x males.sh
./males.sh
```

### Web App

Run the frontend and backend with Docker Compose:

```bash
docker compose up --build
```

- Frontend: <http://localhost:8080>
- Backend API: <http://localhost:5001>

## Conclusion

This Corrupt File Generator is a simple yet useful tool to quickly create corrupt files
for testing or experimentation. With CLI tools in Bash, Python, and Rust — plus a
browser-based web app — you can easily generate files with random data in any format and
size. We hope this tool is helpful for your needs, and feel free to contribute or provide
feedback to improve it further.

Thank you for using this tool, and happy coding!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
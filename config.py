"""
Global configuration for DocumentGPT Pro
"""

# ===============================
# Application
# ===============================

APP_NAME = "📄 DocumentGPT Pro"
APP_ICON = "📄"

# ===============================
# Models
# ===============================

LLM_MODEL = "llama3.2:3b"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ===============================
# LLM Defaults
# ===============================

DEFAULT_TEMPERATURE = 0.2
DEFAULT_TOP_K = 3

# ===============================
# Document Processing
# ===============================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
TOP_K_RESULTS = DEFAULT_TOP_K

# ===============================
# Storage
# ===============================

UPLOAD_FOLDER = "uploads"
VECTOR_DB_PATH = "chroma_db"

# ===============================
# Supported File Types
# ===============================

SUPPORTED_FILE_TYPES = [
    "pdf",
    "docx",
    "txt"
]
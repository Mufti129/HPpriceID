#!/bin/bash
# Script Sinkronisasi Otomatis ke GitHub Repository
# Penggunaan: ./git_sync.sh "Pesan commit pembaruan"

COMMIT_MSG="${1:-update: update smartphone dataset, pipeline, and models}"

echo "🔄 Menyiapkan pembaruan untuk GitHub..."
git add .

echo "📝 Membuat commit: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

echo "🚀 Melakukan push ke origin main..."
git push origin main

echo "✅ Pembaruan berhasil di-push ke GitHub https://github.com/Mufti129/HPpriceID"

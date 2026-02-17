# 🚀 Panduan Deploy ke Render.com

## Langkah-langkah Deploy:

### 1. **Persiapan di GitHub**
- Pastikan semua file sudah di-commit dan di-push ke GitHub
- Verifikasi repository Anda public atau Render bisa akses

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 2. **Daftar Akun Render**
- Kunjungi [render.com](https://render.com)
- Daftar gratis (gunakan akun GitHub Anda untuk kemudahan)
- Verifikasi email Anda

### 3. **Deploy Aplikasi**
1. Login ke Render dashboard
2. Klik **"New +"** → pilih **"Web Service"**
3. Pilih repository: `nivyanyctra/hok_item_recommendation`
4. Atur pengaturan:
   - **Name**: `hok-item-recommendation` (atau nama lain)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (untuk testing)
5. Klik **"Create Web Service"**

### 4. **Verifikasi Deploy**
- Render akan otomatis deploy ketika Anda click "Create"
- Tunggu 2-5 menit sampai build selesai
- Jika ada error, lihat di tab "Logs"
- Akses aplikasi melalui URL yang diberikan Render (contoh: `hok-recommendation.onrender.com`)

### 5. **Update Deployment (Setiap push ke main)**
Setiap kali Anda push ke GitHub, Render akan otomatis re-deploy

```bash
git add .
git commit -m "Update features"
git push origin main
# Render akan otomatis deploy dalam 1-2 menit
```

## Troubleshooting:

| Masalah | Solusi |
|---------|--------|
| Build gagal | Lihat Logs tab → cek error message. Biasanya masalah requirements.txt |
| "Port not open" | Pastikan di app.py menggunakan `port = int(os.environ.get('PORT', 5000))` |
| Aplikasi lambat | Render Free tier punya keterbatasan. Upgrade ke Paid untuk performance lebih baik |
| Module not found | Tambah package ke requirements.txt dan push ulang |

## Tips:
- ✅ Gunakan **Free Plan** untuk testing awal
- ✅ Upgrade ke **Starter ($7/month)** jika production dan butuh uptime 24/7
- ✅ Set **Auto-Deploy** di Settings untuk auto-deploy setiap push
- ✅ Monitor logs di dashboard Render untuk debugging

---
**Selesai! Aplikasi Anda sekarang live di internet! 🎉**

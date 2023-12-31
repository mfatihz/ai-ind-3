# Project CV 2: Person Tracking

Dataset
- Data 'person' diunduh dari fiftyone, sebanyak 3000 data untuk training dan 500 data testing
- Untuk mempermudah pengaturan data, lokasi download data fiftyone (/root/fiftyone) pada Google Colaboratory diubah, menyesuaikan dengan lokasi default dari YOLOv8 (/content/datasets)

Struktur Direktori Data
- Struktur folder data diubah agar sesuai dengan default dari YOLOv8: terdiri dari pasangan folder 'images' dan folder 'labels' dan masing-masing folder tersebut memiliki sub folder 'train' dan 'val'.
- Proses pengaturan folder ini dilakukan dengan linux command untuk mengurangi proses manual dan human-error.
- Untuk project kali ini, folder images diisi dengan data gambar COCO (dalam format jpg) sedangkan folder labels berisi file txt. Masing-masing gambar tersebut memiliki pasangan file txt-nya sendiri.

Annotations dan Labels
- Dilakukan perubahan format data bounding box COCO (xl, yt, w, h) ke dalam format YOLO (xc/wimg, yc/himg, w/wimg, h/himg)
- Untuk setiap data training dan testing, fiftyone menyediakan data label gambar dengan format json yang isinya gabungan dari keseluruhan datanya. Agar memenuhi persyaratan untuk training pada yolo, data json tersebut diproses agar menghasilkan data labels, yang mana untuk masing-masing data gambar akan memiliki satu data label yang bersesuaian. Label yang dihasilkan, seperti yang telah dijelaskan di atas, diletakkan dalam folder 'labels/train' dan 'labels/val'
- Dilakukan penyesuaian index classes (dalam hal ini index person = 1 pada data fiftyone diubah menjadi 0)

Log
- Hasil logging proses training secara default disimpan dalam /contents/run dan akan dihapus ketika Google Colaboratory ditutup. Agar bisa permanen dan dimanfaatkan untuk proses lainnya, hasil logging ini disimpan secara permanen ke dalam folder Google Drive 

Data pengujian
- Model: yolov8n dan yolov8m (https://github.com/ultralytics/ultralytics)
- Epoch: 50

Hasil pengujian
- Model: yolov8n
  - waktu training: 50 epochs, 1.345 hours
  - nilai validasi mAP50: 0.673
  - nilai validasi mAP50-95: 0.436
  - inference time (3 gambar): 168.2ms, 24.8ms, 34.9ms (rataan: 75.97ms)
- Model: yolov8m
  - waktu training: 50 epochs, 1.618 hours
  - nilai validasi mAP50: 0.729
  - nilai validasi mAP50-95: 0.482
  - inference time (3 gambar): 141.4ms, 67.0ms, 28.4ms (rataan: 80.13ms)

Penutup
- Karena keterbatasan waktu dan hardware, pengujian baru bisa dilakukan untuk 2 model (yolov8n dan yolov8m) dan belum ada perbandingan penggunaan nilai Hyperparameter. 
- Dari hasil pengujian diperoleh lama waktu training untuk yolov8m lebih panjang dibandingkan yolov8n. Hal ini disebabkan jumlah parameter yolov8m yang lebih banyak dibandingkan yolov8n.
- Dari hasil pengujian, nilai uji validasi yolov8m lebih baik dibandingkan yolov8n karena yolov8m memiliki lebih banyak feature.
- Dari hasil pengujian, inference time yolov8n lebih cepat dibandingkan yolov8m karena parameter yang digunakan dalam perhitungan lebih sedikit.
- Pada saat melakukan prediksi, dari pengujian tiga data gambar dapat ditunjukkan bahwa model sudah bisa mendeteksi dua data gambar dengan baik (gambar 2 dan gambar 3). Untuk gambar pertama, kedua model tidak bisa mendeteksi object dengan lengkap.
- Dari grafik metrik uji dapat dilihat bahwa hasil training masih belum konvergen. Hal ini menunjukkan bahwa hasil pengujian masih bisa dioptimalkan lagi terutama dengan menambah nilai epoch.

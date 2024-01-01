# Project 3: Self-Driving Car


## Latar Belakang
Self-driving car merupakan kendaraan yang dapat berjalan tanpa perlu input manusia. Mereka mengkombinasikan sensor dan software untuk mengendalikan, menavigasi, dan menjalankan kendaraan.

Salah satu persyaratan mendasar yang harus dimiliki oleh self-driving car adalah kemampuan dalam mengenali objek-objek sekitar, misalnya, jalan, pagar, gedung, orang/pejalan kaki. Kemampuan ini bisa dicapai, salah satu caranya, dengan mempergunakan sensor visual (kamera) sebagai input dan kemudian mengolah hasil inputan tersebut dalam algoritma machine learning untuk mengenali objek dalam inputan.


## Tujuan
Tujuan yang hendak dicapai dalam percobaan ini adalah melakukan segmentasi visual (membagi gambar berdasarkan jenis kelasnya) terhadap objek-objek yang sering ditemui ketika berkendara di sepanjang jalan raya.


## Percobaan 
### Dataset
Dataset mempergunakan data yang sudah disediakan dalam dashboard project. Dataset terdiri dari 12 kelas object yang sering ditemui di sepanjang jalan:

`sky`, `building`, `pole`, `road`, `pavement`, `tree`, `signsymbol`, `fence`, `car`, `pedestrian`, `bicyclist`, `unlabeled`.

Data terdiri dari 367 data training dan 101 data testing. Data training kemudian dibagi dengan proporsi 80/20 untuk testing dan validation. Sebagai tambahan, pada dataset training terdapat beberapa data duplikasi yang perlu difilter agar tidak disertakan dalam proses training. Proses memfilter data ini dilakukan secara otomatis dalam class `Dataset` pytorch.

Data yang dipakai dalam percobaan ini dapat dilihat dalam folder `datasets`.


### Model
Model yang dipakai dalam proses segmentasi adalah UNet dengan mempergunakan libary `https://github.com/qubvel/segmentation_models.pytorch`.

Library tersebut dipilih karena menyediakan berbagai variasi encoder dan pre-trained weight.


### Hyperparameter
Percobaan dilakukan dengan mengkombinasikan berbagai nilai hyperparameter, yang secara sederhana, dapat dibagi menjadi dua tahap. Di tahap awal mempergunakan berbagai kombinasi hyperparameter dengan beban komputasi yang tidak terlalu tinggi. Tahap berikutnya dilanjutkan dengan mempergunakan hyperparameter yang lebih besar beban komputasinya (misalnya, dengan memperbesar epoch atau mempergunakan encoder yang memiliki jumlah parameter yang lebih banyak).

Hyperparameter | Setting
--- | ---
Decoder | resnet34, resnet50, resnet101, efficientnet-b4
Decoder weighting | imagenet
Activation | softmax 2d
Learning Rate | 1e-4 (for 0-24 epoch), 1e-5 (for 25-49 epoch), 5e-6 (for 50-74 epoch), 1e-6 (for next epochs)
Metrics | DiceLoss, IoU(threshold=0.5), Accuracy
Optimizers | Adam


### Hasil Percobaan
classes | encoder | pretrained | epoch | augmention | dice_loss | iou_score | accuracy | training time
--- | --- | --- | --- | --- | --- | --- | --- | ---
12 | resnet34 | no | 50 | yes | 0.2034 | 0.6702 | * | *
12 | resnet34 | yes | 50 | yes | 0.1247 | 0.7869 | * | *
12 | resnet50 | no | 50 | yes | 0.3523 | 0.4832 | * | *
12 | resnet50 | yes | 50 | yes | 0.1197 | 0.8043 | * | *
12 | efficientnet-b4 | yes | 50 | yes | 0.1903 | 0.7236 | * | *

classes | encoder | pretrained | epoch | augmention | dice_loss | iou_score | accuracy | training time
--- | --- | --- | --- | --- | --- | --- | --- | ---
3 | resnet50 | yes | 50 | yes | 0.9328 | 0.06404 | * | *
12 | resnet34 | yes | 200 | yes | 0.1164 | 0.7969 | * | *
12 | resnet101 | yes | 50 | no | 0.1941 | 0.7617 | 0.9792 | 45.67 min
12 | resnet101 | yes | 50 | yes | 0.1869 | 0.7299 | 0.9749 | 48.64 min
12 | resnet101 | yes | 200 | yes | 0.1154 | 0.8121 | 0.9828 | 192.26 min
> tidak didokumentasikan
> 3 classes: car, pedestrian, bicyclist


Simulasi hasil segmentasi untuk mask `road` bisa dilihat secara lengkap dalam folder `videos`

https://github.com/mfatihz/ai-ind-3/assets/10268517/7ba042df-04c1-4a01-b5fe-91e0347c8ad9


## Pembahasan
- Dari plot metric diperoleh hasil bahwa nilai epoch di atas 30 hasil metric sudah tidak banyak berubah (dice loss, IoU score, accuracy).
- Segmentasi bisa dilakukan dengan baik pada objek-objek berukuran besar tapi belum bisa mengenali objek-objek dengan ukuran kecil.
- Perubahan hyperparameter tetap belum dapat meningkatkan hasil segmentasi pada objek-objek kecil.


## Kesimpulan
- Kelas-kelas untuk segmentasi memiliki luas area yang sangat bervariasi dan merupakan kondisi 'imbalance classes' (objek berukuran kecil memiliki jumlah pixel yang jauh lebih sedikit dibandingkan dengan objek-objek di sekitarnya).
- Jumlah data yang dipergunakan dalam training kurang banyak dan juga kurang bervariasi.
- Akibat adanya kondisi-kondisi di atas, segmentasi cenderung hanya akurat pada object-object yang besar dan tidak dapat mendeteksi object-object kecil.


## Saran 
- Jumlah dan variasi data untuk training diperbanyak.

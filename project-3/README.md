# Project 3: Self Driving Car

## Tujuan
Tujuan yang hendak dicapai dalam percobaan ini adalah melakukan segmentasi visual terhadap objek-objek yang sering ditemui ketika berkendara di sepanjang jalan raya.

## Percobaan 
### Dataset
Dataset mempergunakan data yang sudah disediakan dalam dashboard project. Dataset terdiri dari 12 kelas object yang sering ditemui di sepanjang jalan:

`sky, building, pole, road, pavement, tree, signsymbol, fence, car, pedestrian, bicyclist, unlabeled`.

Data terdiri dari 367 data training dan 101 data testing. Data training kemudian dibagi dengan proporsi 80/20 untuk testing dan validation. Sebagai tambahan, pada dataset training terdapat beberapa data duplikasi yang perlu difilter agar tidak disertakan dalam proses training. Proses memfilter data ini dilakukan secara otomatis dalam class 'Dataset' pytorch.

### Model
Model yang dipakai dalam proses segmentasi adalah UNet dengan mempergunakan libary `https://github.com/qubvel/segmentation_models.pytorch`.

Library tersebut dipilih karena menyediakan berbagai variasi encoder dan pre-trained weight. Selain itu library ini juga sudah banyak dipakai untuk berbasai kasus segmentasi lainnya dengan hasil yang sangat memuaskan.

### Hyperparameter
Percobaan dilakukan dengan mengkombinasikan berbagai nilai hyperparameter, yang secara sederhana, dapat dibagi menjadi dua tahap. Di tahap awal dipergunakan berbagai kombinasi hyperparameter dengan beban komputasi yang tidak terlalu tinggi. Berikutnya dilanjutkan dengan penggunaan hyperparameter yang lebih besar beban komputasinya (misalnya, dengan memperbesar epoch atau mempergunakan encoder yang memiliki jumlah parameter yang lebih banyak).

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

3 classes: car, pedestrian, bicyclist

231229_1512__p3_12_unet_qubvel_resnet101_imagenet_50_6fps_short.mp4

![](231229_1512__p3_12_unet_qubvel_resnet101_imagenet_50_6fps_short.mp4)



## Pembahasan
- Dari plot metric diperoleh hasil bahwa di atas epoch 30 nilai metric sudah tidak banyak berubah (dice loss, IoU score, accuracy).
- Segmentasi bisa dilakukan dengan baik pada objek-objek berukuran besar tapi belum bisa mengenali objek-objek dengan ukuran kecil.
- Penggunaan hyperparameter tidak dapat meningkatkan hasil segmentasi pada objek-objek kecil.

## Kesimpulan
- Kelas-kelas untuk segmentasi memiliki luas area (= jumlah pixel) yang sangat bervariasi dan merupakan kondisi imbalance classes (objek berukuran kecil memiliki jumlah pixel yang relatif lebih sedikit dibandingkan dengan background-nya)
- Jumlah data yang dipergunakan dalam training tidak terlalu banyak dan juga kurang bervariasi.
- Akibat adanya kondisi-kondisi di atas, segmentasi cenderung hanya dilakukan pada object-object yang besar sedangkan object-object kecil menjadi tidak terdeteksi.

## Saran 
- Jumlah dan variasi data untuk training diperbanyak

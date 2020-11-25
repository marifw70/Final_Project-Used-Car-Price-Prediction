# Final_Project-Used-Car-Price-Prediction
Final Project Used Car Price Predition by Muhammad Arif Wicaksono_ JCDS 10

dataset berasal dari https://www.kaggle.com/austinreese/craigslist-carstrucks-data

## Background Information

Sekarang dalam masa pandemi Covid 19 mobil bekas tiba tiba
menjadi komoditas industri terpanas seperti di Amerika Serikat
Laporan New York Times pada Selasa, 8 September 2020
mengungkapkan bahwa konsumen memilih kendaraan bekas
sebagai mobil kedua atau ketiga sehingga mereka dapat
menghindari angkutan umum selama pandemi virus Covid 19.

Permintaan mobil tua juga didorong oleh penghentian produksi
mobil baru sekitar dua bulan pada awal 2020 Pada Juli 2020 nilai
rata rata mobil bekas melonjak lebih dari 16 persen menurut
Edmunds com Pada Juni dealer mobil waralaba menjual 1 2 juta
mobil dan truk bekas atau naik 22 persen dari tahun sebelumnya.

## PROBLEM
Dengan peluang jual beli mobil bekas yang sedang melonjak
penjualannya membuat sebagian orang ingin membeli mobil
bekas karena ingin menghindari kendaraan umum selama
pandemi Covid 19 Namun yang menjadi persoalan mereka takut
jika harga yang dijual tidak sesuai ekspektasi

## GOALS
Pada tugas akhir ini saya ingin menganalisis dan membuat aplikasi
mengenai prediksi harga mobil agar membuat para pembeli
mobil maupun penjual mobil bisa mengetahui harga pasti mobil
mobil bekas yang dijual berdasarkan fitur fiturnya

## Steps:
- Handling Missing Values File Handling Missing Values
- Exploratory Data Analysis EDA
- Feature Selection
- Feature Engineering
- Machine Learning Modelling with K nearest neighbors Regressor, Decision Tree Regressor, Random Forest Regressor dan XGBoost Regressor, optimizing model with Scalling and Hyper  Parameter Tuning Machine Learning Modelling
- Evaluation Metrics
- Conclusion

## CONCLUSION

### Data Distribusi
Pada dataset Craiglist Vehicle ini terdapat 25 kolom Berdasarkan kolom price yang menjadi target terlihat menunjukkan
Skewness yang bernilai positif dimana ekor distribusi berada di sebelah kanan nilai terbanyak Berarti,sebagian besar distri
busi berada di nilai rendah dan nilai rata rata nya diatas nilai median Hal ini juga menunjukkan bahwa kebanyakan dari
mobil yang dijual harganya dibawah rata rata median dan ada beberapa mobil yang terjual dengan harga yang sangat tinggi
jauh melebihi harga pasaran

### Analisis
- Pada sample dataset yang saya gunakan bahwa kebanyakan jenis mobil yang dijual di
Amerika adalah sedan

- manufacturer yang paling sering dijual adalah Ford yang penjualan terbesarnya ada di
negara bagian california

- Untuk median price mobil bekas berdasaran tahun rilisnya tidak selalu lebih murah
terbukti pada tahun 2009 mobil luxury car lebih mahal dibanding beberapa tahun se
telahnya sehingga perlu juga membandingkan dengan kolom lainnya

- Untuk orang orang yang ingin membeli mobil basic, merk Saturn memiliki median
harga paling rendah yaitu 5499 dan pada mobil luxury merk yang memiliki median
paling rendah adalah Hyundai

- lalu berdasarkan harga, type hatchback memiliki median paling murah dikelas basic a
taupun luxury sedangkan paling mahal untuk basic adalah pickup dan untuk luxury a
dalah truck

- selebihnya harga mobil akan berpengaruh tergantung dari fasilitas ataupun kondisi m
obil itu sendiri seperti misal dari bahan bakarnya,cylinders transmisinya ukuran me
sin penggeraknya kondisi dan status mobil tersebut

- Berdasarkan informasi dari web https :://www edmunds com/car buying/ 10
steps to buying a used car html ada beberapa tips untuk membeli mobil bekas
yaitu:
• tentukan dulu tipe mobil apa yang ingin dibeli
• tentukan beberapa merk dan coba bandingkan plus minus dari merk yang sudah ditentukan
• lalu cek harga pasar berdasarkan area tempat yang ingin dibeli
• setelah itu cek historikal dari kendaraan tersebut dan coba untuk melakukan test drive mobil tersebut
• setelah yakin coba untuk cek harga pasar dengan menggunakan machine learning yang telah dibuat


Link For Access Model Machine Learning Random Forest
https://drive.google.com/file/d/1a0wcUoZh_Q-CODh_cv-Fq8ndZa2zeMmJ/view?usp=sharing


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
#
# # Upload file dataset.xlsx ke Google Colab terlebih dahulu
# file_path = 'dataset.xlsx'
#
# # Membaca dataset
# df = pd.read_excel(file_path)

# # Membuat histogram
# fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
# fig.suptitle("Histogram untuk Masing-masing Film", fontsize=28)
#
# films = ["Squid Game 1", "Squid Game 2", "Squid Game 3"]
#
# for i, film in enumerate(films):
#     axes[i].bar(df["Nilai"], df[film], color='skyblue', alpha=0.7) # Membuat diagram batang pada subplot ke-i (axes[i])
        # alpha=0.7 : Memberikan transparansi untuk batang, sehingga tampil lebih lembut.
#     axes[i].set_title(film, fontsize=20)
#     axes[i].set_xlabel("Nilai", fontsize=20)
#     axes[i].set_ylabel("Jumlah Polling" if i == 0 else "", fontsize=20)
#     axes[i].tick_params(axis='both', labelsize=18)
#
# plt.tight_layout(rect=[0, 0, 1, 0.95])
# plt.show()

# # Fungsi untuk menghitung statistik berbobot
# def weighted_statistics(values, weights):
#     # Menghitung mean berbobot
#     mean = np.average(values, weights=weights)
#
#     # Menghitung median berbobot
#     expanded_data = np.repeat(values, weights)  # Memperluas data berdasarkan bobot
#     median = np.median(expanded_data)
#
#     # Menghitung mode berbobot
#     mode = values[np.argmax(weights)]
#
#     # Menghitung standar deviasi berbobot
#     variance = np.average((values - mean)**2, weights=weights)
#     std_dev = np.sqrt(variance)
#
#     return mean, median, mode, std_dev
#
# # Hitung statistik untuk masing-masing film
# stats = {"Statistik": ["Mean", "Median", "Mode", "Standard Dev"]}
# for film in ["Squid Game 1", "Squid Game 2", "Squid Game 3"]:
#     mean, median, mode, std_dev = weighted_statistics(df["Nilai"], df[film])
#     stats[film] = [mean, median, mode, std_dev]
#
# stats_df = pd.DataFrame(stats)
# print("Tabel Statistik:")
# print(stats_df)

# # Membuat boxplot berbobot
# fig, axes = plt.subplots(1, 3, figsize=(18, 6))
# fig.suptitle("Boxplot untuk Nilai Masing-masing Film", fontsize=28)
#
# for i, film in enumerate(["Squid Game 1", "Squid Game 2", "Squid Game 3"]):
#     # Perluas data untuk menggambarkan distribusi berbobot
#     expanded_data = np.repeat(df["Nilai"], df[film]) # Mengulangi setiap nilai dalam df["Nilai"] sebanyak jumlah/frekuensi yang ada dalam df[film]
#     sns.boxplot(x=expanded_data, ax=axes[i], color='lightgreen') # Data yang akan diplot, Boxplot ditampilkan pada subplot ke-i, Warna boxplot.
#     axes[i].set_title(film, fontsize=20)
#     axes[i].set_xlabel("Nilai", fontsize=20)
#     axes[i].tick_params(axis='both', labelsize=20) #  Menyesuaikan ukuran font untuk label sumbu.
#
# plt.tight_layout(rect=[0, 0, 1, 0.95]) # Mengatur tata letak agar subplot tidak saling tumpang tindih
# Menyisakan ruang untuk judul utama (suptitle) di atas.
# plt.show()
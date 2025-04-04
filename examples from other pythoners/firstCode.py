

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm

# Grafik boyutları
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

# Başlangıç verisi
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

line, = ax.plot(x, y, color='blue', lw=2)

# Renk haritası
colors = cm.viridis(np.linspace(0, 1, 100))

# Animasyon fonksiyonu
def animate(i):
    ax.clear()  # Ekranı temizle
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1.5, 1.5)
    
    # Grafik efektleri
    if i % 100 < 25:
        y = np.sin(x + i * 0.05)  # Sinüs dalgası
        line, = ax.plot(x, y, color='blue', lw=2)
    elif i % 100 < 50:
        y = np.cos(x + i * 0.05)  # Cosinus dalgası
        line, = ax.plot(x, y, color='green', lw=2)
    elif i % 100 < 75:
        y = np.tan(x)  # Tangens dalgası
        line, = ax.plot(x, y, color='red', lw=2)
    else:
        y = np.sin(x + i * 0.1)  # Yeniden sinüs dalgası
        line, = ax.plot(x, y, color='purple', lw=2)

    # Ekran başlık ve etiketler
    ax.set_title(f"Grafik Efekt: {i//25 + 1}", fontsize=14)
    ax.set_xlabel('X Ekseni', fontsize=10)
    ax.set_ylabel('Y Ekseni', fontsize=10)

    return line,

# Animasyonu oluştur
ani = FuncAnimation(fig, animate, frames=600, interval=100, blit=True)

# 1 dakika boyunca animasyonu göster
plt.show()

import psutil
import time

def display_performance_stats():
    # Mendapatkan penggunaan CPU dan memori
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_stats = psutil.virtual_memory()

    # Menampilkan informasi
    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage: {memory_stats.percent}%")
    print("-" * 30)

def optimize_for_game():
    print("Memulai optimalisasi untuk permainan...")
    # Implementasikan optimalisasi tambahan di sini (sesuai kebutuhan)

def main():
    try:
        while True:
            display_performance_stats()
            optimize_for_game()
            time.sleep(5)  # Tunda selama 5 detik sebelum menampilkan statistik lagi

    except KeyboardInterrupt:
        print("\nBerhenti. Selamat bermain!")

if __name__ == "__main__":
    main()

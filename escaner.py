import os

print("=" * 50)
print(" AUTO NETWORK RECON ")
print("=" * 50)

objetivo = input("Ingresa la IP o rango de red: ")

archivo = "reporte_red.txt"

comando = f"nmap -sS {objetivo} -oN {archivo}"

print("\n[+] Ejecutando escaneo...\n")

os.system(comando)

print(f"\n[+] Escaneo completado.")
print(f"[+] Reporte guardado en: {archivo}")

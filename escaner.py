#!/usr/bin/env python3

import os
import datetime

print("=" * 60)
print("          AUTO NETWORK RECON")
print("=" * 60)

objetivo = input("\n[+] Ingresa la IP o rango objetivo: ")

fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

archivo_reporte = f"reporte_{fecha}.txt"

comando = f"nmap -sS -Pn {objetivo} -oN {archivo_reporte}"

print("\n[+] Ejecutando escaneo...\n")

os.system(comando)

print("\n[+] Escaneo finalizado correctamente.")
print(f"[+] Reporte generado: {archivo_reporte}")

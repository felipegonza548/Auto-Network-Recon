
import os
import datetime
import xml.etree.ElementTree as ET

print("=" * 60)
print("          AUTO NETWORK RECON")
print("=" * 60)

objetivo = input("\n[+] Ingresa la IP o rango objetivo: ")

fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

archivo_reporte = f"reporte_{fecha}.txt"

comando = f"nmap -sS -sV -O -Pn {objetivo} -oN {archivo_reporte} -oX reporte.xml"

print("\n[+] Ejecutando escaneo avanzado...\n")

os.system(comando)

print("\n[+] Escaneo finalizado correctamente.")
print(f"[+] Reporte TXT generado: {archivo_reporte}")
print("[+] Reporte XML generado: reporte.xml")

print("\n===================================")
print("      ANALISIS DE SERVICIOS")
print("===================================\n")

try:

    tree = ET.parse("reporte.xml")
    root = tree.getroot()

    for host in root.findall("host"):

        for port in host.findall(".//port"):

            puerto = port.attrib.get("portid")

            servicio = port.find("service")

            if servicio is not None:

                nombre = servicio.attrib.get("name", "desconocido")
                producto = servicio.attrib.get("product", "")
                version = servicio.attrib.get("version", "")
                extrainfo = servicio.attrib.get("extrainfo", "")

                print(f"[+] Puerto: {puerto}")
                print(f"    Servicio : {nombre}")
                print(f"    Producto : {producto}")
                print(f"    Version  : {version}")
                print(f"    Extra    : {extrainfo}")
                print("-" * 40)

except Exception as e:

    print(f"[!] Error analizando XML: {e}")


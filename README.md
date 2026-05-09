# Auto-Network-Recon

## Nota
Este proyecto fue desarrollado como Prueba de Concepto (PoC) dentro de mi laboratorio personal de ciberseguridad para automatizar tareas básicas de reconocimiento de red.

---

# Descripción

Script en Python que automatiza escaneos de red utilizando Nmap y genera reportes organizados en archivos de texto para facilitar el análisis inicial de servicios expuestos.

---

# ¿Por qué hice este proyecto?

Como estudiante y entusiasta de ciberseguridad, identifiqué que ejecutar comandos manuales repetitivos consumía tiempo durante procesos de reconocimiento. Desarrollé esta herramienta para optimizar la recolección de información y reforzar mis conocimientos en automatización y análisis de redes.

---

# Tecnologías Utilizadas

- Python 3
- Nmap
- Linux (Kali Linux)
- Bash

---

# ¿Cómo funciona?

1. El usuario ejecuta el script.
2. El sistema solicita una IP o rango de red.
3. Se ejecuta un escaneo TCP SYN con Nmap.
4. El resultado se guarda automáticamente en un archivo .txt

---

# Ejecución

```bash
python3 escaner.py

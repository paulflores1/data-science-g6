import csv

with open("archivo.csv", "w", newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["dni", "Nombre", "Email"])
    escritor_csv.writerow(["70021852", 28, "Madrid"])
    escritor_csv.writerow(["70021852", 34, "Barcelona"])
    escritor_csv.writerow(["70021852", 22, "Valencia"])
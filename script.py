# Erata Maharshi (210050049) and Motupalli Yashwanth (210050099)
import os
import pandas as pd
genes_folder = "genes"
localization_sequence = "SKL"

def check_localization(gene_name):
    gene_file = gene_name.strip() + ".txt"
    gene_file = os.path.join(genes_folder, gene_file)
    if os.path.exists(gene_file):
        with open(gene_file, 'r') as f:
            gene_sequence = f.read()
            if localization_sequence in gene_sequence:
                return "YES"
            else:
                return "NO"
    else:
        return "Gene file not found"

def main():
    with open("genes.txt", "r") as gene_names_file:
        gene_names = gene_names_file.readlines()
    results = []
    for gene_name in gene_names:
        gene_name = gene_name.strip()
        localization_status = check_localization(gene_name)
        results.append({'Gene': gene_name, 'Localization Sequence Present?': localization_status})
    df = pd.DataFrame(results)
    df.to_excel("result.xlsx", index=False)

if __name__ == "__main__":
    main()

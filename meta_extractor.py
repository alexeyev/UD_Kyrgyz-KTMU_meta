import csv

input_file = "ky_ktmu-ud-test.conllu"
output_file = "ky_ktmu-ud-test.conllu.tsv"

input_file = "ky_ktmu-ud-train.conllu"
output_file = "ky_ktmu-ud-train.conllu.tsv"

# Initialize variables
sentences = []
sent_id = ""
text = ""

with open(input_file, "r", encoding="utf-8") as infile:
    for line in infile:
        line = line.strip()
        if line.startswith("# sent_id = "):
            sent_id = line.replace("# sent_id = ", "")
        elif line.startswith("# text = "):
            text = line.replace("# text = ", "")
        elif line == "":  # End of sentence
            if sent_id and text:
                sentences.append((sent_id, text))
            sent_id = ""
            text = ""

with open(output_file, "w", encoding="utf-8", newline="") as tsvfile:
    tsv_writer = csv.writer(tsvfile, delimiter="\t")
    tsv_writer.writerow(["sent_id", "text", "genre", "url"])
    for sent_id, text in sentences:
        tsv_writer.writerow([sent_id, text, "", ""])

print(f"TSV file generated: {output_file}")

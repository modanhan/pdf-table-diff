import camelot


def createEntries(filename, generic_name_idx=0):
    entries = []

    tables = camelot.read_pdf(filename, pages="all")
    for table in tables:
        df = table.df
        for _, row in df.iterrows():
            if row[generic_name_idx].lower() == "generic name":
                continue
            entry = []
            for item in row:
                entry.append(item)
            if row[generic_name_idx] == "":
                prev = entries[-1]
                amended = tuple([x + y for x, y in zip(prev, entry)])
                entries[-1] = amended
                continue
            entries.append(tuple(entry))

    return entries


# generic_name_idx = 0
# e2021 = createEntries("doc_2021.pdf", generic_name_idx)
# e2022 = createEntries("doc_2022.pdf", generic_name_idx)

generic_name_idx = 1
e2021 = createEntries("PY1-FDL-2021.pdf", generic_name_idx)
e2022 = createEntries("PY1-FDL-2022W.pdf", generic_name_idx)

for d in [x for x in e2022 if x not in set(e2021)]:
    print(d[generic_name_idx].replace("\n", ""))

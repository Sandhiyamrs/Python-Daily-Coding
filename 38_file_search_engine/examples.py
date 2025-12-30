from file1_file_search_engine import search_files

results = search_files(
    directory="projects/",
    keyword="invoice"
)

for r in results:
    print("Found:", r)

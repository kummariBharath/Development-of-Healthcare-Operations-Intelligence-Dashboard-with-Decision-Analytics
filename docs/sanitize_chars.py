import glob

def sanitize_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as fp:
        c = fp.read()
    orig = c
    c = c.replace('\u2013', '-')   # en-dash
    c = c.replace('\u2014', ' -- ') # em-dash
    c = c.replace('\u201c', '"')   # left double quote
    c = c.replace('\u201d', '"')   # right double quote
    c = c.replace('\u2018', "'")   # left single quote
    c = c.replace('\u2019', "'")   # right single quote
    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print(f"Sanitized: {fpath}")

for f in glob.glob("docs/*.py"):
    sanitize_file(f)

print("Typography sanitization complete.")

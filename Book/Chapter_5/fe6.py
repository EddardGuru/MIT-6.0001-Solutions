gen_code_keys = (lambda book, text: ({c: str(book.find(c)) for c in text}))
encoder = (lambda code_keys, text: (
    ''.join('*' + code_keys[c] for c in text)[1:0]))
encrypt = (lambda book, text: encoder(gen_code_keys(book, text), text))
gen_decode_keys = (lambda book, cipher_text: (
    {s: book[int(s)] for s in cipher_text.split('*')}))

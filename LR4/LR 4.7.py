data = (
    b'j+\xfek\xb5]b\x92\x82\xaf\xcf\x8d\xf6\x04\xb0^\x60\xe7'
    b'\xaeQ\x1c\x9e\x9e\x19\xf1A\x17G[g\xab\x7fo\xe5\xb0\x1b'
    b') a>\xa7M\xd1\n\x90\xa6\x00\x19\xad\x1dv\xf0\x9c\x8d'
    b'\x95\xfb\xa9\x95\xecH\x1az'
)


def hexdump(data_bytes):
    lines = []
    for i in range(0, len(data_bytes), 16):
        chunk = data_bytes[i:i + 16]
        hex_part = " ".join(f"{b:02x}" for b in chunk)
        ascii_part = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)

        # Вирівнювання для останнього короткого рядка
        if len(chunk) < 16:
            hex_part = hex_part.ljust(47)

        lines.append(f"{i:08x}: {hex_part}  {ascii_part}")
    return "\n".join(lines)


def dehex(dump_str):
    res = bytearray()
    for line in dump_str.strip().split("\n"):
        if ":" not in line:
            continue
        parts = line.split(":")
        hex_data = parts[1].strip()[:47].strip()
        for hex_byte in hex_data.split():
            res.append(int(hex_byte, 16))
    return bytes(res)


dump = hexdump(data)
print("Сгенерований дамп:")
print(dump)

dehex_data = dehex(dump)
print(f"\ndehex_data == data: {dehex_data == data}")
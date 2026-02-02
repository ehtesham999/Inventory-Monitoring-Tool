import uuid
def generate_sku(name: str) -> str:
    id = uuid.uuid4().hex[:6].upper()
    clean_name = name[:3].upper()

    return f"{clean_name}-{id}"


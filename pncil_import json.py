import json

# Ver cuántos chunks se generaron
with open(r"C:\Users\agarmendia\Desktop\proyectoUFERAG\data\processed\documents.jsonl", 'r', encoding='utf-8') as f:
    documentos = [json.loads(line) for line in f]

print(f"Total documentos: {len(documentos)}")
print(f"\nPrimer documento:")
print(json.dumps(documentos[0], indent=2, ensure_ascii=False)[:500])
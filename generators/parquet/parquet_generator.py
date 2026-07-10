import os
import pyarrow as pa
import pyarrow.parquet as pq
from generators.base_generator import BaseGenerator


class ParquetGenerator(BaseGenerator):
    """
    Write a single Parquet file:
    columns = book_index, book_name, chapter, verse, text
    """

    def __init__(self, source_dir, format_dir) -> None:
        super().__init__(source_dir, format_dir)

    def generate(self, language: str, translation: str) -> None:
        data = self.load_json(language, translation)
        prepared = self.prepare_data(data)

        # Build list-of-dicts for Parquet
        rows = []
        for b_idx, book in enumerate(prepared.get("books", []), start=1):
            bname = book.get("name")
            for ch in book.get("chapters", []):
                cnum = ch.get("chapter")
                for v in ch.get("verses", []):
                    rows.append({
                        "book_index": b_idx,
                        "book_name": bname,
                        "chapter": v.get("chapter", cnum),
                        "verse": v.get("verse"),
                        "text": v.get("text"),
                    })

        table = pa.Table.from_pylist(rows, schema=pa.schema([
            pa.field("book_index", pa.int32()),
            pa.field("book_name", pa.string()),
            pa.field("chapter", pa.int32()),
            pa.field("verse", pa.int32()),
            pa.field("text", pa.string()),
        ]))

        out_dir = os.path.join(self.format_dir, "parquet")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{translation}.parquet")

        pq.write_table(table, out_path, compression="snappy")
        print(f"Parquet file for {translation} written to {out_path}")

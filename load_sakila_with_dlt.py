import dlt
import duckdb

# Läs från vår befintliga DuckDB och ladda till Evidence med staging-schema
source_db = 'data/sakila.duckdb'
dest_db = 'dashboard/sources/sakila/sakila.duckdb'

# Skapa pipeline
pipeline = dlt.pipeline(
    pipeline_name="sakila",
    destination=dlt.destinations.duckdb(dest_db),
    dataset_name="staging"
)

# Koppla till source DuckDB
source_conn = duckdb.connect(source_db, read_only=True)

# Hämta alla tabeller
tables_query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'main'"
tables = source_conn.execute(tables_query).fetchdf()['table_name'].tolist()

print(f"Hittat {len(tables)} tabeller i source DuckDB")

# Ladda varje tabell med dlt
for table in tables:
    print(f"Laddar {table}...")
    
    # Läs data
    df = source_conn.execute(f"SELECT * FROM {table}").fetchdf()
    
    # Skapa dlt resource
    @dlt.resource(name=table, write_disposition="replace")
    def load_table():
        return df.to_dict('records')
    
    # Kör pipeline
    info = pipeline.run(load_table())
    print(f"✓ {table}: {len(df)} rader")

source_conn.close()
print(f"\n✓ Alla tabeller laddade till {dest_db} med staging-schema!")
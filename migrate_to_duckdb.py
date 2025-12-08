import sqlite3
import duckdb
import pandas as pd

SQLITE_PATH = "data/sqlite-sakila-db/sqlite-sakila.sq"
DUCKDB_PATH = "data/sakila.duckdb"

# Koppla till SQLite-databasen
print("Kopplar till SQLite-databasen...")
sqlite_conn = sqlite3.connect(SQLITE_PATH)
print("✓ Kopplad till SQLite")

# Koppla till DuckDB-databasen (skapar filen om den inte finns)
print("Kopplar till DuckDB-databasen...")
duckdb_conn = duckdb.connect(DUCKDB_PATH)
print("✓ Kopplad till DuckDB")

# Hämta alla tabellnamn från SQLite
print("\nHämtar tabellnamn från SQLite...")
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query, sqlite_conn)
table_names = tables['name'].tolist()

print(f"Hittade {len(table_names)} tabeller:")
for table in table_names:
    print(f"  - {table}")

    # Migrera varje tabell från SQLite till DuckDB
print("\nMigrerar tabeller till DuckDB...")

for table in table_names:
    # Läs hela tabellen från SQLite
    df = pd.read_sql(f"SELECT * FROM {table}", sqlite_conn)
    
    # Skriv tabellen till DuckDB
    duckdb_conn.execute(f"CREATE TABLE {table} AS SELECT * FROM df")
    
    print(f"✓ Migrerade {table}: {len(df)} rader")

print("\n✓ Migration klar!")

# Stäng databasanslutningar
sqlite_conn.close()
duckdb_conn.close()
print("Databasanslutningar stängda.")
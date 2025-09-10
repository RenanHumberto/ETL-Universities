from src.extract import Extract
from src.transform import Transform
from src.load import Load

# Extract
extractor = Extract()
raw_data = extractor.extract_country("Brazil")

# Transform
transformer = Transform()
transformed_df = transformer.transform_data(raw_data)

# Load
loader = Load()
loader.create_sqlite_table(transformed_df, "universities", "universidades_br")

# Consultas SQL
# Total de universidades por país
count_df = loader.count_universities_by_country("universities", "universidades_br")
print("Total de universidades por país:")
print(count_df)

# Listagem de universidades de um país específico
country_df = loader.list_universities_by_country("universities", "universidades_br", "Brazil")
print("\nUniversidades no Brasil:")
print(country_df)

# Busca por nomes que contenham um termo
search_df = loader.search_universities_by_name("universities", "universidades_br", "University")
print("\nUniversidades com 'University' no nome:")
print(search_df)
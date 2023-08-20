from sqlalchemy import create_engine, MetaData, Table, select, insert

# CREATE INSTANCE OF SQLALCHEMY
engine = create_engine("sqlite:///./books.sqlite")

# CONNECT TO DB
conn = engine.connect()

# METADATA INFO FOR THE TABLE
metadata = MetaData()
book_table = Table("book", metadata, autoload_with=engine)

# INSERTING A NEW BOOK
insert_stmt = insert(book_table).values(title="Of Mice and Men")
result = conn.execute(insert_stmt)
print(result)

# GETTING DATA FROM THE TABLE
select_stmt = select(book_table)
result = conn.execute(select_stmt)
print(result.all())
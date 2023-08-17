from sqlalchemy import create_engine, MetaData, Table, select, insert, update, delete

# create an instane of sqlalchemy engine
engine = create_engine("sqlite:///./books.sqlite")

# establish a connection to the database
conn = engine.connect()

# metadata information for sqlalchemy about the table
metadata = MetaData()
author_table = Table("author", metadata, autoload_with=engine)

# retrieving data from the database
select_stmt = select(author_table)
result = conn.execute(select_stmt)
print(result.all())

# INSERTING NEW DATA 
insert_statement = insert(author_table).values(first_name="Amsu", last_name="Warner")
result = conn.execute(insert_statement)
print(result)

# UPDATE THE DATABASE
def update_author(id, firstName, lastName):
    update_stmt = (
        update(author_table)
            .where(author_table.c.author_id == id)
            .values(first_name = firstName, last_name = lastName)
    )
    conn.execute(update_stmt)
    conn.commit()


def delete_author(id):
    delete_stmt = delete(author_table).where(author_table.c.author_id == id)
    conn.execute(delete_stmt)
    conn.commit()
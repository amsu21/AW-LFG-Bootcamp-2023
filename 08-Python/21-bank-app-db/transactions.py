from sqlalchemy import create_engine, MetaData, Table, select, update

engine = create_engine("sqlite:///.transactions.sqlite")

conn = engine.connect()

metadata = MetaData()
transactions_table = Table("transactions", metadata, autoload_with=engine)

# GET ALL TRANSACTIONS
select_stmt = select(transactions_table)
result = conn.execute(select_stmt)
print(result.all())

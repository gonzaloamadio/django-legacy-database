import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Chinook",
    user="postgres",
    password="apeel")

# REF: https://pynative.com/python-postgresql-transaction-management-using-commit-and-rollback/

# Execute in transaction
with conn:
    with conn.cursor() as cur:
        # display the PostgreSQL database server version

        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)

        # add ID column
        cur.execute('ALTER TABLE public."PlaylistTrack" ADD COLUMN id INTEGER')

        # generate IDs
        cur.execute('SELECT "PlaylistId", "TrackId" FROM public."PlaylistTrack"')
        rows = cur.fetchall()
        for i, (pl, tr) in enumerate(rows):
            cur.execute('UPDATE public."PlaylistTrack" SET id = %s WHERE "PlaylistId" = %s AND "TrackId" = %s', (i+1, pl, tr))

        # db.commit()

        # REF: https://stackoverflow.com/questions/36468950/postgresql-add-existing-column-to-composite-primary-key#fromHistory

        # drop composite primary keys, add new primary key and set as "AUTO_INCREMENT" field
        cur.execute('ALTER TABLE public."PlaylistTrack" DROP CONSTRAINT "PK_PlaylistTrack"')
        cur.execute('ALTER TABLE public."PlaylistTrack" ADD CONSTRAINT "PK_PlaylistTrack" PRIMARY KEY(id)')
        # cur.execute('ALTER TABLE public."PlaylistTrack" CHANGE COLUMN id id INTEGER AUTO_INCREMENT')


echo "### Seeding MongoDB... "
mongorestore ./docker-entrypoint-initdb.d/dump/
echo "### Finished seeding "
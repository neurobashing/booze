#!/bin/sh

# trim last , (json doesn't allow trailing , in lists)
# fix escaping of names
rm index.json
echo '[' >> index.json
for file in search_data/*; do
    cat "$file" >> index.json
    echo ',' >> index.json
done
FILEC=$(cat index.json)
echo "${FILEC%?}" > index.json
echo ']' >> index.json
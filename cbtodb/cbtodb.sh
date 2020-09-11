#!/bin/bash
# script to take what is on clipboard and try to turn it into
# a sqlite database table

TABLE_NAME="tmp$(date +%Y%m%d%H%M%S)"
SQLITE_DB_FILE_LOCATION="cbtodb.db"
TSV_FILE_LOCATION="/tmp/cbtodb_data_${TABLE_NAME}.tsv"

if [ ! -f "$SQLITE_DB_FILE_LOCATION" ]; then
    echo "making new sqlite db file - ${SQLITE_DB_FILE_LOCATION} - you'll need to add connection for this in DBeaver"
    sqlite3 $SQLITE_DB_FILE_LOCATION "VACUUM;"
fi

echo "$(pbpaste)" > $TSV_FILE_LOCATION

echo ".mode tabs 
.import ${TSV_FILE_LOCATION} ${TABLE_NAME} 
.header on 
.mode column
select * from ${TABLE_NAME} limit 5;
.header off
select '... ' || count(*) || ' rows in table' from ${TABLE_NAME}" | sqlite3 $SQLITE_DB_FILE_LOCATION


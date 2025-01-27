#!/bin/bash

mysql -u$DATABASE_USER -p$DATABASE_PASSWORD -h$DATABASE_HOST $DATABASE_NAME < create_table.sql

#!/bin/bash

mysql -u$DATABASE_USER -p$DATABASE_PASSWORD -h$DATABASE_HOST $DATABASE_NAME < database/create_table.sql
mysql -u$DATABASE_USER -p$DATABASE_PASSWORD -h$DATABASE_HOST $DATABASE_NAME < database/create_tests_results.sql

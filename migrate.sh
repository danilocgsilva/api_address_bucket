#!/bin/bash

mysql -u$DATABASE_USER -p$DATABASE_PASSWORD -h$DATABASE_HOST api_address_bucket < create_table.sql

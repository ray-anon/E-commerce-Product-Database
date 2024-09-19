#!/bin/sh

export PGUSER="postgres"

psql -c "CREATE DATABASE fkcommerce"

psql fkcommerce -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"
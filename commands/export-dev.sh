#!/bin/bash
poetry export --without-hashes --format=requirements.txt > requirements-dev.txt --with dev
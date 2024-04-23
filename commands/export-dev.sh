#!/bin/bash
poetry export --without-hashes --format=requirements.txt > dev.requirements.txt --with dev
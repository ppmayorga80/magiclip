#!/bin/bash

echo "             _     _ _     _       _                            _  "
echo " _ __  _   _| |__ | (_)___| |__   | |_ ___    _ __  _   _ _ __ (_) "
echo "| '_ \| | | | '_ \| | / __| '_ \  | __/ _ \  | '_ \| | | | '_ \| | "
echo "| |_) | |_| | |_) | | \__ \ | | | | || (_) | | |_) | |_| | |_) | | "
echo "| .__/ \__,_|_.__/|_|_|___/_| |_|  \__\___/  | .__/ \__, | .__/|_| "
echo "|_|                                          |_|    |___/|_|       "
echo "                                                                   "

python -m build
twine upload --verbose dist/*

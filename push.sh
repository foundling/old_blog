#!/bin/bash
python freeze.py
scp -r blog/build/* alexr@104.131.106.239:/var/www/html/alexramsdell/

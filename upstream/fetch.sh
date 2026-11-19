#!/bin/sh
# Download the free Canepari PDFs used by this project into upstream/downloads/ (git-ignored).
set -e
cd "$(dirname "$0")"
mkdir -p downloads
get() { curl -fsSL -o "downloads/$1" "$2"; echo "fetched $1"; }
get npt-ch-00-06.pdf "https://canipa.net/lib/exe/fetch.php?media=docs:npt-ch-00-06_2023-06-20_first.pdf"
get npt-ch-07-14.pdf "https://canipa.net/lib/exe/fetch.php?media=docs:npt-ch-07-14_2023-07-20_main.pdf"
echo "Compare checksums with SOURCES.md:"; sha256sum downloads/*.pdf

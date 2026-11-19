# Upstream sources

These are free to download from the author's site, [canipa.net](https://canipa.net/doku.php?id=pdf). They are **not copied into this repo**: I have not seen a licence that allows redistribution. Run `./fetch.sh` to download them into `upstream/downloads/` (git-ignored).

## Used for the labels in this project
| File | What | Pages used | SHA-256 (downloaded 2026-11-19) |
|---|---|---|---|
| Natural Phonetics & Tonetics, Chs. 0-6 (first) | Intro, classification of sounds | background | `826958e8e79ace3d96cc16aaa8f52192b7ce41973ad4dc288aa98aa3464138e5` |
| Natural Phonetics & Tonetics, Chs. 7-14 (main) | canIPA contoids | **fig 10.1, book pp. 166-168** (the 63 places and 18 manners); ch. 10 intro ("seven sections") | `085da4f47126df40997557b7edae2ec68eccdb3b1cf557e7e9ec2dd6e348e3c2` |

Book: Luciano Canepari, *Natural Phonetics & Tonetics: Articulatory, Auditory & Functional*, Lincom, 2007 (updated 2008). A checksum change means the site's file has been updated since this work was done.

## Other places
- Author's site index of free PDFs: https://canipa.net/doku.php?id=pdf
- Luciano Canepari on Wikipedia: https://en.wikipedia.org/wiki/Luciano_Canepari
- The charts credit his work as: "La Fonetica naturale, con IPA".

## What was taken from the book
Only the **structure**: the place families and their sub-position counts, the manner names, and the grouping of manners. That structure is recorded in `tools/labels.py` with the book pages cited there. No text or figures are copied.

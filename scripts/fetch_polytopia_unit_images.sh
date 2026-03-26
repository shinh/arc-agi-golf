#!/usr/bin/env bash
set -uo pipefail

# Download Polytopia unit images from wiki pages using MediaWiki APIs.
# Usage:
#   scripts/fetch_polytopia_unit_images.sh Warrior "Mind Bender" Knight
#   scripts/fetch_polytopia_unit_images.sh -f units.txt

api=${POLYTOPIA_WIKI_API:-https://polytopia.fandom.com/api.php}
out=${POLYTOPIA_IMAGE_DIR:-images}
mkdir -p "$out"

a=()
if [ "${1:-}" = "-f" ]; then
  # Read unit names from a text file (one unit per line).
  while IFS= read -r x; do [ -n "$x" ] && a+=("$x"); done < "${2:?units file is required}"
  shift 2
fi
a+=("$@")
[ "${#a[@]}" -gt 0 ] || { echo "unit names are required" >&2; exit 1; }

for u in "${a[@]}"; do
  # Resolve canonical page title from search results.
  q=$(curl -fsSLG "$api" --data-urlencode action=query --data-urlencode format=json --data-urlencode list=search --data-urlencode "srsearch=$u" --data-urlencode srlimit=1 2>/dev/null || true)
  [ -n "$q" ] || { echo "skip: $u (api unreachable: $api)" >&2; continue; }
  t=$(echo "$q" | jq -r '.query.search[0].title // empty')
  [ -n "$t" ] || { echo "skip: $u (page not found)" >&2; continue; }

  # Pull thumbnail URL from the page.
  j=$(curl -fsSLG "$api" --data-urlencode action=query --data-urlencode format=json --data-urlencode prop=pageimages --data-urlencode pithumbsize=512 --data-urlencode "titles=$t" 2>/dev/null)
  p=$(echo "$j" | jq -r '.query.pages|to_entries[0].value.thumbnail.source // empty')
  [ -n "$p" ] || { echo "skip: $u/$t (image not found)" >&2; continue; }

  s=$(echo "$u" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/_/g;s/__*/_/g;s/^_//;s/_$//')
  e=$(echo "$p" | sed -n 's/.*\(\.[A-Za-z0-9][A-Za-z0-9]*\)\($\|?\).*/\1/p')
  [ -n "$e" ] || e=.png
  f="$out/$s$e"

  # Save image file.
  if curl -fsSL "$p" -o "$f" 2>/dev/null; then
    echo "$u -> $f"
  else
    echo "skip: $u/$t (download failed)" >&2
  fi
done

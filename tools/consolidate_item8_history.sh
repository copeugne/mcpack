#!/usr/bin/env bash
# Build a new PR branch from reviewed endpoint trees; never move an existing ref.
set -euo pipefail

source_ref=$1
target_branch=$2
mapping=$3
base=b0e4fc0f1c997414d64ef73af208f92028528054
plan=evidence/item-8/history-consolidation-ranges.tsv
git check-ref-format "refs/heads/$target_branch"
test "$(git rev-parse origin/main)" = "$base"
git merge-base --is-ancestor "$base" "$source_ref"
test ! -e "$mapping"
if git show-ref --verify --quiet "refs/heads/$target_branch"; then
    echo "Destination branch already exists" >&2
    exit 1
fi

declare -A endpoints
while IFS=$'\t' read -r first last title; do
    test -z "${endpoints[$first]+set}"
    endpoints[$first]=$last
done < "$plan"
mapfile -t commits < <(git rev-list --first-parent --reverse "$base..$source_ref")
parent=$base
pending_mapping=$(mktemp)
message=$(mktemp)
trap 'rm -f "$pending_mapping" "$message"' EXIT
consumed=0
for ((i=0; i<${#commits[@]}; i++)); do
    first=${commits[$i]}
    last=${endpoints[$first]:-$first}
    start_index=$i
    while test "${commits[$i]}" != "$last"; do
        i=$((i+1))
        if ((i >= ${#commits[@]})); then
            echo "Plan endpoint is not in the source interval: $last" >&2
            exit 1
        fi
    done
    if test "$first" != "$last"; then consumed=$((consumed+1)); fi
    git show -s --format=%B "$last" > "$message"
    printf '\nPreserved source interval: %s..%s\n' "$first" "$last" >> "$message"
    tree=$(git rev-parse "$last^{tree}")
    next=$(
        GIT_AUTHOR_NAME="$(git show -s --format=%an "$last")" \
        GIT_AUTHOR_EMAIL="$(git show -s --format=%ae "$last")" \
        GIT_AUTHOR_DATE="$(git show -s --format=%aI "$last")" \
        GIT_COMMITTER_DATE="$(git show -s --format=%cI "$last")" \
        git commit-tree "$tree" -p "$parent" -F "$message"
    )
    test "$(git rev-parse "$next^{tree}")" = "$tree"
    for ((j=start_index; j<=i; j++)); do
        printf '%s\t%s\n' "${commits[$j]}" "$next" >> "$pending_mapping"
    done
    parent=$next
done
test "$consumed" -eq "${#endpoints[@]}"
test "$(git rev-parse "$parent^{tree}")" = "$(git rev-parse "$source_ref^{tree}")"
mv "$pending_mapping" "$mapping"
git update-ref "refs/heads/$target_branch" "$parent" 0000000000000000000000000000000000000000
printf 'Source: %s\nNew head: %s\nCombined intervals: %s\n' "$source_ref" "$parent" "$consumed"

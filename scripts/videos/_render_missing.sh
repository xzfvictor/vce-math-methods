#!/usr/bin/env bash
# Render the missing Year 10 scenes serially.
set -uo pipefail
ROOT="/home/victor/maths-decoded"
SCENES=(
  "m10-measurement-trig/surveying-design"
  "m10-number-approximations/compound-errors"
  "m10-probability-conditional/two-way-venn"
  "m10-probability-conditional/simulation"
  "m10-probability-conditional/conditional-language"
  "m10-probability-conditional/real-world"
  "m10-probability-conditional/trees-without-replacement"
  "m10-statistics-investigations/time-series"
  "m10-statistics-investigations/cycle"
  "m10-space-networks/euler-polyhedra"
  "m10-statistics-claims/causation-ethics"
  "m10-statistics-claims/axes-samples"
  "m10-probability-experiments/tree-diagrams"
  "m10-probability-experiments/replacement-independence"
  "m10-measurement-scaling/errors"
  "m10-statistics-two-way/build-read"
  "m10-statistics-two-way/percentages-association"
  "m10-statistics-scatter/scatter-fit"
  "m10-statistics-scatter/interpolation-causation"
  "m10-statistics-boxplots/comparing-displays"
  "m10-statistics-boxplots/five-number-summary"
  "m10-statistics-boxplots/boxplots"
  "m10-statistics-boxplots/digital-tools"
  "m10-space-proofs/isosceles-properties"
  "m10-space-proofs/congruent-triangles"
)
for key in "${SCENES[@]}"; do
  topic="${key%/*}"
  lesson="${key#*/}"
  if [ -z "$topic" ] || [ -z "$lesson" ]; then
    echo "skip $key (empty topic or lesson)"
    continue
  fi
  stem="${topic}-${lesson}"
  cls=""
  for part in $(echo "$stem" | tr '-' ' '); do
    first="$(echo "${part:0:1}" | tr '[:lower:]' '[:upper:]')"
    rest="${part:1}"
    cls="${cls}${first}${rest}"
  done
  cls="${cls}Scene"
  echo "=== $key ==="
  bash "${ROOT}/scripts/videos/_render.sh" "${ROOT}/scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql 2>&1 | tail -3
done

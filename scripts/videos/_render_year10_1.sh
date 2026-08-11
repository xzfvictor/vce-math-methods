#!/usr/bin/env bash
set -euo pipefail

for row in \
  "m10-algebra-factorisation|grouping-in-pairs|M10AlgebraFactorisationGroupingInPairsScene" \
  "m10-algebra-fractions|add-subtract|M10AlgebraFractionsAddSubtractScene" \
  "m10-algebra-binomial|difference-of-squares|M10AlgebraBinomialDifferenceOfSquaresScene" \
  "m10-algebra-algorithms|pointers|M10AlgebraAlgorithmsPointersScene" \
  "m10-algebra-linear-inequalities|solve|M10AlgebraLinearInequalitiesSolveScene" \
  "m10-algebra-simultaneous|graphical|M10AlgebraSimultaneousGraphicalScene" \
  "m10-algebra-relations|transformations|M10AlgebraRelationsTransformationsScene" \
  "m10-algebra-exponentials|using-logs|M10AlgebraExponentialsUsingLogsScene" \
  "m10-algebra-numerical|graphical|M10AlgebraNumericalGraphicalScene" \
  "m10-algebra-quadratics|completing-square|M10AlgebraQuadraticsCompletingSquareScene" \
  "m10-measurement-log-scales|reading-scale|M10MeasurementLogScalesReadingScaleScene" \
  "m10-measurement-scaling|errors|M10MeasurementScalingErrorsScene" \
  "m10-measurement-trig|surveying-design|M10MeasurementTrigSurveyingDesignScene" \
  "m10-space-proofs|congruent-triangles|M10SpaceProofsCongruentTrianglesScene" \
  "m10-space-networks|euler-polyhedra|M10SpaceNetworksEulerPolyhedraScene" \
  "m10-statistics-boxplots|digital-tools|M10StatisticsBoxplotsDigitalToolsScene" \
  "m10-statistics-investigations|time-series|M10StatisticsInvestigationsTimeSeriesScene" \
  "m10-statistics-two-way|percentages-association|M10StatisticsTwoWayPercentagesAssociationScene" \
  "m10-probability-conditional|trees-without-replacement|M10ProbabilityConditionalTreesWithoutReplacementScene"
do
  IFS="|" read -r topic lesson cls <<< "$row"
  bash scripts/videos/_render.sh "scripts/videos/${topic}-${lesson}.py" "$cls" "$topic" "$lesson" ql
done

#!/usr/bin/env bash
set -euo pipefail

for row in \
  "m10-algebra-exponent-laws|three-laws|M10AlgebraExponentLawsThreeLawsScene" \
  "m10-algebra-fractions|multiply-divide|M10AlgebraFractionsMultiplyDivideScene" \
  "m10-algebra-formulas|substitute|M10AlgebraFormulasSubstituteScene" \
  "m10-algebra-algorithms|pseudocode-loops|M10AlgebraAlgorithmsPseudocodeLoopsScene" \
  "m10-algebra-linear-inequalities|graph|M10AlgebraLinearInequalitiesGraphScene" \
  "m10-algebra-gradients|parallel|M10AlgebraGradientsParallelScene" \
  "m10-algebra-linear-fractions|clear-numerical|M10AlgebraLinearFractionsClearNumericalScene" \
  "m10-algebra-modelling|choose-model|M10AlgebraModellingChooseModelScene" \
  "m10-algebra-numerical|refine|M10AlgebraNumericalRefineScene" \
  "m10-algebra-quadratics|discriminant|M10AlgebraQuadraticsDiscriminantScene" \
  "m10-measurement-log-scales|real-world|M10MeasurementLogScalesRealWorldScene" \
  "m10-measurement-trig|bearings|M10MeasurementTrigBearingsScene" \
  "m10-number-approximations|rounding-truncation|M10NumberApproximationsRoundingTruncationScene" \
  "m10-space-proofs|dynamic-geometry|M10SpaceProofsDynamicGeometryScene" \
  "m10-statistics-boxplots|five-number-summary|M10StatisticsBoxplotsFiveNumberSummaryScene" \
  "m10-statistics-claims|axes-samples|M10StatisticsClaimsAxesSamplesScene" \
  "m10-statistics-scatter|scatter-fit|M10StatisticsScatterScatterFitScene" \
  "m10-probability-conditional|conditional-language|M10ProbabilityConditionalConditionalLanguageScene" \
  "m10-probability-conditional|two-way-venn|M10ProbabilityConditionalTwoWayVennScene"
do
  IFS="|" read -r topic lesson cls <<< "$row"
  bash scripts/videos/_render.sh "scripts/videos/${topic}-${lesson}.py" "$cls" "$topic" "$lesson" ql
done

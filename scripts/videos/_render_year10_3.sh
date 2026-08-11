#!/usr/bin/env bash
set -euo pipefail

for row in \
  "m10-algebra-exponent-laws|negative-zero-indices|M10AlgebraExponentLawsNegativeZeroIndicesScene" \
  "m10-algebra-binomial|expand-foil|M10AlgebraBinomialExpandFoilScene" \
  "m10-algebra-formulas|rearrange|M10AlgebraFormulasRearrangeScene" \
  "m10-algebra-linear-eq|solve|M10AlgebraLinearEqSolveScene" \
  "m10-algebra-simultaneous|substitution|M10AlgebraSimultaneousSubstitutionScene" \
  "m10-algebra-gradients|perpendicular|M10AlgebraGradientsPerpendicularScene" \
  "m10-algebra-linear-fractions|algebraic-denominators|M10AlgebraLinearFractionsAlgebraicDenominatorsScene" \
  "m10-algebra-modelling|compound-interest|M10AlgebraModellingCompoundInterestScene" \
  "m10-algebra-quadratics|null-factor-law|M10AlgebraQuadraticsNullFactorLawScene" \
  "m10-measurement-area-volume|surface-area|M10MeasurementAreaVolumeSurfaceAreaScene" \
  "m10-measurement-scaling|scale|M10MeasurementScalingScaleScene" \
  "m10-measurement-trig|elevation-depression|M10MeasurementTrigElevationDepressionScene" \
  "m10-number-approximations|compound-errors|M10NumberApproximationsCompoundErrorsScene" \
  "m10-space-proofs|isosceles-properties|M10SpaceProofsIsoscelesPropertiesScene" \
  "m10-statistics-boxplots|boxplots|M10StatisticsBoxplotsBoxplotsScene" \
  "m10-statistics-claims|causation-ethics|M10StatisticsClaimsCausationEthicsScene" \
  "m10-statistics-scatter|interpolation-causation|M10StatisticsScatterInterpolationCausationScene" \
  "m10-probability-conditional|real-world|M10ProbabilityConditionalRealWorldScene" \
  "m10-probability-experiments|tree-diagrams|M10ProbabilityExperimentsTreeDiagramsScene"
do
  IFS="|" read -r topic lesson cls <<< "$row"
  bash scripts/videos/_render.sh "scripts/videos/${topic}-${lesson}.py" "$cls" "$topic" "$lesson" ql
done

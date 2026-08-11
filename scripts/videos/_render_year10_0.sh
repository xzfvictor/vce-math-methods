#!/usr/bin/env bash
set -euo pipefail

for row in \
  "m10-algebra-factorisation|common-factor|M10AlgebraFactorisationCommonFactorScene" \
  "m10-algebra-exponent-laws|combined-applications|M10AlgebraExponentLawsCombinedApplicationsScene" \
  "m10-algebra-binomial|factor-monic|M10AlgebraBinomialFactorMonicScene" \
  "m10-algebra-algorithms|arrays-matrices|M10AlgebraAlgorithmsArraysMatricesScene" \
  "m10-algebra-linear-eq|model|M10AlgebraLinearEqModelScene" \
  "m10-algebra-simultaneous|elimination|M10AlgebraSimultaneousEliminationScene" \
  "m10-algebra-relations|shape-signature|M10AlgebraRelationsShapeSignatureScene" \
  "m10-algebra-exponentials|matching-bases|M10AlgebraExponentialsMatchingBasesScene" \
  "m10-algebra-modelling|inverse-proportion|M10AlgebraModellingInverseProportionScene" \
  "m10-algebra-quadratics|quadratic-formula|M10AlgebraQuadraticsQuadraticFormulaScene" \
  "m10-measurement-area-volume|volume|M10MeasurementAreaVolumeVolumeScene" \
  "m10-measurement-scaling|proportion|M10MeasurementScalingProportionScene" \
  "m10-measurement-trig|pythagoras-trig|M10MeasurementTrigPythagorasTrigScene" \
  "m10-space-proofs|proof-vs-demo|M10SpaceProofsProofVsDemoScene" \
  "m10-space-networks|network-basics|M10SpaceNetworksNetworkBasicsScene" \
  "m10-statistics-boxplots|comparing-displays|M10StatisticsBoxplotsComparingDisplaysScene" \
  "m10-statistics-investigations|cycle|M10StatisticsInvestigationsCycleScene" \
  "m10-statistics-two-way|build-read|M10StatisticsTwoWayBuildReadScene" \
  "m10-probability-conditional|simulation|M10ProbabilityConditionalSimulationScene" \
  "m10-probability-experiments|replacement-independence|M10ProbabilityExperimentsReplacementIndependenceScene"
do
  IFS="|" read -r topic lesson cls <<< "$row"
  bash scripts/videos/_render.sh "scripts/videos/${topic}-${lesson}.py" "$cls" "$topic" "$lesson" ql
done

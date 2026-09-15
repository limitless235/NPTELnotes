#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

build() {
  local course="$1" file="$2"
  echo "Building $course / $file ..."
  "$ROOT/scripts/build-pdf.sh" "$course" "$file"
}

# Course 1: Cyber Security and Privacy
for v in vol-01-lectures-01-10 vol-02-lectures-11-20 vol-03-lectures-21-30 vol-04-lectures-31-40; do
  build courses/01-cyber-security-and-privacy "${v}.md"
done

# Course 2: Ethical Hacking
for v in vol-01 vol-02 vol-03 vol-04 vol-05 vol-06; do
  build courses/02-ethical-hacking "${v}.md"
done

# Course 3: Generative AI
for v in vol-01 vol-02 vol-03 vol-04; do
  build courses/03-generative-ai-llms "${v}.md"
done

# Course 4: Cyber Security Tools IGNOU
for v in vol-01 vol-02 vol-03 vol-04; do
  build courses/04-cyber-security-tools-ignou "${v}.md"
done

# Course 5: Information Security
for v in vol-01 vol-02 vol-03 vol-04; do
  build courses/05-information-security-cec "${v}.md"
done

echo "All PDFs built."

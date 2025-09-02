# System Architecture

## Overview
The Title Verification System checks new submissions against existing titles using:
- Rule-based validation
- String similarity (Levenshtein distance)
- AI-based semantic similarity

## Workflow
1. Input new title
2. Run rule-based checks
3. Compare with database for similarity
4. Use AI for deep semantic similarity
5. Return result
